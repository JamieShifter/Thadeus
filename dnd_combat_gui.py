import dnd_objects
import dnd_data
import dnd_mechanics
import dnd_save_template


class Combat:

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


game_on = Combat()

new_game = Combat()
print("1st list : 2nd list")
for i in range(len(game_on.turn_list)):
    print("{} : {}".format(game_on.turn_list[i].name, new_game.turn_list[i].name))



