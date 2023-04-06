class FixtureUtils:
    def DeleteFixtureByID(self, id_fixture, info):
        ui.status=info['rowData']['id_fix']
        res=ui.messageBox('Question', 'Are you sure you want to delete device {}'.format(info['rowData']['Path']), buttons=['Yes', 'No'])
        if res==0 and int(id_fixture) > 0:
            self.executeUpdateQuery(
                "DELETE FROM fixture_float_data WHERE id_fixture=?", [id_fixture])
            self.executeUpdateQuery(
                "DELETE FROM cue_float_data WHERE id_fixture=?", [id_fixture])
            self.executeUpdateQuery(
                "DELETE FROM fixture WHERE id=?", [id_fixture])
            self.UpdateFromDb()
            me.iop.fixparlistrender.cook(force=True)
            self.SetInitCue(1)
            ui.status="Fixture: {} + its fields and cues have been deleted".format(info['rowData']['Path'])

    def DeleteFixtureParByID(self, id_fix_par, id_fixture, par_name, info):
#        print ("Fuck")
#       return 
        ui.status=info['rowData']['id']
        myPARinfo=info['rowData']['Parameter']
        res=ui.messageBox('Question', 'Are you sure you want to delete parameter {} from the device and cues?'.format(info['rowData']['Parameter']), buttons=['Yes', 'No'])
        if res==0:
            print("{}, {}, {}".format(id_fixture, id_fix_par, par_name))
            self.executeUpdateQuery("DELETE FROM fixture_float_data WHERE id=?", [id_fix_par])
            self.executeUpdateQuery("DELETE FROM cue_float_data WHERE id_fixture=? and par_name=?", [
                                    id_fixture, str(par_name)])
            # self.executeUpdateQuery(
            #     "DELETE FROM fixture_float_data WHERE id=?", [id_fix_par])
            self.UpdateFromDb()
            me.iop.fixparlistrender.cook(force=True)
            self.SetInitCue(1)
            ui.status="Fixture: par. {} and its cues have been deleted".format(myPARinfo)

    def DeleteCueParByID(self, id_fix_par, id_fixture, par_name, info):
        #res=ui.messageBox('Question', 'Are you sure you want to delete parameter {} from the device and cues?'.format(info['rowData']['Par.']), buttons=['Yes', 'No'])
        if int(info['rowData']['id'])==-1:
            ui.status="Field {} is not in this cue, it is set somewhere earlier".format(info['rowData']['Par.'])
            return 
        print("{}, {}, {}".format(id_fixture, id_fix_par, par_name))
        self.executeUpdateQuery("DELETE FROM cue_float_data WHERE id_fixture=? and par_name=? and id_cue=?", [
                                id_fixture, str(par_name), int(self.Curcueid)])
        # self.executeUpdateQuery(
        #     "DELETE FROM fixture_float_data WHERE id=?", [id_fix_par])
        self.UpdateFromDb()
        me.iop.fixparlistrender.cook(force=True)
        self.SetInitCue(1)
        ui.status="Cues: field {} has been deleted from the cue".format(info['rowData']['Par'])
