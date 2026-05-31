# Vioso

## Overview

TouchDesigner includes the [Vioso TOP](<./Vioso_TOP.md> "Vioso TOP") which lets you read in calibration data retrieved from the [VIOSO 6](<https://vioso.com/software/vioso6/>) Software. Vioso's auto-alignment technology makes the setup of installations like multi-projector panorama displays and multi-projector setups for projection mapping more automated and quick. 

You can download VIOSO 6 from [here](<https://vioso.com/software/vioso6/>) and use it as a trial for 30 days with an demo overlay. The procedure is to use Vioso with your projectors, do the alignment, which outputs files that TouchDesigner understands to do the appropriate image warping and blending, taking into account differences in projector light and tinted surfaces. 

See also [CamSchnappr](<./Palette-camSchnappr.md> "Palette:camSchnappr"), which is less automated and required a 3D model of the objects you are projecting on. CamSchnappr has been upgraded to do multi-projector blending on a given 3D model. 

See also [Projection Mapping](<./Projection_Mapping.md> "Projection Mapping"), [Scalable Displays](<./Scalable_Display_TOP.md> "Scalable Display TOP"), [kantanMapper](<./Palette-kantanMapper.md> "Palette:kantanMapper"), [camSchnappr](<./Palette-camSchnappr.md> "Palette:camSchnappr"), [projectorBlend](<./Palette-projectorBlend.md> "Palette:projectorBlend")

## Requirements

Depending on how many channels need to be calibrated, the projectors need to be properly connected to the computer and the VIOSO 6 Software must be installed. Also a TouchDesigner build needs to be installed and a camera needs to be connected to the computer. We have had good experience with the Logitech HD Pro range of Webcams. When setting up the scene it is advised to have the projector overlap between 10% and 25% of the projector area. The camera needs to be able to see the complete scene and should be mounted so it cannot move during the calibration process. 

## Starting Calibration

Start VIOSO 6 and follow the instructions as outline in the [VIOSO 6 Documentation](<https://helpdesk.vioso.com/documentation/vioso-6-overview/>)

For a simple test calibration on a flat screen: 
1. start VIOSO 6
  2. click the Calibrate Button
  3. select the "single client calibration" on the next dialog
  4. select the projectors to calibrate in the Displays and Camera Dialog
     1. if you setup your projectors in a NVidia Surround, NVidia Mosaic, AMD Eyefinity or Matrox or Datapath single large display configuration, use the "Display Split" function to identify the correct projectors
  5. select the "flat screen" setup in the Displays and Camera Dialog
  6. select the camera you want to use in the Displays and Camera Dialog
  7. select the appropriate setup of your projectors in the Display arrangement Dialog
  8. in the Adjust Camera Dialog you have the ability to draw a mask around the area that the projector is projecting onto, if the camera view area is much larger then the actual projection screen, this will improve results during calibration
  9. adjust the size of the scan pattern so that the camera can clearly identify each projected circle
  10. after successful calibration, you can fine adjust the result in the Final Adjustments Dialog using keystone and mesh warping tools
  11. save the project and select Export Calibration from the File Menu of Vioso 6 
     1. select the appropriate calibration setup from the list
     2. select "Wings/VIOSO" format from the Export format dropdown
     3. select the file name and export path by clicking the Select button beside the file name field.
     4. make sure no toggles are selected and hit export
  12. the result should be a single .vwf file which you can load into the [Vioso TOP](<./Vioso_TOP.md> "Vioso TOP")
