WIDTH = 15
HEIGHT = 15
TITLE = 'predigame'
background('bg1')

text('predigame : control panel', BLACK, (1, 0.5), size=1)

image('ground4', pos=(0,HEIGHT-3), tag=OBSTACLE)
image('ground6', pos=(WIDTH-1,HEIGHT-3), tag=OBSTACLE)

for x in range(1, WIDTH-1, 1):
   image('ground5', pos=(x, HEIGHT-3), tag=OBSTACLE)

porter = actor('Porter', (10, 0), size=6)
porter.mass(10).rate(2)
porter.act(IDLE_FRONT, -1)

def die(e, p):
   e.kill()

def left():
   e = actor('Zombie-'+str(randint(1,6)), pos=(1,-1), size=4, tag='enemy')
   e.mass(1).rate(4)
   e.speed(1)
   e.attributes['destination'] = 16
   e.collides(porter, die)
   callback(left, randint(5,10))
callback(left, 5)

def emonitor():
   for e in get('enemy'):
      # the enemy is IDLE.. move it!
      if e.action.startswith(IDLE):
         e.move_to((e.attributes['destination'], e.y))
      if e.y >= HEIGHT:
         # the enemy fell into the void.. kill it!
         e.kill()
callback(emonitor, 0.5, FOREVER)

def pmonitor():
    for e in get('enemy'):
        if (porter.x - e.x) < 3:
           porter.act(ATTACK_LEFT, 1)
    if porter.action == IDLE_LEFT:
        porter.act(IDLE_FRONT, FOREVER)
callback(pmonitor, 0.25, FOREVER)

def browsertab(img):
    import webbrowser
    webbrowser.open_new_tab('http://predigame.io')
learn = image('pglearn', (0.5, HEIGHT-1.75), size = 4)
learn.clicked(browsertab)

def opendiag(img):
    import subprocess
    subprocess.Popen(["python", "open_diag.py"])
explore = image('pgexplore', (5.5, HEIGHT-1.75), size = 4)
explore.clicked(opendiag)

def creatediag(img):
    import subprocess
    subprocess.Popen(["python", "create_diag.py"])
pgcreate = image('pgcreate', (10.5, HEIGHT-1.75), size = 4)
pgcreate.clicked(creatediag)
