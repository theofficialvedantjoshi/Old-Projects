import pygame,sys
from pygame.locals import*
from pygame import mixer
import random
import math
pygame.init()
clock = pygame.time.Clock()
fps = 20
scrw = 600
scrh = 600
x = 480
y = 480
vel = 10
menu = True
menu2 = False
game = False
#screen
icon = pygame.image.load('ufo.png')
end = pygame.image.load('end.png')
menu_pic = pygame.image.load('Menu1.png')
menu_2pic = pygame.image.load('Menu2.png')
win = pygame.display.set_mode((scrw,scrh))
pygame.display.set_icon(icon)
pygame.display.set_caption("SpaceInvaders")
menu1 = pygame.display.set_mode((scrw,scrh))
menu2_scr = pygame.display.set_mode((scrw,scrh))
mixer.music.load('background.wav')
mixer.music.play(-1)
#images
bg = pygame.image.load('bg.png')
pl = pygame.image.load('spaceship.png')
pl2 = pygame.image.load('ship2.png')
pl3 = pygame.image.load('ship3.png')
pl4 = pygame.image.load('ship4.png')
run = True
#bullet
bullet = pygame.image.load('bullet.png')
bulletX = 480
bulletY  = 480
bullet_vel = 20 
firestate = "ready"
#enemy
enemy = []
enemyX = []
enemyY = []
enemies = 6
enemyX_vel = []
enemyY_vel = []
#spawn enemies
for i in range(enemies):
    enemyX.append(random.randint(0,534))
    enemyY.append(random.randint(50,150))
    enemy.append(pygame.image.load('enemy.png'))
    enemyX_vel.append(8)
    enemyY_vel.append(20)
#shooting
def firebullet():
    global firestate
    firestate = "shoot"
#collision    
def iscollision(enemyX,enemyY,bulletX,bulletY):
    dist = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2))) 
    if dist < 51:
        return True
    else:
        return False       
score = 0
font = pygame.font.SysFont(None,60)
def pick(text,color,ax,ay):
    choose = font.render(text,True,color)
    menu2_scr.blit(choose,(ax,ay))
#main_LOOP
while run:
    while menu:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type ==QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            menu2 = True
            menu = False
        if keys[pygame.K_q]:
            pygame.quit()
            run = False    
        menu1.blit(menu_pic,(0,0))
        pygame.display.update()
    while menu2:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type ==QUIT:
                run = False
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            run = False
        if keys[pygame.K_a]:
            game = True
            menu2=False
            menu = False
        if keys[pygame.K_s]:
            game = True
            pl = pygame.image.load('ship2.png')
            menu2=False
            menu = False 
        if keys[pygame.K_d]:
            game = True
            pl = pygame.image.load('ship3.png')
            menu2=False
            menu = False  
        if keys[pygame.K_f]:
            game = True
            pl = pygame.image.load('ship4.png')
            menu2=False
            menu = False                  
        menu2_scr.blit(menu_2pic,(0,0))
        menu2_scr.blit(pl,(50,400))
        menu2_scr.blit(pl2,(200,400))
        menu2_scr.blit(pl3,(400,400))
        menu2_scr.blit(pl4,(540,400))
        pick("A",(255,255,255),75,350)
        pick("S",(255,255,255),220,350)
        pick("D",(255,255,255),420,350)
        pick("F",(255,255,255),550,350)
        pygame.display.update()                
    while game:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type ==QUIT:
                run = False
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            run = False
        if keys[pygame.K_RIGHT] and x < 536:
            x+=vel
        if keys[pygame.K_LEFT] and x > 0:
            x-=vel
        if keys[pygame.K_SPACE]:
            if firestate is "ready":
                bs = mixer.Sound('laser.wav')
                bs.play()
                bulletX = x
            firebullet()     
        #drawing_to_screen
        win.blit(bg,(0,0))
        win.blit(pl,(x,y))
        #enemy_movement
        for i in range(enemies):
            win.blit(enemy[i],(enemyX[i],enemyY[i]))
            enemyX[i]+=enemyX_vel[i]
            if enemyX[i] >=534:
                enemyX_vel[i] = -8
            if enemyX[i] <=0:
                enemyX_vel[i] = 8
                enemyY[i]+= enemyY_vel[i]
            if enemyX[i] > 534:
                enemyY[i] +=enemyY_vel[i]   
            #collision
            collision = iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
            if collision:
                exp = mixer.Sound('exp.wav')
                exp.play()
                firestate = "ready"
                bulletY = 480
                score+=1
                #print(score)
                enemyX[i] = random.randint(0,500)
                enemyY[i] = random.randint(50,150)
            if enemyY[i] > 450:
                enemyX[i] = random.randint(0,500)
                enemyY[i] = random.randint(50,150)
                score-=1           
        if bulletY < 0:
            bulletY = 480
            firestate = "ready"    
        if firestate is "shoot":
            bulletY -= bullet_vel
            win.blit(bullet,(bulletX,bulletY))               
        pick("Score:"+str(score),(255,255,255),0,0)
        if score > 30:
            win.blit(end,(0,0))        
        pygame.display.update()
pygame.quit()    
