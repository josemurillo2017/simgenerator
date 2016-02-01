class World(object):

	def __init__(self, events, agents):
		self.name = "New World"
		self.events = events
		self.agents = agents 

	def __repr__(self):
		return self.name

class Person(object):
	'''
	Creates a person with two dictionaries for the traits and amount and traits and values
	Dictionaries are strings
	'''
	def __init__(self, traits, trait_value, name):
		self.name = name
		self.trait_value = eval(trait_value)
		self.traits = eval(traits)

		#Human Qualities
		self.alive = True
		self.busy = 0
		self.tension = False

		#Groups
		self.friends = []
		self.enemy =[]
		self.stranger =[]
		self.person = None
		self.group = False

	def is_busy(self):
		if self.busy != 0:
			return True
		return False

	def meet_person(self, person):
		self.person = person

	def create_group(self):
		self.group = True

	def survive_encounter(self, danger=50):
		import random
		if random.randint(0,100) < danger:
			self.alive = False
			print("You're dead, mate")
			return False
		self.tension = False
		print("That zombie was no match for you")
		return True

	def __repr__(self):
		return self.name

class Event(object):
	'''
	Creates event

	Input:
		Name= strings
		Description = strings
		List of traits = string of list of all the traits
		Condition/activity: to access trait use person.traits["Name of the Trait"]

	'''
	def __init__(self, name, desc, trait_list, det_cond, det_amount, prob_cond, act, time):
		self.name = name
		self.description = desc
		self.traits=eval(trait_list)
		self.det_cond = det_cond
		self.prob_cond = prob_cond
		self.activity = act
		self.time = int(time)
		self.det_amount = det_amount
	
	def will_happen(self,person):
		if eval(self.det_cond):
			import random
			rand_out = random.randint(0,100)
			#print(self.name, "needs to reach ", rand_out, " in order to succeed.")
			rand_prob = (100- int(self.det_amount))*random.randint(0,100)/100
			#print("The random factor is ", rand_prob)
			det_prob = int(self.det_amount)* (min(int(eval(self.prob_cond))/(5*len(self.traits)),1))
			if det_prob <0:
				det_prob = 0
			#print("and the other value is", det_prob)
			if (det_prob + rand_prob > rand_out):
				return True
			return False

	def do(self,person):
		exec(self.activity)
		person.busy += self.time
	
	def __repr__(self):
		return self.name


