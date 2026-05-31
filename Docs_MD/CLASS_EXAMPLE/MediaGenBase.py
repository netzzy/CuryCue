"""
MediaGenBase - Base class for media generation (images/videos).

Provides common functionality for ImageGen and VideoGen classes.
"""

from AopUtil import AopUtil
from models_registry import extract_provider_from_model_id, get_models_by_provider, get_registry
import os
import base64
import re
import tempfile
from datetime import datetime


class MediaGenBase(AopUtil):
    """Base class for media generation with common functionality."""
    
    def __init__(self, ownerComp, media_type='media'):
        """
        Initialize the base media generation class.
        
        Args:
            ownerComp: TouchDesigner component
            media_type (str): 'image', 'video', or 'media' (for base class)
        """
        super().__init__(ownerComp)
        self.ownerComp = ownerComp
        self.media_type = media_type
        self.logger = op('Logger').ext.Logger if op('Logger') else print
        self.tdAsyncIO = self.ownerComp.op('TDAsyncIO')
    
    def _generate_filename(self, prompt, output_dir, file_extension='.png'):
        """
        Generate filename and filepath using prompt words and node name subfolder.
        
        Args:
            prompt (str): The text prompt
            output_dir (str): Base output directory
            file_extension (str): File extension (e.g., '.png', '.mp4')
            
        Returns:
            tuple: (filepath, filename) - Full path and filename
        """
        # Get first couple of words from prompt (sanitize for filename)
        words = prompt.split()[:3]  # First 3 words
        prompt_snippet = '_'.join(words).lower()
        # Remove invalid filename characters
        prompt_snippet = re.sub(r'[^\w\s-]', '', prompt_snippet)
        prompt_snippet = re.sub(r'[-\s]+', '_', prompt_snippet)
        
        # Create subfolder with node name
        node_name = self.ownerComp.name
        subfolder = os.path.join(output_dir, node_name)
        os.makedirs(subfolder, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{prompt_snippet}_{timestamp}{file_extension}"
        filepath = os.path.join(subfolder, filename)
        
        return filepath, filename
    
    def _get_prompt_from_operator(self):
        """
        Get prompt text from PROMPT operator.
        
        Returns:
            str: Prompt text
            
        Raises:
            ValueError: If PROMPT operator not found
        """
        prompt_op = self.ownerComp.op('PROMPT')
        if prompt_op:
            return prompt_op.text
        raise ValueError("PROMPT operator not found. Please provide a prompt argument or create a PROMPT operator.")
    
    def _check_ref_in1_exists(self):
        """
        Check if REF_IN1_ operator exists and is not empty.
        
        Returns:
            bool: True if REF_IN1_ exists and is not empty (128x128)
        """
        ref_in1_resized = self.ownerComp.op('REF_IN1_')
        if ref_in1_resized:
            width, height = ref_in1_resized.width, ref_in1_resized.height
            # 128x128 typically means empty in TouchDesigner
            return width != 128 or height != 128
        return False
    
    def _check_ref_in2_exists(self):
        """
        Check if REF_IN2_ operator exists and is not empty.
        
        Returns:
            bool: True if REF_IN2_ exists and is not empty (128x128)
        """
        ref_in2_resized = self.ownerComp.op('REF_IN2_')
        if ref_in2_resized:
            width, height = ref_in2_resized.width, ref_in2_resized.height
            # 128x128 typically means empty in TouchDesigner
            return width != 128 or height != 128
        return False
    
    def _check_ref_in_exists(self, index):
        """
        Generic helper to check if REF_IN{i}_ operator exists and is not empty.
        
        Args:
            index (int): The index of the REF_IN operator (1-7)
            
        Returns:
            bool: True if REF_IN{i}_ exists and is not empty (128x128)
        """
        ref_in_resized = self.ownerComp.op(f'REF_IN{index}_')
        if ref_in_resized:
            width, height = ref_in_resized.width, ref_in_resized.height
            # 128x128 typically means empty in TouchDesigner
            return width != 128 or height != 128
        return False
    
    def _encode_image_to_base64(self, ref_image):
        """
        Encode a TouchDesigner TOP operator image to base64 data URI.
        
        Args:
            ref_image: TouchDesigner TOP operator
            
        Returns:
            str: Base64-encoded image data URI, or None if failed
        """
        if not ref_image:
            return None
        
        try:
            # Save to temporary file
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
                temp_path = temp_file.name
            
            # Save the image from TOP operator
            ref_image.save(temp_path)
            
            # Read and encode to base64
            with open(temp_path, 'rb') as f:
                image_bytes = f.read()
                encoded_image = base64.b64encode(image_bytes).decode('utf-8')
            
            # Format as data URI
            data_uri = f'data:image/png;base64,{encoded_image}'
            
            # Get image dimensions for logging
            width, height = ref_image.width, ref_image.height
            size_kb = len(image_bytes) / 1024
            
            # Clean up temp file
            try:
                os.unlink(temp_path)
            except:
                pass
            
            self.logger.log(f"Image encoded and prepared: {width}x{height} ({size_kb:.1f} KB, base64 data URI ready)", level='INFO')
            
            return data_uri
            
        except Exception as e:
            self.logger.log(f"Error encoding image: {e}", level='ERROR')
            # Clean up temp file on error
            try:
                if 'temp_path' in locals():
                    os.unlink(temp_path)
            except:
                pass
            return None
    
    def Clearfiles(self):
        """Pulse callback for Clear Files button - clears SAVED_FILES table and adds empty row."""
        try:
            saved_files_table = self.ownerComp.op('SAVED_FILES')
            if saved_files_table:
                # Clear all rows from the table
                saved_files_table.clear()
                
                # Add one empty row
                saved_files_table.appendRow(['../empty.png', ''])
                
                # Set Scroll cursor to 0
                scroll_op = self.ownerComp.op('Scroll')
                if scroll_op:
                    scroll_op.par.Cursor = 0
                    self.logger.log("Set Scroll cursor to 0", level='INFO')
                
                self.logger.log("Cleared SAVED_FILES table and added empty row", level='INFO')
                
                # Clear logs like Logger.clearlog pulse
                logger_op = op('Logger')
                if logger_op and hasattr(logger_op.ext.Logger, 'Clearlog'):
                    logger_op.ext.Logger.Clearlog()
            else:
                self.logger.log("SAVED_FILES table operator not found", level='WARNING')
        except Exception as e:
            self.logger.log(f"Error clearing SAVED_FILES table: {e}", level='ERROR')
    
    def _add_to_saved_files_table(self, filepath, prompt):
        """
        Add a row to the SAVED_FILES table with filename and prompt.
        
        Args:
            filepath (str): Full path to the generated media file
            prompt (str): The prompt used to generate the media
        """
        try:
            saved_files_table = self.ownerComp.op('SAVED_FILES')
            if saved_files_table:
                # Get just the filename from the full path
                filename = os.path.basename(filepath)
                
                # Ensure table has headers if it's empty
                if saved_files_table.numRows == 0:
                    saved_files_table.appendRow(['filename', 'prompt'])
                
                # Insert new row with filename and prompt
                saved_files_table.appendRow([filename, prompt])
                self.logger.log(f"Added to SAVED_FILES table: {filename}", level='INFO')
                
                # Set Scroll cursor to the last row (newly added row)
                scroll_op = self.ownerComp.op('Scroll')
                if scroll_op:
                    last_row_index = saved_files_table.numRows - 1
                    scroll_op.par.Cursor = last_row_index
                    self.logger.log(f"Set Scroll cursor to row {last_row_index}", level='INFO')
            else:
                self.logger.log("SAVED_FILES table operator not found", level='WARNING')
        except Exception as e:
            self.logger.log(f"Error adding to SAVED_FILES table: {e}", level='ERROR')
    
    def Stopgeneration(self):
        """Pulse callback for Stop Generation button - cancels all active generation tasks."""
        try:
            # Cancel all active tasks
            self.tdAsyncIO.ext.AsyncIOManager.Cancelactive()
            
            # Update Active status to False
            self.ownerComp.par.Active = False
            
            media_type_label = 'image' if self.media_type == 'image' else 'video'
            self.logger.log(f"Stopped all active {media_type_label} generation tasks", level='INFO')
        except Exception as e:
            self.logger.log(f"Error stopping generation tasks: {e}", level='ERROR')
    
    def _update_active_status(self):
        """Update the Active parameter based on whether there are active tasks."""
        active_tasks_count = self.tdAsyncIO.ext.AsyncIOManager.GetActiveTasksCount()
        self.ownerComp.par.Active = active_tasks_count > 0
    
    def _extract_provider_from_model_id(self, model_id):
        """
        Extract provider name from model ID.
        
        Args:
            model_id (str): Model identifier
            
        Returns:
            str: Provider name, or None if not found
        """
        return extract_provider_from_model_id(model_id)
    
    def _get_models_for_provider(self, provider, media_type=None):
        """
        Get list of model IDs for a given provider.
        
        Args:
            provider (str): Provider name (e.g., 'Kling', 'Google')
            media_type (str, optional): 'image' or 'video' to filter by type
            
        Returns:
            list: List of model IDs for the provider
        """
        models_dict = get_models_by_provider(provider, media_type)
        return list(models_dict.keys())
    
    def _update_model_menu(self, provider):
        """
        Update the Model parameter's menu items based on selected provider.
        
        Args:
            provider (str): Provider name
        """
        if not hasattr(self.ownerComp.par, 'Model'):
            return
        
        # Get models for this provider and media type
        model_ids = self._get_models_for_provider(provider, self.media_type)
        
        if not model_ids:
            # No models found, clear menu
            self.ownerComp.par.Model.menuNames = []
            self.ownerComp.par.Model.menuLabels = []
            self.ownerComp.par.Model = ''
            return
        
        # Sort model IDs for consistent ordering
        model_ids.sort()
        
        # Update menu items
        self.ownerComp.par.Model.menuNames = model_ids
        self.ownerComp.par.Model.menuLabels = model_ids
        
        # Set to first model if current selection is invalid
        current_model = self.ownerComp.par.Model.eval()
        if current_model not in model_ids:
            self.ownerComp.par.Model = model_ids[0]
    
    def _model_requires_reference(self, model_id):
        """
        Check if a model requires reference images based on registry.
        
        Args:
            model_id (str): Model identifier
            
        Returns:
            bool: True if model requires reference images, False otherwise
        """
        registry = get_registry()
        model_config = registry.get(model_id)
        
        if not model_config:
            return False
        
        detection = model_config.get('detection', {})
        return detection.get('requires_reference', False)
    
    def _model_supports_image_parameter(self, model_id):
        """
        Check if a model supports image parameters and whether they are required.
        
        Args:
            model_id (str): Model identifier
            
        Returns:
            tuple: (supports_image, is_required)
                - supports_image (bool): Whether model supports image parameters
                - is_required (bool): Whether image is required (defaults to False if not specified)
        """
        registry = get_registry()
        model_config = registry.get(model_id)
        
        if not model_config:
            return (False, False)
        
        model_params = model_config.get('parameters', {})
        
        # Check for any image parameter
        image_param_names = ['image_url', 'first_frame_image', 'image_urls']
        image_param = None
        for param_name in image_param_names:
            if param_name in model_params:
                image_param = model_params[param_name]
                break
        
        if not image_param:
            return (False, False)
        
        # Check if image is required (defaults to False if not specified)
        is_required = False
        if isinstance(image_param, dict):
            is_required = image_param.get('required', False)
        
        return (True, is_required)
    
    # Abstract methods to be implemented by subclasses
    def setup_parameters(self):
        """Setup custom parameters. Must be implemented by subclass."""
        raise NotImplementedError("Subclass must implement setup_parameters()")
    
    def _detect_model(self):
        """Detect which model to use. Must be implemented by subclass."""
        raise NotImplementedError("Subclass must implement _detect_model()")
    
    def Generate(self, *args, **kwargs):
        """Generate media. Must be implemented by subclass."""
        raise NotImplementedError("Subclass must implement Generate()")

