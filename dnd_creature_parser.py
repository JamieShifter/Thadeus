import pandas as _pd
import os as _os
import re



file_creatures = _pd.ExcelFile(str(_os.getcwd()) + r"\dbs\dnd_creatures.xlsx")
creatures = open("creatures.py", "w")
crt_list = []

def parseCreatures(file_creatures):
    for ark in file_creatures.sheet_names:
        nazwa = ark.lower().replace(' ', '_')
        arkusz = file_creatures.parse(ark).fillna("")
        crt = {}
        index = []
        crt["MAIN"] = {}
        crt["ABILITIES"] = {}
        crt["SKILLS"] = {}
        crt["PERKS"] = []
        crt["EQUIPMENT"] = {}
        crt["SPECIAL"] = []
        crt["ID"] = nazwa
        for row in range(len(arkusz)):
            if arkusz["VALUE"][row].isupper():
                index.append((arkusz["VALUE"][row], row))
        index.append(("END", len(arkusz)))
        for i in range(len(index)):
            name = index[i][0]
            val = index[i][1]
            if name == "MAIN":
                for row in range(val+1, index[i+1][1]-1):
                    if arkusz["VALUE"][row] == "hit_dice":
                        crt["MAIN"]["hit_dice"] = str(arkusz["KEY"][row]).split(",")
                    else:
                        crt["MAIN"]["{0}".format(arkusz["VALUE"][row])] = "{0}".format(arkusz["KEY"][row])
            elif name == "ABILITIES":
                for row in range(val+1, index[i+1][1]):
                    crt["ABILITIES"]["{0}".format(arkusz["VALUE"][row])] = "{0}".format(arkusz["KEY"][row])
            elif name == "SKILLS":
                for row in range(val+1, index[i+1][1]):
                    crt["SKILLS"]["{0}".format(arkusz["VALUE"][row])] = "{0}".format(arkusz["KEY"][row])
            elif name == "PERKS":
                for row in range(val+1, index[i+1][1]):
                    crt["PERKS"].append(arkusz["VALUE"][row])
            elif name == "EQUIPMENT":
                for row in range(val+1, index[i+1][1]):
                    crt["EQUIPMENT"]["{0}".format(arkusz["VALUE"][row])] = "{0}".format(arkusz["KEY"][row])
            elif name == "SPECIAL":
                for row in range(val+1, index[i+1][1]):
                    crt["SPECIAL"].append(arkusz["VALUE"][row])
            else:
                pass
        crt_list.append(crt)
        creatures.write(crt["ID"].lower().replace(" ", "_"))
        creatures.write(" = %s" % crt)
        creatures.write("\n")
    creatures.close()


parseCreatures(file)



