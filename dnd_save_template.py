import dnd_objects
import dnd_data

Thadeus = dnd_objects.crude_make_creature("Thadeus")
Marishka = dnd_objects.crude_make_creature("Marishka", crt_type=dnd_data.creatures["cleric1"])
Boris = dnd_objects.crude_make_creature("Boris", crt_type=dnd_data.creatures["wizard1"])
Carl = dnd_objects.crude_make_creature("Carl", crt_type=dnd_data.creatures["rogue1"])
Elsa = dnd_objects.crude_make_creature("Elsa", crt_type=dnd_data.creatures["fighter1b"])

Gulbur = dnd_objects.crude_make_creature("Gulbur", crt_type=dnd_data.creatures["orc"])
Murbur = dnd_objects.crude_make_creature("Murbur", crt_type=dnd_data.creatures["orc"])
Basil = dnd_objects.crude_make_creature("Basil", crt_type=dnd_data.creatures["orc"])
Canto = dnd_objects.crude_make_creature("Canto", crt_type=dnd_data.creatures["orc"])
Lipp = dnd_objects.crude_make_creature("Lipp", crt_type=dnd_data.creatures["orc"])

charpool = [Thadeus, Marishka, Boris, Carl, Elsa, Gulbur, Murbur, Basil, Canto, Lipp]
