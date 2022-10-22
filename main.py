import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Bunny Game')

clock = pygame.time.Clock()
FPS = 60

value = 0

moving = False

velocity = 12

x1 = 100
y1 = 150

moving_left = False
moving_right = False

BG = (166, 199, 222)

def drawBg():
    screen.fill(BG)

class Bunny(pygame.sprite.Sprite):
    def __init__(self, x1, y1, scale):
        pygame.sprite.Sprite.__init__(self)
        img =  [pygame.image.load('Images/movel_0.png'),
                pygame.image.load('Images/movel_1.png'),
                pygame.image.load('Images/movel_2.png'),
                pygame.image.load('Images/movel_3.png')]
        
        self.image = img 
        #pygame.transform.scale(img, ((img.get_width() * scale), (img.get_height() * scale)))
        #self.rect = self.image[0].get_rect()
        #self.rect.center = (x1, y1)

    #def draw(self):
     #   screen.blit(self.image, (x1, y1))


player1 = Bunny(x1, y1, 0.5)

run = True
while run:
    #drawBg()
    
    
    clock.tick(FPS)

    for event in pygame.event.get():
        
        
        if event.type == pygame.QUIT:
            run = False
        

                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving = False
                moving_left = False
                # print("Stopped moving left")
            if event.key == pygame.K_d:
                moving = False
                moving_left = False
                # print("Stopped moving right")
        
        key_pressed_is = pygame.key.get_pressed()
 
        if key_pressed_is[pygame.K_a]:
            x1 -= 10
            moving = True
        if key_pressed_is[pygame.K_d]:
            x1 += 10
            moving = True


        
        
        if moving:
            value += 1

        
        if value >= len(player1.image):
            value = 0

        image = player1.image[value]

        image = pygame.transform.scale(image, (100,100))

        screen.blit(image, (x1, y1))

        

        pygame.display.update()

        screen.fill((0,0,0))

pygame.quit()