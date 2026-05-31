# Palette:firmata Ext

These Extensions reference a specific [Palette:firmata](<./Palette-firmata.md> "Palette:firmata").   
  
# FirmataExt

FirmataExt description 

## Members

No operator specific members. 

## Methods`FirmataExt.QueryAnalogMap()`→`None`: 

> Sends a Analog Mapping Request to the Serial DAT`FirmataExt.QueryCapabilities()`→`None`: 

> Sends a Capability Request to the Serial DAT`FirmataExt.QueryState(pin=None, send=True)`→`bytearray`: 

> Sends a Pin State Request to the Serial DAT, returns the message. 
> 
>   * pin - (Keyword, Optional) integer number of the pin
>   * send - (Keyword, Optional) select if the message should be send to the Serial DAT
>`FirmataExt.QueryVersion()`→`None`: 

> Sends a Firmware request to the Serial DAT`FirmataExt.ReportAnalog(state=False)`→`None`: 

> Enable and Disable the reporting for all analog pins. 
> 
>   * state - (Keyworkd, Optional) Turn analog reporting on or off.
>`FirmataExt.ReportDigital(state=False)`→`None`: 

> Enable and Disable the reporting for all digital pins 
> 
>   * state - (Keyword, Optional) Turn digital reporting on or off.
>`FirmataExt.Reset()`→`None`: 

> Resets the internaly stored data about the connected arduino.`FirmataExt.SetMode(pin, mode)`→`None`: 

> Constructs a message to set a pin to the specified mode. 
> 
>   * pin - The pin number.
>   * mode - The mode identifier.
>`FirmataExt.SetSampling(interval)`→`None`: 

> Set the Sampling Interval for Firmata in ms. 19: default 99: Arduino Mega 
> 
>   * interval - intNumber of ms of the sampling interval
>`FirmataExt.SetValue(pin, value)`→`None`: 

> Creates the message for sending a value to a pinand sends the message to the serial DAT. 
> 
>   * pin - The number of the pin.
>   * value - The value to set the pin to.
>
