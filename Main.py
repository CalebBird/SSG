i = ""

class Player(object):
	
	def __init__(self, name = "", health = 60):
		
		self.name = name
		self.health = health


def setup():
	player = Player(i, 60)
	print("Setting up...")
	
def main():
	i = input("Welcome to SSG. What is your name?")
	setup()

main()