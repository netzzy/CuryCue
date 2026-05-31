# Beat Dialog

The Beat dialog under the Dialogs menu lets you set the beats-per-minute (BPM) of a TouchDesigner project by letting you tap in the beat while you are listening to music. It is used by the [Beat CHOP](<./Beat_CHOP.md> "Beat CHOP") to determine the length of its cycles and its "phase" (when it returns to the start of a loop).   
  
### How to set BPM and Phase

From the **Dialogs** menu get the **Beat** panel. 

To set the BPM, first turn on the Listen button. Then press the Tap button **EVERY 4 BEATS** , preferably at the beginning of each bar. The BPM adjusts every time you tap. After 10 or 20 seconds, stop pressing the Tab button, and turn off the Listen button. It will keep the latest BPM until you Listen/Tap again. 

The Beat Panel will average out your taps to the closest BPM, so you can keep tapping EVERY 4th BEAT to get a more accurate average BPM. 

After the cycles drifts from the music, you can resync the beginning of a ramp cycle to the start of a bar of music: With the Listen button off, press the Tap button once. It will re-sync, and not affect the BPM. 

The orange triangle on the beat circle lets you adjust the phase in case you want to advance/retard your visual relative to the music. 

You can watch the beat cycle, or use the [Beat CHOP](<./Beat_CHOP.md> "Beat CHOP") to generate 0-to-1 ramps based on the beats-per-minute. 

Note: you can set the global beats-per-minute with the python command:`op('/local/time').tempo = 140`See Also: [Beat CHOP](<./Beat_CHOP.md> "Beat CHOP").
