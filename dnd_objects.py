#######################################################################################################################
#   Name: dnd_creature
#   Author: JamieShifter
#   Date: 29.01.2020
#   Usage: This module contains superclass 'Creature' used for instantiation of concrete creatures throughout the game
#
#######################################################################################################################
# IMPORTS
import dnd_mechanics
import dnd_data
import observer_pattern
import dnd_IC


#######################################################################################################################
# GLOBALS = NONE
#######################################################################################################################
# CLASSES

class Creature(observer_pattern.Observer): #TODO: Turn management, bonus actions, modifiers
    """
This class will serve as an abstract class. It will not be instantiated with default values.
It will be instantiated as a concrete Monster/Character class containing concrete values, when there's a need
to do so.
Parameters will have to be passed as in the example given below:
>>> thadeus = Creature
>>> thadeus.name = 'thadeus'
"""

# ======================================================================================================================
# VARIABLES
# ======================================================================================================================
# METHODS

    def __init__(self):
        self.name = ""
        self.level = 1  # will advance if gained enough xp
        self.xp = 0  # experience points
        self.hp = 0  # current hp
        self.max_hp = 0  # maximum hp for this level
        self.ac = 0  # armor class/how much you have to throw to hit somebody
        self.eq = {}  # list of items
        self.eq_on = {}  # list of items that you wear
        self.physical_state = "normal"  # incapacitated, prone, crouch, normal, poisoned
        self.mental_state = ""  # yet to be implemented
        self.engaged = 0  # 1 means you are currently in combat, 0 means you are disengaged
        self.trigger_dodge = 0  # 1 means you will try to dodge the next attack coming at you, uses action
        self.speed = 0  # your current speed
        self.max_speed = 0  # your maximum speed
        self.adv = 0  # 1 means you have advantage on chosen activity, -1 means disadvantage
        self.hidden = 0  # 1 means you are hidden
        self.hit_dice = []  # your hit dice
        self.death_saves = {'success': 0, 'failure': 0}  # keeping track of your death saving throws, should be reset
        self.defined_initiative = 0  # takes any number
        self.char_class = ""  # class of your character, modifiers are applied
        self.passive_perception = 0
        self.proficiency_bonus = 0
        self.moneybag = {}
        self.weight = 0.0
        self.watchlist = {"attack": 0, "hide": 0, "disengage": 0, "dodge": 0, "move": 0}
        self.actionlist = {"attack": 0, "hide": 0, "disengage": 0, "dodge": 0, "move": 0}
        self.target = ''
        # STATS
        self.abilities = {
            'con': 0,
            'int': 0,
            'wis': 0,
            'cha': 0,
            'dex': 0,
            'str': 0
        }
        self.skills = {
            'athletics': 0,
            'religion': 0,
            'nature': 0,
            'investigation': 0,
            'history': 0,
            'arcana': 0,
            'survival': 0,
            'perception': 0,
            'medicine': 0,
            'insight': 0,
            'animal_handling': 0,
            'persuasion': 0,
            'performance': 0,
            'intimidation': 0,
            'deception': 0,
            'stealth': 0,
            'acrobatics': 0,
            'sleigh_of_hand': 0
        }
        self.proficiency = {}

        self.special = []

        self.perks = []

        self.carrying_cap = 0

    def weaponUsedNow(self):
        eq_on_list = self.eq_on[:]
        return eq_on_list[0]

    def initiative(self):
        score = (self.abilities["dex"] - 10)//2
        return score

    def watched(self, action):
        self.watchlist[action] = 1


    def update(self, subject: observer_pattern.Subject):
        if self.target != self.name:
            if self.actionlist["attack"] == 1:
                self.attack(self.weaponUsedNow(), self.target)
                self.actionlist["attack"] = 0
        elif self.actionlist["hide"] == 1:
            self.hide()
            self.actionlist["hide"] = 0
        elif self.actionlist["disengage"] == 1:
            self.disengage()
            self.actionlist["disengage"] = 0
        elif self.actionlist["dodge"] == 1:
            self.dodge()
            self.actionlist["dodge"] = 0
        elif self.actionlist["move"] == 1:
            self.move(int(self.target))
            self.actionlist["move"] = 0
        dnd_IC.readyTriggerFlag.reset_state()


    def ready(self, observed, trigger, action, target=None):
        try:
            dnd_IC.readyTriggerFlag.attach(self)
        except:
            dnd_IC.readyTriggerFlag._observers.append(self)
        observed.watched(trigger)
        self.actionlist[action] = 1
        self.target = target if target != None else self.name


    def carryingCap(self):
        self.carrying_cap = int(self.abilities["str"]) * 15


    def currentWeight(self):
        self.weight = 0
        for k, v in self.eq.items():
            if k != "moneybag":
                self.weight += v["weight"]
        return self.weight


    def weightCheck(self):
        # This would need to run every time something is changed in eq
        if self.currentWeight() <= self.carrying_cap:
            self.speed = self.max_speed
        else:
            print("You are encumbered")
            self.speed /= 2


    def resetDeathSavingThrows(self):
        self.death_saves['success'] = 0
        self.death_saves['failure'] = 0


    def deathSavingThrow(self):
        if self.physical_state != "dead":
            if self.hp <= 0:
                roll = dnd_mechanics.roll(20, 1)
                if roll == 20:
                    self.hp = 1
                    self.resetDeathSavingThrows()
                    print("Gods blessing! {} wakes up and regains 1 Hit Point".format(self.name))
                elif roll == 1:
                    self.death_saves["failure"] += 2
                    print("{} feels the cold hand of death on the shoulder\nDeath Save Failures: {}\nDeath Save Successes: {}".format(self.name, self.death_saves["failure"], self.death_saves["success"]))
                elif roll >= 10:
                    self.death_saves["success"] += 1
                    print("{} doesn't give up on life!\nDeath Save Failures: {}\nDeath Save Successes: {}".format(self.name, self.death_saves["failure"], self.death_saves["success"]))
                else:
                    self.death_saves["failure"] += 1
                    print("{} is slowly drifting into the abyss...\nDeath Save Failures: {}\nDeath Save Successes: {}".format(self.name, self.death_saves["failure"], self.death_saves["success"]))
                if self.death_saves["failure"] >= 3:
                    self.physical_state = "dead"
                    print("{} is dead".format(self.name))
                    self.resetDeathSavingThrows()
                elif self.death_saves["success"] >= 3:
                    self.physical_state = "normal"
                    self.hp = 1
                    print("{} is back on feet!".format(self.name))
                    self.resetDeathSavingThrows()
            else:
                print("{} is fine!".format(self.name))
        else:
            print("{} is dead, there's nothing you can do...".format(self.name))

    def showHP(self):
        print("{0)/{1}".format(self.hp, self.max_hp))


    def showSpeed(self):
        print("{0)/{1}".format(self.speed, self.max_speed))


    def stabilize(self, target):
        if self.hp >= 0:
            if target.physical_state != "dead":
                roll = dnd_mechanics.roll(20, 1)
                score = roll + self.skills["medicine"] if self.skills["medicine"] == 1 else roll + self.skills["medicine"] + self.proficiency_bonus
                if score >= 10:
                    target.resetDeathSavingThrows()
                    target.hp = 0
                    print("{} managed to stabilize {}".format(self.name, target.name))
                else:
                    print("{} didn't manage to stabilize {}!".format(self.name, target.name))
                    pass
            else:
                print("{} is dead, there's nothing {} could do...".format(target.name, self.name))
        else:
            print("{} can't stabilize {}, {} is dying".format(self.name, target.name, self.name))


    def knockOut(self, target):
        if self.hp >= 0:
            if target.hp <= 0:
                print("{} knocked out {}".format(self.name, target.name))
                target.physical_state = "knocked-out"
                target.hp = 0
            else:
                print("{} can't knock out {}, {} is on guard!".format(self.name, target.name, target.name))
        else:
            print("{} can't knock out {}, {} is dying".format(self.name, target.name, self.name))


    def kill(self, target):
        if self.hp >= 0:
            if target.hp <= 0:
                print("{} killed {}".format(self.name, target.name))
                target.physical_state = "dead"
            else:
                print("{} can't kill {}, {} is on guard!".format(self.name, target.name, target.name))
        else:
            print("{} can't kill {}, {} is dying".format(self.name, target.name, self.name))

    def checkOnEnemy(self, target):
        if target.hp <= 0:
            target.physical_state = "unconscious"
            print("{} is uncoscious".format(target.name))
        else:
            pass

    def usePerk(self, perk, *targets):
        targetlist = []
        caster = self
        if len(targets) == 0:
            dnd_IC.usePerk(perk, self)
        elif self in targets and len(targets) > 1:
            targetlist.append(self)
            targets.remove(self)
            for i in targets:
                targetlist.append(i)
                dnd_IC.usePerk(caster, perk, targetlist)
        else:
            dnd_IC.usePerk(caster, perk, *targets)


    def castSpell(self, spell, *targets): # TODO: Add spells and spellcasting
        pass


    def attack(self, weapon="current", *targets): #TODO: If character has more dexterity than strength, he can choose to use it as a modifier if a weapon is light enough:/
        wpn = self.weaponUsedNow() if weapon == "current" else dnd_data.items[weapon] #TODO: Sneak attack grants a modifier to dexterity based attacks(check the class sheet)
        hit_roll = 0
        damage_score = 0
        total_ac = 0
        for i in targets:
            # ============ #
            # dodge_mechanics
            if i.trigger_dodge != 0:
                self.adv = -1
            # ============ #
            if int(self.hp) >= 0 and i.physical_state != "dead":
                # ====== HIT_ROLL ====== #
                if self.adv == 0:
                    hit_roll = dnd_mechanics.roll(20, 1)
                    print("{} rolls {} on a hit roll".format(self.name, hit_roll))
                elif self.adv == 1:
                    hit_roll = max(dnd_mechanics.roll(20, 1), dnd_mechanics.roll(20, 1))
                    print("{} has an advantage and rolls {} on a hit roll".format(self.name, hit_roll))
                else:
                    hit_roll = min(dnd_mechanics.roll(20, 1), dnd_mechanics.roll(20, 1))
                    print("{} has a disadvantage and rolls {} on a hit roll".format(self.name, hit_roll))
                dmg_type = self.abilities["dex"] if "RANGED" in wpn["type"] else self.abilities["str"]
                modifier = round((dmg_type - 10) / 2)
                hit_score = hit_roll + modifier + self.proficiency_bonus
                print("... Adding hit roll ({}), modifier ({}) and proficiency bonus ({}), sum is: {}".format(
                    hit_roll, modifier, self.proficiency_bonus, hit_score))
                if "parry" in i.perks:
                    total_ac += dnd_mechanics.roll(6, 1)
                else:
                    total_ac = i.ac
                if hit_roll == 20:
                    damage_roll = dnd_mechanics.roll(self.hit_dice[0], self.hit_dice[1] * 2)
                elif hit_roll != 20 and hit_score >= total_ac:
                    damage_roll = dnd_mechanics.roll(self.hit_dice[0], self.hit_dice[1])
                else:
                # ===== MISS ====== #
                    print("{} missed, hit score({}) is lesser that {} armor class ({})".format(self.name, hit_score,
                                                                                           i.name, total_ac))
                    break
                damage_score = damage_roll + modifier
                damage_type = wpn["damage"][2]
                if "immunity.{}".format(damage_type) in i.special:
                    i.hp -= 0
                    print("{0} hit with {1}, it seems to have no effect!".format(i.name, wpn['name']))
                    self.checkOnEnemy(i)
                elif "vulnerability.{}".format(damage_type) in i.special:
                    i.hp -= damage_score * 2
                    print("{0} hit with {1}, caused damage is {2}".format(i.name, wpn['name'], damage_score * 2))
                    self.checkOnEnemy(i)
                elif "resistance.{}".format(damage_type) in i.special:
                    i.hp -= damage_score / 2
                    print("{0} hit with {1}, caused damage is {2}".format(i.name, wpn['name'], damage_score / 2))
                    self.checkOnEnemy(i)
                else:
                    i.hp -= damage_score
                    print("{0} hit with {1}, caused damage is {2}".format(i.name, wpn['name'], damage_score))
                    self.checkOnEnemy(i)
            elif i.hp <= 0 and i.physical_state != "dead":
                if damage_score >= i.max_hp:
                    i.physical_state = "dead"
                elif hit_roll == 20 and damage_score << i.max_hp:
                    i.death_saves["failure"] += 2
                elif hit_roll << 20 and damage_score << i.max_hp:
                    i.death_saves["failure"] += 1
                else:
                    pass
            elif int(self.hp) <= 0:
                print("{} can't fight with 0 or less hp".format(self.name))
                print("{} Current physical state is: {}\n".format(self.name, self.physical_state))
            elif i.physical_state == "dead":
                print("Chop, chop, {} attacks dead body of {}".format(self.name, i.name))

        if self.watchlist["attack"] == 1:
            dnd_IC.readyTriggerFlag.change_state()
        else:
            pass


    def move(self, distance: int):
        if self.hp >= 0:
            if self.speed >= distance:
                self.speed -= distance
                if self.watchlist["move"] == 1:
                    dnd_IC.readyTriggerFlag.change_state()
                else:
                    pass
            else:
                print("{} can't cover that distance, {} has only {} points left!".format(self.name, self.name, self.speed))
        else:
            print("...{} can't move now, dying".format(self.name))



    def dash(self):
        if self.hp >= 0:
            self.speed *= 2
            print("{} used dash! Now it's speed is doubled!".format(self.name))
        else:
            print("...{} can't use dash right now, dying".format(self.name))
        if self.watchlist["dash"] == 1:
            dnd_IC.readyTriggerFlag.change_state()
        else:
            pass


    def disengage(self):
        if self.hp >= 0:
            self.engaged = 0
            print("{} is disengaged from combat".format(self.name))
        else:
            print("...{} can't disengage right now, dying".format(self.name))
        if self.watchlist["didengage"] == 1:
            dnd_IC.readyTriggerFlag.change_state()
        else:
            pass


    def dodge(self):
        if self.physical_state == "incapacitated" or self.speed == 0:
            print("{} can't dodge right now, because of current physical state or speed".format(self.name))
            pass
        elif self.hp <= 0:
            print("{} can't dodge right now, dying".format(self.name))
            pass
        else:
            self.trigger_dodge = 1
            print("{} is ready to dodge incoming attack!".format(self.name))
        if self.watchlist["dodge"] == 1:
            dnd_IC.readyTriggerFlag.change_state()
        else:
            pass


    def help(self, target):
        if self.hp >= 0:
            if target.adv <= 0:
                target.adv += 1
                print("{} helped {}, now {} has an advantage!".format(self.name, target.name, target.name))
            else:
                print("%s already has advantage" % target.name)
        else:
            print("...{} can't help {} right now, {} is dying".format(self.name, target.name, self.name))


    def hide(self):
        if self.hp >= 0:
            if self.hidden == 0:
                self.hidden = 1
                print("{} is now hidden!".format(self.name))
            else:
                print("{} is already trying to hide".format(self.name))
            if self.watchlist["hide"] == 1:
                dnd_IC.readyTriggerFlag.change_state()
            else:
                pass

        else:
            print("...{} can't hide right now, {} is dying".format(self.name, self.name))


    def search(self, obj, target):
        if self.hp >= 0:
            print("You're looking for {} in {}".format(target, obj))
            score = dnd_mechanics.roll(20, 1)
            total = self.skills["perception"] + score
            if total >= 10:
                print("Success, you've found {}!".format(target))
            else:
                print("After a while of searching, you didn't manage to find {}".format(target))
        else:
            print("...{} can't search anything right now, {} is dying".format(self.name, self.name))


    def use(self, object):
        object.use()  # TO BE DONE


    def lootAll(self, target):
        for k, v in target.eq.items():
            if k in self.eq:
                if k != "moneybag":
                    self.eq[k]["quantity"] += 1
                else:
                    for cur, val in v.items():
                        self.eq["moneybag"][cur] = val
            else:
                self.eq[k] = v
        target.eq = {}


    def balancedLootMoney(self, target, *people):
        factor = len(people)
        if "moneybag" in target.eq:
            pool = target.eq["moneybag"].copy()
            for cur in target.eq["moneybag"]:
                target.eq["moneybag"][cur] = 0
            for k, v in pool.items():
                v = int(v)
                if v >> 0 and v%factor == 0:
                    for p in people:
                        if k not in p.eq["moneybag"]:
                            p.eq["moneybag"][k] = 0
                        p.eq["moneybag"][k] += v%factor
                    pool[k] = 0
                elif v%factor != 0:
                    while pool[k] != 0:
                        for p in people:
                            if k not in p.eq["moneybag"]:
                                p.eq["moneybag"][k] = 0
                            p.eq["moneybag"][k] += 1
                            pool[k] -= 1
                            if pool[k] == 0:
                                break
                else:
                    pass

    
    def addNewItem(self, name, quantity, cost, weight, type, obj):
        self.eq[name] = {'name': name, 'quantity': quantity, 'cost': cost, 'weight': weight, 'type': type, 'obj': obj}


#======================================================================================================================
# MAKE CREATURE METHOD

def crude_make_creature(crt_name, crt_type=dnd_data.creatures["fighter1"]):
    creature = Creature()
    if crt_type["EQUIPMENT"]["money"] is "0":
        cur_money = {"gp": 0}
    elif "random" in crt_type["EQUIPMENT"]["money"][0]:
        level = int(crt_type["EQUIPMENT"]["money"][0].strip(")").split("(")[1])
        cur_money = dnd_mechanics.randomize_money(level)
    else:
        cur_money = {crt_type["EQUIPMENT"]["money"][0].split(" ")[1]: int(crt_type["EQUIPMENT"]["money"][0].split(" ")[0])}
    creature.name = crt_name
    creature.xp = int(crt_type["MAIN"]["xp"])
    creature.hp = int(crt_type["MAIN"]["max_hp"])
    creature.max_hp = int(crt_type["MAIN"]["max_hp"])
    creature.ac = int(crt_type["MAIN"]["ac"])
    try:
        creature.proficiency_bonus = int(crt_type["MAIN"]["proficiency_bonus"])
    except:
        creature.proficiency_bonus = 0
    for id in crt_type["EQUIPMENT"]["equipment"]:
        try:
            spid = id.split(" ")
            if spid[0].isdigit():
                if len(spid) == 1:
                    pass
                else:
                    quant = spid[0]
                    spid.pop(0)
                    item = '_'.join(spid)
                    creature.eq[item] = dnd_data.items.get(item).copy()
                    creature.eq[item]["quantity"] = int(quant)
            elif "random" in id:
                def yieldItems():
                    itemlevel = int(id.replace(")", "").split("(")[1])
                    for i in dnd_mechanics.randomizedItemList(itemlevel):
                        creature.eq[i] = dnd_data.items.get(i.replace(" ", "_")).copy()
                yieldItems()
            else:
                creature.eq[id.replace(" ", "_")] = dnd_data.items.get(id.replace(" ", "_")).copy()
                creature.eq[id.replace(" ", "_")]["quantity"] = 1
        except:
            if "random" not in id:
                creature.eq[id.replace(" ", "_")] = {
                    'name': id.replace(" ", "_"),
                    'quantity': 1,
                    'cost': [0, 'gp'],
                    'weight': 0.0,
                    'type': 'OTHER',
                    'obj': 'misc'
                }
            else:
                pass
    for id in crt_type["EQUIPMENT"]["equipment on"]:
        if id in creature.eq:
            try:
                spid = id.split(" ")
                if len(spid) == 1 and spid[0].isdigit():
                    pass
                else:
                    creature.eq_on[id.replace(" ", "_")] = creature.eq[id.replace(" ", "_")]
                    creature.eq_on[id.replace(" ", "_")]["quantity"] = creature.eq[id.replace(" ", "_")]["quantity"]
            except:
                raise
        elif id == '':
            pass
        else:
            try:
                creature.eq[id.replace(" ", "_")] = dnd_data.items.get(id.replace(" ", "_")).copy()
            except:
                pass
    creature.moneybag = dnd_mechanics.calculate_money(cur_money)
    creature.eq["moneybag"] = cur_money
    creature.physical_state = crt_type['MAIN']['physical_state']
    creature.speed = int(crt_type['MAIN']['max_speed'])
    creature.max_speed = int(crt_type['MAIN']['max_speed'])
    if len(crt_type['MAIN']['hit_dice']) >> 1:
        for i in crt_type['MAIN']['hit_dice']:
            creature.hit_dice.append(int(i))
    else:
        for i in crt_type['MAIN']['hit_dice'][0].split("."):
            creature.hit_dice.append(int(i))
    creature.defined_initiative = crt_type['MAIN']['defined_initiative']
    creature.char_class = crt_type["MAIN"]['char_class']
    creature.passive_perception = crt_type["MAIN"]['passive_perception']

    for k, v in crt_type["ABILITIES"].items():
        creature.abilities[k] = int(v)
    for k, v in crt_type["SKILLS"].items():
        creature.skills[k] = int(v)
    creature.perks = crt_type["PERKS"]
    creature.special = crt_type["SPECIAL"]
    creature.carryingCap()
    creature.weight = creature.currentWeight()
    char_dict[crt_name] = creature
    return creature

char_dict = {}



# ======================================================================================================================

# UNIT TEST


if __name__ == "__main__":

    Thadeus = crude_make_creature("Thadeus")
    Marita = crude_make_creature("Marita")
    Absol = crude_make_creature("Absol")
    Enemy = crude_make_creature("Enemy", crt_type=dnd_data.creatures["doppelganger"])
    Thadeus.balancedLootMoney(Enemy, Thadeus, Marita, Absol)
    people = [Thadeus, Marita, Absol, Enemy]
    for i in people:
        print(i.eq['moneybag'])






# ======================================================================================================================