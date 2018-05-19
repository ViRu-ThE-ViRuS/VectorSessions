class Player:
	age, speed, health, money = 10, 0, 100, 100

	def __init__(self, age=10, speed=0, health=100, money=1000) -> None:
		self.age, self.speed, self.health, self.money = age, speed, health, money

	def __str__(self):
		return " ".join([
			"Player is currently %s year(s) old." % self.age,
			"He and / or she is moving with a speed of %s," % self.speed,
			"has %s health," % self.health,
			"and %s money." % self.money
		])

	def move(self):
		self.speed += 5
		print("Speed increased by 5! Current speed is %s." % self.speed)

	def stop(self):
		self.speed = 0
		print("Speed reset to %s!" % self.speed)

	def take_damage(self, damage):
		self.health = max(self.health - damage, 0)
		print(
			"Took %s damage! Current health is %s." % (damage, self.health) if self.health != 0
			else "Took %s damage and *ded" % damage
		)

	def heal(self):
		self.health = 100
		print("Health reset to %s." % self.health)

	def make_money(self, money):
		self.money += money
		print("Made %s bling! Currently have %s." % (money, self.money))

	def spend_money(self, money):
		self.money -= money
		print(
			"Spent %s money! Currently have %s." % (money, self.money) if self.money != 0
			else "Spent %s money! Currently %s in debts :(." % (money, -self.money)
		)


def main():
	p = Player()
	p.move()
	p.stop()
	p.take_damage(1000)
	p.heal()
	p.make_money(1000)
	p.spend_money(3000)
	p.make_money(2000)
	print(p)


if __name__ == '__main__':
	main()
