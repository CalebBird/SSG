#TODO's
#Add a log function for debugging

i = ""

scene = 1

class Player(object):
	
	def __init__(self, name = "", health = 60):
		
		self.name = name
		self.health = health

class Computer(object):
	
	def __init__(self):
		#TODO Log computer init
		
	
	
	def Login(self, password = "34cwrD"):
		
		self.password = password
		i = input("Password:")
		
		if(i = self.password):
			self.commandHandler()
	
		
	def commandHandler():	
		i = input("Please input a command, enter 'Help' for a list of commands")
	
	def help():
		print("Green house")
		print("Inventory")
		print("Oxygen")
		print("Water")
		print("Fuel")
		print("Location")
		print("Move")
		print("Status")
		print("Leave")
		commandHandler()
		

def setup():
	player = Player(i, 60)
	print("Setting up...")
	
	
def openingscene():
	print("You wake up in a dark space ship, inside of a cyrotube, you have zero memories, only your name.")
	i = input("Once you leave the tube, you notice a computer with a stick note. Press 1 to read the sticky note or Press 2 to enter the computer.")	
	if(i == "1")
	
		i = input("the sticky note says '34cwrD'. Press 1 to enter the computer")
		
	
	else:
		
		#TODO
			
	

def main():
	i = input("Welcome to SSG. What is your name?")
	setup()

main()

