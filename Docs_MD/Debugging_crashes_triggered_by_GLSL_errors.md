# Debugging crashes triggered by GLSL errors

With the transition to Vulkan as the API running TouchDesigner, it's much easier for GLSL code to trigger full scale application when certain illegal operations occur. In particular the errors that can cause a crash are out of bounds array access in either sampler arrays or uniform arrays. 

If you are writing custom GLSL MAT or TOP code and getting a full application crash that says the GLSL may be the culprit. There are a few things to check right off the bat. 
1. In the GLSL TOP, ensure your access to the sTD*Inputs[] arrays is in range. Use the TD_NUM_*_INPUTS defines to add if statements to your code if you are dynamically selecting which input to sample via a variable (instead of a constant).
  2.   3. If using Uniform Arrays (not texture buffers), ensure you are feeding enough data for any array entry that may be accessed by the GLSL code.
  4. Ensure you have no infinite loops such as for loops or while loops.
  5. If your shader is very complex, some GPUs may not be able to complete the work before the OS deciding the app has crashed. You may need to optimize the code for lower end GPUs.

## Robust Buffer Access

Some GPUs have the ability to enable a feature called Robust Buffer Access. This helps protects against crashes caused by GLSL array access issues. It should **not** be used as a way to avoid errors though, and only used as a way to get hints that a crash is caused by out-of-bounds array access. To enable this feature set a system environment variable TOUCH_ROBUST_BUFFER_ACCESS=1 and launch TD. If your crash stops occurring with this set, then it's a hint that the crash is likely due to the GLSL code doing an out-of-bounds array access. If the feature is not supported by your GPU, then a message box will come up stating it's not supported. 

## Nvidia Aftermath

On Nvidia GPUs if you are running into a crash that you can't determine the cause of, you can create a special GPU specific crash file if you set the windows system environment variable TOUCH_ENABLE_NV_AFTERMATH=1. Send this to support@derivative.ca and we can take a closer look at it.
