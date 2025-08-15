class Person(object):

    kind = 'human'
    # クラス変数にはなるべくリストを使わない
    # l = []

    def __init__(self):
        self.x = 100

    @classmethod
    def talk(cls):
        print('hello', cls.kind)

    @staticmethod
    def about():
        print('about me')

class Car(object):
    def run(self):
        print('run')

class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

class Word(object):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

person_car = PersonCarRobot()
person_car.talk()
person_car.fly()
person_car.run()

a = Person
a.talk()
a.about()

w = Word('test')
w2 = Word('test')

print(w == w2)