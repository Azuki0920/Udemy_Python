# import 文の呼び出し方法
import lesson_pacage.tools.utils

r = lesson_pacage.tools.utils.say_twice('hello')
print(r)

# この書き方が一番好み
from lesson_pacage.tools import utils

r = utils.say_twice('hello')
print(r)

# どこから呼ばれたかが分かりづらいため、あまり使われないが関数だけimportもできる
from lesson_pacage.tools.utils import say_twice

r = say_twice('hello')
print(r)

from lesson_pacage.talk import human
print(
    human.sing(),
    human.cry()
)

# import * も出来るが、何が呼ばれてるか分かりづらいので、非推奨
from lesson_pacage.talk import *
print(
    animal.sing(),
    animal.cry()
)

s = "foenszhlfcnsgksdlfhsla;sdmfk"

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)

from termcolor import colored

print(colored('test', 'green'))

"""
◆import順は以下の順とし、分かれ目には改行を入れる。
# 標準ライブラリ
# サードパーティライブラリ
# 自分たちが作ったパッケージ
# ローカルパッケージ
"""

print(__name__)

def main():
    r = lesson_pacage.talk.animal.sing()
    print(r)

if __name__ == '__main__':
    main()

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Person init called', self.name)

    def say_something(self):
        print('hello, my name is {}'.format(self.name))
        self.run(2)

    def run(self, num):
        print('run' * num)

    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')

    def __del__(self):
         print('good bye')

person = Person(name='ali', age=18)
person.say_something()

class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(name=None, age=age)
        else:
            raise ValueError

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(name=None, age=age)
        else:
            raise ValueError

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, person):
        person.drive()

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enabled):
        if self.passwd == '456':
            self._enable_auto_run = is_enabled
        else:
            raise ValueError

    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto_run')

toyota = ToyotaCar('Lexus')
print(toyota.model)
toyota.run()

tesla = TeslaCar(passwd='456')
tesla.enable_auto_run = True
print(tesla.model)
tesla.run()
tesla.auto_run()

baby = Baby()
adult = Adult()
car = Car()
# car.ride(baby)
car.ride(adult)