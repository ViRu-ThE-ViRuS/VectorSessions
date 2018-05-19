from .Player import *


class Enemy:
	def __init__(self):
		self.age = int()
		self.movement_speed = int()
		self.health = int()
		self.attack_power = int()

	def move(self):
		self.movement_speed += 5

	def stop(self):
		self.movement_speed = 0

	def take_damage(self):
		self.health -= 50

	def heal(self):
		self.health = 100

	def booster(self):
		self.attack_power += 50

	def attack(self):
		Jason_Brody.take_damage()

	def __str__(self):
		print("Age:", self.age)
		print("Speed:", self.movement_speed)
		print("Health:", self.health)
		print("Attack Power:", self.attack_power)


Vaas_Montenegro = Enemy()

Vaas_Montenegro.age = 30
Vaas_Montenegro.movement_speed = 0
Vaas_Montenegro.health = 100
Vaas_Montenegro.attack_power = 20

print("Move")
Vaas_Montenegro.move()
Vaas_Montenegro.__str__()
print("--------------")
print("Stop")
Vaas_Montenegro.stop()
Vaas_Montenegro.__str__()
print("--------------")
print("Damage")
Vaas_Montenegro.take_damage()
Vaas_Montenegro.__str__()
print("--------------")
print("Heal")
Vaas_Montenegro.heal()
Vaas_Montenegro.__str__()
print("--------------")
print("Attack")
Vaas_Montenegro.attack()
Vaas_Montenegro.__str__()
print("--------------")
print("Booster")
Vaas_Montenegro.booster()
Vaas_Montenegro.__str__()
print("--------------")
