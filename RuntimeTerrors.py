import turtle
import math
import random
win = turtle.Screen()
win.title("Space Invaderz")

#background
win.bgpic("GalaxyBackground.gif")
win.bgcolor("black")

#register the shapes
#us
win.register_shape("BlackHatHackerEnemy.gif") #test commit
win.register_shape("ComputerSpaceship.gif")
win.register_shape("BinaryBullet.gif")
win.register_shape("invadershipinverted.gif")
#Title Sequence
begin_pen = turtle.Turtle() #us
begin_pen.hideturtle()
def beginGame():
 begin_pen.color("#FFFFFF")
 begin_pen.penup()
 begin_pen.setposition(0,200)
 begin = '''Welcome to Space Invaders!'''
 begin_pen.write(begin, False, align= "Center", font =("Times New Roman", 30, "normal")) #changed font
beginGame()
warning_pen = turtle.Turtle() #us
warning_pen.hideturtle()
def Warning():
 warning_pen.color("#d1231d")
 warning_pen.penup()
 warning_pen.setposition(0,0)
 warning = "WARNING"
 for i in range(5):
 	warning_pen.speed(3)
 	warning_pen.write(warning, False, align = "Center", font = ("Arial", 35, "bold")) #changed font

 warning_pen.clear()

#border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
 border_pen.fd(600)
 border_pen.lt(90)
border_pen.hideturtle()

#create player
player = turtle.Turtle()
player.shape("ComputerSpaceship.gif")
player.penup()
player.speed(15)
player.setposition(0,-250)
player.setheading(90)
begin_pen.clear()

#player bullet
bullet = turtle.Turtle()
bullet.shape("BinaryBullet.gif")
bullet.pensize(7)
bullet.penup()
bullet.speed(60)
bullet.setheading(90)
bullet.shapesize(.5,.5)
bullet.hideturtle()

#Score Board
score = 0
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("green")
score_pen.penup()
score_pen.setposition(-290,270)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "Left", font = ("Times New Roman", 16, "normal"))
score_pen.hideturtle()
bulletspeed = 22

#ready to fire bullet
#fired bullet = moving
bulletstate = "ready"
#move player
playerspeed = 15
def MoveLeft():
 	x = player.xcor()
 	x -= playerspeed
 	if x < -280:
 		x = -280
 	player.setx(x)

def MoveRight():
 	x = player.xcor()
 	x += playerspeed
 	if x > 280:
 		x = 280
 	player.setx(x)

def FireBullet():
 global bulletstate #any change to the bullet is changed in the global state as well
 if bulletstate == "ready":
 	bulletstate == "fire"
 	#move coordinate to above the player
 	x = player.xcor()
 	y = player.ycor() +10 #so bullet is at the top of the ship (tip of triangle)
 	bullet.setposition(x,y)
 	bullet.showturtle()

def isCollision(t1, t2):
 	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
 	if distance < 38:
 		return True
 	else:
 		return False

def noCollision(t1,t2): #us
	if t2.ycor() < -250:
		return True
	else:
 		return False
#keyboard binding
#we translated this
win.listen()
win.onkey(MoveLeft, "Left")
win.onkey(MoveRight, "Right")
win.onkey(FireBullet,"space") #space = spacebar

#choose a number of enemies
NumberOfEnemies = 7
Enemies = []
for i in range(NumberOfEnemies):
	Enemies.append(turtle.Turtle())

for enemy in Enemies:
	enemy.shape("BlackHatHackerEnemy.gif")
	enemy.penup()
	enemy.speed(10)
	x = random.randint(-200,200)
	y = random.randint(100,250) #test
	enemy.setposition(x,y)


#us down
enemy2 = turtle.Turtle() #commit
def Enemy2():#us down
	def Enemy2():#us down
 		enemy2.shape("invadershipinverted.gif")
 		enemy2.penup()


enemy2 = enemy
enemyspeed = 10
while True:
 for enemy in Enemies:
 	#Move the enemy
 	x = enemy.xcor()
 	x += enemyspeed
 	enemy.setx(x)


 #move enemy back and down
 if enemy.xcor() >= 280:
 	#nested loop that moves all enemies down
 	for e in Enemies:
	 	y = e.ycor()
 		y -= 60
 		e.sety(y)
 		#change enemy direction
 		enemyspeed *=-1
 elif enemy.xcor() <= -280:
 	#nested loop that moves all enemies down
 	for e in Enemies:
 		y = e.ycor()
 		y -= 60
 		e.sety(y)
 		#change enemy direction
 		enemyspeed *= -1

 #move the bullet along with movement of ship
 y = bullet.ycor()
 y += bulletspeed
 bullet.sety(y)
 #if bullet goes to top... the FireBullet function won't fire anymore bullets...
 #thus, must check if bullet has gone to top
 if bullet.ycor() >275:
 	bullet.hideturtle()
 	bulletstate == "ready" #this allows us to fire the bullet again
 #check for collision between bullet and enemy
 if isCollision(bullet,enemy):
 	#reset bullet
 	bullet.hideturtle()
 	bulletstate == "ready"
 	bullet.setposition(0,-400)
 	#update the score
 	previousEnemyYcor = enemy.ycor()#Jesse helped with this
 	if previousEnemyYcor <= 0:
 		score += 50
 	else:
 		score += 10
 	#reset enemy
 	x = random.randint(-200,200)
 	y = random.randint(100,250)
 	enemy.setposition(x,y)

 	scorestring = "Score: %s" %score
 	score_pen.clear() #so the score doesn't add on top of each other.. makes it clear
 	score_pen.write(scorestring, False, align = "Left", font = ("Times New Roman", 16, "normal"))

 enemy2 = enemy

 if score >= 80:#us
 	Enemy2()
 EnemyYcor = enemy.ycor()
 if EnemyYcor <= -10:
 	Warning()


 if isCollision(player,enemy):
 	player.hideturtle()
 	enemy.hideturtle()
 	border_pen.hideturtle() #us down
 	end_pen = turtle.Turtle()
 	end_pen = turtle.Turtle()
 	end_pen.color("#FF0000")
 	end_pen.penup()
 	end_pen.setposition(0,0)
 	end = "Game Over"
 	end_pen.write(end, False, align = "Center", font = ("Bree Sherif", 85 , "normal"))
 	end_pen.hideturtle()
 	win.exitonclick()
 	break
 if noCollision(player,enemy): #us
 	player.hideturtle()
 	enemy.hideturtle()
 	border_pen.hideturtle()
 	end_pen = turtle.Turtle()
 	end_pen.color("#FF0000")
 	end_pen.speed(10)
 	end_pen.pendown()
 	end_pen.setposition(0,0)
 	end = "Game Over"
 	end_pen.write(end, False, align = "Center", font = ("Bree Sherif", 85 , "normal"))
 	end_pen.hideturtle()
 	win.exitonclick()
 	break
