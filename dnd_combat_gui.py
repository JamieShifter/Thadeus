import dnd_objects
import dnd_data
import dnd_mechanics


class Combat:
    """
    Order of use:
    1. make an instance of Combat()
    2. instance.load_scenario(path to scenario)
    3. instance.load_charpool()
    4. instance.start_routine()
    5. instance.run()

    """

    def __init__(self, conditions=0):
        """

        :param conditions:
                0 - normal
                1 - heroes surprise enemies
                2 - enemies surprise heroes
        """
        self.conditions = conditions
        self.surprise_list = []
        self.heroes = []
        self.enemies = []
        self.charpool = []
        self.initiative_scores = {}
        self.turn_list = []

    def start_routine(self):
        self.assign()
        self.check_for_surprise()
        self.sort()

    def check_for_surprise(self):
        if self.conditions == 1:
            for enemy in self.enemies:
                for hero in self.heroes:
                    modifier = 2 if hero.hidden == 1 else 0
                    counter = 0
                    if enemy.passive_perception < hero.abilities["dex"] + modifier:
                        counter += 1
                        if counter == len(self.heroes):
                            self.surprise_list.append(enemy)
        elif self.conditions == 2:
            for hero in self.heroes:
                for enemy in self.enemies:
                    counter = 0
                    modifier = 2 if enemy.hidden == 1 else 0
                    if hero.passive_perception < enemy.abilities["dex"] + modifier:
                        counter += 1
                        if counter == len(self.enemies):
                            self.surprise_list.append(hero)
        else:
            pass

    def assign(self):
        for char in self.charpool:
            if char.char_class == "fighter" \
                    or char.char_class == "wizard" \
                    or char.char_class == "cleric" \
                    or char.char_class == "rogue":
                self.heroes.append(char)
            else:
                self.enemies.append(char)

    def sort(self):
        for char in self.charpool:
            score = dnd_mechanics.roll(20, 1) + char.initiative()
            self.initiative_scores[str(char.name)] = score

        while len(self.initiative_scores) > 0:
            max_value = max(self.initiative_scores.values())
            character = [name for name, score in self.initiative_scores.items() if score == max_value][0]
            self.turn_list.append([c for c in self.charpool if c.name == character][0])
            del self.initiative_scores[character]

        for i in self.turn_list:
            if i in self.surprise_list:
                self.turn_list.append(self.turn_list.pop(i))

    def turn(self, char):
        print("{}, now it's your turn! What are you gonna do?".format(char.name))
        request = str(input("->  "))
        return request

    def load_scenario(self, scenario): # TODO: Importing combat scenarios after button click
        """
        Current idea is to import one file: dnd_current_scenario, but before doing it - rewrite it from a different
        scenario file. So you specify the path -> file gets opened -> file gets copied -> file gets written as new current
        scenario file -> then import current scenario file -> use charpool that exists there.

        :param scenario: path to an existing scenario
        :return: nothing, just assigns a charpool with created characters.
        """
        open("dnd_current_scenario.py", "w").close()
        f = open('{}'.format(scenario))
        f1 = open('dnd_current_scenario.py', 'a')
        for x in f.readlines():
            f1.write(x)
        f.close()
        f1.close()

    def load_charpool(self):
        import dnd_current_scenario
        self.charpool = dnd_current_scenario.charpool

    def run(self):
        stat = True
        h_counter = 0
        e_counter = 0
        while stat:  # TODO: knock out and kill counters
            if h_counter == len(self.heroes) or e_counter == len(self.enemies):
                stat = False
            for char in self.turn_list:
                print(char.name)
                main_action_counters = {
                    "attack": 0,
                    "dodge": 0,
                    "ready": 0,
                    "hide": 0,
                    "use": 0,
                    "stabilize": 0,
                    "perk": 0,
                    "spell": 0,
                    "dash": 0,
                    "disengage": 0,
                    "help": 0,
                }

                bonus_action_counters = {
                    "knockout": 0,
                    "kill": 0,
                    "use": 0,
                    "move": 0,
                    "special_perk": 0,
                    "search": 0,
                    "other": 0,
                }
                main_counter = 0
                bonus_counter = 0
                finished = False
                if stat is False:
                    break
                while not finished:
                    if char.turns_to_skip["quantity"] > 0:
                        print("{} has to skip turn.\nReason: {}".format(char.name, char.turns_to_skip["reason"]))
                        char.turns_to_skip["quantity"] -= 1
                        finished = True
                    else:
                        # THOSE LINES ARE TO BE REMOVED ONCE GUI IS IMPLEMENTED
                        request = str(input())
                        if request == "main":
                            main_action_counters["attack"] += 1
                        elif request == "bonus":
                            bonus_action_counters["other"] += 1
                        elif request == "split":
                            char.usePerk("split")
                        else: # DANGEROUS BUT NECESSARY FOR TESTING, DELETE OR HASH ONCE DONE
                            eval(request)
                        # ======================================================
                        if 1 in main_action_counters.values():
                            main_counter = 1
                        if 1 in bonus_action_counters.values():
                            bonus_counter = 1
                        if main_counter == 1 and bonus_counter == 1:
                            finished = True
                            print("One tour finished")


game_on = Combat()
game_on.load_scenario(r"C:\Users\User\PycharmProjects\Thadeus\dbs\combat_scenarios\test_scenario_ochre_jelly.txt")
# FOR TESTING OF COURSE MODIFY THE PATH TO SCENARIO
game_on.load_charpool()
game_on.start_routine()
# game_on.run()
# if __name__ == "__main__":
#     game_on = Combat()
#     game_on.load_scenario(r"C:\Users\User\PycharmProjects\Thadeus\dbs\combat_scenarios\test_scenario_ochre_jelly.txt")
#     # FOR TESTING OF COURSE MODIFY THE PATH TO SCENARIO
#     game_on.load_charpool()
#     game_on.start_routine()
#     game_on.run()





