import main_classes as mc

Link = mc.Player(20,30,40,50)
Link.name = "Link"
Link.move(30)
Link.stop()
Link.take_damage(50)
Link.heal(50)
Link.spend_money(60)
Link.make_money(100)
Link.stats()

Ganon = mc.Enemy(20,30,40,50)
Ganon.name = "Ganon"
Ganon.move(30)
Ganon.stop()
Ganon.take_damage(50)
Ganon.heal(50)
Ganon.booster(60)
Ganon.lessen_ammo(100)
Ganon.stats()
Ganon.attack(Link)
        
