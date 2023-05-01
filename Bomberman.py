from pynput import keyboard
from pynput.keyboard import Key

width = 13
height = 11
map = []
x = 0
y = 0
for i in range(height):
    map.append([])
    for u in range(width):
        if(i > 0 and i < height and u > 0 and u < width and i % 2 == 0 and u  % 2 == 0):
            map[i].append("#")
        else:
            map[i].append("_")
        
player = "@"
playerCoords = [0][0]
numBombs = 1        
bomb = "!"        

def screen():
    print("")
    for o in range(len(map)):
        print(map[o])

map[x][y] = player
screen()

def right():
    x+=1
    map[x][y] = player
    screen()

def on_key_release(key):
    if key == Key.right: 
        right()
    elif key == Key.left:
        print("Left key clicked")
    elif key == Key.up:
        print("Up key clicked")
    elif key == Key.down:
        print("Down key clicked")
    elif key == Key.esc:
        exit()
with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()