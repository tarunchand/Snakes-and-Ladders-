#! /usr/bin/env python3

import pygame
import random
import time

pygame.init()

dice_value = 1

dice_rollen = False

ladder_size = 0


#Resolution
width = 1366
height = 768

#Colours
black=(10,10,10)
white=(250,250,250)
red= (200,0,0)
green=(0,200,0)
blue=(0,0,200)
grey=(50,50,50)
yellow=(150,150,0)
purple=(43,3,132)

#Graphics
board=pygame.image.load("graphics/board_768.jpg")
dice1=pygame.image.load("graphics/dice1.png")
dice2=pygame.image.load("graphics/dice2.png")
dice3=pygame.image.load("graphics/dice3.png")
dice4=pygame.image.load("graphics/dice4.png")
dice5=pygame.image.load("graphics/dice5.png")
dice6=pygame.image.load("graphics/dice6.png")
dice = [dice1,dice2,dice3,dice4,dice5,dice6]
player1=pygame.image.load("graphics/p1.png")
player2=pygame.image.load("graphics/p2.png")
player3=pygame.image.load("graphics/p3.png")
player4=pygame.image.load("graphics/p4.png")
players=[player1,player2,player3,player4]
india = pygame.image.load("graphics/india.png")
uk = pygame.image.load("graphics/uk.png")
snake = pygame.image.load("graphics/snake.png")
#pplayer1=pygame.image.load("graphics/p1.JPG")
#pplayer2=pygame.image.load("graphics/p2.JPG")
#pplayer3=pygame.image.load("graphics/p3.JPG")
#pplayer4=pygame.image.load("graphics/p4.JPG")
#pplayers = [pplayer1,pplayer2,pplayer3,pplayer4]

title=pygame.image.load("graphics/title_1366x768.jpg")

fireworks = []

for i in range(27):
	fireworks.append(pygame.image.load("graphics/fireworks/frame_" + str(i) + "_delay-0.06s.gif"))


#Board Coordinates

vals = [0,311,685,387,685,460,685,538,685,616,685,683,685,759,685,836,685,911,685,982,685,982,611,911,611,836,611,759,611,683,611,616,611,538,611,460,611,387,611,311,611,311,536,387,536,460,536,538,536,616,536,683,536,759,536,836,536,911,536,982,536,982,461,911,461,836,461,759,461,683,461,616,461,538,461,460,461,387,461,311,461,311,383,387,383,460,383,538,383,616,383,683,383,759,383,836,383,911,383,982,383,982,309,911,309,836,309,759,309,683,309,616,309,538,309,460,309,387,309,311,309,311,235,387,235,460,235,538,235,616,235,683,235,759,235,836,235,911,235,982,235,982,159,911,159,836,159,759,159,683,159,616,159,538,159,460,159,387,159,311,159,311,86,387,86,460,86,538,86,616,86,683,86,759,86,836,86,911,86,982,86,982,13,911,13,836,13,759,13,683,13,616,13,538,13,460,13,387,13,311,13]



game_display=pygame.display.set_mode((width,height),pygame.FULLSCREEN)
pygame.display.set_caption('Snakes & Ladders')
clock = pygame.time.Clock()

pygame.mixer.music.load('music/01.mp3')
pygame.mixer.music.play(-1)

def roll_dice():
	global dice_value
	global dice_rollen

	dice_value=random.randint(1,6)
	dice_rollen=True


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,fs,n):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()


	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(game_display,ac,(x,y,w,h))
		if click[0]==1:
			if n==5:
				pygame.quit()
				quit()
			elif n<5:
				scores=[0,0,0,0]
				print('Number of players ' + str(n))
				play(n,scores)
			elif n==6:
				roll_dice()
				time.sleep(1)
	else:
		pygame.draw.rect(game_display,ic,(x,y,w,h))


	smallText = pygame.font.Font('freesansbold.ttf',fs)
	textSurf,textRect = text_objects(msg,smallText)
	textRect.center=((x+(w/2)),(y+(h/2)))
	game_display.blit(textSurf,textRect)



'''
	smallText = pygame.font.Font('freesansbold.ttf',fs)
   	textSurf, textRect = text_objects(msg, smallText)
   	textRect.center=((x+(w/2)),(y+(h/2)))
   	game_display.blit(textSurf,textRect)
'''



def ladders(x):

    global ladder_size

    if x==1:
    	ladder_size = 2
    	return 38
    elif x==4:
    	ladder_size = 1
    	return 14	
    elif x==9:
    	ladder_size = 1
    	return 31
    elif x==28:
    	ladder_size = 2
    	return 84
    elif x==21:
    	ladder_size = 1
    	return 42
    elif x==51:
    	ladder_size = 1
    	return 67
    elif x==80:
    	ladder_size = 1
    	return 100
    elif x==71:
    	ladder_size = 1
    	return 91
    else:
    	ladder_size = 0
    	return x

def snakes(x): 
    if x==17:
    	return 7
    elif x==54:
    	return 34
    elif x==62:
    	return 19
    elif x==64:
    	return 60
    elif x==87:
    	return 24
    elif x==93:
    	return 73
    elif x==95: 
    	return 75
    elif x==98: 
    	return 79
    else:
    	return x
'''
def x_cor(k):
	if k == 100:
		return 304
	elif k<=10 :
		return 304+(k-1)*(75.8)
	else:
		y = k%10
		x = k/10
		if y!=0:
			if x%2==0:
				return 304+(y-1)*(75.8)
			else:
				return 1062-y*75.8
		else:
			if x%2==0:
				return 304
			else:
				return 986.2

def y_cor(k):
	if k == 100:
		return 5
	elif k<=10:
		return 687.2
	else:
		y = k%10
		x = k/10
		if y==0:
			x = x-1
		return 687.2-x*75.8



'''		



def play(n,scores):

	global dice_value
	global dice_rollen
	global ladder_size

	player_turn = 1

	game_display.fill(purple)
	game_display.blit(board,(299,0))
	for i in range(n):
			game_display.blit(players[i],(15+i*75,700))
			pygame.display.update()
	
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		button('Player Number ',1167,400,150,50,red,yellow,20,9)
		button(str(player_turn) ,1167,500,150,50,red,yellow,20,9)
		button('turn',1167,600,150,50,red,yellow,20,9)


		button('Quit',1167,70,150,50,red,yellow,20,5)
		pygame.display.update()

		button('Roll Dice',100,600,150,50,red,yellow,20,6)
		

		#print('Dice Value is ' + str(dice_value))

		#game_display.blit(dice[dice_value-1],(120,400))
		pygame.display.update()

		if dice_rollen == True:

			snak = False

			new_score = scores[player_turn-1]+dice_value

			temp = scores[player_turn-1]

			pygame.mixer.music.load('music/dice.mp3')
			pygame.mixer.music.play()
			time.sleep(1)

			game_display.blit(dice[dice_value-1],(120,400))
			pygame.display.update()

			pygame.mixer.music.load('music/01.mp3')
			pygame.mixer.music.play(-1)

			if ladders(new_score)!= new_score :
				scores[player_turn-1]=ladders(new_score)
			elif snakes(new_score)!=new_score :
				snak = True
				scores[player_turn-1]=snakes(new_score)
			else:
				scores[player_turn-1]=new_score

			print('Scores of player : ' + str(scores))

			if scores[player_turn-1]>=100 :
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							quit()
					print('Player ' + str(player_turn) +' Won')
					game_display.fill(blue)
					button('Player' + str(player_turn) + 'Won',100,100,300,300,red,yellow,40,5)
					#game_display.blit(players[player_turn-1],(600,300))
					pygame.display.update()
					for i in range(27):
						game_display.blit(fireworks[i],(600,200))
						pygame.display.update()
						time.sleep(0.06)

			
			while temp<=new_score:
				game_display.fill(purple)
				game_display.blit(board,(299,0))
				game_display.blit(dice[dice_value-1],(120,400))
				pygame.display.update()
				for i in range(n):
					if i!=player_turn-1:
						game_display.blit(players[i],(vals[2*scores[i]-1],vals[2*scores[i]]))
						pygame.display.update()
				game_display.blit(players[player_turn-1],(vals[2*temp-1],vals[2*temp]))
				pygame.display.update()
				temp=temp+1
				time.sleep(1)

			if ladder_size == 1:
					pygame.mixer.music.load('music/01.mp3')
					pygame.mixer.music.play(-1)
					game_display.blit(india,(0,0))
					pygame.display.update()
					time.sleep(1)
			elif ladder_size == 2:
					pygame.mixer.music.load('music/01.mp3')
					pygame.mixer.music.play(-1)
					game_display.blit(uk,(0,0))
					pygame.display.update()
					time.sleep(1)
			if snak:
				pygame.mixer.music.load('music/01.mp3')
				pygame.mixer.music.play(-1)
				game_display.blit(snake,(0,0))
				pygame.display.update()
				time.sleep(1)


			

			game_display.fill(purple)
			game_display.blit(board,(299,0))
			pygame.display.update()
			for i in range(n):
				game_display.blit(players[i],(vals[2*scores[i]-1],vals[2*scores[i]]))
				pygame.display.update()
	


			if (player_turn+1)<=n:
				player_turn=player_turn+1
			else:
				player_turn=1

			



			dice_rollen = False
			
			


		








start = False

while not start:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key== pygame.K_RETURN:
				start = True


	game_display.fill(green)
	game_display.blit(title,(0,0))

	pygame.display.update()             

	clock.tick(60)

game_display.fill(blue)
pygame.display.update()

while start:
	
	button('Two Players',650,70,150,50,red,yellow,20,2)

	pygame.display.update()

	button('Three Players',650,270,150,50,red,yellow,20,3)

	pygame.display.update()

	button('Four Players',650,470,150,50,red,yellow,20,4)

	pygame.display.update()

	button('Quit',650,670,150,50,red,yellow,20,5)

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()












pygame.quit()
quit()



