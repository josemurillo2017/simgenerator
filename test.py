#All fun and games. Nothing serious happening here. Just messing around to see if the various functions work

from classes import *
from simulation_functions import *

jose = Person("{'Handsome': 100, 'Sexy':20}", "{'Handsome': 100, 'Sexy': 20}")
jenny = Person("{'Handsome': 10, 'Sexy':200}", "{'Handsome': 100, 'Sexy': 200}")
being_awesome = Event("Being Awesome", "YES!", ['Sexy'], "person.traits['Sexy']>10", "person.traits['Sexy'] +=10", 1)
being_handsome = Event("Being Handsome", "YES!", ['Handsome'], "person.traits['Sexy']>10", "person.traits['Handsome'] +=10",1)
world_zombie = World([being_awesome, being_handsome], [jose, jenny])
simulate_event(world_zombie, jenny)
