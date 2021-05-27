import pygame
import random

class Alien:
	r"""Rysuje przeciwnika i sprawdza czy zostal trafiony:
		Alien(screen) - przyjmuje pygame'owy Surface i na nim wyswietla.
	"""
	def __init__(self, screen):
		self.state=True
		self.screen=screen
		self.v = random.randint(5,10)
		self.posX=0
		self.posY=250+random.randint(-20,20)
		self.hit_channel = pygame.mixer.Channel(1)
		self.hit_sound1 = pygame.mixer.Sound(r"dzwieki/hit.wav")
		self.hit_sound2 = pygame.mixer.Sound(r"dzwieki/hit2.wav")
		self.hit_sounds=[]
		self.hit_sounds.append(self.hit_sound1)
		self.hit_sounds.append(self.hit_sound2)
		
		
	def draw(self):
		"""Zdefiniuj metode rysowania dla swojego aliena ;)
		"""
		pass
		
			
	def move(self):			#wspolna metoda dla wszystkich alienow
		self.posX+=self.v
		self.posY+=random.randint(-5,5)
		if self.posX>self.screen.get_width()+180:
			self.posX=0
			self.v = random.randint(5,10)
			self.posY=250+random.randint(-50,50)
		if self.posY<200:
			self.posY=201
		elif self.posY>400:
			self.posY=399
			
	def alive(self):
		self.state=True
		self.posX=0
		