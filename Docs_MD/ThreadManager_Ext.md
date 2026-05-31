# ThreadManager Ext

The extension for the [Thread Manager](<./Thread_Manager.md> "Thread Manager"). 

# TDTask

A task to be created and passed to the ThreadManager task queue. A TDTask should always be enqueued to the Manager using the ThreadManagerExt.EnqueueTask method. 

Args: 
* target (Callable): The main method to be called in the thread. Args and kwargs are passed to this method when executed.
  * SuccessHook (Callable, optional): The method to be called uppon completion of the target method, in the main thread. Defaults to None.
  * ExceptHook (Callable, optional): The method to be called in case of exception, in the main thread, while executing the target method. Defaults to None.
  * RefreshHook (Callable, optional): The method to be called every frames, in the main thread, while the target method is executing. Defaults to None.
  * args (tuple, optional): A tuple of arguments to be passed to the target method. Defaults to ().
  * kwargs (dict, optional): A dictionary of keyword arguments to be passed to the target method. Defaults to None.

## Members`Manager`→`ext.ThreadManagerExt`: 

> The ThreadManager extension from which this TDTask was Enqueued.`SuccessHook`→`Callable`: 

> The method to be called upon completion of the target method, in the main thread. Defaults to None.`ExceptHook`→`Callable`: 

> The method to be called in case of exception, in the main thread, while executing the target method. Defaults to None.`RefreshHook`→`Callable`: 

> The method to be called every frames, in the main thread, while the target method is executing. Defaults to None.`State`→`ext.ThreadManagerExt.TDTaskStates`: 

> The current TDTaskState of the TDTask. Default to TDTaskStates.STANDBY.`RanBy`→`int`: 

> The ID of the TDThread that picked this TDTask for execution. Default to None.`StateLock`→`threading.Lock`: 

> A threading lock used to access TDTask members safely.

## Methods`TDTask.GetStateSafe()`→`TDTaskStates`: 

> Helper method designed to be safe to use in a threading context.`TDTask.SetStateSafe(state: ext.ThreadManagerExt.TDTaskStates)`→`None`: 

> Helper method designed to be safe to use in a threading context. Set the current TDTaskState of the TDTask.`TDTask.GetRanBySafe()`→`int`: 

> Helper method designed to be safe to use in a threading context. Return the ID of the TDThread that picked the TDTask for execution.`TDTask.SetRanBySafe(ranBy: int)`→`None`: 

> Helper method designed to be safe to use in a threading context. Set the current ID of the TDThread that picked this TDTask for execution.

# TDThread

A thread with a few extras that are TD specifics. 

Inheriting from the threading.Thread class. 

Args: 
* target (Callable): The main method to be called in the thread. Args and kwargs are passed to this method when executed.
  * SuccessHook (Callable, optional): The method to be called uppon completion of the target method, in the main thread. Defaults to None.
  * ExceptHook (Callable, optional): The method to be called in case of exception, in the main thread, while executing the target method. Defaults to None.
  * RefreshHook (Callable, optional): The method to be called every frames, in the main thread, while the target method is executing. Defaults to None.
  * task (TDTask, optional): A TDTask to be passed when enequeuing for immediate or standalone run. Defaults to None.
  * InPool (bool, optional): A boolean used to create the TDThread as a Worker Thread, part of a pool. Defaults to False.
  * InfoQueue (queue, optional): A queue to be used to exchange data between this thread and the main thread. Defaults to None.

## Members`TDTask`→`ext.ThreadManagerExt.TDTask`: 

> A task that was assigned when the TDThread got initialized. This is usually the case when EnqueueTask is used on the ThreadManagerExt and that force is set to true (and all workers are busy) or standalone is set to true.`SuccessHook`→`Callable`: 

> The method to be called uppon completion of the target method, in the main thread. Defaults to None.`ExceptHook`→`Callable`: 

> The method to be called in case of exception, in the main thread, while executing the target method. Defaults to None.`Exception`→`tuple`: 

> A tuple storing the exception data: excType, excValue, excTrace. This is being cleared in the clean method when the TDThread state gets to TDThreadStates.DONE.`RefreshHook`→`Callable`: 

> The method to be called every frames, in the main thread, while the target method is executing. Defaults to None.`Manager`→`ext.ThreadManagerExt`: 

> The ThreadManager extension from which this TDThread was Enqueued.`State`→`ext.ThreadManagerExt.TDThreadStates`: 

> The current TDThreadState of the TDThread. Default to TDThreadStates.STANDBY.`InfoQueue`→`queue`: 

> A queue to be used to exchange data between this thread and the main thread. Defaults to None.`Progress`→`float`: 

> A value to be set using SetProgressSafe from the threaded method, and to be accessed from the main thread using GetProgressSafe.`InPool`→`bool`: 

> A boolean used to create the TDThread as a Worker Thread, part of a pool. Defaults to False.`StateLock`→`threading.Lock`: 

> A threading lock used to access TDThread members safely.`LoopReady`→`threading.Event`: 

> A threading event used to control the worker loop.

## Methods`TDThread.GetStateSafe()`→`TDThreadStates`: 

> Helper method designed to be safe to use in a threading context.`TDThread.SetStateSafe(state: ext.ThreadManagerExt.TDThreadStates)`→`None`: 

> Helper method designed to be safe to use in a threading context. Set the current TDThreadStates of the TDThread.`TDThread.GetExceptionSafe()`→`tuple`: 

> Helper method designed to be safe to use in a threading context.`TDThread.SetExceptionSafe(exception: tuple)`→`None`: 

> Helper method designed to be safe to use in a threading context. Set the current Exception of the TDThread if a threaded method resulted in an exception.`TDThread.GetProgressSafe()`→`Float`: 

> Helper method designed to be safe to use in a threading context.`TDThread.SetProgressSafe(float)`→`None`: 

> Helper method designed to be safe to use in a threading context. Set the current Progress of the TDThread.`TDThread.GetThreadInfoSafe()`→`dict`: 

> Helper method designed to be safe to use in a threading context. Return the current Info dict of the TDThread.

# ThreadManagerExt

The extension of the Thread Manager COMP. Most users should only need to create`TDTasks`and enqueue them using`ThreadManagerExt.EnqueueTask`. 

## Members`Logger`→`Logger COMP`: 

> Reference to a local TouchDesigner Logger. Not to be used within a thread.`ManagerCondition`→`threading.Condition`: 

> Class that implements a condition variable. A condition variable allows one or more threads to wait until they are notified by another thread. If the lock argument is given and not None, it must be a Lock or RLockobject, and it is used as the underlying lock. Otherwise, a new RLock objectis created and used as the underlying lock.`MaxNumberOfThreads`→`int`: 

> The theoritical limit of logical thread on the current hardware. Equal to os.cpu_count(). This is used as a clamping limit for the pool, however, this is not a hard limit and creating threads manually is still possible, a fallback strategy can be set using self.ownerComp.par.Stategyonmaxthreadsreached.`MaxNumberOfWorkers`→`int`: 

> The maximum number of worker threads that are making the pool.`SafeLogger`→`logging.Logger`: 

> Reference to the python logger object of a local TouchDesigner Logger. Can be used safely within threaded methods.`Shutdown`→`bool`: 

> Used to signal the worker threads to get out of the work loop and shutdown. This should only be set using the StateLock or one of the helper methods.`StateLock`→`threading.Lock`: 

> A threading lock used to access ThreadManagerExt members safely.`Subscribers`→`List[COMP]`**(Read Only)** : 

> The list of Subscribers that registered to this Broadcaster.`Tasks`→`List[TDTask]`: 

> The list of tasks currently registered on the Thread Manager and awaiting to be picked in a pool.`Threads`→`List[TDThread]`: 

> The list of TDThreads currently registered on the Thread Manager. This includes worker threads.`ThreadsCount`→`int`: 

> The number of threads currently running and registered on the ThreadManager.`Workers`→`List[TDThread]`: 

> The list of TDThreads that are part of the worker pool.`WorkersCount`→`int`: 

> The number of worker threads currently running and registered on this ThreadManager.

## Methods`ThreadManagerExt.EnqueueTask(task: ThreadManagerExt.TDTask, force: bool = False, standalone: bool = False)`→`ThreadManagerExt.TDThread`: 

> Add a TDTask to the task queue to later be picked by an available TDThread that is part of the pool. EnqueueTask is promoted as users can create tasks outside of the ThreadManager context and later enqueue them to be ingested by the pool. 
> 
> Args: 
> 
>   * task (TDTask): The TDTask to be added to the task queue or to the TDThread (for forced or standalone modes).
>   * force (bool): Force the task to run immediately, whether it is as part of the pool or in a standalone TDThread. Default to False.
>   * standalone (bool): Force the task to run immediately in a standalone TDThread. Default to False. Prevail on`force`argument.
>`ThreadManagerExt.GetTaskById(taskId: str)`→`ThreadManagerExt.TDTask`: 

> Provided a task ID get a matching existing TDTask, or None. This method is promoted as its useful to be accessed from other components. 
> 
> Args: 
> 
>   * taskId (str): The taskId to be retrieved from the TDTasks list.
>`ThreadManagerExt.GetThreadById(threadId: str)`→`TDThread`: 

> Provided a thread ID get a matching existing TDThread, or None if not found. This method is promoted as its useful to be accessed from other components. 
> 
> Args: 
> 
>   * threadId (str): The threadId to be retrieved from the TDThreads list.
>`ThreadManagerExt.PostProcess(ThreadManagerExt.TDThread)`→`None`: 

> Called when the thread is done executing the threaded mathod and the TDThread.State == self.TDThreadStates.FINISHING or FAILED. This is equally called for standalone thread execution and worker execution within the worker loop. 
> 
> Args: 
> 
>   * tdThread (TDThread): The TDThread which finished executing its threaded method.
>`ThreadManagerExt.Done(ThreadManagerExt.TDThread)`→`None`: 

> When the postprocess is completed (the Success or Except hooks were called) and the state of the thread is set to TDThreadStates.DONE, this method is called to cleanup and / or reset the TDThread. 
> 
> Args: 
> 
>   * finishingThread (TDThread): The TDThread that reached Done and should go through cleanup and / or reset.
>`ThreadManagerExt.RemoveNumberOfWorkers(toRemove: int)`: 

> Remove the given number of additional workers. 
> 
> Args: 
> 
>   * toAdd (int): The number of workers to remove.
>`ThreadManagerExt.Subscribe(externalComp: str, messageTypes: List[str])`→`bool`: 

> This method is used to add an external component as a Subscriber of this broadcaster COMP. It's called from the Subscriber, to add itself to the list of Subscribers to this Broadcaster. When a component is registered as a Subscriber, any message type received by the broadcaster that are also in the message types list that the Subscriber registered for will be routed to the Subscriber. 
> 
> Args: 
> 
>   * externalComp (str): The path to a COMP that is registering as a Subscriber on this signaling client.
>   * messageTypes (List[str]): A list of message types that the Subscriber is registering for. When the signaling client is receiving a matching message type, it will route it to the Subscriber.
> 

> 
> Returns: 
> 
>   * bool: Whether the subscription request was a success or not. Will return False if the Subscriber was already registered.
>`ThreadManagerExt.TerminateThread(thread: ThreadManagerExt.TDThread)`→`None`: 

> Terminate and clean the provided TDThread. This method remains promoted for users to have the freedom to terminate a thread manually. Ideally, a thread terminate from the threaded method finishing execution, or an exception being raised. If a thread that gets terminated was part of the pool, it will be later be recreated. Setting the member`Shutdown`attribute to True will force workers to shutdown. 
> 
> Args: 
> 
>   * thread (TDThread): The TDThread to be terminated manually.
>`ThreadManagerExt.ValidateMessageTypes(messageTypes: List[str])`→`bool`: 

> When subscribing, verify that all the list passed are valid str. 
> 
> Args: 
> 
>   * messageTypes: List[str]: The list of strings to validate.
> 


TouchDesigner Build: Latest\nwikieditor2025.30000
