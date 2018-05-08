# Make a class `Player`

#### It should have the following data members:
- `age`
- `movement_speed`
- `health`
- `money`

#### It should have the following features/functionality:
- `move` (to update movement speed by 5 units)
- `stop` (to reset movement speed)
- `take_damage` (to reduce health)
- `heal` (to reset health)
- `make_money` (to make dat doh!)
- `spend_money` (to blow that shit away!)
- `__str__` (to print everything)

**Make an object and call the various functions. They should all print something when called.**

# Make a class `Enemy`

#### It should have the following data members:
- `age`
- `movement_speed`
- `health`
- `attack_power`

#### It should have the following features/functionality:
- `move` (to update movement speed by 5 units)
- `stop` (to reset movement speed)
- `take_damage` (to reduce health)
- `heal` (to reset health)
- `booster` (to increase attack power)
- `attacc` (which takes an object of player and calls its `take_damage` method)
- `__init__` (to initialize all data members to some sensible value)
- `__str__` (to print everything)

**Make an object and call the various functions. They should all pring something when called.**