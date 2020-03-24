import dnd_objects
import dnd_mechanics
<<<<<<< HEAD

class perks:

    def parry(*targets):
        if len(targets) > 1:
            pass
        else:
            for target in targets:
                target.hide() # just to check if it works, indeed it does



    def false_appearance(*targets):
=======
import dnd_data

class perks:


    def false_appearance(caster, *targets):
>>>>>>> e4817f1ec2be1a4db4e7596c98d6fcf037e885d1
        
            pass


    def nimble_escape(*targets):
        pass


    def paralyzing_ray(*targets):
        pass


    def life_drain(*targets):
        pass


    def blood_drain(*targets):
        pass


    def rotting_gaze(*targets):
        pass


    def slam(*targets):
        pass


<<<<<<< HEAD
    def create_food_and_water(*targets):
        
            pass


    def split(*targets):
        
=======
    def create_food_and_water(caster, *targets):
        for target in targets:
            if "food" and "waterskin" in target.eq:
                target.eq["food"].quantity += 1
                target.eq["waterskin"].quantity += 1
            else:
                target.eq["food"] = dnd_data.items["food"].copy()
                target.eq["waterskin"] = dnd_data.items["waterskin"].copy()
                target.eq["food"].quantity += 1
                target.eq["waterskin"].quantity += 1


    def split(*targets):
        for target in targets:
            if target.hp > target.max_hp/2:
                new_name = target.name + " {}".format(split_counter)
                dnd_objects.char_dict[new_name] = dnd_objects.crude_make_creature(new_name,
                                                                                  crt_type=dnd_data.creatures["ochre_jelly"])
                target.hp //= 2
                dnd_objects.char_dict[new_name].hp //= 2

>>>>>>> e4817f1ec2be1a4db4e7596c98d6fcf037e885d1
            pass


    def second_wind(*targets):
        for target in targets:
            roll = dnd_mechanics.roll(10, 1)
            recover = roll + target.level
            if target.hp != target.max_hp and recover <= (target.max_hp - target.hp):
                target.hp += recover
                print("{} used second wind as a bonus action, in result {} healed for {} points and now has {} hp!".format(target.name, target.name, recover, target.hp))
            elif target.hp != target.max_hp and recover > (target.max_hp - target.hp):
                target.hp = target.max_hp
                print("{} used second wind as a bonus action, in result {} healed for {} points and now has {} hp!".format(target.name, target.name, recover, target.hp))
            else:
                print("{} tried to use second wind, but something went wrong".format(target.name))


    def multiattack(*targets):
        
            pass


    def wounding_ray(*targets):
        pass


    def poison_breath(*targets):
        pass


    def web(*targets):
        pass


    def surprise_attack(*targets):
        
            pass


    def confusion_ray(*targets):
        pass


    def bite(*targets):
        pass


    def rejuvenation(*targets):
        
            pass


    def arcane_recovery(*targets):
        # Once per day recover spell slots that is are up to half of your wizard level(rounded up)
            pass


    def ambush(*targets):
        
            pass


    def spider_bite(*targets):
        itself = targets.pop(0)


        pass


    def fear_ray(*targets):
        pass


<<<<<<< HEAD
    def read_thoughts(*targets):
        pass
=======
    def read_thoughts(caster, *targets):
        for target in targets:
            print("{} has read the thoughts of {}! Now {} must reveal one thing {} asks!".
                  format(caster, target, target, caster))
>>>>>>> e4817f1ec2be1a4db4e7596c98d6fcf037e885d1


perks = perks