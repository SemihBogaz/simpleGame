class Characters:
    def __init__(self, hp, dp):
        self.Health = hp
        self.Damage = dp

    def hit(self, rival):
        rival.Health -= self.Damage


x = Characters(70, 40)
y = Characters(100, 50)

print("First situation: ", x.Health)

y.hit(x)

print("Second situation: ", x.Health)
