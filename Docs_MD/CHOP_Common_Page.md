# CHOP Common Page

Time Slice \- Turning this on forces the channels to be "[Time Sliced](<./Time_Slicing.md> "Time Slicing")". A Time Slice is the time between the last cook frame and the current cook frame. 

Scope \- To determine which channels get affected, some CHOPs use a Scope string on the Common page. 

Patterns can be used in the Scope:`*`(match all channels and therefore affect all channels),`?`(match single character. See [Pattern Matching](<./Pattern_Matching.md> "Pattern Matching"). 

Sample Rate Match - Handle cases where multiple input CHOPs' sample rates are different. When the CHOP needs to combine inputs with different sample rates, the Sample Rate Match Options offers these choices: 
* Resample At First Input's Rate - Use rate of first input to resample others.
  * Resample At Maximum Rate - Resample to the highest sample rate.
  * Resample At Minimum Rate - Resample to the lowest sample rate.
  * Error if Rates Differ - Doesn't accept conflicting sample rates.


When Resampling occurs, the curves are interpolated according to the [Interpolation Method Option](</index.php?title=Frequent_CHOP_Parameters&action=edit&redlink=1> "Frequent CHOP Parameters \(page does not exist\)"), or "Linear" if the Interpolate Options are not available. 

Export Method - This will determine how to connect the CHOP channel to the parameter. Refer to the [Export](<./Export.md> "Export") article for more information. 
* DAT Table by Index - Uses the docked DAT table and references the channel via the index of the channel in the CHOP.
  * DAT Table by Name - Uses the docked DAT table and references the channel via the name of the channel in the CHOP.
  * Channel Name is Path:Parameter - The channel is the full destination of where to export to, such has`geo1/transform1:tx`.


Export Root \- This path points to the root node where all of the paths that exporting by **Channel Name is Path:Parameter** are relative to. 

Export Table - The DAT used to hold the export information when using the DAT Table Export Methods (See above).
