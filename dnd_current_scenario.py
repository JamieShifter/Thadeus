import dnd_objects
import dnd_data

Thadeus = dnd_objects.crude_make_creature("Thadeus")
Jelly = dnd_objects.crude_make_creature("Jelly", crt_type=dnd_data.creatures["ochre_jelly"])

charpool = [Thadeus, Jelly]