from settings import *
from map import *
from player import *



def display():
    screen.fill("#ecf0f1")
    map.display()
    player.display()