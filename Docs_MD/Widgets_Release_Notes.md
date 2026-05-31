# Widgets Release Notes

## TDUI 0.26 TDKWidgets Version 0.5.6 - Jan25, 2019

### New Features
* Create/Edit Value Par Exec pulse parameter will add a parameter execute DAT for writing scripts that are attached to Widget Value parameters.
  * Many Widget Sub Component pages have "Customize Interaction" pulse button that provide a Panel Execute DAT connection to the correct sub component for deeper customization of the interaction with the Widget.
  * OP Reference parameters support drag and drop with actual OP type Value parameters supported.
  * New specific widgets support general OP type as well as specific OP types:
1. RenferenceOP
  2. RenferenceCHOP
  3. RenferenceCOMP
  4. RenferenceDAT
  5. RenferenceMAT
  6. RenferenceOBJ
  7. RenferenceSOP
  8. RenferenceTOP

### Bug Fixes and Improvements
* ### Backwards Compatibility
* **BACKWARDS COMPABITILITY WARNING** -
  * All inline script parameters on Widgets have been changed and therefore any scripts on these Widget parameters will have been lost.
  * Python value change execute parameters have been moved to the Value page. They parameters are now called "On Value Change Script", "Off To On Script" and "On To Off Script".
