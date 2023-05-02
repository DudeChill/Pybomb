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
        if(i > 0 and i < height and u > 0 and u < width and i % 2 == 1 and u  % 2 == 1):
            map[i].append("#")
        else:
            map[i].append("_")
        
player = "@"
playerCoords = [0][0]
numBombs = 1
bombRange = 1       
bomb = "!"        

def screen():
    print("")
    for o in range(len(map)):
        print(map[o],flush = True)

map[x][y] = player
screen()

def movePlayer(map,player,direction):
    coords = []
    for j in range(len(map)):
        for k in range(len(map[j])):
            if(map[j][k] == "@"):
                y = j
                x = k
                g = y
                h = x
    if(direction == "right" and map[y][x+1] != "#"): 
        h+=1
    elif(direction == "left" and map[y][x-1] != "#"): 
        h-=1
    elif(direction == "up" and map[y-1][x] != "#"): 
        g-=1
    elif(direction == "down" and map[y+1][x] != "#"):  
        g+=1
    map[y][x], map[g][h] = map[g][h], map[y][x]
    screen()

def on_key_release(key):
    if key == Key.right: 
        movePlayer(map,player,"right")
    elif key == Key.left:
        movePlayer(map,player,"left")
    elif key == Key.up:
        movePlayer(map,player,"up")
    elif key == Key.down:
        movePlayer(map,player,"down")
    elif key == Key.esc:
        exit()
with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
