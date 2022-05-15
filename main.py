import numpy as np
import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
t.ht()

print("TEAM MEMBERS: Richard, William, Michael, Andy.")
print("The Möbius strip is a symbol of unity.")
print("After you go around it once, it flips. :D")
print("Can you find the secret message?")
print("Don't press the e or q key no matter what! :D")
print("Use arrow keys or WASD.")

mob = [
  [2, 0, 0, 0, 0],
  [0, 0, 0, 0, 1],
  [0, 0, 1, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 1, 0, 0, 0],
  [1, 0, 0, 0, 0],
  [1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [1, 0, 1, 0, 0], #
  [0, 0, 0, 0, 1],
  [1, 0, 1, 1, 1],
  [1, 0, 1, 0, 0],
  [1, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0], #
  [0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0], # start
  [0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0], # end
  [1, 1, 1, 1, 0], # start2
  [0, 0, 1, 0, 0],
  [0, 0, 1, 1, 0],
  [0, 0, 1, 1, 0],
  [1, 0, 1, 1, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 1, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 1],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0], # end2
  [0, 0, 1, 0, 1],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 1, 1, 1, 1],
  [0, 0, 0, 1, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 0, 0, 0],
  [1, 1, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [1, 1, 0, 0, 0],
  [0, 1, 1, 0, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 1, 0],
  [0, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 0, 0],
  [1, 0, 0, 1, 0],
  [1, 0, 0, 1, 0],
  [1, 0, 0, 1, 0],
  [0, 1, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 1, 0, 1, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 1, 1, 1, 0],
  [0, 1, 0, 1, 0],
]
mob = np.array(mob, int)
mob_len, mob_wid = mob.shape
if(mob_len <= 2*mob_wid):
  raise ValueError("mob_len > 2*mob_wid must be satisfied!")
elif(mob_len <= 4):
  raise ValueError("mob_len > 4 must be satisfied!")
elif(mob_wid <= 1):
  raise ValueError("mon_wid > 1 must be satisfied!")
elif(mob_wid > 20):
  raise ValueError("mob_wid <= 20 must be satisfied!")

grid_size = 200//mob_wid
pos = 0
mob_sect = 0
color_lst = ["silver", "dark gray", "gray", "dim gray", "light slate gray", "slate gray", "light steel blue", "cornflower blue", "royal blue", "blue", "medium blue", "navy", "dark blue", "midnight blue", "light blue", "deep sky blue", "dodger blue", "powder blue", "sky blue", "light sky blue", "steel blue", "cyan", "pale turquoise", "dark turquoise", "turquoise", "medium turquoise", "light sea green", "cadet blue", "dark cyan", "teal", "dark slate gray", "aquamarine", "medium aquamarine", "dark sea green", "medium sea green", "sea green", "pale green", "light green", "medium spring green", "spring green", "lime green", "green", "forest green", "dark green", "lawn green", "lime", "khaki", "yellow", "gold", "goldenrod", "burlywood", "saddle brown", "sandy brown", "orange", "dark orange", "chocolate", "firebrick", "dark red", "maroon", "brown", "coral", "tomato", "orange red", "red", "crimson", "deep pink", "hot pink", "medium violet red", "purple", "dark magenta", "violet", "magenta", "dark orchid", "dark violet", "blue violet", "blue violet", "rebecca purple", "rebecca purple", "rebecca purple", "slate blue", "dark slate blue"]
crazycolors = False;

def mob_update(colors):
  global crazycolors
  t.pu()
  t.goto(130, 0)
  t.pd()
  t.write("Don't press q or e. :D", font = ("Arial", 11, "normal"))
  t.pu()
  t.goto(-0.5*mob_wid*grid_size, -0.5*mob_wid*grid_size)
  t.pd()
  a = 0
  
  s.tracer(0)
  for i in range(mob_wid):
    for j in range(mob_wid):
      t.fillcolor(
        "white" if(colors[a] == 0)
        else (random.choice(color_lst) if crazycolors else "green") if(colors[a] == 1)
        else "black"
      )
      t.begin_fill()
      for k in range(4):
        t.fd(grid_size)
        t.lt(90)
      t.end_fill()
      t.fd(grid_size)
      a += 1
    
    t.bk(mob_wid*grid_size)
    t.lt(90)
    t.fd(grid_size)
    t.rt(90)
  s.update()

def get_colors(pos):
  pos %= 2*mob_len
  if(pos <= mob_len - mob_wid):
    return mob[pos:pos + mob_wid].flatten()
  elif(pos < mob_len):
    return np.concatenate((
      mob[pos:], mob[:, ::-1][:pos - mob_len + mob_wid]
    )).flatten()
  elif(pos <= mob_len + mob_wid):
    return mob[:, ::-1][pos - mob_len:pos - mob_len + mob_wid].flatten()
  else:
    return np.concatenate((
      mob[:, ::-1][pos - mob_len:], mob[:pos - mob_len - mob_wid]
    )).flatten()

def move_lateral(x, y, pos, dir):
  if(pos >= mob_len):
    move_lateral(x, y, pos - mob_len, -dir)
    return
  new_x, new_y = x, y
  if(np.clip(x + dir, 0, mob_wid - 1) != x):
    new_x, new_y = x + dir, y
  if(mob[new_y, new_x] == 0):
    mob[[y, new_y], [x, new_x]] = mob[[new_y, y], [new_x, x]]

def move_vertical(x, y, pos, dir):
  if(pos >= mob_len):
    move_vertical(x, y, pos - mob_len, dir)
    return
  new_x, new_y = x, y
  if((dir == 1 and pos == mob_len - 1) or (dir == -1 and pos == 0)):
    new_x, new_y = mob_wid - x - 1, (y + dir)%mob_len
  else:
    new_x, new_y = x, y + dir
  if(mob[new_y, new_x] == 0):
    mob[[y, new_y], [x, new_x]] = mob[[new_y, y], [new_x, x]]

def move(x, y, key):
  global crazycolors
  if(key in ["Right", "Left", "d", "a"]):
    dir = 1 if(key in ["Right", "d"]) else -1
    move_lateral(x, y, pos, dir)
  elif(key in ["Up", "Down", "w", "s"]):
    dir = 1 if(key in ["Up", "w"]) else -1
    move_vertical(x, y, pos, dir)
  elif(key == "e"):
    print("\a"*600)
  elif (key == "q"):
    crazycolors = not crazycolors

def get_move(x, y, key):
  s.onkeypress(lambda: move(x, y, key), key)

while(True):
  mob_update(get_colors(pos))
  
  y, x = np.array(np.where(mob == 2)).T[0]
  for key in ["Right", "Left", "Up", "Down", "w", "s", "d", "a", "e", "q"]:
    get_move(x, y, key)
  s.listen()
  
  y = np.array(np.where(mob == 2)).T[0][0]
  if(0 <= y <= mob_wid - 1):
    if(mob_len - mob_wid <= pos <= mob_len - 1):
      mob_sect = 1
    elif(2*mob_len - mob_wid <= pos <= 2*mob_len - 1):
      mob_sect = 0
  elif(mob_len - mob_wid <= y <= mob_len - 1):
    if(0 <= pos <= mob_wid - 1):
      mob_sect = 1
    elif(mob_len <= pos <= mob_len + mob_wid - 1):
      mob_sect = 0
  pos = y + mob_sect*mob_len
