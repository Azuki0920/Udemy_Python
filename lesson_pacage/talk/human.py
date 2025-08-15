from lesson_pacage.tools import utils
"""
以下のような書き方もできるが、これも分かりづらい
from ..tools import utils
"""

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')



