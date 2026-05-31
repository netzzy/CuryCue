# Macro

A **macro** is a single word that represents a script of commands. The user can pass arguments to the script via the macro. Macros are written in the legacy [Tscript](<./Tscript.md> "Tscript"). 

The F1 to F12 keys run macros. The F1 macro puts you in [Perform Mode](<./Perform_Mode.md> "Perform Mode"). Pressing F9 or F10 over a panel brings up the network of the panel element you are pointing at. 

Access Macros via Dialogs -> Macros in the TouchDesigner menu bar, and learn about the dialog at [Macros Dialog](<./Macros_Dialog.md> "Macros Dialog"). 

Macros can be created locally in any component. A Text DAT placed inside a component's`local/macros`component will define a macro for the component, the name of the macro is the name of the Text DAT. TouchDesigner will search for a macro in the current component first, if not found it will look in the parent component, and so on up to the [Root](<./Root.md> "Root"). Any macro defined in the root will be available for use anywhere in the project. 

Macros can also be defined more simply by using the [Tscript](<./Tscript.md> "Tscript")`Macro`Command. 

See also [Script](<./Script.md> "Script"), [DAT](<./DAT.md> "DAT") and [Python](<./Python.md> "Python").
