import pygame
import color
import time
import random
from game import *
from alienone import *
from alientwo import *
from alienthree import *
from gun import *
from level import *


resolution = (900,600) # (900,600) max rozdzielka - biega o tlo
pygame.init()
pygame.display.set_caption("pyKapitan Bomba")
screen = pygame.display.set_mode(resolution)

font = pygame.font.Font(None, 25)	
pygame.mouse.set_visible(True)
done=False
shoot=False
clicked=False
back=False	
type_name=False


clock=pygame.time.Clock()
lvl = Level(screen)	
gun = Gun(screen)


aliens=[AlienOne(screen),AlienTwo(screen),AlienThree(screen)]



game = Game(screen)
game.state["pokazmenu"]=True #zeby pokazalo menu

while done==False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True
		if event.type == pygame.KEYDOWN:
			if type_name:
				if event.key==8:
					if len(game.name):
						del game.name[-1]
				elif event.key==13 or event.key==271: #kody obu przyciskow ENTER
					type_name=False
					game.scoreToFile()
					game.state["pokazmenu"]=True
				else: 
					game.name.append(event.unicode)
   	    
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if game.state["pokazmenu"]:
				clicked=True
			if game.state["wyniki"]:
				back=True
			if game.state["graj"]:
				shoot=True
			
				
		
	#START
	
	if game.state["pokazmenu"]:
		if clicked:
			game.choice(pygame.mouse.get_pos())
			clicked=False
		pygame.mouse.set_visible(True)
		game.showMenu()
			
	if game.state["graj"]: #kolejnosc wazna
		for elem in game.state:
				game.state[elem]=False
		game.state["graj"]=True
		game.menu_sound.stop()
		pygame.mouse.set_visible(False)
		lvl.blit()       #blitowanie tla
		
		
		if game.score<=40:
			for i in range(0,2):
				if aliens[i].state:
					aliens[i].draw()
				else:
					aliens[i].alive()
		else:
			for i in range(1,3):
				if aliens[i].state:
					aliens[i].draw()
				else:
					aliens[i].alive()
		
		if shoot:
			gun.shoot()
			for alien in aliens:
				if alien.isHit(pygame.mouse.get_pos()):
					game.score+=1
					alien.state=False
			shoot=False
		gun.draw()
		dif_time = round(game.time_s-time.clock(),1)
		pygame.draw.rect(screen, color.black, ((0,550),(100,600)))
		pygame.draw.rect(screen, color.green, ((0,550),(100,600)),2)
		text = font.render("wynik: "+str(game.score),True,color.green)
		screen.blit(text, (7,555))
		text = font.render("czas: "+ str(dif_time),True,color.green)
		screen.blit(text, (7,575))
		if dif_time<=0:
			type_name=True
			game.state["graj"]=False
	if type_name:
		screen.fill(color.black)
		pygame.mouse.set_visible(True)
		text = font.render("KONIEC GRY",True,color.green)	
		screen.blit(text, (375,255))
		text = font.render("TYPE YOUR NAME SOLDIERZE:",True,color.green)	
		screen.blit(text, (300,275))			
		text = font.render("".join(game.name)+"_",True,color.green)
		screen.blit(text, (300,295))
			
		
	if game.state["wyniki"]:
		for elem in game.state:
			game.state[elem]=False
		game.state["wyniki"]=True
		game.state["pokazmenu"]=True
		game.showScores()
		if back: #zeby wyjsce trzeba klinkac myszka
			game.state["pokazmenu"]=True
			game.state["wyniki"]=False
			back=False
		
		
	if game.state["wyjscie"]:
		done=True		


	#END
	pygame.display.update()
	clock.tick(30)	

pygame.quit()