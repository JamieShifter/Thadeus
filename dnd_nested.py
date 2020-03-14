"""
Function that returns /'bludgeoning'/ when the type of damage is /'bl/'
"""

mace = {"name":"mace", 'damage':(1,8,"bl"), 'cost':(75, "gp"),"weight":4,"properties":"" }

for i in mace:
    if i =='damage':
        if mace[i][len(mace[i])-1]=='bl':
            print('bludgeoning')
        else: print('dupa')


"""
Function that returns amount of particular coins and overall value
"""


gp={"cost":1}
sp={"cost":0.1}
cp={"cost":0.01}
pp={"cost":10}
ep={"cost":0.5}
sakwa=[gp,gp,gp,ep,sp,sp]

def howmuch():
    d = 0
    for i in sakwa:
        d += (i["cost"])
    gpc=str(sakwa.count(gp))+" gp"
    spc = str(sakwa.count(sp)) + " sp"
    epc = str(sakwa.count(ep)) + " ep"
    cpc = str(sakwa.count(cp)) + " cp"
    ppc = str(sakwa.count(pp)) + " pp"
    list=(gpc, spc, epc, cpc, ppc)
    for i in list:
        if i[0] != '0':
            print(i)
    print(d)




