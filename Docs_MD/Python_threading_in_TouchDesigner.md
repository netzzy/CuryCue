# Python threading in TouchDesigner

Working with threads is challenging, and threading in TouchDesigner is difficult. 

The main obstacle to overcome is that the main TouchDesigner thread needs to run continuously, this main thread is responsible for running the user interface and is how the timeline moves forward and frames are generated. 

Blocking the main thread will result in frame drops or worse it could hang or crash TouchDesigner. 

A general rule of thumb is to avoid accessing objects on the main TouchDesigner thread from other threads, whether reading or writing. 

There are ways to work with Python's own threading library within secondary threads which allows for the use of while loops and other blocking methods. This often involves an Execute DAT, which checks the thread status and dequeues objects every frame. 

As of **TouchDesigner 2023.31500+** , TouchDesigner includes a [Thread Manager](<./Thread_Manager.md> "Thread Manager"). 

The [Thread Manager](<./Thread_Manager.md> "Thread Manager") simplifies threading and task handling in TouchDesigner for Python developers. Advanced users can access the [Thread Manager](<./Thread_Manager.md> "Thread Manager") COMP directly using`op.TDResources.ThreadManager`. Alternatively, users who want an easier component based approach can look at the [Thread Manager Client](<./Palette-threadManagerClient.md> "Palette:threadManagerClient") available in the Palette's ThreadManager folder. It’s a simple callback-oriented component that wraps around the [Thread Manager](<./Thread_Manager.md> "Thread Manager"). 

Additionally, various debugging tools are available such as the [Threads Monitor](<./Palette-threadsMonitor.md> "Palette:threadsMonitor") COMP which has advanced logging features. The [Thread Manager](<./Thread_Manager.md> "Thread Manager") settings can be tweaked from the Threads Monitor COMP.
