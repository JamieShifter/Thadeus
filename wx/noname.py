# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1200, 728), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.tab_mainmenupanel = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TAB_TRAVERSAL)
        self.m_notebook1.AddPage(self.tab_mainmenupanel, u"Main Menu", False)
        self.tab_characterpanel = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.TAB_TRAVERSAL)
        gs_character = wx.GridSizer(0, 4, 0, 0)

        self.m_charlist = wx.ListCtrl(self.tab_characterpanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.LC_LIST)
        gs_character.Add(self.m_charlist, 0, wx.ALL | wx.EXPAND, 5)

        fg_char_main = wx.FlexGridSizer(16, 3, 0, 0)
        fg_char_main.SetFlexibleDirection(wx.BOTH)
        fg_char_main.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.t_charname = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        self.t_charname.Wrap(-1)
        fg_char_main.Add(self.t_charname, 0, wx.ALL, 5)

        self.tf_charname = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_READONLY)
        fg_char_main.Add(self.tf_charname, 0, wx.ALL, 5)

        fg_char_main.AddSpacer(5)

        self.t_charclass = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Class", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.t_charclass.Wrap(-1)
        fg_char_main.Add(self.t_charclass, 0, wx.ALL, 5)

        self.tf_charclass = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_READONLY)
        fg_char_main.Add(self.tf_charclass, 0, wx.ALL, 5)

        fg_char_main.AddSpacer(5)

        self.t_charlevel = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Level", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.t_charlevel.Wrap(-1)
        fg_char_main.Add(self.t_charlevel, 0, wx.ALL, 5)

        self.tf_charlevel = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_READONLY)
        fg_char_main.Add(self.tf_charlevel, 0, wx.ALL, 5)

        fg_char_main.AddSpacer(5)

        self.t_charphys = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Physical state", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.t_charphys.Wrap(-1)
        fg_char_main.Add(self.t_charphys, 0, wx.ALL, 5)

        self.tf_charphys = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_READONLY)
        fg_char_main.Add(self.tf_charphys, 0, wx.ALL, 5)

        fg_char_main.AddSpacer(5)

        self.t_charhp = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Hit Points", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.t_charhp.Wrap(-1)
        fg_char_main.Add(self.t_charhp, 0, wx.ALL, 5)

        self.tf_charhp = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, wx.TE_READONLY)
        fg_char_main.Add(self.tf_charhp, 0, wx.ALL, 5)

        fg_char_main.AddSpacer(5)

        self.t_charexp = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Experience", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.t_charexp.Wrap(-1)
        fg_char_main.Add(self.t_charexp, 0, wx.ALL, 5)

        self.tf_charexp = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, wx.TE_READONLY)
        fg_char_main.Add(self.tf_charexp, 0, wx.ALL, 5)

        fg_char_main.AddSpacer(5)

        fg_char_main.AddSpacer(5)

        self.b_levelup = wx.Button(self.tab_characterpanel, wx.ID_ANY, u"LevelUp", wx.DefaultPosition, wx.Size(75, 30),
                                   0)
        fg_char_main.Add(self.b_levelup, 0, wx.ALL, 5)

        fg_char_main.AddSpacer(5)

        fg_char_main.AddSpacer(5)

        self.m_staticline1 = wx.StaticLine(self.tab_characterpanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.LI_HORIZONTAL)
        fg_char_main.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        fg_char_main.AddSpacer(5)

        fg_char_main.AddSpacer(5)

        self.t_dsc1 = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"STAT", wx.DefaultPosition, wx.DefaultSize, 0)
        self.t_dsc1.Wrap(-1)
        fg_char_main.Add(self.t_dsc1, 0, wx.ALL, 5)

        self.t_dsc2 = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"MOD", wx.DefaultPosition, wx.DefaultSize, 0)
        self.t_dsc2.Wrap(-1)
        fg_char_main.Add(self.t_dsc2, 0, wx.ALL, 5)

        self.t_charstr = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"STRENGTH", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.t_charstr.Wrap(-1)
        fg_char_main.Add(self.t_charstr, 0, wx.ALL, 5)

        self.tf_char_str_stat = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main.Add(self.tf_char_str_stat, 0, wx.ALL, 5)

        self.tf_char_str_mod = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main.Add(self.tf_char_str_mod, 0, wx.ALL, 5)

        self.t_chardex = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"DEXTERITY", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.t_chardex.Wrap(-1)
        fg_char_main.Add(self.t_chardex, 0, wx.ALL, 5)

        self.tf_char_dex_stat = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main.Add(self.tf_char_dex_stat, 0, wx.ALL, 5)

        self.tf_char_dex_mod = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main.Add(self.tf_char_dex_mod, 0, wx.ALL, 5)

        self.t_charconst = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"CONSTITUTION", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.t_charconst.Wrap(-1)
        fg_char_main.Add(self.t_charconst, 0, wx.ALL, 5)

        self.tf_char_cons_stat = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main.Add(self.tf_char_cons_stat, 0, wx.ALL, 5)

        self.tf_char_cons_mod = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main.Add(self.tf_char_cons_mod, 0, wx.ALL, 5)

        self.t_charint = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"INTELLIGENCE", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.t_charint.Wrap(-1)
        fg_char_main.Add(self.t_charint, 0, wx.ALL, 5)

        self.tf_char_int_stat = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main.Add(self.tf_char_int_stat, 0, wx.ALL, 5)

        self.tf_char_int_mod = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main.Add(self.tf_char_int_mod, 0, wx.ALL, 5)

        self.t_charwis = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"WISDOM", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.t_charwis.Wrap(-1)
        fg_char_main.Add(self.t_charwis, 0, wx.ALL, 5)

        self.tf_char_wis_stat = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main.Add(self.tf_char_wis_stat, 0, wx.ALL, 5)

        self.tf_char_wis_mod = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main.Add(self.tf_char_wis_mod, 0, wx.ALL, 5)

        self.t_charcha = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"CHARISMA", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.t_charcha.Wrap(-1)
        fg_char_main.Add(self.t_charcha, 0, wx.ALL, 5)

        self.tf_char_cha_stat = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main.Add(self.tf_char_cha_stat, 0, wx.ALL, 5)

        self.tf_char_cha_mod = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main.Add(self.tf_char_cha_mod, 0, wx.ALL, 5)

        gs_character.Add(fg_char_main, 1, wx.EXPAND, 5)

        fg_char_main2 = wx.FlexGridSizer(13, 3, 0, 0)
        fg_char_main2.SetFlexibleDirection(wx.BOTH)
        fg_char_main2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.t_charac = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Armor Class", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.t_charac.Wrap(-1)
        fg_char_main2.Add(self.t_charac, 0, wx.ALL, 5)

        self.tf_charac = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, wx.TE_READONLY)
        fg_char_main2.Add(self.tf_charac, 0, wx.ALL, 5)

        fg_char_main2.AddSpacer(5)

        self.t_charinit = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Initiative", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.t_charinit.Wrap(-1)
        fg_char_main2.Add(self.t_charinit, 0, wx.ALL, 5)

        self.tf_charinit = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_READONLY)
        fg_char_main2.Add(self.tf_charinit, 0, wx.ALL, 5)

        fg_char_main2.AddSpacer(5)

        self.t_charspeed = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Speed", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.t_charspeed.Wrap(-1)
        fg_char_main2.Add(self.t_charspeed, 0, wx.ALL, 5)

        self.tf_charspeed = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_READONLY)
        fg_char_main2.Add(self.tf_charspeed, 0, wx.ALL, 5)

        fg_char_main2.AddSpacer(5)

        self.t_charhit = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Hit Dice", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.t_charhit.Wrap(-1)
        fg_char_main2.Add(self.t_charhit, 0, wx.ALL, 5)

        self.tf_charhit = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, wx.TE_READONLY)
        fg_char_main2.Add(self.tf_charhit, 0, wx.ALL, 5)

        fg_char_main2.AddSpacer(5)

        fg_char_main2.AddSpacer(5)

        self.t_chards = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Death Saves", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.t_chards.Wrap(-1)
        fg_char_main2.Add(self.t_chards, 0, wx.ALL, 5)

        fg_char_main2.AddSpacer(5)

        self.tf_chars = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main2.Add(self.tf_chars, 0, wx.ALL, 5)

        self.t_charsf = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Success/Failure", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        self.t_charsf.Wrap(-1)
        fg_char_main2.Add(self.t_charsf, 0, wx.ALL, 5)

        self.tf_charf = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.Size(50, -1), wx.TE_READONLY)
        fg_char_main2.Add(self.tf_charf, 0, wx.ALL, 5)

        self.t_charperception = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Perception", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.t_charperception.Wrap(-1)
        fg_char_main2.Add(self.t_charperception, 0, wx.ALL, 5)

        self.m_textCtrl25 = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_READONLY)
        fg_char_main2.Add(self.m_textCtrl25, 0, wx.ALL, 5)

        fg_char_main2.AddSpacer(5)

        fg_char_main2.AddSpacer(5)

        self.m_staticline2 = wx.StaticLine(self.tab_characterpanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 10),
                                           wx.LI_HORIZONTAL)
        fg_char_main2.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        fg_char_main2.AddSpacer(5)

        fg_char_main2.AddSpacer(5)

        self.m_bitmap2 = wx.StaticBitmap(self.tab_characterpanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                         wx.Size(100, 120), 0)
        fg_char_main2.Add(self.m_bitmap2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fg_char_main2.AddSpacer(5)

        fg_char_main2.AddSpacer(5)

        self.b_charprofic = wx.Button(self.tab_characterpanel, wx.ID_ANY, u"Proficiency", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        fg_char_main2.Add(self.b_charprofic, 0, wx.ALL, 5)

        fg_char_main2.AddSpacer(5)

        fg_char_main2.AddSpacer(5)

        self.b_charperks = wx.Button(self.tab_characterpanel, wx.ID_ANY, u"Perks", wx.DefaultPosition, wx.DefaultSize,
                                     0)
        fg_char_main2.Add(self.b_charperks, 0, wx.ALL, 5)

        fg_char_main2.AddSpacer(5)

        fg_char_main2.AddSpacer(5)

        self.b_charexpertise = wx.Button(self.tab_characterpanel, wx.ID_ANY, u"Expertise", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        fg_char_main2.Add(self.b_charexpertise, 0, wx.ALL, 5)

        fg_char_main2.AddSpacer(5)

        fg_char_main2.AddSpacer(5)

        self.t_charpersonal = wx.Button(self.tab_characterpanel, wx.ID_ANY, u"Personal", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        fg_char_main2.Add(self.t_charpersonal, 0, wx.ALL, 5)

        gs_character.Add(fg_char_main2, 1, wx.EXPAND, 5)

        g_skills = wx.GridSizer(18, 2, 0, 0)

        self.t_acrobatics = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Acrobatics", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.t_acrobatics.Wrap(-1)
        g_skills.Add(self.t_acrobatics, 0, wx.ALL, 5)

        self.tf_acrobatics = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_acrobatics, 0, wx.ALL, 5)

        self.t_animalhandling = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Animal Handling",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.t_animalhandling.Wrap(-1)
        g_skills.Add(self.t_animalhandling, 0, wx.ALL, 5)

        self.tf_animalhandling = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_animalhandling, 0, wx.ALL, 5)

        self.t_arcana = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Arcana", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.t_arcana.Wrap(-1)
        g_skills.Add(self.t_arcana, 0, wx.ALL, 5)

        self.tf_arcana = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_arcana, 0, wx.ALL, 5)

        self.t_athletics = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Athletics", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.t_athletics.Wrap(-1)
        g_skills.Add(self.t_athletics, 0, wx.ALL, 5)

        self.tf_athletics = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_athletics, 0, wx.ALL, 5)

        self.t_deception = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Deception", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.t_deception.Wrap(-1)
        g_skills.Add(self.t_deception, 0, wx.ALL, 5)

        self.tf_deception = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_deception, 0, wx.ALL, 5)

        self.t_history = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"History", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.t_history.Wrap(-1)
        g_skills.Add(self.t_history, 0, wx.ALL, 5)

        self.tf_history = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_history, 0, wx.ALL, 5)

        self.t_insight = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Insight", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.t_insight.Wrap(-1)
        g_skills.Add(self.t_insight, 0, wx.ALL, 5)

        self.tf_insight = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_insight, 0, wx.ALL, 5)

        self.t_intimidation = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Intimidation", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.t_intimidation.Wrap(-1)
        g_skills.Add(self.t_intimidation, 0, wx.ALL, 5)

        self.tf_intimidation = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_intimidation, 0, wx.ALL, 5)

        self.t_investigation = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Investigation", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.t_investigation.Wrap(-1)
        g_skills.Add(self.t_investigation, 0, wx.ALL, 5)

        self.tf_investigation = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_investigation, 0, wx.ALL, 5)

        self.t_medicine = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Medicine", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.t_medicine.Wrap(-1)
        g_skills.Add(self.t_medicine, 0, wx.ALL, 5)

        self.tf_medicine = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_medicine, 0, wx.ALL, 5)

        self.t_nature = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Nature", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.t_nature.Wrap(-1)
        g_skills.Add(self.t_nature, 0, wx.ALL, 5)

        self.tf_nature = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_nature, 0, wx.ALL, 5)

        self.t_perception = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Perception", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.t_perception.Wrap(-1)
        g_skills.Add(self.t_perception, 0, wx.ALL, 5)

        self.tf_perception = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_perception, 0, wx.ALL, 5)

        self.t_performance = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Performance", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.t_performance.Wrap(-1)
        g_skills.Add(self.t_performance, 0, wx.ALL, 5)

        self.tf_performance = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                          wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_performance, 0, wx.ALL, 5)

        self.t_persuasion = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Persuasion", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.t_persuasion.Wrap(-1)
        g_skills.Add(self.t_persuasion, 0, wx.ALL, 5)

        self.tf_persuasion = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_persuasion, 0, wx.ALL, 5)

        self.t_religion = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Religion", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.t_religion.Wrap(-1)
        g_skills.Add(self.t_religion, 0, wx.ALL, 5)

        self.tf_religion = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_religion, 0, wx.ALL, 5)

        self.t_sleighofhand = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Sleigh of hand", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.t_sleighofhand.Wrap(-1)
        g_skills.Add(self.t_sleighofhand, 0, wx.ALL, 5)

        self.tf_sleighofhand = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_sleighofhand, 0, wx.ALL, 5)

        self.t_stealth = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Stealth", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.t_stealth.Wrap(-1)
        g_skills.Add(self.t_stealth, 0, wx.ALL, 5)

        self.tf_stealth = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_stealth, 0, wx.ALL, 5)

        self.t_survival = wx.StaticText(self.tab_characterpanel, wx.ID_ANY, u"Survival", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.t_survival.Wrap(-1)
        g_skills.Add(self.t_survival, 0, wx.ALL, 5)

        self.tf_survival = wx.TextCtrl(self.tab_characterpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                       wx.DefaultSize, wx.TE_READONLY)
        g_skills.Add(self.tf_survival, 0, wx.ALL, 5)

        gs_character.Add(g_skills, 1, wx.EXPAND, 5)

        self.tab_characterpanel.SetSizer(gs_character)
        self.tab_characterpanel.Layout()
        gs_character.Fit(self.tab_characterpanel)
        self.m_notebook1.AddPage(self.tab_characterpanel, u"Character", True)
        self.tab_equipmentpanel = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                           wx.TAB_TRAVERSAL)
        gSizer9 = wx.GridSizer(0, 3, 0, 0)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        box_characterChoices = []
        self.box_character = wx.ComboBox(self.tab_equipmentpanel, wx.ID_ANY, u"Character", wx.DefaultPosition,
                                         wx.DefaultSize, box_characterChoices, 0)
        bSizer9.Add(self.box_character, 0, wx.ALL, 5)

        gSizer11 = wx.GridSizer(10, 6, 0, 0)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        self.i_head = wx.BitmapButton(self.tab_equipmentpanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                      wx.Size(30, 30), wx.BU_AUTODRAW)
        gSizer11.Add(self.i_head, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        self.i_neck = wx.BitmapButton(self.tab_equipmentpanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                      wx.Size(30, 30), wx.BU_AUTODRAW)
        gSizer11.Add(self.i_neck, 1, wx.ALL | wx.EXPAND, 5)

        self.i_chest = wx.BitmapButton(self.tab_equipmentpanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                       wx.Size(30, 30), wx.BU_AUTODRAW)
        gSizer11.Add(self.i_chest, 1, wx.ALL | wx.EXPAND, 5)

        self.i_arms = wx.BitmapButton(self.tab_equipmentpanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                      wx.Size(30, 30), wx.BU_AUTODRAW)
        gSizer11.Add(self.i_arms, 1, wx.ALL | wx.EXPAND, 5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        self.i_ring = wx.BitmapButton(self.tab_equipmentpanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                      wx.Size(30, 30), wx.BU_AUTODRAW)
        gSizer11.Add(self.i_ring, 1, wx.ALL | wx.EXPAND, 5)

        self.i_legs = wx.BitmapButton(self.tab_equipmentpanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                      wx.Size(30, 30), wx.BU_AUTODRAW)
        gSizer11.Add(self.i_legs, 1, wx.ALL | wx.EXPAND, 5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        self.i_boots = wx.BitmapButton(self.tab_equipmentpanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                       wx.Size(30, 30), wx.BU_AUTODRAW)
        gSizer11.Add(self.i_boots, 1, wx.ALL | wx.EXPAND, 5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        self.i_weapon1 = wx.BitmapButton(self.tab_equipmentpanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                         wx.Size(30, 30), wx.BU_AUTODRAW)
        gSizer11.Add(self.i_weapon1, 1, wx.ALL | wx.EXPAND, 5)

        self.i_weapon2 = wx.BitmapButton(self.tab_equipmentpanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                         wx.Size(30, 30), wx.BU_AUTODRAW)
        gSizer11.Add(self.i_weapon2, 1, wx.ALL | wx.EXPAND, 5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        self.tf_weapon1 = wx.TextCtrl(self.tab_equipmentpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, wx.TE_READONLY)
        gSizer11.Add(self.tf_weapon1, 0, wx.ALL, 5)

        gSizer11.AddSpacer(5)

        self.tf_weapon2 = wx.TextCtrl(self.tab_equipmentpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                      wx.DefaultSize, wx.TE_READONLY)
        gSizer11.Add(self.tf_weapon2, 0, wx.ALL, 5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        self.t_armor = wx.StaticText(self.tab_equipmentpanel, wx.ID_ANY, u"Armor: ", wx.DefaultPosition, wx.DefaultSize,
                                     0)
        self.t_armor.Wrap(-1)
        gSizer11.Add(self.t_armor, 0, wx.ALL, 5)

        gSizer11.AddSpacer(5)

        self.tf_armor = wx.TextCtrl(self.tab_equipmentpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, wx.TE_READONLY)
        gSizer11.Add(self.tf_armor, 0, wx.ALL, 5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        gSizer11.AddSpacer(5)

        self.t_modifiers = wx.StaticText(self.tab_equipmentpanel, wx.ID_ANY, u"Modifiers: ", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.t_modifiers.Wrap(-1)
        gSizer11.Add(self.t_modifiers, 0, wx.ALL, 5)

        gSizer11.AddSpacer(5)

        self.tf_modifiers = wx.TextCtrl(self.tab_equipmentpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, wx.TE_READONLY)
        gSizer11.Add(self.tf_modifiers, 0, wx.ALL, 5)

        bSizer9.Add(gSizer11, 1, wx.EXPAND, 5)

        gSizer9.Add(bSizer9, 1, wx.EXPAND, 5)

        gSizer10 = wx.GridSizer(0, 1, 0, 0)

        self.l_backpack = wx.ListCtrl(self.tab_equipmentpanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.LC_LIST)
        gSizer10.Add(self.l_backpack, 1, wx.ALL | wx.EXPAND, 5)

        gSizer9.Add(gSizer10, 1, wx.EXPAND, 5)

        gSizer12 = wx.GridSizer(20, 3, 0, 0)

        self.t_money = wx.StaticText(self.tab_equipmentpanel, wx.ID_ANY, u"Money", wx.DefaultPosition, wx.DefaultSize,
                                     0)
        self.t_money.Wrap(-1)
        gSizer12.Add(self.t_money, 0, wx.ALL, 5)

        self.tf_money = wx.TextCtrl(self.tab_equipmentpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                    wx.DefaultSize, wx.TE_READONLY)
        gSizer12.Add(self.tf_money, 0, wx.ALL, 5)

        gSizer12.AddSpacer(5)

        self.t_weigth = wx.StaticText(self.tab_equipmentpanel, wx.ID_ANY, u"Weight", wx.DefaultPosition, wx.DefaultSize,
                                      0)
        self.t_weigth.Wrap(-1)
        gSizer12.Add(self.t_weigth, 0, wx.ALL, 5)

        self.tf_weight = wx.TextCtrl(self.tab_equipmentpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.DefaultSize, wx.TE_READONLY)
        gSizer12.Add(self.tf_weight, 0, wx.ALL, 5)

        self.t_overencumbered = wx.StaticText(self.tab_equipmentpanel, wx.ID_ANY, u"Overencumbered!",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.t_overencumbered.Wrap(-1)
        self.t_overencumbered.Hide()

        gSizer12.Add(self.t_overencumbered, 0, wx.ALL, 5)

        self.b_trade = wx.Button(self.tab_equipmentpanel, wx.ID_ANY, u"Trade!", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer12.Add(self.b_trade, 0, wx.ALL, 5)

        gSizer12.AddSpacer(5)

        gSizer12.AddSpacer(5)

        gSizer12.AddSpacer(5)

        gSizer12.AddSpacer(5)

        gSizer12.AddSpacer(5)

        self.b_use = wx.Button(self.tab_equipmentpanel, wx.ID_ANY, u"Use", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer12.Add(self.b_use, 0, wx.ALL, 5)

        gSizer9.Add(gSizer12, 1, wx.EXPAND, 5)

        self.tab_equipmentpanel.SetSizer(gSizer9)
        self.tab_equipmentpanel.Layout()
        gSizer9.Fit(self.tab_equipmentpanel)
        self.m_notebook1.AddPage(self.tab_equipmentpanel, u"Equipment", False)
        self.tab_actionpanel = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        gSizer13 = wx.GridSizer(0, 3, 0, 0)

        gSizer14 = wx.GridSizer(2, 1, 0, 0)

        bSizer15 = wx.BoxSizer(wx.VERTICAL)

        r_characteractionChoices = [u"sample"]
        self.r_characteraction = wx.RadioBox(self.tab_actionpanel, wx.ID_ANY, u"Character", wx.DefaultPosition,
                                             wx.DefaultSize, r_characteractionChoices, 1, wx.RA_SPECIFY_COLS)
        self.r_characteraction.SetSelection(0)
        bSizer15.Add(self.r_characteraction, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gSizer14.Add(bSizer15, 1, wx.EXPAND, 5)

        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        self.b_goaction = wx.Button(self.tab_actionpanel, wx.ID_ANY, u"GO!", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer16.Add(self.b_goaction, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.tree_action = wx.TreeCtrl(self.tab_actionpanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TR_DEFAULT_STYLE)
        bSizer16.Add(self.tree_action, 1, wx.ALL | wx.EXPAND, 5)

        gSizer14.Add(bSizer16, 1, wx.EXPAND, 5)

        gSizer13.Add(gSizer14, 1, wx.EXPAND, 5)

        bSizer18 = wx.BoxSizer(wx.VERTICAL)

        bSizer19 = wx.BoxSizer(wx.VERTICAL)

        bSizer19.SetMinSize(wx.Size(-1, 400))
        r_enemyactionChoices = [u"sample"]
        self.r_enemyaction = wx.RadioBox(self.tab_actionpanel, wx.ID_ANY, u"Enemy", wx.DefaultPosition, wx.DefaultSize,
                                         r_enemyactionChoices, 1, wx.RA_SPECIFY_COLS)
        self.r_enemyaction.SetSelection(0)
        bSizer19.Add(self.r_enemyaction, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer18.Add(bSizer19, 1, wx.EXPAND, 5)

        bSizer21 = wx.BoxSizer(wx.VERTICAL)

        bSizer21.SetMinSize(wx.Size(-1, 25))
        bSizer23 = wx.BoxSizer(wx.VERTICAL)

        gSizer21 = wx.GridSizer(1, 3, 1, 0)

        gSizer21.SetMinSize(wx.Size(-1, 25))
        box_charactionindChoices = []
        self.box_charactionind = wx.ComboBox(self.tab_actionpanel, wx.ID_ANY, u"Character", wx.DefaultPosition,
                                             wx.DefaultSize, box_charactionindChoices, 0)
        gSizer21.Add(self.box_charactionind, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        box_actionindChoices = []
        self.box_actionind = wx.ComboBox(self.tab_actionpanel, wx.ID_ANY, u"Action", wx.DefaultPosition, wx.DefaultSize,
                                         box_actionindChoices, 0)
        gSizer21.Add(self.box_actionind, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        self.b_goind = wx.Button(self.tab_actionpanel, wx.ID_ANY, u"GO!", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer21.Add(self.b_goind, 0, wx.ALL | wx.ALIGN_BOTTOM, 5)

        bSizer23.Add(gSizer21, 1, wx.EXPAND, 5)

        self.m_treeCtrl5 = wx.TreeCtrl(self.tab_actionpanel, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 300),
                                       wx.TR_DEFAULT_STYLE)
        bSizer23.Add(self.m_treeCtrl5, 1, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer21.Add(bSizer23, 1, wx.EXPAND, 5)

        bSizer18.Add(bSizer21, 1, wx.EXPAND, 5)

        gSizer13.Add(bSizer18, 1, wx.EXPAND, 5)

        bSizer24 = wx.BoxSizer(wx.VERTICAL)

        l_logChoices = []
        self.l_log = wx.ListBox(self.tab_actionpanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, l_logChoices,
                                wx.LB_EXTENDED)
        bSizer24.Add(self.l_log, 1, wx.ALL | wx.EXPAND, 5)

        self.c_commandline = wx.TextCtrl(self.tab_actionpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(-1, 200), 0)
        bSizer24.Add(self.c_commandline, 0, wx.ALL | wx.EXPAND, 5)

        gSizer13.Add(bSizer24, 1, wx.EXPAND, 5)

        self.tab_actionpanel.SetSizer(gSizer13)
        self.tab_actionpanel.Layout()
        gSizer13.Fit(self.tab_actionpanel)
        self.m_notebook1.AddPage(self.tab_actionpanel, u"Action", False)
        self.tab_mappanel = wx.Panel(self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.m_notebook1.AddPage(self.tab_mappanel, u"Map", False)

        bSizer2.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer2)
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar(1, 0, wx.ID_ANY)
        self.m_menubar2 = wx.MenuBar(0)
        self.SetMenuBar(self.m_menubar2)

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_charlist.Bind(wx.EVT_LIST_ITEM_SELECTED, self.UpdateScreen)
        self.b_charperks.Bind(wx.EVT_BUTTON, self.PerksPopUp)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def UpdateScreen(self, event):
        event.Skip()

    def PerksPopUp(self, event):
        event.Skip()


###########################################################################
## Class PerksPopUp
###########################################################################


class w_PerksPopUp(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_scrolledWindow = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                  wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow.SetScrollRate(5, 5)
        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.t_perks = wx.StaticText(self.m_scrolledWindow, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize,
                                     0)
        self.t_perks.Wrap(-1)
        bSizer12.Add(self.t_perks, 1, wx.ALL | wx.EXPAND, 5)

        self.m_scrolledWindow.SetSizer(bSizer12)
        self.m_scrolledWindow.Layout()
        bSizer12.Fit(self.m_scrolledWindow)
        bSizer11.Add(self.m_scrolledWindow, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer11)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass