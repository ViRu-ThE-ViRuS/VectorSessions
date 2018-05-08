# OOP Classes and Objects Solution_Set2 Naman Modani


class Player:

    def __init__ (self):
        age = int()
        movement_speed = int()
        health = int()
        money = int()

        self.age = age
        self.movement_speed = movement_speed
        self.health = health
        self.money = money

    def move(self):
        self.movement_speed += 5

    def stop(self):
        self.movement_speed = 0

    def take_damage(self):
        self.health -= 5

    def heal(self):
        self.health += 5

    def make_money(self):
        self.money += 10000

    def spend_money(self):
        self.money -= 10000

    def __str__ (self):
        print("Age:", self.age)
        print("Speed:", self.movement_speed)
        print("Health is:", self.health)
        print("Money is: $", self.money)

BigPapaPyscho = Player()

BigPapaPyscho.money = 1000000
BigPapaPyscho.health = 100
BigPapaPyscho.movement_speed = 0
BigPapaPyscho.age = 3625

# He's old,why not?

print("Move")
BigPapaPyscho.move()
BigPapaPyscho.__str__()
print("\n")


print("Stop")
BigPapaPyscho.stop()
BigPapaPyscho.__str__()
print("\n")


print("Take Damage")
BigPapaPyscho.take_damage()
BigPapaPyscho.__str__()
print("\n")


print("Heal")
BigPapaPyscho.heal()
BigPapaPyscho.__str__()
print("\n")


print("Make Money")
BigPapaPyscho.make_money()
BigPapaPyscho.__str__()
print("\n")


print("Spend Money")
BigPapaPyscho.spend_money()
BigPapaPyscho.__str__()
print("\n")

#TheEnd.
