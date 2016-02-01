def utility(event, person):
    '''
    Returns the utility of the event
    #It works#
    '''
    trait_value = person.trait_value
    utils = 0

    for trait in event.traits:
        utils += trait_value[trait]

    return utils/len(event.traits)

def simulate_event(world, person):
    '''
    Takes a world and a person in that world.
    Takes the person through all the events
    and makes the event with the highest utility occur
    '''
    highest_util=0
    event_occuring = None
    
    for event in world.events:
        #print("Checking", event.name)
        if event.will_happen(person):
            priority_number = utility(event, person)
            #print(person.name," is considering ", event.name)
            if priority_number > highest_util:
                highest_util = priority_number
                event_occuring = event
    if event_occuring != None:
        print(person.name, "is ", event_occuring.name)
        print(person.name, " says: ", event_occuring.description)
        event_occuring.do(person)
    else:
        print(person.name, "wants to be lazy for this turn")
        
def sim_world(world):
    '''
    Simulates one trun in the world

    '''
    for person in world.agents:
        #print("Simulating ", person.name)
        if person.alive:
            if not person.is_busy():
                #print(person.name, " is being lazy")
                simulate_event(world, person)
            else:
                print(person.name, "is busy for this turn")
        else:
            print(person.name, "is dead RIP :(")
        person.busy = max(0, person.busy-1)
