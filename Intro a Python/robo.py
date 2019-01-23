class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '<%s, %s>' % (self.x, self.y)

class Robot(Point):

    def move_up(self):
        if self.y < 10:
            self.y += 1
        else:
            print('movimento proibido')

    def move_down(self):
        if self.y > 0:
            self.y -= 1
        else:
            print("movimento proibido")

    def move_left(self):
        if self.x > 0:
            self.x -= 1
        else:
            print('movimento proibido')

    def move_right(self):
        if self.x < 10:
            self.x += 1
        else:
            print('movimento proibido')

class Reward(Point):

    def __init__(self, x, y, name):
        Point.__init__(self, x, y)
        self.name = name

    def __repr__(self):
        return '<Reward> %s' % str(self)

def check_reward(robot, rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print('O robo achou a recompensa: %s' % reward.name)
            ok = True
    return ok

import random

r1 = Reward(random.randint(0,10), random.randint(0,10), 'moeda')
r2 = Reward(random.randint(0,10), random.randint(0,10), 'gasolina')
r3 = Reward(random.randint(0,10), random.randint(0,10), 'moeda de ouro')
r4 = Reward(random.randint(0,10), random.randint(0,10), 'martelo do Thor')
r5 = Reward(random.randint(0,10), random.randint(0,10), 'mundial do palmeiras')
r6 = Reward(random.randint(0,10), random.randint(0,10), 'bicampeonato do atl mineiro')
r7 = Reward(random.randint(0,10), random.randint(0,10), 'gol da alemanha')
r8 = Reward(random.randint(0,10), random.randint(0,10), 'martelo do Thor')
r9 = Reward(random.randint(0,10), random.randint(0,10), '3 balas de morango')
r10 = Reward(random.randint(0,10), random.randint(0,10), 'macbook')
rewards = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]

robot = Robot(random.randint(0,10), random.randint(0,10))

for i in range(10):
    movimento = input('Digite up, down, left ou right para o movimento: ')
    if movimento == 'up':
        robot.move_up()
    elif movimento == 'down':
        robot.move_down()
    elif movimento == 'left':
        robot.move_left()
    elif movimento == 'right':
        robot.move_right()
    else:
        print('movimento invalido')
        continue
    print(robot)
    check_reward(robot, rewards)
