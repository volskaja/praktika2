import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((300,300))
ekraani_pind.fill((0,0,200))
pygame.display.set_caption("volskaja")

ekraani_pind.fill((250,0,250))

pygame.draw.rect(ekraani_pind, (0, 0, 0), (100, 30, 100, 250))# Рисование корпуса светофора
pygame.draw.circle(ekraani_pind, (255, 0, 0), (150, 70), 30)# Рисование красного сигнала
pygame.draw.circle(ekraani_pind, (255, 255, 0), (150, 145), 30)# Рисование желтого сигнала
pygame.draw.circle(ekraani_pind, (0, 255, 0), (150, 220), 30)#Рисование зеленого сигнала


pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

pygame.quit()


