# Filter per Sample

CHOPs that (temporally) filter over time, like the [Lag CHOP](<./Lag_CHOP.md> "Lag CHOP") and [Filter CHOP](<./Filter_CHOP.md> "Filter CHOP") can also treat each sample as its own filter. Turn on their Filter per Sample parameter and each sample will behave like separate filter.   
  
For example, if you have 20 channels that are 100 samples long that are all set to 0, feeding into a Filter CHOP with Filter per Sample turned on, and then you set only one sample of the input to 1, that sample of the output will ramp up to 1 over one second, but all other samples will remain 0. Each sample is a separate filter. 

Other CHOPs with this feature are [Hold CHOP](<./Hold_CHOP.md> "Hold CHOP"), [Slope CHOP](<./Slope_CHOP.md> "Slope CHOP"), [Speed CHOP](<./Speed_CHOP.md> "Speed CHOP") and [Spring CHOP](<./Spring_CHOP.md> "Spring CHOP").
