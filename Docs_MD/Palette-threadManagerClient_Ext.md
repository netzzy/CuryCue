# Palette:threadManagerClient Ext

These Extensions reference a specific [Palette:threadManagerClient](<./Palette-threadManagerClient.md> "Palette:threadManagerClient"). This is the extension of the ThreadManagerClient.   
  
# ClientQueueManager

A wrapper to handle both the Refresh queues and the success payload. 

## Members`refreshPayloadQueue`→`queue.Queue`: 

> The queue to be used for refresh payloads, during execution of the threaded method.`successPayload`→`Object`: 

> A member that can hold a generic object such as a dict, to be used on success.`stateLock`→`threading.Lock`: 

> A lock to be used when accessing the success payload. The queue does not require a lock.

## Methods`ClientQueueManager.AddInRefreshQueue(data: object)`→`None`: 

> Put in queue without blocking execution the object passed as data.`ClientQueueManager.SetSuccessPayload(data: object)`→`None`: 

> Set the success payload from the threaded method to be used in the main thread success method. This is relying on the stateLock. 
> 
> Args: 
> 
>   * data (object): The object to be set as the successPayload.
>`ClientQueueManager.GetSuccessPayload()`→`object`: 

> Get the success payload relying on state lock.`ClientQueueManager.Reset()`→`None`: 

> Reset the ThreadManagerClient COMP to a default state.

# ThreadManagerClientExt

This is the extension of the ThreadManagerClient. 

The ThreadManagerClient is a custom TouchDesigner component designed to rely on the Thread Manager COMP. 

The ThreadManagerClient is designed around it's callback DAT. Users should review the template code and adapt it to their own cases. 

The customized methods implemented in the ThreadManagerClient Callback are generating a TDTask that gets passed to the Thread Manager TDTask queue. 

Keep in mind that users need to be cautious when using threading in TouchDesigner. As a rule of thumb don't access objects from the main TouchDesigner thread such as OPs, COMPs, Parameters, from another thread. Whether it be for writing, reading, or any other operation. 

While advanced developers can rely on the Thread Manager directly,users not familiar with threading should consider using the ThreadManager Client instead. 

## Members`threadManager`→`Thread Manager COMP`: 

> The Thread Manager that this client is relying on.`logger`→`Logger COMP`: 

> Reference to a local TouchDesigner Logger. Not to be used within a thread.`safeLogger`→`logging.Logger`: 

> Reference to the python logger object of a local TouchDesigner Logger. Can be used safely in threaded methods.`clientQueueManager`→`ClientQueueManager`: 

> The clientQueue manager used as a helper for the ThreadManagerClient.`callbackDat`→`Text DAT`: 

> The DAT used for callbacks.

TouchDesigner Build: Latest\nwikieditor2025.30000
