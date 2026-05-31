"""
DotChatUtil - Base utility class for TouchDesigner chat/language operators.
Provides common functionality for parameter creation, setup, and standardization.
"""

import datetime
import sys

class AopUtil:
    def __init__(self, ownerComp, default_color=(0.98, 0.52, 0.02), **kwargs):
        """
        Initialize the utility class with an owner component.
        
        Args:
            ownerComp: The TouchDesigner component this utility is attached to
            default_color (tuple): Default RGB color for the operator
            **kwargs: Additional keyword arguments including:
                     - mac_compatible (bool): Whether the operator works on macOS
        """
        self.ownerComp = ownerComp
        self.default_color = default_color
        
        # Platform compatibility (defaults to True for backwards compatibility)
        self.mac_compatible = kwargs.get('mac_compatible', True)
        self.is_mac = sys.platform == 'darwin'
        
        # Define colors - using instance variables to allow override
        self.compatible_color = default_color
        self.incompatible_color = kwargs.get('incompatible_color', (0.5, 0.1, 0.1))
        self.disabled_color = kwargs.get('disabled_color', (0.2, 0.2, 0.2))
        
        # Setup initial state
        self.initialize()
        
    def initialize(self):
        """Set up initial state and configuration."""
        # Initialize basic operator settings
        self.ownerComp.tags.add('LOP')  # Language Operator tag
        self.setup_about_page()
        self.set_color()
        
    def create_parameter(self, par_name, par_type, page='Custom', default=None, norm_min=None, norm_max=None, size=1, menu_items=None, label=None, order=None, replace=False, section=None, menuNames=None, menuLabels=None, help_text=None, help = None):
        '''
        Creates a custom parameter on a specified page in a TouchDesigner component, supporting a wide 
        range of parameter types. This function allows for creating basic types like 'float', 'int', 
        'str', 'bool', and 'menu', as well as node reference types such as 'op', 'comp', etc. Advanced 
        options like 'label', 'order', and 'replace' enable further customization. For 'float' and 'int' 
        types, 'size' determines the number of values associated with the parameter. The 'default' 
        parameter sets the initial value, with special handling for 'menu' types where it sets the menu 
        options. If 'replace' is set to False, the function errors if the parameter already exists.

        Parameters:
        par_name (str): The name of the parameter. 
        par_type (str): The type of the parameter. Supported types are:
                        'float', 'int', 'str', 'bool', 'menu', 'op', 'comp', 'object', 'panelcomp', 
                        'top', 'chop', 'sop', 'mat', 'dat', 'xy', 'xyz', 'xyzw', 'wh', 'uv', 'uvw', 
                        'rgb', 'rgba', 'file', 'folder', 'pulse', 'momentary', 'python', 'par', 'header'.
        page (str): The page name where the parameter will be added. Defaults to 'Custom'.
        default: The default value for the parameter. For 'menu', it should be a list of strings.
        norm_min, norm_max (optional): Normalized minimum and maximum values for 'float' and 'int' types.
        size (int, optional): Number of values for 'float' and 'int' types. Defaults to 1.
        menu_items (list of str, optional): List of menu items for 'menu' type parameters.
        label (str, optional): Display label of the parameter. Defaults to par_name.
        order (int, optional): Display order of the parameter.
        replace (bool, optional): Determines whether to replace an existing parameter. Defaults to True.
                                If set to False, the function errors if the parameter already exists.
        section (bool, optional): If set to True, adds a visual separator above this parameter. Useful for organizing parameters into distinct sections on the UI.
        menuNames (list of str, optional): List of menu names for 'menu' type parameters.
        menuLabels (list of str, optional): List of menu labels for 'menu' type parameters.

        Returns:
        The created parameter object.
        '''
        # print(f"Creating parameter: Name: {par_name}, Type: {par_type}, Page: {page}")
        # Check if the parameter already exists
        if hasattr(self.ownerComp.par, par_name):
            if not replace:
                # If the parameter exists and 'replace' is False, skip creating the parameter
                return getattr(self.ownerComp.par, par_name)
        # Check if the page exists
        custom_page = next((p for p in self.ownerComp.customPages if p.name == page), None)
        if not custom_page:
            # If the page doesn't exist, create it
            custom_page = self.ownerComp.appendCustomPage(page)
        # Mapping for parameter creation based on type
        create_method = {
            'float': lambda: custom_page.appendFloat(par_name, label=label, size=size, order=order, replace=replace),
            'int': lambda: custom_page.appendInt(par_name, label=label, size=size, order=order, replace=replace),
            'str': lambda: custom_page.appendStr(par_name, label=label, order=order, replace=replace),
            'string': lambda: custom_page.appendStr(par_name, label=label, order=order, replace=replace),
            'bool': lambda: custom_page.appendToggle(par_name, label=label, order=order, replace=replace),
            'toggle': lambda: custom_page.appendToggle(par_name, label=label, order=order, replace=replace),
            'menu': lambda: custom_page.appendMenu(par_name, label=label, order=order, replace=replace),
            'strmenu': lambda: custom_page.appendStrMenu(par_name, label=label, order=order, replace=replace),
            'op': lambda: custom_page.appendOP(par_name, label=label, order=order, replace=replace),
            'comp': lambda: custom_page.appendCOMP(par_name, label=label, order=order, replace=replace),
            'object': lambda: custom_page.appendObject(par_name, label=label, order=order, replace=replace),
            'panelcomp': lambda: custom_page.appendPanelCOMP(par_name, label=label, order=order, replace=replace),
            'top': lambda: custom_page.appendTOP(par_name, label=label, order=order, replace=replace),
            'chop': lambda: custom_page.appendCHOP(par_name, label=label, order=order, replace=replace),
            'sop': lambda: custom_page.appendSOP(par_name, label=label, order=order, replace=replace),
            'mat': lambda: custom_page.appendMAT(par_name, label=label, order=order, replace=replace),
            'dat': lambda: custom_page.appendDAT(par_name, label=label, order=order, replace=replace),
            'xy': lambda: custom_page.appendXY(par_name, label=label, order=order, replace=replace),
            'xyz': lambda: custom_page.appendXYZ(par_name, label=label, order=order, replace=replace),
            'xyzw': lambda: custom_page.appendXYZW(par_name, label=label, order=order, replace=replace),
            'wh': lambda: custom_page.appendWH(par_name, label=label, order=order, replace=replace),
            'uv': lambda: custom_page.appendUV(par_name, label=label, order=order, replace=replace),
            'uvw': lambda: custom_page.appendUVW(par_name, label=label, order=order, replace=replace),
            'rgb': lambda: custom_page.appendRGB(par_name, label=label, order=order, replace=replace),
            'rgba': lambda: custom_page.appendRGBA(par_name, label=label, order=order, replace=replace),
            'file': lambda: custom_page.appendFile(par_name, label=label, order=order, replace=replace),
            'folder': lambda: custom_page.appendFolder(par_name, label=label, order=order, replace=replace),
            'pulse': lambda: custom_page.appendPulse(par_name, label=label, order=order, replace=replace),
            'momentary': lambda: custom_page.appendMomentary(par_name, label=label, order=order, replace=replace),
            'python': lambda: custom_page.appendPython(par_name, label=label, order=order, replace=replace),
            'par': lambda: custom_page.appendPar(par_name, label=label, order=order, replace=replace),
            'header': lambda: custom_page.appendHeader(par_name, label=label, order=order, replace=replace)
        }.get(par_type.lower())

        if create_method is None:
            raise ValueError(f"Unsupported parameter type: {par_type}")

        new_param_group = create_method()

        if new_param_group is None:
            raise Exception("Parameter group creation failed")

        if not hasattr(new_param_group, 'pars'):
            raise Exception(f"Expected ParGroup, got {type(new_param_group)}")

        new_param = new_param_group[0] if new_param_group.pars else None

        if new_param is None:
            raise Exception("Parameter creation failed")
        # Set default, norm_min, norm_max, and menu_items based on the parameter type
        if par_type.lower() == 'menu' or par_type.lower() == 'strmenu':
            if menuNames:
                new_param.menuNames = menuNames
            elif menu_items:
                new_param.menuNames = menu_items
            if menuLabels:
                new_param.menuLabels = menuLabels
            elif menu_items:
                new_param.menuLabels = menu_items
        if default is not None:
            if par_type.lower() == 'rgb':
                # RGB parameters create three sub-parameters (r,g,b)
                if isinstance(default, (list, tuple)) and len(default) == 3:
                    setattr(self.ownerComp.par, f"{par_name}r", default[0])
                    setattr(self.ownerComp.par, f"{par_name}g", default[1])
                    setattr(self.ownerComp.par, f"{par_name}b", default[2])
            else:
                setattr(self.ownerComp.par, par_name, default)


        if par_type in ['float', 'int']:
            if norm_min is not None:
                new_param.normMin = norm_min
                new_param.min = norm_min
                new_param.clampMin = True
            if norm_max is not None:
                new_param.normMax = norm_max
                new_param.max = norm_max
                new_param.clampMax = True

        if section:
            new_param.startSection = True
        if help_text:
            new_param.help = help_text
        if help:
            new_param.help = help
        return new_param
            
    def setup_table(self, table_name, headers=None):
        """Create or get a Table DAT with optional headers."""
        table = self.ownerComp.op(table_name)
        if table is None:
            table = self.ownerComp.create(tableDAT, table_name)
            table.clear()
            if headers:
                table.appendRow(headers)
        return table
        
    def setup_text_dat(self, dat_name):
        """Create or get a Text DAT."""
        text_dat = self.ownerComp.op(dat_name)
        if text_dat is None:
            text_dat = self.ownerComp.create(textDAT, dat_name)
        return text_dat
        
    
    def setup_about_page(self):
        """Configure the About page with version info and standard parameters."""
        about_page = next((p for p in self.ownerComp.customPages if p.name == 'About'), None)
        if not about_page:
            about_page = self.ownerComp.appendCustomPage('About')
            
        # Create standard About page parameters
        self.create_parameter('Bypass', 'bool', 'About', 
                            label='Bypass', default=False)
        self.create_parameter('Showbuiltin', 'bool', 'About',
                            label='Show Built-in Parameters', default=False)
                            
        version_par = self.create_parameter('Version', 'str', 'About',
                                             label='Version', 
                                             default='1.0.0', # Default handled below
                                             section=True,)
        version_par.readOnly = True
        
        
    def set_color(self, color=None):
        """Set the operator color based on platform compatibility and bypass state."""
        if self.ownerComp.par.Bypass.eval():
            self.ownerComp.color = self.disabled_color
            return
            
        # Only apply incompatible color if explicitly set as incompatible
        if self.is_mac and self.mac_compatible is False:
            self.ownerComp.color = self.incompatible_color
            return
            
        self.ownerComp.color = color if color else self.compatible_color
            
    def show_builtin(self):
        """Toggle built-in parameters visibility."""
        self.ownerComp.showCustomOnly = 1 - self.ownerComp.par.Showbuiltin.eval()
        
    def increment_version(self, level='patch'):
        """
        Increment the version number.
        
        Args:
            level (str): Version part to increment ('major', 'minor', or 'patch')
        """
        version = self.ownerComp.par.Version.eval()
        major, minor, patch = map(int, version.split('.'))
        
        if level == 'major':
            major += 1
            minor = 0
            patch = 0
        elif level == 'minor':
            minor += 1
            patch = 0
        elif level == 'patch':
            patch += 1
            
        new_version = f"{major}.{minor}.{patch}"
        self.ownerComp.par.Version = new_version
        self.ownerComp.par.Lastupdated = datetime.datetime.now().strftime('%Y-%m-%d')
        
    def Bypass(self):
        """Handle bypass state change."""
        self.set_color()
        
    def Showbuiltin(self):
        """Handle show built-in parameters toggle."""
        self.show_builtin()