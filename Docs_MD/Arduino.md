# Arduino

TouchDesigner supports [Arduino](<http://arduino.cc/>) via the [Serial DAT](<./Serial_DAT.md> "Serial DAT"). 

**Example Videos**
* [[1]](<http://vimeo.com/19050970>) Here is a video by Rob Bairos showing TouchDesigner and Arduino.
  * [[2]](<http://vimeo.com/groups/touchdesigner/videos/8725492>) Another by Markus Heckmann presenting at MUTEK.
  * [[3]](<http://vimeo.com/groups/touchdesigner/videos/13109381>) Dave Robert at MIT on Never-Ending Drawing Machine (cue to 3:15 and to 7:50).


She the OP Snippets on the Serial DAT. (Help -> Operator Snippets) 

See also [Palette:Firmata](</index.php?title=Palette:Firmata&action=edit&redlink=1> "Palette:Firmata \(page does not exist\)"). 

## Sending data from the Arduino

Begin by installing Arduino, and any necessary serial drivers. 

Here is an example file: [Media:Arduino sample.tox](<./images/a/a5/Arduino_sample.bin> "Arduino sample.tox")

The following simple sketch will output some values once per second: 
[code] 
     void setup()
     {
       // start serial port at 9600 bps:
       Serial.begin(9600);
     }
     void loop()
     {
       delay(1000);
        
       int  i = 1234;
       Serial.print(i, DEC);
       Serial.print('\n');
      
       float f = 321.7;
       Serial.print(f);
       Serial.print('\n');
     }
    
[/code]

In order to receive these messages in TouchDesigner, place down a [Serial DAT](<./Serial_DAT.md> "Serial DAT"). By default, all the parameters should be compatible with the above sketch and you should see these two values arriving in the DAT every second. 

More specifically, make sure the communication parameters are set to the same baud rate as the Arduino. By default the settings are 9600,8,N,2 but the baud rate can be increased if required. Also, make sure the Table Format is set to **One Row Per Line**. 

The above sketch outputs a single new line character '`\n`' after each value. Unfortunately, executing a`println()`command will not work in this case, as it outputs both a carriage return and a new line, which are interpreted as blank lines in the Serial In DAT. 

To see the actual received byte values at any time, turn on the Value Column parameter under the Received Messages parameter 

Make sure to turn **off** the **Active** parameter in the [Serial DAT](<./Serial_DAT.md> "Serial DAT"), while using the Arduino to upload new sketches over the shared serial connection. 

Turn the **Active** parameter back **on** after the sketch is uploaded. 

Alternatively, for binary communication, the sketch print statements could output individual bytes: 
[code] 
     char a = 123;
     Serial.print(a, BYTE);
    
[/code]

In this case, the Serial In DAT Table Format should be set to **One Row Per Byte**. 

Make sure to turn on 'Value Column' in the DAT to show their numeric values. 

In addition to the above log, a python script can be called for each received entry. 

## Receiving data on the Arduino

Finally, to output characters back to the Arduino, use the [Serial DAT's](<./SerialDAT_Class.htm#Methods> "SerialDAT Class") send methods. 

Bytes can be sent through the same [Serial DAT](<./Serial_DAT.md> "Serial DAT"). 

Use the Arduino commands:`Serial.available()`and`Serial.read()`to access these bytes on the Arduino. 

The following link shows how these commands are used in an Arduino Sketch: 

[[4]](<http://arduino.cc/en/Serial/Available>)

When receiving multiple byte messages, it is important to remember that the stream has no well defined start or end bytes. Therefore one common method is to append all bytes to a character buffer until the newline is received. Once the newline is received, the character buffer can be parsed for the required elements. 
[code] 
     //
     // Parse incoming messages consisting of three decimal values followed by a carriage return
     //  Example  "12 34 56\n"
     //  In TouchDesigner:     op('serial1').send("12 34 56", terminator="\n")
     //
     char buffer[16];   //maximum expected length 
     int len = 0;
     void setup()
     {
       Serial.begin(9600); 
     }
     void loop()
     {
         if (Serial.available() > 0) 
         {
             int incomingByte = Serial.read();
             buffer[len++] = incomingByte;
             //
             // check for overflow
             //
             if (len >= 16)
             {
                 // overflow, resetting
                 len = 0;
             }
             //
             // check for newline (end of message)
             //
             if (incomingByte == '\n')
             {
                 int red, green, blue;
                 int n = sscanf(buffer, "%d %d %d", &red, &green, &blue);
                 if (n == 3)
                 {
                     // valid message received, use values here..
                 }
                 else
                 {
                      // parsing error, reject
                 }
                 len = 0; // reset buffer counter
             }
         }
     }
    
[/code]
