import dnd_data as dat
import dnd_objects as ob
import dnd_mechanics as mc
import observer_pattern as flag
import dnd_concrete as p_con

char_pool = []


class readyTriggerFlagDefinition(flag.Subject):
    _observers = []
    _state = 0


    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def change_state(self):
        self._state = 1
        self.notify()

    def reset_state(self):
        self._state = 0


def usePerk(perk, *targets):
    if perk == "parry":
        p_con.perks.parry(*targets)
    elif perk == "false_appearance":
        p_con.perks.false_appearance(*targets)
    elif perk == "paralyzing_ray":
        p_con.perks.paralyzing_ray(*targets)
    elif perk == "life_drain":
        p_con.perks.life_drain(*targets)
    elif perk == "blood_drain":
        p_con.perks.blood_drain(*targets)
    elif perk == "rotting_gaze":
        p_con.perks.rotting_gaze(*targets)
    elif perk == "slam":
        p_con.perks.slam(*targets)
    elif perk == "create_food_and_water":
        p_con.perks.create_food_and_water(*targets)
    elif perk == "split":
        p_con.perks.split(*targets)
    elif perk == "second_wind":
        p_con.perks.second_wind(*targets)
    elif perk == "multiattack":
        p_con.perks.multiattack(*targets)
    elif perk == "wounding_ray":
        p_con.perks.wounding_ray(*targets)
    elif perk == "poison_breath":
        p_con.perks.poison_breath(*targets)
    elif perk == "web":
        p_con.perks.web(*targets)
    elif perk == "surprise_attack":
        p_con.perks.surprise_attack(*targets)
    elif perk == "confusion_ray":
        p_con.perks.confusion_ray(*targets)
    elif perk == "nimble_escape":
        p_con.perks.nimble_escape(*targets)
    elif perk == "bite":
        p_con.perks.bite(*targets)
    elif perk == "rejuvenation":
        p_con.perks.rejuvenation(*targets)
    elif perk == "arcane_recovery":
        p_con.perks.arcane_recovery(*targets)
    elif perk == "ambush":
        p_con.perks.ambush(*targets)
    elif perk == "spider_bite":
        p_con.perks.spider_bite(targets)
    elif perk == "fear_ray":
        p_con.perks.fear_ray(*targets)
    elif perk == "read_thoughts":
        p_con.perks.read_thoughts(*targets)
    else:
        print("Could not find perk {}".format(perk))


readyTriggerFlag = readyTriggerFlagDefinition()