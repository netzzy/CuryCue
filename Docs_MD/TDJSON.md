# Summary

The **TDJSON** module provides a variety of Python utility functions for JSON features in TouchDesigner. Most of the functions deal with [Custom Parameters](<./Custom_Parameters.md> "Custom Parameters") and [Parameter Pages](<./Page_Class.md> "Page Class"), but some are good for more general use. When the documentation below refers to a "**JSON object** " it means a JSONable Python object, while "JSON text" is a text representation of such an object. 

To use TDJSON put the following line at the top of your Python script:`import TDJSON`You can now use any of the following functions by calling:`TDJSON.<function name>(...)`**Tip:** See also [JSON DAT](<./JSON_DAT.md> "JSON DAT") for automated conversion and filtering. 

**See also:** [JSON](<./JSON.md> "JSON"), [JSON](<http://www.json.org/>), [JSON overview](<https://www.makeuseof.com/tag/json-laymans-overview/>)

**Note:** older versions of TouchDesigner required this to import TDJSON:`TDJSON = op.TDModules.mod.TDJSON`# Functions

**`jsonToText(jsonObject, indent='\t')`** → **`JSON text (from json.dumps)`**

    Return a JSON object as JSON text with tab indents for readability. 

  *`jsonObject`\- a JSONable Python object.
  *`indent`\- **(Optional)** The indent argument to json.dumps. Defaults to '\t' for readability.


Set to None for default json.dumps behavior. 

**`jsonToDat(jsonObject, dat)`**

    Write a JSON object as JSON text into a dat. 

  *`jsonObject`\- a JSONable Python object.
  *`dat`\- a DAT to be filled with the JSON text (uses jsonToText). Other text will be overwritten.


**`textToJSON(text, orderedDict=True, showErrors=False)`** → **`JSON object or None`**

    Turn JSON text into a JSON Python object. Returns None if conversion fails unless`showErrors`is True. 

  *`text`\- a JSON text string.
  *`orderedDict`\- **(Optional)** If True, the JSON object returned will be an OrderedDict (from core python module 'collections').
  *`showErrors`\- **(Optional)** if True, raise an exception for conversion errors, otherwise return None if there is an error.


**`datToJSON(dat, orderedDict=True, showErrors=False)`** → **`JSON object or None`**

    Turn JSON text stored in a DAT into a JSON Python object. Returns None if conversion fails unless`showErrors`is True. 

  *`dat`\- a DAT containing a JSON text string.
  *`orderedDict`\- **(Optional)** if True, the JSON object returned will be an OrderedDict (from core python module 'collections').
  *`showErrors`\- **(Optional)** if True, raise an exception for conversion errors, otherwise return None if there is an error.


**`serializeTDData(data, verbose=True)`** → **`JSONable data as is, TD serializable format, or repr(data)`**

    Return a serializable value for a piece of TD data. Standardizes serialized format for TD types OP, Cell, Channel, Page, Par, ParGroup, ParMode. Returns int, float, str, bool, None without change. Returns list or dict without change if JSONable. Other cases return`repr(data)`. 

  *`data`\- anything
  *`verbose`\- **(Optional)** if True, provide full details for TD objects, if not, some extra data will be required when deserializing.


**`deserializeTDData(data, verboseData=None)`** → **`TD object if appropriate info is provided. Otherwise returns data argument unchanged.`**

    return a TD object if data is in format returned by serializeTDData method with verbose=True. If verbose was not set to True, additionalInfo must be provided if a TD object is to be returned. If a TD object is not returned, data will be returned unchanged. 

  *`data`\- anything
  *`verboseData`\- **(Optional)** The following lists must be provided to get a TD object back for non-verbose data created by serializeTDData:
* OP:`['OP']`* ParMode:`['ParMode']`* Par:`['Par', _< Par owner path>_]`* ParGroup:`['ParGroup', _< ParGroup owner path>_]`* Page:`['Page', _< Page owner path>_]`* Channel:`['Channel', _< Channel owner path>_]`* Cell:`['Cell', _< Cell owner path>_]`**`parameterToJSONPar(p, extraAttrs=None, forceAttrLists=False)`** → **`JSON object`**

    Convert a custom parameter, ParGroup, or tuplet to a JSONable Python dict. **NOTE** : a parameter that is a member of a multi-value tuplet will create a JSON object for the entire tuplet. 

  *`p`\- parameter, parGroup, or tuplet
  *`extraAttrs`\- **(Optional)** a list or tuple of attribute names that are not normally stored as part of a parameter's definition e.g. 'val' and 'order'. Can also be a string: '*' indicating all properties of the parameter.
  *`forceAttrLists`\- **(Optional)** If True, all attributes will be stored in a list with the length of the tuplet


**`pageToJSONDict(page, extraAttrs=None, forceAttrLists=False)`** → **`JSON object`**

    Convert a custom page of parameters into a JSONable Python dict. Format: {parameter name: {parameter attributes, ...}, ...} 

  *`page`\- the page to convert.
  *`extraAttrs`\- **(Optional)** a list or tuple of attribute names that are not normally stored as part of a parameter's definition e.g. 'val' and 'order'. Can also be a string: '*' indicating all serializable properties of the parameter.
  *`forceAttrLists`\- **(Optional)** If True, all attributes will be stored in a list with the length of the tuplet


**`opToJSONOp(o, extraAttrs=None, forceAttrLists=False, includeCustomPages=True, includeBuiltInPages=False)`** → **`JSON object`**

    Convert all custom parameter pages to a JSONable python dict. Format: {page name: {parameter name: {parameter attributes, ...}, ...}, ...} 

  *`o`\- the OP to convert.
  *`extraAttrs`\- **(Optional)** a list or tuple of attribute names that are not normally stored as part of a parameter's definition e.g. 'val' and 'order'. Can also be a string: '*' indicating all properties of the parameter.
  *`forceAttrLists`\- **(Optional)** If True, all attributes will be stored in a list with the length of the tuplet
  *`includeCustomPages`\- **(Optional)** If True, include custom par pages
  *`includeBuiltInPages`\- **(Optional)** If True, include builtin pages


**`addParameterFromJSONDict(comp, jsonDict, replace=True, setValues=True, ignoreAttrErrors=False, fixParNames=True, setBuiltIns=False)`** → **`tuple of newly created pars`**

    Add a parameter to`comp`as defined in a parameter JSON object. To set values, expressions, or bind expressions, provide 'val', 'expr', or 'bindExpr' in JSON. 

  *`comp`\- the COMP to add parameters to.
  *`jsonDict`\- the parameter JSON dict.
  *`replace`\- **(Optional)** If False, will cause exception if a parameter already exists.
  *`setValues`\- **(Optional)** If True and no "val" item is provided in the JSON dict, parameter values will be set to their defaults, whether the parameter already existed or not.
  *`ignoreAttrErrors`\- **(Optional)** If True, no exceptions will be raised for invalid attributes in the JSON.
  *`fixParNames`\- **(Optional)** If True, force correct capitalization.
  *`setBuiltIns`\- **(Optional)** If True, set values of builtin parameters if they are found in the JSON.


**`addParametersFromJSONList(comp, jsonList, replace=True, setValues=True, destroyOthers=False, newAtEnd=True, fixParNames=True, setBuiltIns=False)`** → **`tuple with (newParNames, newPageNames)`**

    Add parameters to`comp`as defined in list of parameter JSON dicts. 

  *`comp`\- the COMP to add parameters to.
  *`jsonList`\- the list of par JSON dicts.
  *`replace`\- **(Optional)** If False, will cause exception if a parameter already exists.
  *`setValues`\- **(Optional)** If True and no "val" item is provided in the JSON dict, parameter values will be set to their defaults, whether the parameter already existed or not.
  *`destroyOthers`\- **(Optional)** If True, pars and pages not in jsonList will be destroyed
  *`newAtEnd`\- **(Optional)** If True, new parameters will be sorted to end of page. This should generally be False if you are using 'order' attribute in JSON
  *`fixParNames`\- **(Optional)** If True, force correct capitalization.
  *`setBuiltIns`\- **(Optional)** If True, set state of builtin parameters if they are found in the JSON.


  
**`addParametersFromJSONDict(comp, jsonDict, replace=True, setValues=True, destroyOthers=False, newAtEnd=True, fixParNames=True, setBuiltIns=False)`** → **`tuple with (newParNames, newPageNames)`**

    Add parameters to`comp`as defined in dict of parameter JSON dicts. 

  *`comp`\- the COMP to add parameters to.
  *`jsonDict`\- the dict of par JSON dicts.
  *`replace`\- **(Optional)** If False, will cause exception if a parameter already exists.
  *`setValues`\- **(Optional)** If True and no "val" item is provided in the JSON dict, parameter values will be set to their defaults, whether the parameter already existed or not.
  *`destroyOthers`\- **(Optional)** If True, pars and pages not in jsonDict will be destroyed
  *`newAtEnd`\- **(Optional)** If True, new parameters will be sorted to end of page. This should generally be False if you are using 'order' attribute in JSON
  *`fixParNames`\- **(Optional)** If True, force correct capitalization.
  *`setBuiltIns`\- **(Optional)** If True, set values of builtin parameters if they are found in the JSON.


  
**`addParametersFromJSONOp(comp, jsonOp, replace=True, setValues=True, destroyOthers=False, newAtEnd=True, fixParNames=True, setBuiltIns=False)`** → **`tuple with (newParNames, newPageNames)`**

    Add parameters to`comp`as defined in dict of page JSON dicts ala`opToJSONOp`. 

  *`comp`\- the COMP to add parameters to.
  *`jsonOp`\- the dict of page JSON dicts.
  *`replace`\- **(Optional)** If False, will cause exception if a parameter already exists.
  *`setValues`\- **(Optional)** If True and no "val" item is provided in the JSON dict, parameter values will be set to their defaults, whether the parameter already existed or not.
  *`destroyOthers`\- **(Optional)** If True, pars and pages not in jsonOp will be destroyed
  *`newAtEnd`\- **(Optional)** If True, new parameters will be sorted to end of page. This should generally be False if you are using 'order' attribute in JSON
  *`fixParNames`\- **(Optional)** If True, force correct capitalization.
  *`setBuiltIns`\- **(Optional)** If True, set values of builtin parameters if they are found in the JSON.


  
**`destroyOtherPagesAndParameters(comp, pageNames, parNames)`**

    Destroys all pages and parameters on`comp`that are not found in`pageNames`or`parNames`. 

  *`comp`\- the COMP to destroy pages and parameters on.
  *`pageNames`\- an iterable of names of pages to keep.
  *`parNames`\- an iterable of names of pars to keep.


TouchDesigner Build: Latest\nwikieditorwikieditor2023.112802022.241402021.100002018.28070before 2018.28070
