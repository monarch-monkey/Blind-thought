import pygame
import sys
from pygame.sprite import Sprite,Group
import time
import random

class Rock():
	def __init__(self,screen):
		self.screen = screen
		self.image = pygame.image.load(\
		                'c://Users/Administrator/Desktop/new_game/images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect() 		
		
		self.rect.centerx = 0		
		self.rect.centery = 600
		
	
	def blitme(self):
		self.screen.blit(self.image,self.rect)

class Bullet(Sprite):
	def __init__(self,screen,rock):
		super().__init__()
		self.screen = screen		
		self.rect = pygame.Rect(0,0,3,15)
		self.rect.centerx = rock.rect.centerx
		self.rect.centery = rock.rect.centery
		self.rect.top = rock.rect.top		
		self.y = float(self.rect.y)		
		self.color = (60,60,60)
	
	def update(self):
		self.y -= 1
		self.rect.y = self.y
	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)

class Clock(Sprite):
	def __init__(self,screen):
		super().__init__()
		self.screen = screen
		self.rect = pygame.Rect(0,0,random.randint(0,50),random.randint(0,50))
		self.rect.centerx = random.randint(0,550)
		self.rect.centery = random.randint(0,700)
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)
		self.color = (random.randint(0,200),random.randint(0,200),random.randint(0,200))
		self.clock_dr = True
		self.clock_dr1 = True
		
	def update(self):
		
		if self.x >= 950:
			self.clock_dr = False			
		elif self.x <= 0:
			self.clock_dr = True
		
		if self.y >= 550:
			self.clock_dr1 = False
		elif self.y <= 0:
			self.clock_dr1 = True
		
		if self.clock_dr:
			self.x += 0.5
		else:
			self.x -= 0.5
		self.rect.x = self.x
		
		if self.clock_dr1:
			self.y += 0.5
		else:
			self.y -= 0.5
		self.rect.y = self.y
		
	def draw_clock(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
	def hit(self):
		self.clock_dr = not self.clock_dr
		self.clock_dr1 = not self.clock_dr1

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((1000,600))
	pygame.display.set_caption("Rock")
	bg_color = (230,230,230)
	rock = Rock(screen)
	bullets = Group()
	clocks = Group()		
	speed = 35
	while True:			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()				
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:	
					rock.rect.centerx += speed
				elif event.key == pygame.K_LEFT:
					rock.rect.centerx -= speed
				elif event.key == pygame.K_UP:
					rock.rect.centery -= speed					
				elif event.key == pygame.K_DOWN:
					rock.rect.centery += speed
				elif event.key == pygame.K_SPACE:	
					new_bullet = Bullet(screen,rock)
					bullets.add(new_bullet)
				elif event.key ==pygame.K_a:					
					clocks.add(Clock(screen))
					
		bullets.update()
		clocks.update()
		screen.fill(bg_color)	
		rock.blitme()
		
		if pygame.sprite.spritecollideany(rock,clocks):
			clock.hit()
		for bullet in bullets.sprites():
			bullet.draw_bullet()
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		for clock in clocks:
			clock.draw_clock()		
		collisions = pygame.sprite.groupcollide(bullets,clocks,True,True)		
		
		pygame.display.flip()
run_game()	

		
	
	
	
	