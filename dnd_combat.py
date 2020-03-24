import dnd_objects
import dnd_data
import dnd_mechanics
import dnd_save_template


class Combat:

    doc = {
        "attack":
            """
            Use it to attack other creatures, interface will guide you what to write next. If you feel confident, you
            can use full syntax:
            
            >>> attack <weapon> <target>
            
            You can also pass multiple targets as an argument
            
            >>> attack <weapon> <target> <target1> ...
            """,
        "main":
        """
        Use doc <topic> to learn more about a specific command
        
        > doc: you just used it;)
        
        > attack:
            Physical(usually non-verbal) attack on other creature, use it to shape their character;)
            >>> attack <weapon> <target>
            
        > ready:
            Can you feel it coming? Make yourself ready for it! Check this doc for more details.
            >>> ready <observed> <trigger> <action> <target=None>
            
        > status:
            See what's not shown on your screen, look into stats and souls of your characters!
            >>> status <target>
            
        > stabilize:
            Somebody's dying? Stabilize them, 'cause that's what heroes do...
            >>> stabilize <target>
            
        > knockout:
            Knock the s*it out of this guy lying there helplessly...
            >>> knockout <target>
            
        > kill:
            That's brutal. Use it to instantly kill unconscious creature(also works as a mercy kill).
            >>> kill <target>
            
        > perk:
            Oh boy, use with caution(provided you know what you're doing).
            >>> perk <whatperk> <target>
            
        > spell:
            Do you believe in magic? Or The Force?
            >>> spell <whatspell> <target>
            
        > move:
            What's more to say about it, just do it
            >>> move <distance>
            
        > dash:
            This is a bit tricky, use it to double your speed(counts as an action)
            >>> dash <distance>(optional)
            
        > disengage:
            Tired of fighting? Use it
            >>> disengage
        
        > dodge:
            Not a car, but an action. Use it if you anticipate that someone will attack you soon, doesn't work in real life
            >>> dodge
        
        > help:
            Literally help somebody in whatever they're doing. Funny outcomes possible:D
            >>> help <target>
        
        > hide:
            Sneaky Sneaky
            >>> hide
        
        > search:
            Use it to search the object for a target object(i.e search wardrobe for your cool new socks)
            >>> search <object> <target>
        
        > use:
            Use object on a target(i.e person). Do not objectify other people, that's rude.
            >>> use <object> <target>
        """
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
                    elif "attack" in request[:6]:   # TODO: Need to fix usage of weapons not possessed
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
                    elif "doc" in request[:4]:
                        if request == "doc":
                            print(self.doc["main"])
                        elif " " in request:
                            kwd = request.split(" ")[1]
                            if kwd in self.doc:
                                print(self.doc[kwd])
                            else:
                                print("There is no such command as {}, try writing 'doc' alone to see available commands")
                    elif "ready" in request[:5]:
                        observed = request.split(" ")[1] if " " in request and len(request.split(" ")) > 1 else str(input("Who are you watching?\n-> "))
                        trigger = request.split(" ")[2] if " " in request and len(request.split(" ")) > 2 else str(input("To do what?\n-> "))
                        action = request.split(" ")[3] if " " in request and len(request.split(" ")) > 3 else str(input("What are you gonna do then?\n-> "))
                        target = request.split(" ")[4] if " " in request and len(request.split(" ")) > 4 else str(input("To yourself? yes/no\n-> "))
                        if target == "yes":
                            target = char
                        elif target == "no":
                            target = str(input("Then to whom?\n-> "))
                        else:
                            print("Wrong answer")
                        char.ready(observed, trigger, action, target=target)
                        finished = True
                    elif "status" in request[:6]: # TODO: Hide hp, death saving throws for enemies
                        target = request.split(" ")[1] if " " in request else char
                        for c in self.charpool:
                            if target == c.name:
                                target = c
                        target_hp = "{}/{}".format(target.hp, target.max_hp)
                        target_speed = "{}/{}".format(target.speed, target.max_speed)
                        target_cur_wea = "FIXME" # TODO: Just fix it
                        target_phy = target.physical_state
                        target_dst = "failure: {}, success: {}".format(target.death_saves["failure"], target.death_saves["success"])
                        next_turn = self.turn_list[self.turn_list.index(target)+1]
                        print("""
                        {} - vital info:
                        
                        HP: {}
                        SPEED: {}
                        CURRENT WEAPON: {}
                        PHYSICAL STATE: {}
                        DEATH SAVING THROWS: {}
                        NEXT TURN: {}
                        """.format(target.name, target_hp, target_speed, target_cur_wea, target_phy, target_dst, next_turn.name))
                        pass
                    elif "stabilize" in request[:9]:
                        pass
                    elif "knockout" in request[:8]:
                        pass
                    elif "kill" in request[:4]:
                        pass
                    elif "perk" in request[:4]:
                        pass
                    elif "spell" in request[:5]:
                        pass
                    elif "move" in request[:4]:
                        pass
                    elif "dash" in request[:4]:
                        pass
                    elif "disengage" in request[:9]:
                        pass
                    elif "dodge" in request[:5]:
                        pass
                    elif "help" in request[:4]:
                        pass
                    elif "hide" in request[:4]:
                        pass
                    elif "search" in request[:6]:
                        pass
                    elif "use" in request[:3]:
                        pass
                    else:
                        print("There is {} command, try using 'doc' to see available commands".format(request))


                    if stat == False:
                        break










game_on = Combat()
game_on.run()