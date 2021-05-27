import pygame
import color
import time

class Game:
	"""No menu po prostu...
	"""
	def __init__(self, screen):
		self.screen=screen
		self.score=0
		self.state = {"graj":False,"wyniki":False,"wyjscie":False, "pokazmenu":False}
		self.font = pygame.font.Font(None, 25)
		self.clock = pygame.time.Clock() #do predkosci rakiety
		self.logo = pygame.image.load(r"grafika/logo.png").convert_alpha()
		self.menu_tlo = pygame.image.load(r"grafika/menu_tlo.jpg").convert()
		self.graj1 = pygame.image.load(r"grafika/graj1.png").convert_alpha()
		self.graj2 = pygame.image.load(r"grafika/graj2.png").convert_alpha()
		self.wyniki1= pygame.image.load(r"grafika/wyniki1.png").convert_alpha()
		self.wyniki2 = pygame.image.load(r"grafika/wyniki2.png").convert_alpha()
		self.wyjscie1 = pygame.image.load(r"grafika/wyjscie1.png").convert_alpha()
		self.wyjscie2 = pygame.image.load(r"grafika/wyjscie2.png").convert_alpha()
		self.orzel = pygame.image.load(r"grafika/orzel.png").convert_alpha()
		self.menu_sound = pygame.mixer.Sound(r"dzwieki/menu.wav")
		self.orzelx=self.screen.get_width()-60
		
	def showMenu(self):
		self.screen.blit(self.menu_tlo, (0,0))
		if not pygame.mixer.get_busy():
			self.menu_sound.play()
			
		self.orzelx-=(self.clock.tick()/20) #predkosc orzela 7 (default:20)
		if self.orzelx+self.orzel.get_width()<=0:
			self.orzelx=self.screen.get_width()
		self.screen.blit(self.orzel, (self.orzelx,self.logo.get_height()))
		self.screen.blit(self.logo, (100,0))
		
		x,y = pygame.mouse.get_pos()
		
		if (400>x>200 and 450>y>390):
			self.screen.blit(self.graj2, (200,390))
		else:
			self.screen.blit(self.graj1, (200,390))
			
		if (400>x>200 and 510>y>450):
			self.screen.blit(self.wyniki2, (200,450))
		else:
			self.screen.blit(self.wyniki1, (200,450))
			
		if (400>x>200 and 570>y>510):
			self.screen.blit(self.wyjscie2, (200,510))
		else:
			self.screen.blit(self.wyjscie1, (200,510))
		
	def choice(self, pos):
		x=pos[0]
		y=pos[1]
		if self.state["pokazmenu"]:
			if (400>x>200 and 450>y>390):
				self.state["graj"]=True
				self.score=0
				self.name=[]
				self.time_s=time.clock()+60
			if (400>x>200 and 510>y>450):
				self.state["wyniki"]=True
			if (400>x>200 and 570>y>510):
				self.state["wyjscie"]=True
	
	def showScores(self):
		try:
			scores = open(r"wyniki.fred")
			text=[]
			for line in scores.readlines():
				text.append(self.font.render(line[:-1]+" ptk.",True,color.green))
			scores.close()
			i=0
			pygame.draw.rect(self.screen, color.black, ((200,150),(400,350)))
			pygame.draw.rect(self.screen, color.green, ((200,150),(400,350)),2) #ramka
			for elem in text:
				self.screen.blit(elem, (250,215+i))
				i+=20
			
		except IOError:
			pygame.draw.rect(self.screen, color.black, ((200,150),(300,250)))
			pygame.draw.rect(self.screen, color.green, ((200,150),(300,250)),2) #ramka
			self.screen.blit(self.font.render("JESZCZE NIC NIE MA, GRAJ!",True,color.green), (210,215))
	
	def scoreToFile(self): #name to lista zawierajaca literki
		scores = open(r"wyniki.fred", 'a')
		scores.write("".join(self.name)+" "+str(self.score)+"\n")
		scores.close()
			
		
		
		
			
			