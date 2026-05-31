# How-to calibrate your projector with Scalable Displays

## Overview  
  
TouchDesigner includes the [Scalable Display TOP](<./Scalable_Display_TOP.md> "Scalable Display TOP") which lets you read in calibration data retrieved from [Scalable Display Manager](<http://www.scalabledisplay.com/products/software-only/scalable-display-manager>) Software 

## Requirements
* a computer, referred to as calibration machine, running the [Scalable Display Manager](<http://www.scalabledisplay.com/products/software-only/scalable-display-manager>) Software that is not the output machine. This can be any computer running Microsoft Windows XP or newer with an OpenGL capable graphics card.
  * a Logitech C920 Webcam, Canon Rebel Series or Gigabit Ethernet camera
  * an unlimited amount of computers, referred to as client machine, running the Scalable Display Client Software with projectors connected
  * a license from [Scalable](<http://www.scalabledisplay.com/contact-us-0>) matching your specific requirements. Please contact [Scalable](<http://www.scalabledisplay.com/contact-us-0>) for information on licensing.

### Scalable Display Manager

The Scalable Display Manager Software lets you create "Scalable Mesh Files" to deal with warping and blending across an unlimited amount of computers and projectors. The generated files can be used by the [Scalable Display TOP](<./Scalable_Display_TOP.md> "Scalable Display TOP") to warp and blend TouchDesigners graphical output. 

### Scalable Display Client

The Scalable Display Client Software needs to be installed on all machines used for the final output and is used during the calibration process. 

## Calibration Procedure

On the calibration machine first make sure the Scalable Display Manager is installed, licensed and has a camera connected which has the whole projector output area in view. 

On the client machine make sure the Scalable Display Client Software is installed. Disconnect any displays from the client machines not used for output and make sure all connected projectors run at the same resolution. 

On the calibration machine start the Scalable Display Manager Software and follow the steps to calibrate the projectors. 

**Step 1 - Select client machines**

**Step 2 - Select projectors**

**Step 3 - Select and tune camera**

**Step 4 - Start data collection**

**Step 5 - Select screen type**

**Step 6 - Adjust image boundaries**

_**optional Step 5.1 - Perspective adjustment**_

_**optional Step 5.2 - Tweak blending parameters**_

_**optional Step 5.3 - Tweak perspective grid**_

**Step 7 - Finish**

Once calibration was successful, the Scalable Display Manager will distribute calibration data to all attached clients. 

On the clients the calibration files are saved in the Scalable Display Client installation folder, usually something like _C:/Program Files/Scalable Display/DEI/LocalCalibration/_

The Folder will contain a number of files called: 
* ScalableData
  * ScalableData.ol
  * ScalableData.ol.AlphaPrecursors
  * ScalableData.pol
  * ScalableDataOrthogrpahic
  * ScalableDataOrthographic.ol
  * ScalableDataOrthographic.ol.AlphaPrecursors
  * ScalableDataOrthographic.pol
  * InputBoundaryMask-blend.bmp


**Step 8 - Setup TouchDesigner**

In TouchDesigner attach as many Scalable Display TOPs to your output image as you have projectors connected to the client machine. Select either the ScalableData or the ScalableDataOrthographic file. The files are postfixed with an '_x' where x is the number of the output, so match the file with your Scalable Display TOP. To match the output resolution of your projector, set the Output Resolution Paarameter of the Scalable Display TOP to "Custom Resolution" and enter the projectors output resolution in the Resolution parameter. Also change the Output Aspect parameter to "Resolution". 

**A Support Case Note for using Orthographic Calibration Files**

Case - Projection room was 3 walls and 1 floor projection. The TOP content network had each projector image in its own TOP pathway where the 4 TOP paths correspond to the resolution of each projector. All projectors were the same resolution. Using the orthographic calibration files required that the 4 individual TOP images be combined to stack horizontally into a layout TOP in the order: left wall, center wall, right wall, floor. The layoutTOP output resolution was therefore the projector resolution x4 horizontally. The single 4x horizontally stacked layoutTOP fed each scalable TOP which was set to the individual projector resolution. Each scalable TOP loaded their own orthographic calibration file. 

This stacking has not been required for the perspective calibration files where each single image could be fed directly to their respective ScalableTOP.
