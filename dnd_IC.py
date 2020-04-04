
import observer_pattern
import dnd_concrete as p_con

char_pool = []



class readyTriggerFlagDefinition(observer_pattern.Subject):
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

def usePerk(caster, perk, *targets):
    if perk == "false_appearance":
        p_con.perks.false_appearance(caster, *targets)
    elif perk == "paralyzing_ray":
        p_con.perks.paralyzing_ray(caster, *targets)
    elif perk == "life_drain":
        p_con.perks.life_drain(caster, *targets)
    elif perk == "blood_drain":
        p_con.perks.blood_drain(caster, *targets)
    elif perk == "rotting_gaze":
        p_con.perks.rotting_gaze(caster, *targets)
    elif perk == "slam":
        p_con.perks.slam(caster, *targets)
    elif perk == "create_food_and_water":
        p_con.perks.create_food_and_water(caster, *targets)
    elif perk == "split":
        p_con.perks.split(caster, *targets)
    elif perk == "second_wind":
        p_con.perks.second_wind(caster, *targets)
    elif perk == "multiattack":
        p_con.perks.multiattack(caster, *targets)
    elif perk == "wounding_ray":
        p_con.perks.wounding_ray(caster, *targets)
    elif perk == "poison_breath":
        p_con.perks.poison_breath(caster, *targets)
    elif perk == "web":
        p_con.perks.web(caster, *targets)
    elif perk == "surprise_attack":
        p_con.perks.surprise_attack(caster, *targets)
    elif perk == "confusion_ray":
        p_con.perks.confusion_ray(caster, *targets)
    elif perk == "nimble_escape":
        p_con.perks.nimble_escape(caster, *targets)
    elif perk == "bite":
        p_con.perks.bite(caster, *targets)
    elif perk == "rejuvenation":
        p_con.perks.rejuvenation(caster, *targets)
    elif perk == "arcane_recovery":
        p_con.perks.arcane_recovery(caster, *targets)
    elif perk == "ambush":
        p_con.perks.ambush(caster, *targets)
    elif perk == "spider_bite":
        p_con.perks.spider_bite(targets)
    elif perk == "fear_ray":
        p_con.perks.fear_ray(caster, *targets)
    elif perk == "read_thoughts":
        p_con.perks.read_thoughts(caster, *targets)
        p_con.perks.read_thoughts(caster, *targets)
    else:
        print("Could not find perk {}".format(perk))


readyTriggerFlag = readyTriggerFlagDefinition()