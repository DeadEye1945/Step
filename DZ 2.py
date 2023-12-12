import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 250

    def to_study(self):
        print('Час для навчання')
        self.progress += 10
        self.gladness -= 5

    def to_work(self):
        print('Час для роботи')
        self.money += 10
        self.gladness -= 10

    def to_sleep(self):
      print ('Це час для сну')
      self.gladness += 5

    def to_chill(self):
      print ('Це час для відпочинку')
      self.progress -= 5
      self.gladness += 15
      self.money -= 20

    def is_alive(self):
        if self.progress < -15:
          print('Йди розвивайся')
          self.alive = False
        elif self.gladness <=0:
          print('Упс в тебе депресія')
          self.alive = False
        elif self.progress > 5:
          print('Ти молодець')
          self.alive = True
        elif self.money == 0:
          print('Ти бомж')
          self.alive = False

    def end_of_the_day(self):
          print(f"щастя - {self.gladness}")
          print(f"{round(self.progress,2)}")
          print(f"гроші - {self.money}")

    def live(self, day):
       day = 'Day' + str(day) + 'of' + self.name + 'life'
       print (f"{day:^50}")
       kubik = random.randint(1, 4)
       if kubik == 1:
          self.to_study()
       elif kubik == 2:
          self.to_sleep()
       elif kubik == 3:
          self.to_chill()
       elif kubik == 4:
          self.to_work()
       self.end_of_the_day()
       self.is_alive()

nick = Student(name='Ivan')
for day in range(366):
    if nick.alive == False:
        break
    nick.live(day)
