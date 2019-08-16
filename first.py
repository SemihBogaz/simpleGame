import random
class Enemy:
    def __init__(self):
        self.health = 100
        self.damage = 40

    def hit(self, player):
        player.health -= self.damage


class Player:
    def __init__(self):
        self.health = 500
        self.damage = 80

    def hit(self, enemy):
        enemy.health -= self.damage


player = Player()
enemies = []

for i in range(12):
    enemies.append(Enemy())

player.hit(enemies[4])

print(enemies[4].health)
