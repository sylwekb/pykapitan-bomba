import pygame

class Level:
	"""Rysuje level, tlo itp;		
	"""
	def __init__(self, screen):
		self.screen=screen
		self.tlo = pygame.image.load(r"grafika/tlo.png").convert()
	def blit(self):
		self.screen.blit(self.tlo,(0,0))