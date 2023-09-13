import random

print()


class Animals:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_necessities(self):
        print('Time to go to the toilet!')
        self.progress += 15
        self.glqadness += 15


    def to_necessities(self):
        print('Time to eat')
        self.progress += 10
        self.gladness += 5
    def to_run(self):
        print("Time to run!")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Time to walk")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress < 5:
            print('Passed externally')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness = {self.glqadness}')
        print(f'Progress = {round(self.progress, 2)}')

    def live(self, day):
        day = 'Day ' + str(day) + ' of' + self.name + ' life'
        print(f'{day:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_run()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()


snishana = Animals('Snishana')

for day in range(365):
    if not snishana.alive:
        break
    snishana.live(day)


