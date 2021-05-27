import pygame

class Gun:
	"""Rysuje bron oraz wydaje dzwieki przy oddawaniu strzalu.
		Gun(screen) - przyjmuje pygame'owy Surface i na nim wyswietla.
	"""
	def __init__(self, screen):
		self.screen=screen
		self.gun = pygame.image.load(r"grafika/gun.png").convert_alpha()
		self.cel = pygame.image.load(r"grafika/celownik.png").convert_alpha()
		self.shoot_pic = pygame.image.load(r"grafika/shoot.png").convert_alpha()
		self.shoot_sound = pygame.mixer.Sound(r"dzwieki/shoot.wav")
		self.shoot_sound.set_volume(0.2)

	def draw(self):
		self.posX, self.posY = pygame.mouse.get_pos()
		if self.posX>=600:
			self.screen.blit(self.gun, (self.screen.get_width()-300,self.screen.get_height()-200))
		else:
			self.screen.blit(self.gun, (self.posX,self.screen.get_height()-200))
		self.screen.blit(self.cel, (self.posX-self.cel.get_width()/2,self.posY-self.cel.get_height()/2))
		
	def shoot(self):
		if self.posX>=600:
			self.screen.blit(self.shoot_pic, (self.screen.get_width()-275,self.screen.get_height()-177))
		else:
			self.screen.blit(self.shoot_pic, (self.posX+25,self.screen.get_height()-180))
			
		self.shoot_sound.play()
			
	def get_pos(self):
		return (self.posX, self.posY)