import dnd_objects
import dnd_mechanics

class perks:

    def parry(*targets):
        if len(targets) > 1:
            pass
        else:
            for target in targets:
                target.hide() # just to check if it works, indeed it does



    def false_appearance(*targets):
        
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


    def create_food_and_water(*targets):
        
            pass


    def split(*targets):
        
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


    def read_thoughts(*targets):
        pass


perks = perks