def utility(event, person):
    '''
    Returns the utility of the event
    #It works#
    '''
    trait_value = person.trait_value
    utils = 0

    for trait in event.traits:
        utils += trait_value[trait]

    return utils

def simulate_event(world, person):
    '''
    Takes a world and a person in that world.
    Takes the person through all the events
    and makes the event with the highest utility occur
    '''
    highest_util=0
    event_occuring = None
    
    for event in world.events:
        if event.will_happen(person):
        	priority_number = utility(event, person)
        	print(event.name, " has ", priority_number)
        	if priority_number > highest_util:
        		highest_util = priority_number
        		event_occuring= event
    if event_occuring != None:
        print(event_occuring.name)
        event_occuring.do(person)
        
def sim_world(world):
    '''
    Simulates one trun in the world

    '''
    for person in world.agents:
        if not person.is_busy():
            simulate_event(world, person)
        person.busy = max(0, person.busy-1)
