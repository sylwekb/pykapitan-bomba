import pygame
from alien import *

class AlienThree(Alien):
	def __init__(self, screen):
		Alien.__init__(self,screen)
		self.alien = pygame.image.load(r"grafika/alienthree.png").convert_alpha()
	
	def draw(self):
		self.move()
		self.screen.blit(self.alien, (self.posX-self.alien.get_width(),self.posY))
		
	def isHit(self, mouse_pos): #wspolna metoda dla wszystkich alienow
		mousex=mouse_pos[0]
		mousey=mouse_pos[1]
		
		if (self.posX+130-self.alien.get_width()>mousex>self.posX+90-self.alien.get_width()) and (self.posY+100>mousey>self.posY+30):
			self.hit_channel.play(self.hit_sounds[1])
			return True
		else:
			return False
	
		
		
	