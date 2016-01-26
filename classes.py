class World(object):


	def __init__(self, events_csv, agents_csv):
	    self.events = 0
	    self.agents  = 0
	    self.intialize_events(events_csv)
	    self.intialize_agents(agents_csv)
	    
	def intialize_agents(self,agents_csv):
	   	self.agents = agents_csv
	def intialize_events(self,events_csv):
	   	self.events = events_csv        




class Person(object):
	'''
	Creates a person with two dictionaries for the traits and amount and traits and values
	Dictionaries are strings
	'''
	def __init__(self, traits, trait_value, name):
            self.name = name
	    self.trait_value = eval(trait_value)
	    self.traits = eval(traits)
	    self.busy = 0

	def is_busy():
            if self.busy != 0:
                return False
            return True

class Event(object):
	'''
	Creates event

	Input:
		Name= strings
		Description = strings
		List of traits = string of list of all the traits
		Condition/activity: to access trait use person.traits["Name of the Trait"]

	'''

	def __init__(self, name, description, list_of_traits,condition, activity):
		self.name = name
		self.description = description
		self.traits=list_of_traits
		self.condition = condition
		self.activity = activity

	def will_happen(self,person):
		if eval(self.condition):
		    return True
		return False

	def do(self,person):
		exec(self.activity)
