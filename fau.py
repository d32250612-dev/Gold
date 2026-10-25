import pygame
import colors 
import setting

pygame.init()

sen = pygame.display.set_mode((setting.WIDTH ,setting.HEIGHT))

closk = pygame.time.Clock()



runn = True
while runn == True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            runn = False
    sen.fill(colors.RED)
    pygame.display.flip()
    closk.tick(setting.FPS)


pygame.quit()










