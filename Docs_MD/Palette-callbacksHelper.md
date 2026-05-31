# Summary  
  
The **callbacksHelper** Component provides an easy setup for Python callbacks on your custom components. It installs and sets up parameters on your component for the [CallbacksExt Extension](<./CallbacksExt_Extension.md> "CallbacksExt Extension"), and provides a few other usability features. 

# Set Up

You can find **callbacksHelper** in the [Palette](<./Palette.md> "Palette") under the folder Derivative>Tools. Drag and drop the component from the [Palette](<./Palette.md> "Palette") into your component and pulse the **Set Up Callbacks** parameter. The callback extension is now installed. Specifically: 
* an extension parameter block is added to your component
  * the necessary extension parameters are set up on your component on a new **Callbacks** page.
  * a callback DAT is now docked to you custom component


Note that once the callback system is set up, you still need to leave the callbacksHelper component inside your custom component. 

# Invoking Callbacks

To invoke a callback from the user's callback DAT, simply call the`DoCallback`function on your custom component. To see an example immediately after set up, open a textport and call`<your comp>.DoCallback('onTest', {'extraInfo': 'whatever you want'}`. For more info about **DoCallback** and **CallbacksExt** see the [CallbacksExt Extension](<./CallbacksExt_Extension.md> "CallbacksExt Extension") page. 

# Creating a Default Callbacks DAT

You will find a **defaultCallbacks DAT** docked to callbacksHelper when you drop it. Inside here, you can set up all the default callback stubs and documentation for your component's callback system. At any time, you can pulse **Reset Callback DAT To Default** on the callbacksHelper to copy these default callbacks into the callback DAT docked to your custom component. 

# Parameters

callbacksHelper features are generally accessed using its custom parameters. 

**COMP**`Comp`\- The top level component on which to set up the callback system. This allows you to put callbacksHelper deeper into your custom component if desired. 

**Set Up Callbacks**`Setups`\- Set up the callback system. 

**Edit Default Callbacks DAT**`Editdefaultcallbacksdat`\- Open the default callbacks DAT (the one attached to callbacksHelper) in your default editor 

**Reset Callback DAT To Default**`Resetcallbackdat`\- Copy the text from the default callbacks DAT into the callbacks DAT attached to your custom component 

**Auto-create Callback DAT**`Autocreatecallbackdat`\- When on, in the case that your custom component is dropped in a network and no callback DAT is found, one will automatically be created and docked to your component. 

**Default Callbacks DAT**`DefaultcallbacksDAT`\- The DAT containing your default callback text
