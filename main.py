# import pygame
# import sys



# def main():

# 	screen = pygame.display.set_mode((1020 , 800))
# 	screen.fill("Blue")
# 	clock = pygame.time.Clock()

# 	test_surface = pygame.Surface((80,100))
# 	test_surface.fill('Green')

# 	another_test_surface = pygame.Surface((40 , 70))
# 	another_test_surface.fill("Black")

# 	x_axis = 0

# 	while True:

# 		# screen

# 		screen.blit(test_surface , (100,200))
# 		# test_surface.blit(another_test_surface , (0,0))
# 		pygame.display.update()
# 		clock.tick(20)

# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				pygame.quit()
# 				sys.exit()






# if __name__ == "__main__":

# 	pygame.init()
# 	pygame.display.set_caption("Learning Pygame")
	

# 	main()




#-------------------------------------------------------------------------------

# import pygame
# import sys


# def main():

# 	time = pygame.time.Clock()


# 	font = pygame.font.Font('./font/Pixeltype.ttf' , size = 100)

# 	base_screen = pygame.display.set_mode((800 , 450))
# 	base_screen.fill('white')

# 	sky_screen = pygame.image.load("./graphics/Sky.png")
# 	ground_screen = pygame.image.load('./graphics/ground.png')
# 	snail1 = pygame.image.load("./graphics/snail/snail1.png")
# 	snail2 = pygame.image.load('./graphics/snail/snail2.png')
# 	snails = (snail1 , snail2)

# 	snail_x = 700

# 	text_screen = font.render("WelCoME" , None , "Black")


# 	while True:


# 		base_screen.blit(sky_screen , (0,0))
# 		base_screen.blit(ground_screen, (0, 300))
# 		base_screen.blit(text_screen , (300, 100))


# 		if snail_x < - 100:
# 			snail_x = snail_x + 900

# 		snail_x = snail_x - 1
# 		for snail in snails:
# 			base_screen.blit(snail , ( snail_x, 270))
# 			# print(snail)

# 		for event  in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				pygame.quit()
# 				sys.exit()


# 		pygame.display.update()
# 		time.tick(900)


# if __name__ == "__main__":

# 	pygame.init()

# 	main()


#--------------------------------------------------------------

# import pygame , sys





# def main():


# 	pygame.display.set_caption("My Game")

# 	base_surface = pygame.display.set_mode((800 , 450))
	
# 	sky_surface = pygame.image.load('./graphics/Sky.png')
# 	ground_surface = pygame.image.load("./graphics/ground.png")

# 	snail = pygame.image.load('./graphics/snail/snail1.png')
# 	snail_rect = snail.get_rect(midbottom = (700 , 300))

# 	player = pygame.image.load('./graphics/Player/player_stand.png')
# 	player_rect = player.get_rect(midbottom = (100 , 300))


# 	# sky_rect = sky_surface.get_rect(topleft =(0,0))


# 	font= pygame.font.Font('./font/Pixeltype.ttf' , 80)
# 	txt_surface = font.render("Welcome" , None , 'Black')

# 	clock = pygame.time.Clock()


# 	while True:


# 		base_surface.blit(sky_surface , (0,0))
# 		base_surface.blit(ground_surface , (0,300))
# 		base_surface.blit(txt_surface , (300 , 100))
# 		base_surface.blit(snail , snail_rect)

# 		player_rect.left = player_rect.left + 1

# 		if player_rect.left > 850:
# 			player_rect.left = player_rect.left - 850

# 		base_surface.blit(player , player_rect)

# 		snail_rect.right = snail_rect.right - 1

# 		if snail_rect.right < - 80:
# 			snail_rect.right = snail_rect.right + 900

# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				pygame.quit()
# 				sys.exit()


# 		pygame.display.update()
# 		# clock.tick(99)

# if __name__ == "__main__":

# 	pygame.init()
# 	main()






# Collisons and Mouse --------------


# import pygame , sys


# def main():

# 	base_surface = pygame.display.set_mode((800 , 450))
# 	sky = pygame.image.load('./graphics/Sky.png')
# 	ground = pygame.image.load('./graphics/ground.png')


# 	font = pygame.font.Font('./font/Pixeltype.ttf' , 70)
# 	txt = font.render("WelCOme" , None , "Black")
# 	count = 0


# 	snail = pygame.image.load('./graphics/snail/snail1.png')
# 	snail_rect = snail.get_rect(midbottom = (700,300))

# 	player = pygame.image.load('./graphics/Player/player_walk_1.png')
# 	player_rect = player.get_rect(midbottom = (100, 300))


# 	time = pygame.time.Clock()

# 	while True:


# 		base_surface.blit(sky , (0,0))
# 		base_surface.blit(ground , (0, 300))
# 		# base_surface.blit(txt, (200 , 100))

# 		base_surface.blit(snail, snail_rect)
# 		base_surface.blit(player , player_rect)


# 		if snail_rect.left < -100:
# 			snail_rect.left +=  850
# 		else:
# 			snail_rect.left -= 2


# 		if player_rect.left > 850:
# 			player_rect.left -=  900
# 		else:
# 			player_rect.left += 2		

# 		for event in pygame.event.get():

# 			if event.type == pygame.QUIT:
# 				pygame.quit()
# 				sys.exit()

# 			if event.type == pygame.MOUSEBUTTONDOWN:
# 				print(event.pos)


# 		if player_rect.colliderect(snail_rect):

# 			print("Collision detected ")
# 			count += 1


# 		score = font.render(count , None , "Black")
# 		score_rect = score.get_rect(center = (400, 220))
# 		base_surface.blit(score , score_rect)


# 		# if player_rect.collidepoint(pygame.mouse.get_pos()):
# 		# 	print("Mosuse collion detected")
# 		# 	print(pygame.mouse.get_pressed())



# 		pygame.display.update()
# 		time.tick(60)



# Keyboard Inputs , jump , gravity ---------------------------------------------------


# import pygame , sys

# # def player_gravity()

# def main():

# 	time = pygame.time.Clock()

# 	base = pygame.display.set_mode((800 , 400))

# 	sky = pygame.image.load('./graphics/Sky.png')
# 	sky_rect = sky.get_rect(topleft = (0,0))

# 	ground = pygame.image.load('./graphics/ground.png')
# 	ground_rect= ground.get_rect(topleft = (0,300))

# 	font = pygame.font.Font('./font/Pixeltype.ttf' , 80)
# 	tx_t = font.render("Welcome" , None , "Black")
# 	tx_t_rect = tx_t.get_rect(center = (400 , 100))

# 	player = pygame.image.load('./graphics/Player/player_stand.png')
# 	player_rct = player.get_rect(midbottom = (700,300))
# 	player_gravity = 0

# 	while True:


# 		base.blit(sky, sky_rect)
# 		base.blit(ground , ground_rect)
# 		base.blit(tx_t , tx_t_rect)
# 		base.blit(player, player_rct)

# 		# if player_rct.right < -1:
# 		# 	player_rct.right += 801
# 		# else:
# 		# 	player_rct.right -= 1


# 		print(player_rct.midbottom)

# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				pygame.quit()
# 				sys.exit()
# 			elif event.type == pygame.MOUSEBUTTONUP:
# 				print("colison")
# 				print(event.pos)

# 			elif event.type == pygame.KEYDOWN:
# 				if event.key == pygame.K_SPACE  :
# 						player_gravity = -22
# 						# player_rct.y = -500

					

# 		player_gravity += 1
# 		player_rct.y += player_gravity

# 		pygame.display.update()
# 		time.tick(60)

# if __name__ == '__main__':


# 	pygame.init()
# 	main()


## --- Practice -----------------------------------------------------------------------

# import pygame  , sys


# def main():

# 	base = pygame.display.set_mode((800 , 450))
	
# 	sky = pygame.image.load('./graphics/Sky.png')
# 	sky_rect = sky.get_rect(topleft = (0,0))

# 	ground = pygame.image.load('./graphics/ground.png')
# 	ground_rect = ground.get_rect(topleft = (0,300))


# 	snail = pygame.image.load('./graphics/snail/snail1.png')
# 	snail_rect = snail.get_rect(midbottom = (700 ,300))

# 	player = pygame.image.load('./graphics/Player/player_stand.png')
# 	player_rect = player.get_rect(midbottom = (100 , 300))

# 	font = pygame.font.Font('./font/Pixeltype.ttf', 80)
# 	txt_surface = font.render("Welcome" , None , "Black")
# 	txt_rect = txt_surface.get_rect(center = (400, 50))


# 	time = pygame.time.Clock()

# 	player_gravity = 0

# 	j_flag = True
# 	g_flag = False

# 	while True:

		





# 		base.blit(sky , sky_rect)
# 		base.blit(ground , ground_rect)
# 		base.blit(snail , snail_rect)
# 		base.blit(player , player_rect)
# 		base.blit(txt_surface , txt_rect)
		



# 		if snail_rect.x <  -100:
# 			snail_rect.x = snail_rect.x + 900
# 		else:
# 			snail_rect.x = snail_rect.x  - 10


# 		if player_rect.x > 850:
# 			player_rect.x = player_rect.x - 850
# 		else:
# 			player_rect.x = player_rect.x + 4



# 		if txt_rect.x > 850:
# 			txt_rect.x = txt_rect.x - 1000

# 		else:
# 			txt_rect.x = txt_rect.x + 2




# 		if player_rect.colliderect(snail_rect):
# 			print("Collison Detected")


# 		for event in pygame.event.get():

# 			if event.type == pygame.QUIT:
# 				pygame.quit()
# 				sys.exit()
# 			elif event.type == pygame.KEYDOWN:
# 				j_flag = True
# 				if event.key == pygame.K_SPACE and j_flag:
# 					player_rect.y -= 100
# 					# player_gravity = 70
# 					print(player_rect.y)
# 					# player_rect.y += player_gravity
# 					print(player_gravity)
# 					print(player_rect.y)
# 					j_flag= False
					

					

# 			elif event.type == pygame.MOUSEBUTTONDOWN:
# 				player_gravity = - 20
# 				print("Motion detected")
# 				if event.type == pygame.MOUSEBUTTONDOWN:
# 					print("Jump")

# 		if not (j_flag):
# 			print("I")
# 			player_gravity += 2
# 			player_rect.y = player_rect.y + 4
# 			if player_rect.y == 216:
# 				j_flag = True
# 				print(player_gravity)
# 				print(player_rect.y)

# 			print(player_gravity)
# 			print(player_rect.y)
					



		
# 		# print(player_rect.y)
# 		# print(player_rect.midbottom)

		
		
# 		# if player_rect.y < 216  and g_flag:
# 		# 	player_gravity = player_gravity + 1
# 		# 	player_rect.y =  216

# 		# player_rect.y = 216b



# 		time.tick(60)
# 		pygame.display.update()




# if __name__ == "__main__":



# 	pygame.init()
# 	pygame.display.set_caption("Game Title")

# 	main()


# -------------- Practice -----------------------

# import pygame , sys


# def main():

# 	game_state = True

# 	base = pygame.display.set_mode((800 , 450))
# 	# base.fill("Yellow")

# 	sky = pygame.image.load("./graphics/Sky.png")
# 	sky_rect = sky.get_rect(topleft = (0,0))
# 	ground = pygame.image.load("./graphics/ground.png")
# 	ground_rect = ground.get_rect(topleft = (0,300))

 
# 	snail = pygame.image.load("./graphics/snail/snail1.png")
# 	snail_rect = snail.get_rect(midbottom = (700 , 300))


# 	player = pygame.image.load("./graphics/Player/player_stand.png")
# 	player_rect = player.get_rect(midbottom = (100, 300))
# 	player_gravity = 0

# 	game_over = pygame.image.load("/home/shukla21amber/Pictures/b6c.jpg")


# 	time = pygame.time.Clock()

# 	while True:

# 		if game_state:
# 			base.blit(game_over , (0,0))
# 			# base.blit(sky, sky_rect)
# 			base.blit(ground , ground_rect)
# 			base.blit(player , player_rect)
# 			base.blit(snail , snail_rect)



# 			if snail_rect.right < -10:
# 				snail_rect.right += 840

# 			else:
# 				snail_rect.right -= 2

# 			if player_rect.left > 820:
# 				player_rect.left -= 850
# 			else:
# 				player_rect.left += 2

	 

			
	

# 			player_gravity += 1
# 			player_rect.y += player_gravity
# 			# print(game_state)

# 			if player_rect.bottom >= 300:
# 				player_rect.bottom = 300


# 			if player_rect.colliderect(snail_rect):
# 				game_state = False
# 		else:
# 			base.blit(game_over , (0,0))
# 			base.fill("Yellow")

# 			# print(game_state)







# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				pygame.quit()
# 				sys.exit()

# 			elif event.type == pygame.KEYDOWN and game_state == True :
# 				print("1")
# 				if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
# 					player_gravity = -50

# 			elif event.type == pygame.KEYUP :
# 				if event.key == pygame.K_SPACE:
# 					pass

# 			elif event.type == pygame.KEYDOWN and game_state == False:
# 				print("2")
# 				if event.key == pygame.K_SPACE :
# 					game_state = True
# 					print(game_state)
# 					player_rect.midbottom = (100, 300)
# 					snail_rect.midbottom = (700 , 300)
# 			elif event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
# 				print("Mouse Jump")
# 				# print("jump")
# 				player_gravity = -20


# 		time.tick(60)
# 		pygame.display.update()
		


# if __name__ == "__main__":

# 	pygame.init()
# 	pygame.display.set_caption("Game Practice")
# 	main()






#$                --------------------- PRACTICE ----------------------------


def display_time(font , base_ , count):

	game_count = (pygame.time.get_ticks() - count ) // 1000
	# print(game_count)

	game_time = font.render(f"{game_count}" , None , "Black")
	game_time_rect = game_time.get_rect(topleft = (700 , 50) )
	base_.blit(game_time , game_time_rect)


def main():


	while True:


		base_ = pygame.display.set_mode((800 , 450))

		sky_ = pygame.image.load("./graphics/Sky.png")
		sky_rect = sky_.get_rect(topleft = (0,0))

		ground_ = pygame.image.load("./graphics/ground.png")
		ground_rect = ground_.get_rect(topleft = (0,300))

		player_ = pygame.image.load("./graphics/Player/player_walk_1.png")
		player_rect = player_.get_rect(midbottom = (100 , 300))

		player_stand = pygame.image.load("./graphics/Player/player_stand.png")
		player_stand_scaled = pygame.transform.rotozoom(player_stand , 360 , 2)
		player_stand_scaled_rect = player_stand_scaled.get_rect(center = (400 , 225))


		snail_ = pygame.image.load("./graphics/snail/snail2.png")
		snail_rect = snail_.get_rect(midbottom = (700 , 300))

		font = pygame.font.Font("./font/Pixeltype.ttf" , 50)
		into_ = font.render("Welcome to Game" , None , "Black")
		into_rect = into_.get_rect(topleft = (50 , 50))


		player_gravity = 0
		time = pygame.time.Clock()
		game_state = False
		count = 0
		jump = 0





		while True:

			# ------ Event
			for event in pygame.event.get():
				if event.type == pygame.QUIT:

					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN and player_rect.bottom >= 300 and game_state == True:
					if event.key == pygame.K_SPACE:
						player_gravity = -20
						jump += 1


				elif event.type == pygame.KEYDOWN and  game_state == False:
					if event.key == pygame.K_SPACE:
						game_state = True
						snail_rect.midbottom = (700 , 300)
						player_rect.midbottom = (100 , 300)



			if game_state:

				# ---- Display
				base_.blit(sky_, sky_rect)
				base_.blit(ground_ , ground_rect)
				base_.blit(player_ , player_rect)
				base_.blit(snail_ , snail_rect)
				base_.blit(into_ , into_rect)
				display_time(font, base_ , count)





				# ------- Movement 
				if snail_rect.right  < -10:
					snail_rect.left += 890
				else:
					snail_rect.left -= 1


				if player_rect.left > 850:
					player_rect.left -= 900
				else:
					player_rect.left += 4


				player_gravity += 1
				player_rect.y += player_gravity


				if player_rect.bottom >= 300:
					player_rect.bottom = 300


				if player_rect.colliderect(snail_rect):
					game_state = False
					count = pygame.time.get_ticks()

			else:
				base_.fill((94,94,94))

				game_name = font.render("Pixel Runner" , None , "Green")
				game_name_rect = game_name.get_rect(center = (400 , 100))

				
				base_.blit(player_stand_scaled ,player_stand_scaled_rect )
				base_.blit(game_name , game_name_rect)

				space = font.render("Press space to run" , None , "Green")
				base_.blit(space, space.get_rect(center = (400, 400)))





			pygame.display.update()
			time.tick(60)


if __name__ == "__main__":

	import pygame , sys
	pygame.init()

	pygame.display.set_caption("Pygame Practice")

	main()




















































































































