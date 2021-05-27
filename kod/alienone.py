import pygame
from alien import *

class AlienOne(Alien):
	def __init__(self, screen):
		Alien.__init__(self,screen)
		self.alien = pygame.image.load(r"grafika/alienone.png").convert_alpha()
	
	def draw(self):
		self.move()
		self.screen.blit(self.alien, (self.posX-self.alien.get_width(),self.posY))
		
	def isHit(self, mouse_pos): #wspolna metoda dla wszystkich alienow
		mousex=mouse_pos[0]
		mousey=mouse_pos[1]
		
		if (self.posX+120-self.alien.get_width()>mousex>self.posX+80-self.alien.get_width()) and (self.posY+90>mousey>self.posY+30):
			self.hit_channel.play(self.hit_sounds[0])
			return True
		else:
			return False
	
	
		
		
	