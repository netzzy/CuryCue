# me - this DAT
#
# The functions below are called when a Multi Touch In DAT outputs ID Table.
# dat - the DAT that received a multi-touch event
# event - a named tuple with the following fields:
#   type        - type of event, 'up, 'down', etc
#   primary     - True if this is the first touch established from no touch inputs
#   device      - source input device
#   time        - touch event time stamp
#
#   id          - touch point identifier
#   sn          - event serial number
#   select      - when 1, this row represents a finger is down
#   downf       - the absolute frame number when the finger press occurred
#   upf         - the absolute frame number that the finger press ended
#   x           - x position
#   y           - y position
#   u           - the position, 0 to 1 in the horizontal direction
#   v           - the position, 0 to 1 in the vertical direction
#   downu       - the value of u, when the finger press occurs
#   downv       - the value of v, when the finger press occurs
#   contactx    - width of touch contact area in pixels
#   contacty    - height of touch contact area in pixels
#   contactu    - width of touch contact, 0 to 1
#   contactv    - height of touch contact, 0 to 1
#   monitor     - monitor number, starting with 0
#   clicktime   - like downf, in seconds
#   elapsedtime - the number of seconds that finger has been down
#   changedtime - the time since the finger press that the most recent u or v value changed
#   dclick      - double-tap occurred
#
# you can also access these values via dat[id,valuename]

def onDown(dat, event):
	ui.status=event.type
	return

def onMove(dat, event):
	
	return

def onUp(dat, event):
	return

def onHover(dat, event):
	return

# The function below is called when a Multi Touch In DAT outputs Raw Events.
# dat - the DAT that received a multitouch event
# rowIndex - the row number that was added
# cells - the list of cells that were added

# To access newly added rows by their data type, you can use:
# dat[rowIndex], 'type'] - event type
# dat[rowIndex], 'id']   - touch point identifier
# dat[rowIndex], 'x']    - x position
# dat[rowIndex], 'y']    - y position 
# dat[rowIndex], 'contactX'] - width of touch contact area in pixels
# dat[rowIndex], 'contactY'] - height of touch contact area in pixels
# dat[rowIndex], 'primary']  - true if this is the first touch established from no touch inputs
# dat[rowIndex], 'device']   - source input device
# dat[rowIndex], 'time']     - touch event time stamp

def newRow(dat, rowIndex, cells):
	return
	