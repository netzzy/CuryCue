from MediaGenBase import MediaGenBase
from model_detector import ModelDetector
from api_request_handler import APIRequestHandler
from models_registry import get_registry
import json


class VideoGen(MediaGenBase):

    def __init__(self, ownerComp):
        # Initialize parent class first (with media_type='video')
        super().__init__(ownerComp, media_type='video')
        
        self.logger.log('VideoGen initialized', level='INFO')
        
        # Initialize model detector and registry
        self.registry = get_registry()
        self.model_detector = ModelDetector(self.registry)
        
        # Setup custom parameters
        self.setup_parameters()

    def setup_parameters(self):
        """Create custom parameters for video generation settings."""
        # Create Active parameter (first, bool type)
        self.create_parameter('Active', 'bool', page='Config',
                            label='Active',
                            default=False,
                            help_text='Indicates if video generation is in progress',
                            order=0)
        
        # Create Provider parameter (menu with available providers)
        provider_options = ['Kling', 'Google', 'Ltxv', 'MiniMax', 'Alibaba Cloud', 'LumaAI', 'Runway']
        self.create_parameter('Provider', 'menu', page='Config',
                            label='Provider',
                            menu_items=provider_options,
                            default='Kling',
                            help_text='Select the AI provider',
                            order=1)
        
        # Create Model parameter (menu, initially empty, populated by Provider callback)
        self.create_parameter('Model', 'menu', page='Config',
                            label='Model',
                            menu_items=[],
                            default='',
                            help_text='Select the model (updates based on provider selection)',
                            order=2)
        
        # Create Aspect Ratio parameter (menu based on video API docs)
        aspect_ratio_options = ['16:9', '9:16', '1:1']
        self.create_parameter('Aspectratio', 'menu', page='Config',
                            label='Aspect Ratio',
                            menu_items=aspect_ratio_options,
                            default='16:9',
                            help_text='Video aspect ratio (default: 16:9)')
        
        # Create Resolution parameter (menu, initially disabled, enabled for specific models)
        resolution_options = ['1080p', '1440p', '2160p']
        resolution_par = self.create_parameter('Resolution', 'menu', page='Config',
                            label='Resolution',
                            menu_items=resolution_options,
                            default='1080p',
                            help_text='Video resolution (default: 1080p)')
        resolution_par.readOnly = True  # Initially disabled
        
        # Create Fps parameter (menu, initially disabled, enabled for specific models)
        fps_options = ['25', '50']
        fps_par = self.create_parameter('Fps', 'menu', page='Config',
                            label='FPS',
                            menu_items=fps_options,
                            default='25',
                            help_text='Frames per second (default: 25)')
        fps_par.readOnly = True  # Initially disabled
        
        # Create Generateaudio parameter (bool, initially disabled, enabled for specific models)
        generateaudio_par = self.create_parameter('Generateaudio', 'bool', page='Config',
                            label='Generate Audio',
                            default=True,
                            help_text='Whether to generate audio for the video (default: true)')
        generateaudio_par.readOnly = True  # Initially disabled
        
        # Create Duration parameter (menu based on API docs)
        duration_options = ['5', '10']
        self.create_parameter('Duration', 'menu', page='Config',
                            label='Duration',
                            menu_items=duration_options,
                            default='5',
                            help_text='Video duration in seconds (default: 5)')
        
        # Create CFG Scale parameter
        self.create_parameter('Cfgscale', 'float', page='Config',
                            label='CFG Scale',
                            default=0.9,
                            norm_min=0.0,
                            norm_max=1.0,
                            help_text='Classifier Free Guidance scale (0-1, default: 0.9)')
        
        # Create Generate pulse button
        self.create_parameter('Generate', 'pulse', page='Config',
                            label='Generate Video',
                            help_text='Generate video using current settings')
        
        # Create Stop Generation pulse button
        self.create_parameter('Stopgeneration', 'pulse', page='Config',
                            label='Stop Generation',
                            help_text='Stop all active video generation tasks')
        
        # Create Clear Files pulse button
        self.create_parameter('Clearfiles', 'pulse', page='Config',
                            label='Clear Files',
                            help_text='Clear all entries from SAVED_FILES table')
        
        # Initialize model menu based on default provider
        self.Provider()

    def Provider(self):
        """
        Callback method when Provider parameter changes.
        Updates Model menu items based on selected provider.
        """
        provider = self.ownerComp.par.Provider.eval()
        self._update_model_menu(provider)
        # Update duration options based on first model of provider (will be updated when model is selected)
        self._update_duration_for_model()
        # Update optional parameters based on selected model
        self._update_optional_parameters()
    
    def Model(self):
        """
        Callback method when Model parameter changes.
        Updates Duration menu options and optional parameters based on selected model's requirements.
        """
        self._update_duration_for_model()
        self._update_optional_parameters()
    
    def _update_duration_for_model(self):
        """
        Update Duration parameter menu options based on selected model.
        """
        model_id = self.ownerComp.par.Model.eval()
        if not model_id:
            # No model selected, use default options
            return
        
        model_config = self.registry.get(model_id)
        if not model_config:
            return
        
        # Get duration parameter from model config
        model_params = model_config.get('parameters', {})
        duration_param = model_params.get('duration')
        
        if duration_param and isinstance(duration_param, dict):
            # Check if it's a menu type with options
            if duration_param.get('type') == 'menu' and 'options' in duration_param:
                duration_options = duration_param['options']
                current_duration = str(self.ownerComp.par.Duration.eval())  # Convert to string for comparison
                
                # Update menu options
                self.ownerComp.par.Duration.menuNames = duration_options
                self.ownerComp.par.Duration.menuLabels = duration_options
                
                # If current duration is not in new options, set to first option
                if current_duration not in duration_options:
                    self.ownerComp.par.Duration = duration_options[0]
                    self.logger.log(f"Updated Duration to {duration_options[0]} for model {model_id}", level='INFO')
    
    def _update_optional_parameters(self):
        """
        Update optional parameters (Resolution, Fps, Generateaudio) based on selected model.
        Enables/disables parameters and updates menu options based on model support.
        """
        model_id = self.ownerComp.par.Model.eval()
        if not model_id:
            # No model selected, disable all optional parameters
            if hasattr(self.ownerComp.par, 'Resolution'):
                self.ownerComp.par.Resolution.readOnly = True
            if hasattr(self.ownerComp.par, 'Fps'):
                self.ownerComp.par.Fps.readOnly = True
            if hasattr(self.ownerComp.par, 'Generateaudio'):
                self.ownerComp.par.Generateaudio.readOnly = True
            return
        
        model_config = self.registry.get(model_id)
        if not model_config:
            # Model not found, disable all optional parameters
            if hasattr(self.ownerComp.par, 'Resolution'):
                self.ownerComp.par.Resolution.readOnly = True
            if hasattr(self.ownerComp.par, 'Fps'):
                self.ownerComp.par.Fps.readOnly = True
            if hasattr(self.ownerComp.par, 'Generateaudio'):
                self.ownerComp.par.Generateaudio.readOnly = True
            return
        
        model_params = model_config.get('parameters', {})
        
        # Update Resolution parameter
        if hasattr(self.ownerComp.par, 'Resolution'):
            if 'resolution' in model_params:
                resolution_param = model_params['resolution']
                # Enable parameter
                self.ownerComp.par.Resolution.readOnly = False
                
                # Update menu options if it's a menu type
                if isinstance(resolution_param, dict) and resolution_param.get('type') == 'menu' and 'options' in resolution_param:
                    resolution_options = resolution_param['options']
                    current_resolution = self.ownerComp.par.Resolution.eval()
                    
                    # Update menu options
                    self.ownerComp.par.Resolution.menuNames = resolution_options
                    self.ownerComp.par.Resolution.menuLabels = resolution_options
                    
                    # If current resolution is not in new options, set to first option or default
                    if current_resolution not in resolution_options:
                        new_value = resolution_param.get('default', resolution_options[0])
                        self.ownerComp.par.Resolution = new_value
                        self.logger.log(f"Updated Resolution to {new_value} for model {model_id}", level='INFO')
            else:
                # Disable parameter if model doesn't support it
                self.ownerComp.par.Resolution.readOnly = True
        
        # Update Fps parameter
        if hasattr(self.ownerComp.par, 'Fps'):
            if 'fps' in model_params:
                fps_param = model_params['fps']
                # Enable parameter
                self.ownerComp.par.Fps.readOnly = False
                
                # Update menu options if it's a menu type
                if isinstance(fps_param, dict) and fps_param.get('type') == 'menu' and 'options' in fps_param:
                    fps_options = fps_param['options']
                    current_fps = self.ownerComp.par.Fps.eval()
                    
                    # Update menu options
                    self.ownerComp.par.Fps.menuNames = fps_options
                    self.ownerComp.par.Fps.menuLabels = fps_options
                    
                    # If current fps is not in new options, set to first option or default
                    if current_fps not in fps_options:
                        new_value = fps_param.get('default', fps_options[0])
                        self.ownerComp.par.Fps = new_value
                        self.logger.log(f"Updated Fps to {new_value} for model {model_id}", level='INFO')
            else:
                # Disable parameter if model doesn't support it
                self.ownerComp.par.Fps.readOnly = True
        
        # Update Generateaudio parameter
        if hasattr(self.ownerComp.par, 'Generateaudio'):
            if 'generate_audio' in model_params:
                audio_param = model_params['generate_audio']
                # Check if parameter was previously disabled (before enabling it)
                was_disabled = self.ownerComp.par.Generateaudio.readOnly
                # Enable parameter
                self.ownerComp.par.Generateaudio.readOnly = False
                
                # Set default if parameter was previously disabled
                if was_disabled and isinstance(audio_param, dict) and 'default' in audio_param:
                    default_value = audio_param.get('default', True)
                    self.ownerComp.par.Generateaudio = default_value
                    self.logger.log(f"Set Generateaudio to {default_value} for model {model_id}", level='INFO')
            else:
                # Disable parameter if model doesn't support it
                self.ownerComp.par.Generateaudio.readOnly = True
    
    def _detect_model(self):
        """
        Get the selected model from the Model parameter.
        
        Returns:
            str: Model ID from parameter, or None if not set
        """
        model_id = self.ownerComp.par.Model.eval()
        if not model_id:
            return None
        return model_id
    
    def _get_first_frame_image(self):
        """
        Get and encode the first frame image from REF_IN1 operator.
        Uses base class method for encoding.
        
        Returns:
            str: Base64-encoded image data URI, or None if not found
        """
        # Check if REF_IN1 exists and is not empty
        if not self._check_ref_in1_exists():
            return None
        
        # Get the non-resized version
        ref_image = self.ownerComp.op('REF_IN1')
        if not ref_image:
            return None
        
        # Use base class method to encode
        data_uri = self._encode_image_to_base64(ref_image)
        if data_uri:
            self.logger.log("Collected first frame image from REF_IN1", level='INFO')
        
        return data_uri
    
    def _get_last_frame_image(self):
        """
        Get and encode the last frame image from REF_IN2 operator.
        Uses base class method for encoding.
        
        Returns:
            str: Base64-encoded image data URI, or None if not found
        """
        # Check if REF_IN2 exists and is not empty
        if not self._check_ref_in2_exists():
            return None
        
        # Get the non-resized version
        ref_image = self.ownerComp.op('REF_IN2')
        if not ref_image:
            return None
        
        # Use base class method to encode
        data_uri = self._encode_image_to_base64(ref_image)
        if data_uri:
            self.logger.log("Collected last frame image from REF_IN2", level='INFO')
        
        return data_uri
    
    def _get_multiple_reference_images(self):
        """
        Collect and encode multiple reference images from REF_IN1 through REF_IN7.
        Returns a list of base64-encoded image data URIs.
        Used for models like klingai/video-o1-reference-to-video.
        
        Returns:
            list: List of base64-encoded image data URIs (up to 7 images)
        """
        image_urls = []
        max_images = 7  # REF_IN1 through REF_IN7
        
        for i in range(1, max_images + 1):
            # Check if REF_IN{i}_ exists and is not empty
            if not self._check_ref_in_exists(i):
                continue
            
            # Get the non-resized version
            ref_image = self.ownerComp.op(f'REF_IN{i}')
            if not ref_image:
                continue
            
            try:
                # Use base class method to encode
                data_uri = self._encode_image_to_base64(ref_image)
                if data_uri:
                    image_urls.append(data_uri)
                    self.logger.log(f"Collected reference image from REF_IN{i}", level='INFO')
            except Exception as e:
                self.logger.log(f"Error processing REF_IN{i}: {e}", level='ERROR')
        
        return image_urls


    
    def _convert_parameter_value(self, param_name, value, param_def):
        """
        Convert a parameter value to the correct API type based on parameter definition.
        
        Args:
            param_name (str): Name of the parameter
            value: The value to convert
            param_def (dict): Parameter definition from model config (may contain 'api_type')
            
        Returns:
            Converted value with appropriate type (int, str, bool, float)
        """
        if value is None:
            return None
        
        # Get api_type from parameter definition, default to 'str' for backward compatibility
        api_type = param_def.get('api_type', 'str') if isinstance(param_def, dict) else 'str'
        
        try:
            if api_type == 'int':
                return int(value)
            elif api_type == 'float':
                return float(value)
            elif api_type == 'bool':
                return bool(value)
            elif api_type == 'str':
                return str(value)
            else:
                # Unknown type, default to string
                self.logger.log(f"Unknown api_type '{api_type}' for parameter '{param_name}', using string", level='WARNING')
                return str(value)
        except (ValueError, TypeError) as e:
            self.logger.log(f"Error converting parameter '{param_name}' to {api_type}: {e}. Using original value.", level='WARNING')
            return value
    
    async def _generate_video_async(self, prompt, model, output_dir, duration, aspect_ratio, cfg_scale, first_frame_image=None, last_frame_image=None, multiple_images=None):
        """
        Main async method to generate a video from the AIMLAPI.
        Uses API request handler for unified request handling with polling.
        
        Args:
            prompt (str): The text prompt for video generation
            model (str): The model to use
            output_dir (str): Directory to save the generated video
            duration (int): Video duration in seconds
            aspect_ratio (str): Video aspect ratio
            cfg_scale (float): CFG scale
            first_frame_image (str, optional): Base64-encoded image data URI for image-to-video
            last_frame_image (str, optional): Base64-encoded image data URI for last frame
            multiple_images (list, optional): List of base64-encoded image data URIs for multiple reference images
            
        Returns:
            str: Path to the saved video file, or None if failed
        """
        try:
            # Get API key from AOP
            api_key = op.AOP.Getkey('aimlapi')
            
            # Get AIML API base URL from AOP
            aimlapi_url = op.AOP.par.Aimlapibaseurl.eval()
            
            # Get model configuration from registry
            model_config = self.registry.get(model)
            if not model_config:
                error_msg = f"Model {model} not found in registry"
                self.logger.log(error_msg, level='ERROR')
                return None
            
            # Initialize API request handler
            api_handler = APIRequestHandler(api_key, self.logger, base_url=aimlapi_url)
            
            # Build payload from model config and parameters
            # Only include parameters that are defined in the model config
            payload = {
                'model': model,
                'prompt': prompt
            }
            
            # Get model parameters to check what's supported
            model_params = model_config.get('parameters', {})
            
            # Add duration if model supports it
            if 'duration' in model_params:
                duration_param = model_params['duration']
                # Use api_type from parameter definition to convert value
                payload['duration'] = self._convert_parameter_value('duration', duration, duration_param)
            
            # Add aspect_ratio if model supports it
            if 'aspect_ratio' in model_params:
                aspect_ratio_param = model_params['aspect_ratio']
                # Use api_type from parameter definition to convert value
                payload['aspect_ratio'] = self._convert_parameter_value('aspect_ratio', aspect_ratio, aspect_ratio_param)
            
            # Add cfg_scale only if model supports it
            if 'cfg_scale' in model_params:
                cfg_scale_param = model_params['cfg_scale']
                # Use api_type from parameter definition to convert value
                payload['cfg_scale'] = self._convert_parameter_value('cfg_scale', cfg_scale, cfg_scale_param)
            
            # Add resolution if model supports it AND parameter exists and is enabled (e.g., Ltxv)
            if 'resolution' in model_params:
                if hasattr(self.ownerComp.par, 'Resolution') and not self.ownerComp.par.Resolution.readOnly:
                    resolution_value = self.ownerComp.par.Resolution.eval()
                    resolution_param = model_params['resolution']
                    # Use api_type from parameter definition to convert value
                    payload['resolution'] = self._convert_parameter_value('resolution', resolution_value, resolution_param)
            
            # Add fps if model supports it AND parameter exists and is enabled
            # NOTE: Explicitly exclude Ltxv models as API doesn't support these parameters
            if 'fps' in model_params and not model.startswith('ltxv/'):
                if hasattr(self.ownerComp.par, 'Fps') and not self.ownerComp.par.Fps.readOnly:
                    fps_value = self.ownerComp.par.Fps.eval()
                    fps_param = model_params['fps']
                    # Use api_type from parameter definition to convert value
                    payload['fps'] = self._convert_parameter_value('fps', fps_value, fps_param)
            
            # Add generate_audio if model supports it AND parameter exists and is enabled
            # NOTE: Explicitly exclude Ltxv models as API doesn't support these parameters
            if 'generate_audio' in model_params and not model.startswith('ltxv/'):
                if hasattr(self.ownerComp.par, 'Generateaudio') and not self.ownerComp.par.Generateaudio.readOnly:
                    audio_value = self.ownerComp.par.Generateaudio.eval()
                    audio_param = model_params['generate_audio']
                    # Use api_type from parameter definition to convert value
                    payload['generate_audio'] = self._convert_parameter_value('generate_audio', audio_value, audio_param)
            
            # Handle multiple reference images (for klingai/video-o1-reference-to-video)
            # This model uses image_url, image_url_2, ..., image_url_7
            if multiple_images and len(multiple_images) > 0:
                # Map images to image_url, image_url_2, ..., image_url_7
                for i, image_data in enumerate(multiple_images, start=1):
                    if i == 1:
                        param_name = 'image_url'
                    else:
                        param_name = f'image_url_{i}'
                    
                    if param_name in model_params and image_data:
                        payload[param_name] = image_data
                        self.logger.log(f"Reference image {i} prepared and included in request payload ({param_name})", level='INFO')
            
            # Handle first frame image (for image-to-video models)
            # Different providers use different parameter names
            # Only include the parameter if we have an image (don't send empty/null values)
            if not multiple_images:  # Only handle single image if not using multiple images
                if 'first_frame_image' in model_params:
                    if first_frame_image:
                        payload['first_frame_image'] = first_frame_image
                        self.logger.log("Reference image prepared and included in request payload (first_frame_image)", level='INFO')
                elif 'image_url' in model_params:
                    if first_frame_image:
                        payload['image_url'] = first_frame_image
                        self.logger.log("Reference image prepared and included in request payload (image_url)", level='INFO')
                elif 'image_urls' in model_params:
                    if first_frame_image:
                        payload['image_urls'] = [first_frame_image]
                        self.logger.log("Reference image prepared and included in request payload (image_urls)", level='INFO')
            
            # Handle last frame image (for models that support last_image_url or tail_image_url)
            if 'last_image_url' in model_params:
                if last_frame_image:
                    payload['last_image_url'] = last_frame_image
                    self.logger.log("Last frame image prepared and included in request payload (last_image_url)", level='INFO')
            
            if 'tail_image_url' in model_params:
                if last_frame_image:
                    payload['tail_image_url'] = last_frame_image
                    self.logger.log("Last frame image prepared and included in request payload (tail_image_url)", level='INFO')
            
            # Truncate prompt for logging (don't log whole prompt)
            prompt_preview = prompt[:50] + '...' if len(prompt) > 50 else prompt
            self.logger.log(f"Creating video task with prompt: '{prompt_preview}'", level='INFO')
            self.logger.log(f"Using model: {model}", level='INFO')
            
            # Step 1: Create video generation task
            response_data = await api_handler.create_generation_task(model_config, payload)
            
            if not response_data:
                return None
            
            # Extract generation ID
            generation_id = api_handler.extract_generation_id(response_data)
            if not generation_id:
                error_msg = "No generation ID in response: " + json.dumps(response_data, indent=2)
                self.logger.log(error_msg, level='ERROR')
                return None
            
            self.logger.log(f"Video task created with ID: {generation_id}", level='INFO')
            
            # Step 2: Poll for video result
            poll_response = await api_handler.poll_generation_result(model_config, generation_id)
            
            if not poll_response:
                return None
            
            # Extract video URL from poll response
            video_url = api_handler.extract_media_url(poll_response, media_type='video')
            if not video_url:
                error_msg = "No video URL in completed response: " + json.dumps(poll_response, indent=2)
                self.logger.log(error_msg, level='ERROR')
                return None
            
            # Step 3: Download and save the video
            # Generate filename and filepath using prompt and node name
            filepath, filename = self._generate_filename(prompt, output_dir, file_extension='.mp4')
            
            # Download video
            success = await api_handler.download_media(video_url, filepath)
            if success:
                self._add_to_saved_files_table(filepath, prompt)
                return filepath
            else:
                return None
                        
        except Exception as e:
            error_msg = f"Unexpected error during video generation: {e}"
            self.logger.log(error_msg, level='ERROR')
            return None

    def Generate(self, prompt=None, output_dir=None, aspect_ratio=None, duration=None, cfg_scale=None, completion_callback=None):
        """
        Generate a video using the AIMLAPI asynchronously.
        Can be called from the pulse button (no args) or programmatically (with args).
        Uses selected model from Model parameter.
        
        Args:
            prompt (str, optional): Text prompt. If None, uses op("PROMPT").text from the PROMPT operator
            output_dir (str, optional): Output directory. If None, uses op.AOP.par.Outputdir (global setting)
            aspect_ratio (str, optional): Aspect ratio. If None, uses self.ownerComp.par.Aspectratio
            duration (int, optional): Video duration in seconds. If None, uses self.ownerComp.par.Duration
            cfg_scale (float, optional): CFG scale. If None, uses self.ownerComp.par.Cfgscale
            completion_callback (callable, optional): Callback function that receives the task object
            
        Returns:
            int: Task ID for tracking the async operation, or None if validation fails
        """
        # Use parameters from component if not provided
        if prompt is None:
            # Get prompt from PROMPT operator (uses base class method)
            prompt = self._get_prompt_from_operator()
        
        # Get selected model from parameter
        model = self._detect_model()
        if not model:
            error_msg = "No model selected. Please select a model from the Model parameter."
            self.logger.log(error_msg, level='ERROR')
            return None
        
        # Get model configuration to check for specific parameter support
        model_config = self.registry.get(model)
        if not model_config:
            error_msg = f"Model {model} not found in registry"
            self.logger.log(error_msg, level='ERROR')
            return None
        
        model_params = model_config.get('parameters', {})
        
        # Check if this is the multiple reference images model (klingai/video-o1-reference-to-video)
        multiple_images = None
        first_frame_image = None
        last_frame_image = None
        
        if model == 'klingai/video-o1-reference-to-video':
            # Collect multiple reference images from REF_IN1-7
            multiple_images = self._get_multiple_reference_images()
            if not multiple_images or len(multiple_images) == 0:
                error_msg = f"Model {model} requires at least one reference image, but none were found. Please provide reference images in REF_IN1-REF_IN7."
                self.logger.log(error_msg, level='ERROR')
                return None
            self.logger.log(f"Using {len(multiple_images)} reference image(s) from REF_IN1-REF_IN7 for model {model}", level='INFO')
        else:
            # Check if model supports image parameters
            supports_image, is_required = self._model_supports_image_parameter(model)
            
            # Get first frame image if model supports it (required or optional)
            if supports_image:
                first_frame_image = self._get_first_frame_image()
                if is_required and not first_frame_image:
                    error_msg = f"Model {model} requires a reference image, but none was found. Please provide a reference image in REF_IN1."
                    self.logger.log(error_msg, level='ERROR')
                    return None
                elif first_frame_image:
                    self.logger.log(f"Using reference image from REF_IN1 for model {model}", level='INFO')
            
            # Check if model supports last frame image (last_image_url or tail_image_url)
            if 'last_image_url' in model_params or 'tail_image_url' in model_params:
                last_frame_image = self._get_last_frame_image()
                if last_frame_image:
                    self.logger.log(f"Using last frame image from REF_IN2 for model {model}", level='INFO')
        
        # Get output directory from global AOP parameter
        if output_dir is None:
            output_dir = op.AOP.par.Outputdir.eval()
        aspect_ratio = aspect_ratio if aspect_ratio is not None else self.ownerComp.par.Aspectratio.eval()
        duration = duration if duration is not None else int(self.ownerComp.par.Duration.eval())
        cfg_scale = cfg_scale if cfg_scale is not None else float(self.ownerComp.par.Cfgscale.eval())
        
        # Set Active to True when starting generation
        self.ownerComp.par.Active = True
        
        # Create completion callback that updates Active status
        def on_completion(task):
            # Check if there are any active tasks remaining
            self._update_active_status()
            # Call user's completion callback if provided
            if completion_callback:
                completion_callback(task)
        
        # Create the async coroutine
        coro = self._generate_video_async(prompt, model, output_dir, duration, aspect_ratio, cfg_scale, first_frame_image, last_frame_image, multiple_images)
        
        # Run it through the async manager
        task_id = self.tdAsyncIO.ext.AsyncIOManager.Run(
            coro,
            description=f"Generate Video: {prompt[:50]}...",
            info={'prompt': prompt[:50] + '...' if len(prompt) > 50 else prompt, 'model': model, 'output_dir': output_dir},
            completion_callback=on_completion
        )
        
        return task_id
    
        
        
