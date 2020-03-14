import wx, noname, dnd_objects, dnd_data




Thadeus = dnd_objects.crude_make_creature("Thadeus")
Wera = dnd_objects.crude_make_creature("Wera", crt_type= dnd_data.creatures["wizard1"])
Kub = dnd_objects.crude_make_creature("Kub", crt_type= dnd_data.creatures["ochre_jelly"])


class Mainframe(noname.MyFrame2):

    def __init__(self, parent):
        noname.MyFrame2.__init__(self, parent)
        for i in dnd_objects.char_dict.keys():
            self.m_charlist.Append([i])
        self.current_character = ""


    def UpdateScreen(self, event):
        crt_name = self.m_charlist.GetItemText(self.m_charlist.GetFocusedItem())
        Crt = dnd_objects.char_dict[crt_name]
        self.current_character = crt_name

        self.tf_charname.SetValue(Crt.name)
        self.tf_charclass.SetValue(Crt.char_class)
        self.tf_charlevel.SetValue(str(Crt.level))
        self.tf_charphys.SetValue(str(Crt.physical_state))
        self.tf_charhp.SetValue(str(Crt.hp) + "/" + str(Crt.max_hp))
        self.tf_charexp.SetValue(str(Crt.xp))
        self.tf_char_str_stat.SetValue(str(Crt.abilities["str"]))
        self.tf_char_dex_stat.SetValue(str(Crt.abilities["dex"]))
        self.tf_char_cons_stat.SetValue(str(Crt.abilities["con"]))
        self.tf_char_int_stat.SetValue(str(Crt.abilities["int"]))
        self.tf_char_wis_stat.SetValue(str(Crt.abilities["wis"]))
        self.tf_char_cha_stat.SetValue(str(Crt.abilities["cha"]))
        self.tf_char_str_mod.SetValue(str(round((Crt.abilities["str"] - 10) / 2)))
        self.tf_char_dex_mod.SetValue(str(round((Crt.abilities["dex"] - 10) / 2)))
        self.tf_char_cons_mod.SetValue(str(round((Crt.abilities["con"] - 10) / 2)))
        self.tf_char_int_mod.SetValue(str(round((Crt.abilities["int"] - 10) / 2)))
        self.tf_char_wis_mod.SetValue(str(round((Crt.abilities["wis"] - 10) / 2)))
        self.tf_char_cha_mod.SetValue(str(round((Crt.abilities["cha"] - 10) / 2)))
        self.tf_charac.SetValue(str(Crt.ac))
        self.tf_charinit.SetValue(str(Crt.defined_initiative))
        self.tf_charspeed.SetValue(str(Crt.speed) + "/" + str(Crt.max_speed))
        self.tf_charhit.SetValue(str(Crt.hit_dice).strip("[").strip("]").replace(", ","d"))
        self.m_textCtrl25.SetValue(str(Crt.passive_perception))

        self.tf_acrobatics.SetValue(str(Crt.skills['acrobatics']))
        self.tf_animalhandling.SetValue(str(Crt.skills['animal_handling']))
        self.tf_arcana.SetValue(str(Crt.skills['arcana']))
        self.tf_athletics.SetValue(str(Crt.skills['athletics']))
        self.tf_deception.SetValue(str(Crt.skills['deception']))
        self.tf_history.SetValue(str(Crt.skills['history']))
        self.tf_insight.SetValue(str(Crt.skills['insight']))
        self.tf_intimidation.SetValue(str(Crt.skills['intimidation']))
        self.tf_investigation.SetValue(str(Crt.skills['investigation']))
        self.tf_medicine.SetValue(str(Crt.skills['medicine']))
        self.tf_nature.SetValue(str(Crt.skills['nature']))
        self.tf_perception.SetValue(str(Crt.skills['perception']))
        self.tf_performance.SetValue(str(Crt.skills['performance']))
        self.tf_persuasion.SetValue(str(Crt.skills['persuasion']))
        self.tf_religion.SetValue(str(Crt.skills['religion']))
        self.tf_sleighofhand.SetValue(str(Crt.skills['sleigh_of_hand']))
        self.tf_stealth.SetValue(str(Crt.skills['stealth']))
        self.tf_survival.SetValue(str(Crt.skills['survival']))


    def PerksPopUp(self, event):
        win = TestPopup(self.GetTopLevelParent())
        win.Show(True)


class TestPopup(noname.w_PerksPopUp):

    def __init__(self, parent):
        noname.w_PerksPopUp.__init__(self, parent)
        # crt_name to nie jest to samo crt_name w klasie MainFrame
        crt_name = frame.current_character
        crt_perks = dnd_objects.char_dict[crt_name].perks
        lista_perks = ""
        for i in crt_perks:
            lista_perks += i
            lista_perks += "\n\n"
        self.t_perks.SetLabel(str(lista_perks))


app = wx.App(False)
frame = Mainframe(None)
frame.Show(True)
app.MainLoop()