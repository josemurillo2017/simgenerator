#All fun and games. Nothing serious happening here. Just messing around to see if the various functions work

import classes
import simulation_functions
import create

people = create.create_people("people.csv")
events = create.create_events("events.csv")
new_world = classes.World( events[0:3], people)
round_turn = 0

def go(steps, round_turn = round_turn):
    for i in range(0,steps):
        round_turn += 1
        print("Round", round_turn)
        print()
        simulation_functions.sim_world(new_world)
        print()
        print()