import dnd_objects
import dnd_mechanics
import dnd_data
import dnd_combat_gui

class perks:

    def __init__(self):
        pass

    def false_appearance(self, caster, *targets):
        pass

    def paralyzing_ray(self, caster, *targets):
        for target in targets:
            roll = dnd_mechanics.roll(20, 1)
            target_constitution_check = roll + target.abilities["con"]
            print("{} DC roll: {}\n".format(target.name, roll))
            print("{} modifier: {}\n".format(target.name, target.abilities["con"]))
            print("{} overall score: {}\n".format(target.name, target_constitution_check))
            if target_constitution_check >= 13:
                print("{} tried to use Paralyzing Ray on {}, but failed".format(caster.name, target.name))
            else:
                reason = "{} succesfully used Paralyzing Ray on {}...".format(caster.name, target.name)
                target.skip_turn(1, reason)

    def life_drain(self, caster, target):
        target_roll = dnd_mechanics.roll(20, 1)
        target_constitution_check = target_roll + target.abilities["con"]
        if "resistance.damage.necrotic" in target.special:
            hit_roll = min([dnd_mechanics.roll(20,1), dnd_mechanics.roll(20,1)])
            print("The dice rolls...\n\nResult: {}".format(str(hit_roll)))
            if hit_roll > target.AC:
                print("{} rolled a higher score than {}'s Armor Class - {}...".
                      format(caster.name, target.name, str(target.ac)))
                damage_roll = dnd_mechanics.roll(8,3) + 5
                target.hp -= damage_roll
                print(
                    "{} drained life forces from {}...\nDespite the resistance, "
                    "the attack was successful and took {} of hp.".
                    format(caster.name, target.name, str(damage_roll)))
                if target_constitution_check >= 13:
                    pass
                else:
                    target.max_hp -= damage_roll
                    print("Horribly, it also lowered {}'s maximum hp by the same amount!".format(target.name))
            else:
                print("{} rolled a lower score than {}'s Armor Class - {}...".
                      format(caster.name, target.name, str(target.ac)))
                print("{}'s attack failed...".format(caster.name))
        elif "immunity.damage.necrotic" in target.special:
            print("{} tried to drain life from {}\nFortunately {} "
                  "is completely immune to necrotic damage, therefore took no damage".
                  format(caster.name, target.name, target.name))
        elif "vulnerability.damage.necrotic" in target.special:
            hit_roll = max([dnd_mechanics.roll(20, 1), dnd_mechanics.roll(20, 1)])
            print("The dice rolls...\n\nResult: {}".format(str(hit_roll)))
            if hit_roll > target.AC:
                print("{} rolled a higher score than {}'s Armor Class - {}...".format(caster.name, target.name,
                                                                                      str(target.ac)))
                damage_roll = dnd_mechanics.roll(8, 3) + 5
                target.hp -= damage_roll
                print(
                    "{} drained life forces from {}...\nDue to the vulnerability, "
                    "the attack was successful and took {} of hp.".
                    format(caster.name, target.name, str(damage_roll)))
                if target_constitution_check >= 13:
                    pass
                else:
                    target.max_hp -= damage_roll
                    print("Horribly, it also lowered {}'s maximum hp by the same amount!".format(target.name))
            else:
                print("{} rolled a lower score than {}'s Armor Class - {}...".format(caster.name, target.name,
                                                                                     str(target.ac)))
                print("{}'s attack failed...".format(caster.name))
        else:
            hit_roll = dnd_mechanics.roll(20, 1)
            print("The dice rolls...\n\nResult: {}".format(str(hit_roll)))
            if hit_roll > target.AC:
                print("{} rolled a higher score than {}'s Armor Class - {}...".format(caster.name, target.name,
                                                                                      str(target.ac)))
                damage_roll = dnd_mechanics.roll(8, 3) + 5
                target.hp -= damage_roll
                print(
                    "{} drained life forces from {}...\nThe attack was successful and took {} of hp.".
                    format(caster.name, target.name, str(damage_roll)))
                if target_constitution_check >= 13:
                    pass
                else:
                    target.max_hp -= damage_roll
                    print("Horribly, it also lowered {}'s maximum hp by the same amount!".format(target.name))
            else:
                print("{} rolled a lower score than {}'s Armor Class - {}...".format(caster.name, target.name,
                                                                                     str(target.ac)))
                print("{}'s attack failed...".format(caster.name))

    def blood_drain(self, caster, target):
        if caster.physical_state != "latched":
            caster.physical_state = "latched"
            print("A Strige just latched to {}!".format(target.name))
        else:
            pass
        damage = (dnd_mechanics.roll(4, 1) + 3)
        target.hp -= damage
        print("A Strige just drained blood from {} dealing {} damage!".format(target.name, str(damage)))
        target.checkOnMe()
        if target.hp <= 0:
            caster.physical_state = "normal"

    def rotting_gaze(self, caster, target):
        target_saving_throw = dnd_mechanics.roll(20, 1) + target.abilities["con"]
        caster_damage_throw = dnd_mechanics.roll(6, 3)
        if target_saving_throw >= 12:
            print("{} Just had a bizzare feeling of being observed...".format(target.name))
        else:
            print("{} Looks at it's hands... There are black spots on the skin, also the smell...\n"
                  "They smell like a dead rat! Now everything starts to get itchy! Then this feeling of dizzyness...\n"
                  "{} pukes on the ground, taking {} damage!".format(target.name, target.name, caster_damage_throw))
            target.hp -= caster_damage_throw
            target.checkOnMe()

    def slam(self, caster, target):
        hit_roll = min([(dnd_mechanics.roll(20, 1) + 3), (dnd_mechanics.roll(20, 1) + 3)]) \
            if "resistance.damage.bludgeoning" in target.special else (dnd_mechanics.roll(20, 1) + 3)
        damage_roll = dnd_mechanics.roll(6, 1) + 1
        if hit_roll >= target.ac:
            target.hp -= damage_roll
            print("{} mindlessly slammed on {}, dealing {} damage!".format(caster.name, target.name, str(damage_roll)))
        else:
            print("{} mindlessly tried to slam on {}, but missed".format(caster.name, target.name))

    def create_food_and_water(self, caster, *targets):
        for target in targets:
            if "food" and "waterskin" in target.eq:
                target.eq["food"].quantity += 1
                target.eq["waterskin"].quantity += 1
            else:
                target.eq["food"] = dnd_data.items["food"].copy()
                target.eq["waterskin"] = dnd_data.items["waterskin"].copy()
                target.eq["food"].quantity += 1
                target.eq["waterskin"].quantity += 1

    def split(self, caster, *targets):
        if caster.hp >= 10:
            division_hp = caster.hp//2
            division_max_hp = caster.max_hp//2
            caster.placeholder["split_counter"] = 1
            new_name = caster.name + str(caster.placeholder["split_counter"]+1)
            Splitted = dnd_objects.crude_make_creature(new_name, crt_type=dnd_data.creatures["ochre_jelly"])
            caster.hp, Splitted.hp = division_hp
            caster.max_hp, Splitted.max_hp = division_max_hp
            Splitted.placeholder["split_counter"] = 1
            dnd_combat_gui.game_on.charpool.append(Splitted)
            dnd_combat_gui.game_on.turn_list.append(Splitted)
            dnd_combat_gui.game_on.enemies.append(Splitted)
            print("{} just split into two smaller ones!")
        else:
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

    def read_thoughts(caster, *targets):
        for target in targets:
            print("{} has read the thoughts of {}! Now {} must reveal one thing {} asks!".
                  format(caster, target, target, caster))


perks = perks()