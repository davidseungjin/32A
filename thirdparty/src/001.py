import pygame

def run() -> None:
	pygame.init()

	# creates a window containing a surface that is
	# 700 pixels wide and 600 pixels tall.
	surface = pygame.display.set_mode((700,600))
	running = True

	color_amount = 0
	clock = pygame.time.Clock()
	circle_center_x = 350
	circle_center_y = 300



	while running:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		color_amount = (color_amount + 1) % 256
		circle_center_x = (circle_center_x + 1) % 350
		circle_center_y = (circle_center_y - 1) % 300

		surface.fill(pygame.Color(color_amount, color_amount, color_amount))
		pygame.draw.circle(surface, pygame.Color(255, 255, 0), (circle_center_x, circle_center_y), 100)

		pygame.display.flip()

	pygame.quit()

if __name__ == '__main__':
	run()
