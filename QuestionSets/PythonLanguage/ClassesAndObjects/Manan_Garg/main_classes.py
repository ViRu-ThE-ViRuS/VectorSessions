class Player():
    def __init__(self,w,x,y,z):
        self.age = w
        self.movement_speed = x
        self.health = y
        self.money = z

    def move(self,speed):
        if self.health < 0:
            print ("you are dead")
        else:
            self.movement_speed += speed
            print ("moving at " + str(self.movement_speed))
           
    def stop(self):
        if self.health < 0:
            print ("you are dead")
        else: 
            self.movement_speed = 0
            print ("movement speed is 0, you have stopped")

    def take_damage(self,damage):
        self.health -= damage
        if self.health <= 0:
            print ("You are dead")
        else:
            print ("health is " + str(self.health))
            
    def heal(self,hp):
        self.health += hp
        print ("health is " + str(self.health))

    def make_money(self,cash):
        if self.health < 0:
            print ("you are dead")
        else: 
            self.money += cash
            print ("money is " + str(self.money))

    def spend_money(self,cheque):
        if self.health < 0:
            print ("you are dead")
        else: 
            q = self.money - cheque
            if q < 0:
                print ("cant pay")
            else:
                self.money -= cheque
                print ("money is" + str(self.money))
    
    def stats(self):
        if self.health < 0:
            print ("you are dead")
        else: 
            print("age is " + str(self.age))
            print("health is " + str(self.health))
            print("speed is " + str(self.movement_speed))
            print("money is " + str(self.money))

class Enemy():
    def __init__(self,w,x,y,z):
        self.age = w
        self.movement_speed = x
        self.health = y
        self.attack_power = z

    def move(self,speed):
        if self.health < 0:
            print ("you are dead")
        else:
            self.movement_speed += speed
            print ("moving at " + str(self.movement_speed))
           
    def stop(self):
        if self.health < 0:
            print ("you are dead")
        else: 
            self.movement_speed = 0
            print ("movement speed is 0, you have stopped")

    def take_damage(self,damage):
        self.health -= damage
        if self.health <= 0:
            print ("You are dead")
        else:
            print ("health is " + str(self.health))
            
    def heal(self,hp):
        self.health += hp
        print ("health is " + str(self.health))

    def booster(self,ammo):
        if self.health < 0:
            print ("you are dead")
        else: 
            self.attack_power += ammo
            print ("attack power is " + str(self.attack_power))

    def lessen_ammo(self,empty_ammo):
        if self.health < 0:
            print ("you are dead")
        else: 
            q = self.attack_power - empty_ammo
            if q <= 0:
                print ("ammo finished")
                self.attack_power = 0
                print ("ammo gone")
            else:
                self.attack_power -= empty_ammo
                print ("attack power is" + str(self.attack_power)) 
    
    def stats(self):
        if self.health < 0:
            print ("you are dead")
        else: 
            print("age is " + str(self.age))
            print("health is " + str(self.health))
            print("speed is " + str(self.movement_speed))
            print("attack power is " + str(self.attack_power))

    def attack(self,Player):
        if self.health < 0:
            print ("you are dead")
        else:
            Player.take_damage(self.attack_power)
