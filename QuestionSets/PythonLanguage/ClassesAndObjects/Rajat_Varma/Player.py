class Player:
	def __init__(self):
		self.age = int()
		self.movement_speed = int()
		self.health = int()
		self.money = int()

	def move(self):
		self.movement_speed += 10

	def stop(self):
		self.movement_speed = 0

	def take_damage(self):
		self.health -= 10

	def heal(self):
		self.health = 100

	def make_money(self):
		self.money += 1000

	def spend_money(self):
		self.money -= 1000

	def __str__(self):
		print("Age:", self.age)
		print("Speed:", self.movement_speed)
		print("Health:", self.health)
		print("Money:", self.money)


Jason_Brody = Player()

Jason_Brody.money = 100
Jason_Brody.health = 100
Jason_Brody.movement_speed = 0
Jason_Brody.age = 25

print("Move")
Jason_Brody.move()
Jason_Brody.__str__()
print("--------------")
print("Stop")
Jason_Brody.stop()
Jason_Brody.__str__()
print("--------------")
print("Damage")
Jason_Brody.take_damage()
Jason_Brody.__str__()
print("--------------")
print("Heal")
Jason_Brody.heal()
Jason_Brody.__str__()
print("--------------")
print("Make Money")
Jason_Brody.make_money()
Jason_Brody.__str__()
print("--------------")
print("Spend Money")
Jason_Brody.spend_money()
Jason_Brody.__str__()
print("--------------")
