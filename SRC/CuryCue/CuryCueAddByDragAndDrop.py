class CuryCueAddByDragAndDrop:
    def DroppedItem(self, info):
        # if info['dragItems']['type']=="baseCOMP":
        #     print ("COMP!")
        myItem = info['dragItems']
        if len(myItem) > 0:
            # TODO на все comp реагировать
            if type(myItem[0]) == baseCOMP or type(myItem[0]) == geometryCOMP or type(myItem[0]) == containerCOMP:
                print("base! name: {}, path: {}".format(
                    myItem[0].name, myItem[0].path))
                self.AddNewFixture(myItem[0].name, myItem[0].path)
                self.UpdateFromDb()
                me.iop.fixparlistrender.cook(force=True)
                self.SetInitCue(1)

            elif type(myItem[0] == Par):
                # self.AddNewFixture(myItem[0].name, myItem[0].path)
                # print ("name:{}, owner: {}, value: {}".format(myItem[0].name,myItem[0].owner, myItem[0].val))
                # вызов добавлялки
                if hasattr(myItem[0], "owner"):
                    self.AddNewFixturePar(
                        myItem[0].owner, myItem[0].name, myItem[0].val[0])

    # добаывлялка нового параметра
    def AddNewFixturePar(self, path, par_name, par_value):

        if self.checkFixtureByPath(path):
            myFixture = self.LocalFixturesByPath[path]
            print("name:{}, owner: {}, value: {}, id_fix: {}".format(
                par_name, path, par_value, myFixture.id))
            
            if self.checkFixtureParByName(myFixture, par_name) is not True:
                self.executeUpdateQuery("INSERT INTO fixture_float_data (id_fixture, par_name, default_value, is_enabled) VALUES (?, ?, ?, 1)",
                                        [myFixture.id, par_name, par_value])
                ui.status = "Fixture: field {} added to {}".format(par_name, myFixture.name)
             
                self.UpdateFromDb()
                me.iop.fixparlistrender.cook(force=True)
                self.SetInitCue(1)
                
                
                

    def AddNewFixture(self, name, path):
        if self.checkFixtureByPath(path) is not True:
            self.executeUpdateQuery(
                "INSERT INTO fixture (name, global_object_location, is_enabled, `order`) VALUES (?, ?, 1, 1)", [name, path])
            ui.status = "Fixture: added {} ({})".format(name, path)
            pass
        pass
