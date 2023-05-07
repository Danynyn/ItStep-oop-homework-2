import random
x = int(input(print('Take your class Botan(1) Zybrila(2) Norm(3) NeNaLesson(4) Krytih(5)')))
if x == 1 :
    y = int(input(print('Take your complexity SonOleharha(1) Easy(2) Normal(3) Hard(4) SvillageVcity(5)')))
    if y == 1 :
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 50
                self.progress = 0
                self.bylling = 0
                self.money = 1000000
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 1
                self.happiness -= 0
                self.money -= 100
                self.money += 5

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 2

            def to_chill(self):
                print('Chill time!')
                self.happiness += 4
                self.progress -= 0
                self.money -= 1000

            def byling(self):
                print("You son oliharha")
                self.bylling += 0.1


            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.bylling == 100:
                    b = random.randint(1,2)
                    if b == 1 :
                        print('syicid')
                        self.active = False
                    elif b == 1 :
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 20:
                    self.to_study()
                elif d100 < 60:
                    self.to_sleep()
                elif d100  < 99:
                    self.to_chill()
                elif d100 <  100:
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 2:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 50
                self.progress = 0
                self.bylling = 0
                self.money = 1000
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.4
                self.happiness -= 0.5
                self.money += 5

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 2

            def to_chill(self):
                print('Chill time!')
                self.happiness += 4
                self.progress -= 0
                self.money -= 10

            def byling(self):
                print("Botan")
                self.bylling += 3

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 60:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 90:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 3:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 50
                self.progress = 0
                self.bylling = 0
                self.money = 500
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.2
                self.happiness -= 1
                self.money += 4

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 2

            def to_chill(self):
                print('Chill time!')
                self.happiness += 4
                self.progress -= 0.1
                self.money -= 15

            def byling(self):
                print("Botan")
                self.bylling += 4

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 60:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 90:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 4:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 50
                self.progress = 0
                self.bylling = 0
                self.money = 250
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.15
                self.happiness -= 2
                self.money += 3

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 1.8

            def to_chill(self):
                print('Chill time!')
                self.happiness += 3
                self.progress -= 0.13
                self.money -= 20

            def byling(self):
                print("Botan")
                self.bylling += 6

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 60:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 90:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 5:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 50
                self.progress = 0
                self.bylling = 0
                self.money = 100
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.13
                self.happiness -= 2.5
                self.money += 2.5

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 1.4

            def to_chill(self):
                print('Chill time!')
                self.happiness += 2.5
                self.progress -= 0.15
                self.money -= 25

            def byling(self):
                print("Selanin")
                self.bylling += 8

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 60:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 90:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
if x == 2 :
    y = int(input(print('Take your complexity SonOleharha(1) Easy(2) Normal(3) Hard(4) SvillageVcity(5)')))
    if y == 1 :
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 25
                self.progress = 0
                self.bylling = 0
                self.money = 1000000
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 1.2
                self.happiness -= 0
                self.money -= 100
                self.money += 5

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 2

            def to_chill(self):
                print('Chill time!')
                self.happiness += 2
                self.progress -= 0
                self.money -= 1000

            def byling(self):
                print("You son oliharha")
                self.bylling += 0.2


            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.bylling == 100:
                    b = random.randint(1,2)
                    if b == 1 :
                        print('syicid')
                        self.active = False
                    elif b == 1 :
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 30:
                    self.to_study()
                elif d100 < 60:
                    self.to_sleep()
                elif d100  < 99:
                    self.to_chill()
                elif d100 <  100:
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 2:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 25
                self.progress = 0
                self.bylling = 0
                self.money = 1000
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.6
                self.happiness -= 0.3
                self.money += 7

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 3

            def to_chill(self):
                print('Chill time!')
                self.happiness += 1.5
                self.progress -= 0.05
                self.money -= 10

            def byling(self):
                print("Zybrila")
                self.bylling += 5

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 70:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 85:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 3:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 25
                self.progress = 0
                self.bylling = 0
                self.money = 500
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.4
                self.happiness -= 0.5
                self.money += 5

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 2

            def to_chill(self):
                print('Chill time!')
                self.happiness += 1
                self.progress -= 0.13
                self.money -= 15

            def byling(self):
                print("Zybrila")
                self.bylling += 6

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 70:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 85:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 4:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 25
                self.progress = 0
                self.bylling = 0
                self.money = 250
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.24
                self.happiness -= 1
                self.money += 4

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 2

            def to_chill(self):
                print('Chill time!')
                self.happiness += 0
                self.progress -= 0.19
                self.money -= 20

            def byling(self):
                print("Zybrila")
                self.bylling += 9

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 70:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 85:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 5:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 25
                self.progress = 0
                self.bylling = 0
                self.money = 100
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.18
                self.happiness -= 2
                self.money += 3

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 1.6

            def to_chill(self):
                print('Chill time!')
                self.happiness -= 0.5
                self.progress -= 0.15
                self.money -= 25

            def byling(self):
                print("Selanin")
                self.bylling += 12

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 70:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 85:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
if x == 3 :
    y = int(input(print('Take your complexity SonOleharha(1) Easy(2) Normal(3) Hard(4) SvillageVcity(5)')))
    if y == 1 :
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 75
                self.progress = 0
                self.bylling = 0
                self.money = 1000000
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 1
                self.happiness -= 0
                self.money -= 100
                self.money += 5

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 2

            def to_chill(self):
                print('Chill time!')
                self.happiness += 5
                self.progress -= 0
                self.money -= 1000

            def byling(self):
                print("You son oliharha")
                self.bylling += 0.1


            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.bylling == 100:
                    b = random.randint(1,2)
                    if b == 1 :
                        print('syicid')
                        self.active = False
                    elif b == 1 :
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 10:
                    self.to_study()
                elif d100 < 50:
                    self.to_sleep()
                elif d100  < 99:
                    self.to_chill()
                elif d100 <  100:
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 2:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 75
                self.progress = 0
                self.bylling = 0
                self.money = 1000
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.3
                self.happiness -= 1
                self.money += 3

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 3

            def to_chill(self):
                print('Chill time!')
                self.happiness += 6
                self.progress -= 0.1
                self.money -= 10

            def byling(self):
                print("Noob")
                self.bylling += 1

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 40:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 95:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 3:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 75
                self.progress = 0
                self.bylling = 0
                self.money = 500
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.19
                self.happiness -= 3
                self.money += 2

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 2

            def to_chill(self):
                print('Chill time!')
                self.happiness += 4
                self.progress -= 0.19
                self.money -= 15

            def byling(self):
                print("Noob")
                self.bylling += 3

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 40:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 95:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 4:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 75
                self.progress = 0
                self.bylling = 0
                self.money = 250
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.12
                self.happiness -= 5
                self.money += 1

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 4

            def to_chill(self):
                print('Chill time!')
                self.happiness += 3
                self.progress -= 0.22
                self.money -= 20

            def byling(self):
                print("Noob")
                self.bylling += 3

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 40:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 95:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 5:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 75
                self.progress = 0
                self.bylling = 0
                self.money = 100
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.18
                self.happiness -= 2
                self.money += 1

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 2

            def to_chill(self):
                print('Chill time!')
                self.happiness += 2
                self.progress -= 0.23
                self.money -= 25

            def byling(self):
                print("Selanin")
                self.bylling += 12

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 40:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 95:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
if x == 4 :
    y = int(input(print('Take your complexity SonOleharha(1) Easy(2) Normal(3) Hard(4) SvillageVcity(5)')))
    if y == 1 :
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 100
                self.progress = 0
                self.bylling = 0
                self.money = 1000000
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 1
                self.happiness -= 0
                self.money -= 100
                self.money += 2

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 10

            def to_chill(self):
                print('Chill time!')
                self.happiness += 2
                self.progress -= 0
                self.money -= 1000

            def byling(self):
                print("You son oliharha")
                self.bylling += 0.1


            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.bylling == 100:
                    b = random.randint(1,2)
                    if b == 1 :
                        print('syicid')
                        self.active = False
                    elif b == 1 :
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 10:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100  < 99:
                    self.to_chill()
                elif d100 <  100:
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 2:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 100
                self.progress = 0
                self.bylling = 0
                self.money = 1000
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.2
                self.happiness -= 3
                self.money += 0

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 11

            def to_chill(self):
                print('Chill time!')
                self.happiness += 2
                self.progress -= 0.1
                self.money -= 10

            def byling(self):
                print("Bruh")
                self.bylling += 3

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 10:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 95:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 3:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 100
                self.progress = 0
                self.bylling = 0
                self.money = 500
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.11
                self.happiness -= 6
                self.money -= 1

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 13

            def to_chill(self):
                print('Chill time!')
                self.happiness -= 1
                self.progress -= 0.2
                self.money -= 15

            def byling(self):
                print("Bruh")
                self.bylling += 5

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 10:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 95:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 4:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 100
                self.progress = 0
                self.bylling = 0
                self.money = 250
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.13
                self.happiness -= 8
                self.money -= 3

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 14

            def to_chill(self):
                print('Chill time!')
                self.happiness -= 3
                self.progress -= 0.22
                self.money -= 20

            def byling(self):
                print("Bruh")
                self.bylling += 8

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 10:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 95:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 5:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 100
                self.progress = 0
                self.bylling = 0
                self.money = 100
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.09
                self.happiness -= 8
                self.money -= 5

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 16

            def to_chill(self):
                print('Chill time!')
                self.happiness -= 4
                self.progress -= 0.25
                self.money -= 25

            def byling(self):
                print("Selanin")
                self.bylling += 15

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 10:
                    self.to_study()
                elif d100 < 80:
                    self.to_sleep()
                elif d100 < 95:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')

if x == 5 :
    y = int(input(print('Take your complexity SonOleharha(1) Easy(2) Normal(3) Hard(4) SvillageVcity(5)')))
    if y == 1 :
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 110
                self.progress = 0
                self.bylling = 0
                self.money = 1000000
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 1
                self.happiness -= 0
                self.money -= 100
                self.money += 0

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 2

            def to_chill(self):
                print('Chill time!')
                self.happiness += 11
                self.progress -= 0
                self.money -= 500

            def byling(self):
                print("You son oliharha")
                self.bylling += 0.1


            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.bylling == 100:
                    b = random.randint(1,2)
                    if b == 1 :
                        print('syicid')
                        self.active = False
                    elif b == 1 :
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 10:
                    self.to_study()
                elif d100 < 30:
                    self.to_sleep()
                elif d100  < 99:
                    self.to_chill()
                elif d100 <  100:
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 2:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 110
                self.progress = 0
                self.bylling = 0
                self.money = 1000
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.1
                self.happiness -= 5
                self.money += 1

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 3

            def to_chill(self):
                print('Chill time!')
                self.happiness += 20
                self.progress -= 0.16
                self.money -= 5

            def byling(self):
                print("You shit")
                self.bylling += 1

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 20:
                    self.to_study()
                elif d100 < 40:
                    self.to_sleep()
                elif d100 < 97:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 3:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 110
                self.progress = 0
                self.bylling = 0
                self.money = 500
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.12
                self.happiness -= 3
                self.money += 0

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 2

            def to_chill(self):
                print('Chill time!')
                self.happiness += 20
                self.progress -= 0.21
                self.money -= 7.5

            def byling(self):
                print("You shit")
                self.bylling += 2

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 20:
                    self.to_study()
                elif d100 < 40:
                    self.to_sleep()
                elif d100 < 97:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 4:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 110
                self.progress = 0
                self.bylling = 0
                self.money = 250
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.1
                self.happiness -= 10
                self.money -= 1

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 4

            def to_chill(self):
                print('Chill time!')
                self.happiness += 27
                self.progress -= 0.22
                self.money -= 10

            def byling(self):
                print("You shit")
                self.bylling += 3

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 20:
                    self.to_study()
                elif d100 < 40:
                    self.to_sleep()
                elif d100 < 97:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')
    elif y == 5:
        class Student:
            def __init__(self, name):
                self.name = name
                self.happiness = 110
                self.progress = 0
                self.bylling = 0
                self.money = 300
                self.active = True

            def to_study(self):
                print('zachet!')
                self.progress += 0.08
                self.happiness -= 12
                self.money -= 3

            def to_sleep(self):
                print('ZZZZZZ!')
                self.happiness += 2

            def to_chill(self):
                print('Chill time!')
                self.happiness += 31
                self.progress -= 0.25
                self.money -= 10

            def byling(self):
                print("Selanin")
                self.bylling += 12

            def is_active(self):
                if self.progress < -0.5:
                    print('Vidrahuvaly((((')
                    self.active = False
                elif self.happiness <= 0:
                    print('Depression!')
                    self.active = False
                elif self.progress > 5:
                    print('Passes externally...')
                    self.active = False
                elif self.money <= 0 :
                    print('Bomg')
                    self.active = False
                elif self.byling == 100:
                    b = random.randint(1, 2)
                    if b == 1:
                        print('syicid')
                        self.active = False
                    elif b == 1:
                        print('Strelanina')
                        self.active = False

            def status(self):
                print(f'Happiness: {self.happiness}')
                print(f'Progress: {round(self.progress, 2)}')
                print(f'Byling: {round(self.bylling, 2)}')
                print(f'Money: {round(self.money, 2)}')

            def live_a_day(self, day):
                day_str = f'Day {day} of {self.name} life'
                print(f"{day_str:=^50}")
                d100 = random.randint(1, 100)
                if d100 < 20:
                    self.to_study()
                elif d100 < 40:
                    self.to_sleep()
                elif d100 < 93:
                    self.to_chill()
                elif d100 < 100 :
                    self.byling()
                self.status()
                self.is_active()


        ivan = Student(name='Ivan')

for day in range(365):
    if ivan.active:
        ivan.live_a_day(day)
    else:
        break