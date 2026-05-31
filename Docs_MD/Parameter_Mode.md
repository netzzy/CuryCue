# Parameter Mode

Every [Parameter](<./Parameter.md> "Parameter") can be in one of four modes: Constant Mode, [Expression](<./Expression.md> "Expression") Mode, [Export](<./Export.md> "Export") Mode or Bind ([Binding](<./Binding.md> "Binding")) Mode. 

Move the cursor over any parameter and press the + that appears. It exposes a new line where you can quickly switch the parameter mode: 
* Constant value (grey box)
  * Expression (blue box)
  * Export (green box)
  * Bind (purple box)


Every parameter holds a constant value. Optionally, a python expression can be added to any parameter. The parameter can save different values in both modes and the mode can changed between constant or expression at any time. Click on the blue box to enter python expression mode, and on the grey box to return to constant value mode. 

Export mode can only be selected if there is already an [Export](<./Export.md> "Export") to the parameter. When an export is created to a parameter, the mode will be automatically set to export. After this export connection has been made, the parameter can be set to constant or expression and back to export at any time. This can be a helpful way to temporarily break an export connection when developing or debuging (ie. switch to constant mode and test specific values). 

[Binding](<./Binding.md> "Binding") links parameters together in bi-directional connection. In this mode, changing the value via the UI or a python script will update the value of both (two or more) parameters and keep them in sync. 

See [Working with Parameter Modes](<./Parameter_Dialog.htm#Working_with_Parameter_Modes> "Parameter Dialog") in the Parameters Dialog for more details. 

To change Parameter Mode using python, see`mode`member of [![PythonIcon.png](./images/c/c2/PythonIcon.png)](</File:PythonIcon.png>) [Par Class](<./Par_Class.md> "Par Class").
