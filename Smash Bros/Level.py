from Tile import Tile

red = (255,0,0)
class Level:
    def __init__(self, pSize):
        self.obstacles = []
        self.pSize = pSize

    def getObstacles(self):
        return self.obstacles

    def addObstacle(self, x, y, width, height, type=1):
        self.obstacles.append(Tile(x, y, width, height, self.pSize, type))

    def getTangible(self):
        return self.obstacles

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
