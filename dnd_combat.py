import dnd_objects
import dnd_data
import dnd_mechanics
import dnd_save_template


class Combat:

    doc = {

    }


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
        self.charpool = dnd_save_template.charpool
        self.initiative_scores = {}
        self.turn_list = []
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
            if char.char_class == "fighter"\
                or char.char_class == "wizard"\
                or char.char_class == "cleric"\
                    or char.char_class == "rogue":
                self.heroes.append(char)
            else:
                self.enemies.append(char)

    def sort(self):
        for char in self.charpool:
            score = dnd_mechanics.roll(20, 1) + char.initiative()
            self.initiative_scores[str(char.name)] = score

        while len(self.initiative_scores) > 0:
            max_init = max(self.initiative_scores)
            for c in self.charpool:
                if c.name == max_init:
                    self.turn_list.append(c)
                    del self.initiative_scores[max_init]

        for i in self.turn_list:
            if i in self.surprise_list:
                self.turn_list.append(self.turn_list.pop(i))

    def turn(self, char):
        print("{}, now it's your turn! What are you gonna do?".format(char.name))
        request = str(input("->  "))
        return request



    def run(self):
        stat = True
        h_counter = 0
        e_counter = 0
        while stat:
            if h_counter == len(self.heroes) or e_counter == len(self.enemies):
                """
                Every time someone is knocked out or killed, respective counter is incremented. 
                Every time someone regains consciousness - respective counter is decremented
                """
                stat = False
            for char in self.turn_list:
                finished = False
                if stat == False:
                    break
                while not finished:
                    request = self.turn(char)
                    if request == "__stop":         # exit combat
                        stat = False
                        finished = True
                    elif "attack" in request:   # TODO: Need to fix usage of weapons not possessed
                        weapon = None
                        target = None
                        if request == "attack":
                            weapon = str(input("What weapon do you want to use?\n-> "))
                            target = str(input("And who do you want to attack?\n-> "))
                            for c in self.charpool:
                                if c.name == target:
                                    target = c
                                    break
                            char.attack(weapon, target)
                            finished = True
                        elif " " in request:
                            full_request = request.split(" ")
                            weapon = full_request[1]
                            target = full_request[2] if len(full_request) == 3 else full_request[2:]
                            if isinstance(target, list):
                                targetlist = []
                                for t in target:
                                    for c in self.charpool:
                                        if t == c.name:
                                            targetlist.append(c)
                                char.attack(weapon, targetlist)
                            else:
                                for c in self.charpool:
                                    if target == c.name:
                                        target = c
                                        break
                                char.attack(weapon, target)
                                finished = True
                        else:
                            print("Try again, the format is not correct")
                    elif "doc" in request:
                        if request == "doc":
                            print(self.doc["main"])
                        elif " " in request:
                            kwd = request.split(" ")[1]
                            if kwd in self.doc:
                                print(self.doc[kwd])
                            else:
                                print("There is no such command as {}, try writing 'doc' alone to see available commands")
                    if stat == False:
                        break










game_on = Combat()
game_on.run()