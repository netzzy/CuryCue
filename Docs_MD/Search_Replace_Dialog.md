# SearchReplace Dialog

The Search/Replace Dialog will find, and optionally replace, all occurrences of a given bit of text in a network. It has a wide range of options to narrow search criteria to find exactly what you're looking for. 

This is a great tool for analyzing and editing nodes spread out in your projects. See "Results Area" below. 

Replace operations can be undone. 

# 

Search/Replace - Basic Mode

## Settings

**Path** \- The path to search in. 

**Search** \- The text to search for. 

**Replace** \- The text to replace the Search text with. 

**Options**
* **Case Sensitive** \- Only match text with matching capitalization.
  * **Whole Words** \- Don't match when the Search text is part of a larger word. Any character that is non-alphanumeric and not an underscore is considered a word break.
  * **Regular Expressions** \- Use [regular expressions](<./Palette-searchReplace.htm#Regular_Expressions> "Palette:searchReplace") in Search and Replace text. **Note:** the Search/Replace Dialog does not use wildcards. Use this feature for non-specific searches.


**Display**
* **Relative Paths** \- Display path names starting at the specified search Path.
  * **OP Types** \- Display a column with type of each found Operator.
  * **Found In** \- Display a column with info about where in the Operator the text was found.

## Buttons

**Search** \- refresh the search based on current settings. This must be done each time the settings are changed to update results. 

**Replace** \- replace specified Search text with specified Replace text. This operation can be undone normally. 

## Results Area

**Click on a result** \- Open a floating network viewer of the result. 

**Hold mouse down on a result** \- Pick a pane to show the network of the result. Further clicks will show the result networks in that pane. 

**Drag a result** \- Drags the result operator as if you were dragging it from a network. 

**Right Mouse Button on result** \- Open the options menu for the result. 

# 

Search/Replace - Advanced Mode

## Additional Settings

**OP Types** \- A space separated list of OP types to display in results. If a listed type matches an Operator class name exactly, that class will be included. If not, all operators with the given text in their type label will be included. The dropdown has options for all available operator types. 

**Filter Script** \- A Python expression that will be tested for each "operator" found in the search. If the expression is True, the operator will be included. The dropdown has some example expressions. 

**Max Depth** \- Limits the network depth of the search from the specified Path. 0 means only search the operator in Path, not its children. 1 includes the operator's children, but not its grand-children, etc. 

**Include**
* **Non-Editable DATs** \- Include text found in DATs that cannot be edited. This text will not be affected by Replace operations.
  * **Built-in Pars/Pages** \- Include built-in parameter and page names. These names will not be affected by Replace operations.
  * **Hidden OPs** \- Include operators with their`expose`member set to false, including TouchDesigner system operators.


**Search In** \- These checkboxes select which areas of an operator will be searched for the chosen text. 

## Buttons

**Search** \- refresh the search based on current settings. This must be done each time the settings are changed to update results, unless the **lock checkbox** is on. When on, the search is refreshed whenever a setting changes. Note that even when the lock is on, the search must be refreshed manually to reflect changes in the searched network. 

**Replace Selected** \- replace selected items in the search results . 

**Replace All** \- replace all items in the search results. 

## Results Area

**Click on a result** \- Select the search result. **Ctrl-click** can be used to select/de-select more results. **Shift-click** can be used to select a series of consecutive results. 

**Hold mouse down on a result** \- Pick a pane to show the network of the result. Further clicks will show the result networks in that pane. 

**Drag a result** \- Drags the result operator as if you were dragging it from a network. 

**Right Mouse Button on result** \- Open the options menu for the result.
