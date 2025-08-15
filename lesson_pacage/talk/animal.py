from lesson_pacage.tools import utils
"""
以下のような書き方もできるが、これも分かりづらい
from ..tools import utils
"""

def sing():
    return 'にゃあ'

def cry():
    return utils.say_twice('わん')

if __name__ == '__main__':
    print(sing())
    print('animal:', __name__)

