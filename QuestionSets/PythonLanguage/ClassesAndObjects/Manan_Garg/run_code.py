import main_classes as mc

Modi = mc.Player(20,30,40,50)
Modi.move(30)
Modi.stop()
Modi.take_damage(50)
Modi.heal(50)
Modi.spend_money(60)
Modi.make_money(100)
Modi.stats()

Rahul = mc.Enemy(20,30,40,50)
Rahul.move(30)
Rahul.stop()
Rahul.take_damage(50)
Rahul.heal(50)
Rahul.booster(60)
Rahul.lessen_ammo(100)
Rahul.stats()
Rahul.attack(Modi)
        
