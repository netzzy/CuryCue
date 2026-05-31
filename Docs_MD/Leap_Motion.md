# Leap Motion

The [Leap Motion](<http://www.leapmotion.com>) Controller can be used as an input device to TouchDesigner.   
  
  
The Leap Motion controller tracks hands and fingers in an area directly above the device. It offers low latency, precise tracking and recognizes a number of motions and gestures. The gestures are provided to TouchDesigner through the Leap Motion SDK. TouchDesigner's Leap Motion support will be extended as more features and improvements are added to the device's SDK. 

### 

Leap Motion Support in TouchDesigner

TouchDesigner has built-in support for Leap Motion through the [Leap Motion CHOP](<./Leap_Motion_CHOP.md> "Leap Motion CHOP") and [Leap Motion TOP](<./Leap_Motion_TOP.md> "Leap Motion TOP"). At this time only 1 Leap Motion device can be connected at a time. 

### Leap Motion Licensing

TouchDesigner does not include a license to use the Leap Motion hardware or software. Make sure to check with the UltraLeap website regarding any applicable licenses that you may need for your project. 

  
**Requirements**
* [Leap Motion](<http://www.leapmotion.com/product>) hardware device
  * Install the Leap Motion software available here: [www.leapmotion.com/setup](<http://www.leapmotion.com/setup>)


  
**Ways to interact with Leap Motion in TouchDesigner**

[Leap Motion CHOP](<./Leap_Motion_CHOP.md> "Leap Motion CHOP") \- will bring in sensor data from the LeapMotion controller as CHOP channels. 
* Status channels - how many tracked and tracking channels for each tracked element
  * Hand channels - position, type, and velocity
  * Finger channels - position, rotation, size, is extended, and joints.
  * Tool channels - position and size
  * Gestures 
    * Pinch and Grab strength
    * Circle - index, position, radius, progress
    * Swipe - index, position, start position, speed
    * Key Tap - index, position
    * Screen Tap - index, position


[Leap Motion TOP](<./Leap_Motion_TOP.md> "Leap Motion TOP") \- will bring in image data from the Leap Motion image API. 
* Ability to view camera 0 or camera 1. Use 2 Leap Motion TOPs to view both cameras.
  * Some simple parameters to flip the images and enable Image Correction.

### 

Tips for Working with Leap Motion
* For additional support and troubleshooting, refer to [Leap Motion Support](<http://support.leapmotion.com/home>)

### 

Examples of Leap Motion with TouchDesigner
* [Leap Laser Control](<https://vimeo.com/59602627>) \- Each finger on both hands emit and control individual laser beams.
  * [Projection Mapping with Leap](<https://vimeo.com/79986942>) \- Using Leap Motion as in input device to control projection mapped visuals.
  * [Glasspiel Interactive Installation](<https://vimeo.com/groups/touchdesigner/videos/81704906>) \- Video mapping on sculpture controlled by Leap Motion.
  * [Leap Motion Experiment](<https://vimeo.com/groups/touchdesigner/videos/82151832>) \- An interactive particle system experiment.
  * [Leap Lighting Experiment](<https://vimeo.com/groups/touchdesigner/videos/68185181>) \- Exploration of lighting in a 3D space controlled with Leap Motion.
  * [LED Strip](<http://instagram.com/p/iKTb9Lg4hk>) \- Momo The Monster hooks up an LED strip during hack night.
  * **Shuhei Matsuyama'** s Magic Table 
    * [Magic Table Digital Painting](<https://vimeo.com/groups/touchdesigner/videos/80690105>)
    * [Magic Table Particle Experiment](<https://vimeo.com/73354067>)
  * **Shuhei Matsuyama'** s Digital Paintings 
    * [Ink Wash Painting](<https://vimeo.com/groups/touchdesigner/videos/78044597>)
    * [Psychedelic String](<https://vimeo.com/groups/touchdesigner/videos/81722477>)
    * [Painting CG](<https://vimeo.com/groups/touchdesigner/videos/75503831>)
    * [Painting on a Wall](<https://vimeo.com/groups/touchdesigner/videos/75736105>)
