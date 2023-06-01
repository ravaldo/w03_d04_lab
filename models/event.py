import datetime as dt

def add_new_event(e):
	events.append(e)
	

class Event:
	def __init__(self, date, name, num_guests, room, desc, recurring=False):
		self.date = dt.datetime.strptime(date, "%d/%m/%Y")
		self.name = name
		self.num_guests = num_guests
		self.room = room
		self.desc = desc
		self.is_recurring = recurring
	
	
	
	def __repr__(self):
		return f"Event: {self.name} with {self.num_guests} guests at {self.room} on {self.date.date()}"


event1 = Event("01/02/2023", "Fringe Festival", 1000, "Edinburgh Room", "laughs")
event2 = Event("10/02/2023", "Comedy Club", 50, "The Stand", "comedy show", True)
event3 = Event("12/02/2023", "Theatre", 500, "The Kings", "drama show")

events = [event1, event2, event3]



	