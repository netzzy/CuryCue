# BlackTrax

[BlackTrax](<http://blacktrax.cast-soft.com/>) is a vision-based real-time tracking system developed by [CAST Software](<http://cast-soft.com/>) that specializes in large-scale performances. BlackTrax Beacons ("BTBeacons") are attached to performers or rigid objects, and the BlackTrax system accurately tracks the Beacon's position, rotation, velocity, and acceleration. 

Examples of large-scale performances using BlackTrax include Cirque du Soleil Toruk - The First Flight, The Weekend's Starboy World Tour, and [Mattia Diomedi's "V"](<http://derivative.ca/Events/2017/MattiaDiomedi/>). 

The BlackTrax Beacon's data can be used to drive visual output such as projection mapping or performance lighting (eg. spotlights). In Mattia Diomedi's "V" (built with TouchDesigner) BlackTrax was used to seamlessly pair the movements of performers with beautiful visuals. Beacons were attached to the hands of 2 performers and their movements affected the output of the LED screen backdrop and the 2 projectors. 

For a more detailed description of "V", see our [Blog article](<http://derivative.ca/Events/2017/MattiaDiomedi/>). 

See also: [BlackTrax Showcase](<http://blacktrax.cast-soft.com/showcase/>). 

BlackTrax tracking data can be brought into TouchDesigner using the [BlackTrax CHOP](<./BlackTrax_CHOP.md> "BlackTrax CHOP"). 

### 

How it works

BlackTrax provides high accuracy tracking of up to 255 Tracking Points (LEDs), or 85 Beacons; Beacons can have up to 3 LEDs. The accuracy is 1/4 inches at a 50-foot distance, and can track a ping pong ball with 7mm accuracy. The tracking speed is 100 frames per second, and the distance for the standard BlackTrax solution is 50 feet, though this can be increased up to 700 feet for upgraded packages. 

The Beacons and LEDs are tracked using BlackTrax cameras. These cameras get the positional data (translation, rotation) from the Beacons and LEDs which is subsequently processed and sent to any 3rd party systems (such as TouchDesigner). 

For additional information see [BlackTrax FAQ](<https://cast-soft.com/faq/>) or [How BlackTrax Works](<http://blacktrax.cast-soft.com/howitworks/>)

### 

Applications

BlackTrax has applications in projection mapping. To projection map onto a movable object, attach BlackTrax Beacons to the object so that no matter where it is in the projector FOV it can be accurately mapped using the positional and rotational data from the beacons. In TouchDesigner this can be achieved using the [BlackTrax CHOP](<./BlackTrax_CHOP.md> "BlackTrax CHOP") and one of TouchDesigner's projection mapping tools, [CamSchnappr](<./Palette-camSchnappr.md> "Palette:camSchnappr") or [Kantan Mapper](<./Palette-kantanMapper.md> "Palette:kantanMapper"). 

BlackTrax is an excellent choice for tracking performers. By attaching Beacons to performers you can track their movements with a high degree of accuracy, and with this data available in TouchDesigner the options are limitless. For inspiration, see [Mattia Diomedi's "V"](<http://derivative.ca/Events/2017/MattiaDiomedi/>) or the [BlackTrax Showcase](<http://blacktrax.cast-soft.com/showcase/>)
