# DAT Export

DAT exporting sends numbers, strings or expressions in a table format to a [parameter](<./Parameter.md> "Parameter") of any [operator](<./Operator.md> "Operator").   
  
To export data from a DAT, the green Export flag at the bottom of the DAT must be on, AND the DAT must be in a table format with properly named columns. The columns are named:`path parameter value enable`Each row represents one value to be exported to a parameter of another node. 

The`path`and`parameter`specify the network path to the operator and parameter where the data will be exported to. 

The`value`column contains the data to be exported. It can be a numeric value, string value or expression. 

The`enable`column is optional. When set to '0' the export in that row is disabled, when set to '1' the export is enabled. 

The DAT's green [Export Flag](<./Export_Flag.md> "Export Flag") must be On to enable the export. Once the export is established, a dotted data [link](<./Link.md> "Link") will connect the DAT and the operator to indicate a connection. 

To disable the export, simply toggle the DAT's export flag off. 

For exporting from CHOPs, see also: [CHOP Export](<./CHOP_Export.md> "CHOP Export").
