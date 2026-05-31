# Uses of CHOPs

## Control External Devices

Get data in-from and out-to external devices using CHOPs. Through [MIDI](<./MIDI.md> "MIDI"), [OSC](<./OSC.md> "OSC"), [Shared Memory](<./Shared_Memory.md> "Shared Memory"), or custom C++ programs (via [Pipe In CHOP](<./Pipe_In_CHOP.md> "Pipe In CHOP") and [Pipe Out CHOP](<./Pipe_Out_CHOP.md> "Pipe Out CHOP"), data can pass in and out of TouchDesigner in a multitude of ways. Such inputs can be used to control any part of your Touch project, or conversely, Touch can control external devices by sending CHOP data out via any of these methods. 

## Real-Time Puppeteering

You can attach the mouse, MIDI or other devices to objects one at a time and perform the motion of the object, building up the motion of a character or object, piece by piece. You can perform these "gestures" with the mouse or other devices and capture the motion in a chop. You can edit the captured motion immediately by trimming, shifting, smoothing, and then combining it with other motion clips. TouchDesigner's realtime puppeteering is a unique way of rapidly creating motion. 

## Dynamics and Special Effects Motion

The creation of special motion effects is easier with CHOPs. You can detect events in the 3D scene, like collisions or direction changes, and then trigger the start of other motion. CHOPs include many tools to smooth curves, simulate physical motion, and add natural-looking random variations to motion. For example, CHOPs can be assembled to simulate physical camera motion, including lags, shakes, bumps and swings. 

## Non-Destructive Motion Editing

You can edit motion using CHOPs in a way that doesn't affect the original motion channels. You can change the timing of motion by shifting, compressing, expanding and warping time. You can apply operators that smooth, reverse, repeat, trim and extend motion. You can go back to any CHOP, change its effect on the resulting motion, and experiment with modified timing easily. 

## Motion Compositing

A group of CHOPs, each containing a motion clip for a character, can be sequenced one after the other, with controls over the blending transition between the motion clips. You can start with one motion clip and temporarily override it with another motion clip. Motion can be layered so that gestures can temporarily and partially override other gestures. Because you can experiment on the blending without destroying the original data, you can easily fine tune layered motion. 

## Facial Animation and Lip Sync

Facial motion can be animated from a set of facial expressions, made of poses and motion clips. Facial poses and motion clips can be composed from other poses and facial motion clips and then re-used. 

  
Lip sync is the facial animation task that uses a voice soundtrack and a library of mouth poses to animate a character's mouth. You can import a voice track, add words of the dialogue to the time line, drop mouth poses and gestures on the time line, then adjust the timing of the poses. You can also filter and smooth the audio to automatically generate approximate mouth motion. 

## Motion Capture Editing

You can import motion capture clips from mocap systems. Defects in captured motion can be cleaned up. Motion capture data can be applied to an inverse or forward kinematics character model, and you can further refine the motion with CHOPs. A CHOP holds multiple-channels of motion. You can easily attach and detach different motion capture moves to one character. 

## Keyframe Pose Interpolation

CHOPs provides an alternative way to hand-edit keyframing in Touch, aside from the channel keyframing documented in the User Guide. 

Within CHOPs you can pose a character, snapshot the angles and IK end-effectors into a single CHOP, sequence several poses one after another, then adjust a timing curve in another CHOP to interpolate between poses. You can easily edit the poses and timing, and you can copy-paste poses and animation to other characters. 

## Audio Editing

You can import audio into Touch from external sources and then trim, filter, resample, sync and mix the sound. You can attach mixed audio to the animation timeline. The 3D animation can be synchronized with the soundtrack with the help of timeline scrubbing and text annotation on the timeline. 

## Audio Synthesis and 3D Sound

Sound effects can be imported from external sources, but audio can also be synthesized from scratch using built-in audio oscillators, filters, reverb and volume controls. Sound effects can then be triggered by any event or motion in the 3D scene, or a sound can be continuously looped. Then the audio can be placed anywhere in the 3D environment of the animation, with audio cues like left-right pan, distance attenuation, muffling and doppler shift. Sounds can be triggered to help users understand conditions in the 3D scene, such as character joint limits. Audio is generated in realtime, or more complex audio can be "rendered" and played back with the animation. 

## Visual Expression Language

CHOPs make a math expression language both visual and interactive. You can build the equivalent math expressions with CHOPs without having to code with a compiler. Using CHOPs you can interactively build expressions and see the results in a graph or Viewport immediately. There is no typing and therefore no "syntax errors". CHOPs do arithmetic, fetch data from other objects and more. 

## Motion Management for Large Projects

A team of animators can maintain many motion clips in a central library. Motion can be easily moved between animators and scenes. CHOPs are a convenient way of managing motion of large projects, where clips for many characters are spread across many scenes. Several animators can work on single characters. Through motion compositing, you can build up or "composite" character motion from a library of motion clips, and then hand-modify them. This helps keep a consistent look for character, especially when several artists animate the same character.
