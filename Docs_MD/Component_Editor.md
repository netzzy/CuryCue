# Component Editor Dialog

## Description  
  
The **Component Editor** is used for many aspects of setting up **custom components** and **Script Operators** (e.g. [Script DAT](<./Script_DAT.md> "Script DAT")), especially the management of **[Custom Parameters](<./Custom_Parameters.md> "Custom Parameters")**. There are also sections for managing **[Extensions](<./Extensions.md> "Extensions")** , **Shortcuts and Tags** , and **[Storage](<./Storage.md> "Storage")**

To open the Component Editor, right-click on the COMP you want to edit and select **Customize Component...**

Each major section of the Component Editor can be collapsed for convenience, and the parameter/page list area can be sized using the handle below it. 

## Header

The header displays and controls which operator you are editing. The name can be changed in the **Component** area. The currently selected component can be changed in the **Path** area. The four **buttons** in the top-right corner will open a **floating viewer** , **parameter dialog** , **network editor** , or this **help page**. 

You can also select which operator to edit by dragging it from a network onto the header. 

## Custom Parameters

The **Custom Parameters** section allows easy editing of a Component's custom [pages](<./Page_Class.md> "Page Class") and [parameters](<./Custom_Parameters.md> "Custom Parameters"). 

### Creating Pages and Parameters

The top two lines of this section are used to create new custom pages and parameters. To create a page, enter the new page name into the text field and press **Add Page**. To create a parameter, enter the new parameter's label into the text field, select the parameter style, select the number of values (if necessary), and press **Add Par**. The label will automatically be converted into a valid parameter name (first letter capital, no special characters) when the parameter is created. If you select a parameter type that can hold a variable number of values (**float** or **int**) you can select a **size** from 1 to 4 as well. 

### Working with the Page and Parameter Lists

The middle area of this section contains a list of the Component's **custom pages** (left) and a list of **custom parameters** (right). The parameter list shows the custom parameters in the currently selected page. Parameters and pages can be dragged to rearrange order. Parameters can also be dragged into different pages. Use **RMB menus** and ctrl-C/ctrl-V for cutting and pasting, including across different Components. Double-click to edit names, and press the 'x' to delete. Drag and drop in the list to reorder them. **TIP:** copying parameters puts them on the clipboard in a human readable JSON format. You can edit these in any text editor, then re-copy them and paste the edited version. 

Dragging a parameter from a **[Parameter Dialog](<./Parameter_Dialog.md> "Parameter Dialog")** into the **Parameter** list duplicates the parameter in your component. A menu will appear with options to automatically create a **[Reference](<./Parameter_Reference.md> "Parameter Reference")** or **[Bind](<./Binding.md> "Binding")** to the new parameter. 
* Bind New Par as Master - put a bind expression on the parameter that was dragged, pointing to the new parameter.
  * Bind New Par as Reference \- put a bind expression on the new parameter, pointing to the parameter that was dragged.
  * Set Reference Expression on Source - put an expression on the parameter that was dragged, pointing to the new parameter.
  * Cancel - do not create an expression or bind expression. Clicking away has the same effect.

### Editing Custom Parameters

When a custom parameter is selected in the list, an editing area is visible below the two lists. This allows changing the custom parameter's settings. The following settings are from top to bottom, with their Python scripting names listed`like this`: 
* **parameter**`tupletName`\- The scripting name of the parameter. Multi-value parameters (e.g. RGB) will have a suffix added to this name for each value.
  * **label**`label`\- The displayed label of the parameter
  * **enable**`enable`\- Disabled pars will be greyed out. Disable parameters that are irrelevant with the current settings
  * **enable expr**`enableExpr`As an alternative to setting the enable state in other scripts, you can enter a Python expression here. If the expression evaluates to True, the parameter will be enabled. This expression evaluates from the context of the custom component. **Example:**`me.par.Useminmax`will enable the parameter if the parameter named`Useminmax`on the same operator evaluates to True.
  * **help**`help`\- The popup help that will be displayed when the parameter's label is hovered over while holding down the Alt key.
  * **read only**`readOnly`\- When True, the parameter value is not settable, but is selectable/copyable and can be referenced by other parameters. This setting is generally used for parameters that are set internally by the component as outputs or informational values. Users can change this setting via the parameter's RMB menu.
  * **section**`section`\- When True, creates a visual divider above the parameter.
  * **style**`style`\- The parameter style (e.g. Int or Float) and the size (when applicable). For information about styles and style-specific values, see [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters").


The above values are common to all parameters. The next section contains values that are specific to certain parameter types and will only appear when applicable. The header contains the actual parameter **name** of each sub-value, when applicable. 
* **default**`default`\- The value is the value that the parameter will be set to when it is "reset" via the parameter RMB menu. The button at the right determines the default mode (constant, expression, or bind). To copy the current parameter value or state (which includes mode data) into the default, click the arrow next to the default section. The menu also includes options for setting all defaults on the page or the entire component.
  * **range min/max**`normMin/normMax`\- The range for parameter sliders. Values outside this range are still allowed in the text entry area and can be set via script.
  * **clamp min/max**`clampMin/clampMax`(checkbox) and`min/max`(value) - define absolute minimums and maximums for the parameter. To enforce clamping, the checkbox to the left of the clamp values must be checked.
  * **menuNames**`menuNames`\- a space separated list of value strings used by menu parameters. This is the actual value that a menu parameter will return. Use quotes for values with spaces in them. Use the **Menu Editor** button for a list-based interface.
  * **menuLabels**`menuLabels`\- a space separated list of label strings used by menu parameters. This is the displayed option that a menu parameter will show in its drop-down. Use quotes for labels with spaces in them. Use the **Menu Editor** button for a list-based interface.
  * **menuSource**`menuSource`\- an expression pointing to another menu parameter or a Python object with`menuNames`and`menuLabels`members. The parameter will retrieve its`menuNames`and`menuLabels`from this source. **TIP:** the utility function`parMenu`in [TDFunctions](<./TDFunctions.md> "TDFunctions") will help create a suitable`menuSource`Python object. You can also use [tdu.TableMenu](<./Tdu_Module.md> "Tdu Module") to create a suitable menuSource object from a table of menu names and labels.

## Extension Code

The **Extension Code** section assists in creating python **[Extensions](<./Extensions.md> "Extensions")** for your custom Component. To create a new extension, simply enter the name in the text field and click **Add**. Once created, you can edit, reinitialize, or delete the extension using the **Edit** , **Init** and **X** buttons on the right. The triangular button expands **Advanced** features that let you create a custom definition and/or name for your extension, or turn Promotion on or off. Use the **+** and **-** buttons to add or remove extension slots. 

**TIP:** It is standard in TouchDesigner to capitalize your extension name and add the suffix **`Ext`**. 

## Shortcuts and Tags

This section lets you set up the identifier features of your Component. You can enter a **[Parent Shortcut](<./Parent_Shortcut.md> "Parent Shortcut")** , a **[Global OP Shortcut](<./Global_OP_Shortcut.md> "Global OP Shortcut")** and add/remove **[Tags](<./Tag.md> "Tag")**. 

Below this, you can set up [Internal Operator](<./Internal_Operators.md> "Internal Operators") shortcuts. Once you have entered a shortcut name in the **Internal OP Shortcut** field, you can use the **Create** button to create an operator if it doesn't exist already. If it does exist, you can enter the path (absolute or relative to the component) in the **Internal OP** field. When that field is pointing to a valid operator, the **Edit** button will open it in the Component Editor. Use the **+** and **-** buttons to add or remove Internal OP shortcut slots. 

## Storage

The **Storage** section gives you direct access to your Component's **[Storage](<./Storage.md> "Storage")** dictionary. You can see all keys and data. Pressing **x** deletes the stored key and data. To change data or keys, double-click on text. To add a new key or refresh the list, use the **Add Key** and **Refresh** buttons at bottom. 

**TIP:** any data you enter will be evaluated by python so if you want to force string type data, enclose it in quotes.
