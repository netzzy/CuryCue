# 10-Bit Color Displays

## Overview

Most computer monitors support 8-bits of information per color (24-bits per pixel), however there are now computer monitors on the market that support 10-bits per color (30-bits per pixel) via DisplayPort and HDMI connectors. This is also known as Deep Color. This added information allows the monitor to display many more shades of color, reducing banding artifacts and increasing the accuracy with which the monitor is able to display content. Examples of some of these monitors are the Dell UltraSharp series of monitors, and the HP DreamColor series of monitors. 

To make all of your visible windows in TouchDesigner be 10-bit color you need do the following:  
1\. Ensure the monitor is connected via DisplayPort or HDMI.  
2\. Set the monitor to be 10-bit (10bpc) in the GPU driver's control panel.  
3\. Set a new Windows environment variable TOUCH_10_BIT_COLOR to 1.  

### Setting Variables on MacOS

On MacOS open a terminal and set the variable like this...`/bin/launchctl setenv TOUCH_10_BIT_COLOR 1`For this command to run every time you login place the following XML code into your user folder as the specified file: ~/Library/LaunchAgents/environment.plist 
[code] 
      <?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "<http://www.apple.com/DTDs/PropertyList-1.0.dtd>">
      <plist version="1.0">
        <dict>
          <key>Label</key>
            <string>my.startup</string>
          <key>ProgramArguments</key>
          <array>
             <string>sh</string>
             <string>-c</string>
             <string>
               /bin/launchctl setenv TOUCH_10_BIT_COLOR 1 
             </string>
          </array>
          <key>RunAtLoad</key>
          <true/>
        </dict>
      </plist>
    
[/code]

## Important Concepts

### The Pixel Format of your Content

It's important to understand that while the visible windows will become 10-bit color, the rest of the TOP content inside TouchDesigner will remain at whatever each TOP's pixel format is set as. So if you are rendering in a [Render TOP](<./Render_TOP.md> "Render TOP") at 8-bit color, then you won't benefit from having your windows be at 10-bit color. The reason for this is that even though all rendering always takes place 32-bit floats, the final color values will get clamped to whatever pixel format the TOP is set at. You'll need to make sure the pixel format has a greater or equal to precision than 10-bit, such as rendering in 16-bit for example, to avoid losing the extra data. 

Another place you will see a difference is in Geometry Viewers. This is because the image in a Geometry Viewer is drawn directly into the window, so it the color values won't get clamped to 8-bit precision (they'll be drawn to the 10-bit window directly). So remember that if you don't see banding in the Geometry Viewer, but do in the Render TOP, double check the pixel format of the Render TOP (or any downstream TOPs that are operation on the data). 

### Blending when using Destination Alpha

When using 10-bit color you are still limited to 32-bits per pixel. So with 30-bits used up for Red, Green and Blue, that only leaves 2 bits for Alpha. That means alpha written to the window can only take on the values of 0.0, 0.33, 0.66 and 1.0. In practice this shouldn't affect you at all as it's very rare that the alpha in the window ever gets used. The only time it gets used is if you are blending and using the destination alpha as a blend factor. It's unlikely you'll ever do this, but if you do be aware that the blending won't look right in the Geometry Viewers. It'll still work fine in 16-bit pixel format TOPs though, as the alpha channel is 16-bit in those TOPs also.
