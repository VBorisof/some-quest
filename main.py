from world import World
from scenario import Scenario

world = World(Scenario("res/scenario.json"))
while world.is_running:
	world.run()
