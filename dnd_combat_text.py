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
            
        > list:
            Use this to see all the characters currently participating in the fight
            
        > end turn:
            Use this to end turn anyway:)
            
        > check eq/check eq full:
            This command lets you see your current wielded weapons/your full equipment
        """,
        "ready":
        """
            Use it to set a trigger on your current character. The interface will lead you through the command;)
            
            >>> ready
            
            Or you can use full syntax:
            
            >>> ready <observed> <trigger> <action> <target=None>
            <observed> = Who are you observing?
            <trigger> = Action of the <observed> that will instantly trigger your <action>
            <action> = Your response to <observed> <trigger>
            <target=None> = if left empty - the <action> will be performed on YOU, 
                otherwise write on whom your <action> should be perfomed!
            
        """,
        "status":
        """
            Displays the status of current character, only the vital information, such as:
            HP: hp/max_hp
            SPEED: speed/max_speed
            CURRENT WEAPON: weapon currently used(equipped)
            PHYSICAL STATE: current physical state of character
            DEATH SAVING THROWS: failures and successes on death saving throws
            NEXT TURN: whose nex turn is
            
        """,
        "stabilize":
        """
            Use this to try and stabilize other creature, granted you are not unconscious or dead;)
            
            >>> stabilize
            
            Or use full syntax:
            
            >>> stabilize <target>
            
        """,
        "knockout":
        """
            Use this to try and knockout other creature granted it just got 0 hp
            
            >>> knockout
            
            Or use full syntax:
            
            >>> knockout <target>
            
        """,
        "kill":
        """
            Use this to try and kill other creature granted it just got 0 hp

            >>> kill

            Or use full syntax:

            >>> kill <target>
        
            """,
        "perk":
        """
            Use this to use a chosen perk, the interface will guide you through the command;)
            
            >>> perk
            
            Or use the full syntax:
            
            >>> perk <whatperk> <target>
            
        """,
        "spell":
            """
                Use this to use a chosen spell, the interface will guide you through the command;)
    
                >>> spell
    
                Or use the full syntax:
    
                >>> spell <whatspell> <target>
    
            """,
        "move":
        """
            Use this to move a specified distance, direction is yet to be implemented!
            The interface will guide you through the command;)
            
            >>> move
            
            Or use the full syntax:
            
            >>> move <distance>
            
            (distance is given in feet)
            
        """,
        "dash":
        """
            Use this to double your current speed! You can also pass <distance> as additional argument and move at the same time!
            
            >>> dash
            >>> dash <distance> = dash + move <distance>
            
        """,
        "disengage":
        """
            If you feel overwhelmed and don't want to provoke a response attack when running away(or you have some other plans:D) - use it
            
            >>> disengage
            
        """,
        "dodge":
        """
            Use this to trigger yourself to try and dodge upcoming attack
            
            >>> dodge
            
        """,
        "help":
        """
            Use this to literally help some other creature(and raise it's advantage in next roll)
            
            >>> help
            
            Or full syntax:
            
            >>> help <target>
            
        """,
        "hide":
        """
            Use this to try and instantly hide!
            
            >>> hide
        """,
        "search":
        """
            Use it to search for an object in some place. The interface will guide you through the command
            
            >>> search
            
            Or use the full syntax:
            
            >>> search <object> <target>
            
        """,
        "use":
        """
            Use this to use a chosen item(on a chosen target)
            
            >>> use
            
            or full syntax:
            
            >>> use <object> <target>
            
        """,
        "check eq":
        """
            Use this to check currently equipped weapons
            
            >>> check eq
            
            Or use with additional argument <full>, to see the full item list on your character
            
            >>> check eq full
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



    def run(self):
        stat = True
        h_counter = 0
        e_counter = 0
        print("+===============================================================+\n")
        print("WELCOME TO THADEUS TURN COMBAT SYSTEM\n")
        print("+===============================================================+\n\n\n")
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
                    elif "attack" in request[:6]:
                        weapon = None
                        target = None
                        if request == "attack":
                            weapon = str(input("What weapon do you want to use?\n-> "))
                            if weapon not in char.eq_on:
                                if weapon not in char.eq:
                                    weapon = str(input("{} does not have such weapon, try again!\n-> ".format(char.name)))
                                else:
                                    dialog = str(input("{} does not have this weapon equipped, but it certainly is in {}'s equipment, do you want to wield it? yes/no"))
                                    if dialog == "no":
                                        weapon = str(
                                            input("What shall be {}'s weapon then?\n-> ".format(char.name)))
                                    elif dialog == "yes":
                                        pass
                                    else:
                                        print("Wrong command!")
                            else:
                                pass
                            target = str(input("And who do you want to attack?\n-> "))
                            for c in self.charpool:
                                if c.name == target:
                                    target = c
                                    break
                            if target not in self.turn_list:
                                target = str(input("There's no {} here, who do you want to attack?\n-> ".format(target)))
                            else:
                                pass
                            for c in self.charpool:
                                if c.name == target:
                                    target = c
                                    break
                            char.attack(weapon, target)
                            finished = True
                        elif " " in request:
                            full_request = request.split(" ")
                            weapon = full_request[1]
                            if weapon not in char.eq_on:
                                if weapon not in char.eq:
                                    weapon = str(
                                        input("{} does NOT have such weapon, what's the WEAPON again?\n-> ".format(char.name)))
                                else:
                                    dialog = str(input(
                                        "{} does not have this weapon equipped, but it certainly is in {}'s equipment, do you want to wield it? yes/no"))
                                    if dialog == "no":
                                        weapon = str(
                                            input("What shall be {}'s weapon then?\n-> ".format(char.name)))
                                    elif dialog == "yes":
                                        pass
                                    else:
                                        print("Wrong command!\n")
                            else:
                                pass
                            target = full_request[2] if len(full_request) == 3 else full_request[2:]
                            for c in self.charpool:
                                if c.name == target:
                                    target = c
                                    break
                            if target not in self.turn_list:
                                target = str(input("There's no {} here, who do you want to attack?\n-> ".format(target)))
                            else:
                                pass
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
                            print("Try again, the format is not correct\n")
                    elif "doc" in request[:4]:
                        if request == "doc":
                            print(self.doc["main"])
                        elif " " in request:
                            kwd = request.split(" ")[1]
                            if kwd in self.doc:
                                print(self.doc[kwd])
                            else:
                                print("There is no such command as {}, try writing 'doc' alone to see available commands\n")
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
                            print("Wrong answer\n")
                        char.ready(observed, trigger, action, target=target)
                        finished = True
                    elif "status" in request[:6]: # TODO: Hide hp, death saving throws for enemies
                        target = request.split(" ")[1] if " " in request else char
                        for c in self.charpool:
                            if target == c.name:
                                target = c
                        target_hp = "{}/{}".format(target.hp, target.max_hp)
                        target_speed = "{}/{}".format(target.speed, target.max_speed)
                        cur_wea = [k for k,v in target.eq_on.items()]
                        target_cur_wea = "{}, {}".format(cur_wea[0], cur_wea[1])
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
                        NEXT TURN: {}\n\n
                        """.format(target.name, target_hp, target_speed, target_cur_wea, target_phy, target_dst, next_turn.name))
                    elif "stabilize" in request[:9]:
                        target = request.split(" ")[1] if " " in request else str(input("Who do you want to stabilize?\n-> "))
                        for c in self.charpool:
                            if target == c.name:
                                target = c
                        char.stabilize(target)
                        finished = True
                    elif "knockout" in request[:8]:
                        target = request.split(" ")[1] if " " in request else str(
                            input("Who do you want to knockout?\n-> "))
                        for c in self.charpool:
                            if target == c.name:
                                target = c
                        char.knockout(target)
                        finished = True
                    elif "kill" in request[:4]:
                        target = request.split(" ")[1] if " " in request else str(
                            input("Who do you want to kill?\n-> "))
                        for c in self.charpool:
                            if target == c.name:
                                target = c
                        char.kill(target)
                        finished = True
                    elif "perk" in request[:4]:
                        perk = request.split(" ")[1] if " " in request else str(
                            input("What perk do you want to use?\n-> "))
                        target = request.split(" ")[2] if " " in request else str(
                            input("On whom do you want to use {}?\n-> ".format(perk)))
                        for c in self.charpool:
                            if target == c.name:
                                target = c
                        char.usePerk(perk, target)
                        finished = True
                    elif "spell" in request[:5]:
                        spell = request.split(" ")[1] if " " in request else str(
                            input("What spell do you want to use?\n-> "))
                        target = request.split(" ")[2] if " " in request else str(
                            input("On whom do you want to use {}?\n-> ".format(spell)))
                        for c in self.charpool:
                            if target == c.name:
                                target = c
                        # char.useSpell(spell, target)
                        # finished = True
                        print("THERE ARE NO SPELLS IMPLEMENTED YET")
                    elif "move" in request[:4]:
                        distance = request.split(" ")[1] if " " in request else str(
                            input("Your current speed is: {}/{}\n\nHow many feet do you want to move?\n-> ".format(char.speed, char.max_speed)))
                        char.move(int(distance))
                        if char.speed == 0:
                            finished = True
                    elif "dash" in request[:4]:
                        distance = request.split(" ")[1] if " " in request else None
                        if distance != None:
                            char.dash()
                            char.move(distance)
                            finished = True
                        else:
                            char.dash()
                    elif "disengage" in request[:9]:
                        char.disengage()
                    elif "dodge" in request[:5]:
                        char.dodge()
                        finished = True
                    elif "help" in request[:4]:
                        target = request.split(" ")[1] if " " in request else str(
                            input("Who do you want to help?\n-> "))
                        for c in self.charpool:
                            if target == c.name:
                                target = c
                        char.help(target)
                        finished = True
                    elif "hide" in request[:4]:
                        char.hide()
                        finished = True
                    elif "search" in request[:6]:
                        obj = request.split(" ")[1] if " " in request else str(
                            input("Where do you want to look?\n-> "))
                        target = request.split(" ")[2] if " " in request else str(
                            input("What are you looking for?\n-> "))
                        char.search(obj, target)
                        finished = True
                    elif "use" in request[:3]:
                        # obj = request.split(" ")[1] if " " in request else str(
                        #     input("What do you want to use?\n-> "))
                        # target = request.split(" ")[2] if " " in request else str(
                        #     input("On what/whom?\n-> "))
                        # char.search(obj, target)
                        # finished = True
                        print("THIS FUNCTION IS NOT IMPLEMENTED YET\n")
                    elif "end turn" in request[:8]:
                        print("Ending {}'s turn\n".format(char.name))
                        finished = True
                    elif "list" in request[:4]:
                        print("HEROES:\n")
                        for hero in self.heroes:
                            print(hero.name)
                        print("\n+=======================================+\nENEMIES:\n")
                        for enemy in self.enemies:
                            print(enemy.name)
                        print("\n+=======================================+\nTo learn details about certain characters, use 'status <target>' command;)\n")
                    elif "check eq" in request[:8]:
                        if request == "check eq":
                            print("{}'s CURRENT WEAPONS:\n\n".format(char.name))
                            for item in char.eq_on:
                                print(item)
                            print("\n\nTo see full item list, write 'check eq full'\n")
                        elif request == "check eq full":
                            print("{}'s ITEM LIST:\n\n".format(char.name))
                            for item in char.eq:
                                print(item)
                            print("\n\n")
                    else:
                        print("There is no {} command, try using 'doc' to see available commands".format(request))

                    if stat == False:
                        break










game_on = Combat()
game_on.run()