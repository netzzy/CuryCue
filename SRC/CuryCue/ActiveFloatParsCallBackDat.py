# me - this DAT
# scriptOp - the OP which is cooking
#
# press 'Setup Parameters' in the OP to call this function to re-create the parameters.

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return

def onCook(scriptOp):
	if hasattr(parent.curycue.ext, "CuryCueClass"): 
		scriptOp.clear()
		myValue=None
		for myPar in parent.curycue.ActiveFields:

			if myPar.par_text_value is None or myPar.par_text_value is not None and len(myPar.par_text_value)==0:
				if not isinstance(myPar.par_value, str):
					myValue=round(myPar.par_value, 4)
			else:
				myValue=myPar.par_text_value
				

			scriptOp.appendRow([myPar.id_par,  myPar.id_fixture, myPar.fixture_name, myPar.par_name, 
			myValue,"", "%g" % myPar.fade_in, "%g" % myPar.delay_in, myPar.fixture_object_location, 
			myPar.full_par_path, "%g" % myPar.is_cue_exist,"%g" %  myPar.is_fading])
	else:
		ui.status="No QQ class"
	return

def onSetupParameters(scriptOp):
	"""Auto-generated by Component Editor"""
	# manual changes to anything other than parJSON will be	# destroyed by Comp Editor unless doc string above is	# changed

	TDJSON = op.TDModules.mod.TDJSON
	parJSON = """
	{
		"Settings": {
			"Cueid": {
				"name": "Cueid",
				"label": "Cue id",
				"page": "Settings",
				"style": "Int",
				"size": 1,
				"default": 0,
				"enable": true,
				"startSection": false,
				"readOnly": false,
				"enableExpr": null,
				"min": 0.0,
				"max": 1.0,
				"normMin": 0.0,
				"normMax": 1.0,
				"clampMin": false,
				"clampMax": false
			}
		}
	}
	"""
	parData = TDJSON.textToJSON(parJSON)
	TDJSON.addParametersFromJSONOp(scriptOp, parData, destroyOthers=True)