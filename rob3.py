import pygame
import random
pygame.init()
win = pygame.display.set_mode((1000,765))
pygame.display.set_caption("Rob Master")

pygame.mixer.set_num_channels(20)

class Welcome(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.chsound = pygame.mixer.Sound("ChoiceSound.wav")
        self.chschannel = pygame.mixer.Channel(19)

        self.chschannel.set_volume(0.3)

        self.image = pygame.image.load("tex\Welcomeimage.png")

        self.creditimage = pygame.image.load("tex\CreditImage.png")

        self.creditquitimage = pygame.image.load("tex\CreditQuit.png")

        self.creditquitrect = pygame.Rect(0, 0, 100, 100)

        self.credits = pygame.font.SysFont('Comic Sans MS', 45)
        self.creditsr = self.credits.render("Игра разработана с нуля на python", True,(255, 255, 255))
        self.creditsr1 = self.credits.render("с использованием библиотеки pygame", True,(255, 255, 255))
        self.creditsr2 = self.credits.render("Трухановым Марком Андреевичем,", True,(255, 255, 255))
        self.creditsr3 = self.credits.render("учеником КГАОУ ДО РМЦ г. Хабаровска", True,(255, 255, 255))

        self.startx = 300
        self.starty = 400
        self.startw = 400
        self.starth = 80

        self.startrect = pygame.Rect(self.startx, self.starty, self.startw, self.starth)

        self.starttxt = pygame.image.load("tex\WelcomeStartGame.png")

        self.starttxtpressed= pygame.image.load("tex\WelcomeStartGamePressed.png")

        self.startchoice = False

        self.creditx = 400
        self.credity = 500
        self.creditw = 200
        self.credith = 80

        self.creditrect = pygame.Rect(self.creditx, self.credity, self.creditw, self.credith)

        self.credittxt = pygame.image.load("tex\WelcomeAuthor.png")

        self.credittxtpressed = pygame.image.load("tex\WelcomeAuthorPressed.png")

        self.creditchoice = False

        self.quitx = 300
        self.quity = 600
        self.quitw = 400
        self.quith = 80

        self.quitrect = pygame.Rect(self.quitx, self.quity, self.quitw, self.quith)

        self.quittxt = pygame.image.load("tex\WelcomeQuit.png")

        self.quittxtpressed = pygame.image.load("tex\WelcomeQuitPressed.png")

        self.quitchoice = False

        self.cr = 0

        self.lvl = -1

    def col(self, cursor):
        if self.cr == False:
            if self.startrect.colliderect(cursor.rect):
                if self.startchoice:
                    self.startchoice = False
                    self.chschannel.play(self.chsound)

                if pygame.mouse.get_pressed()[0]:
                    self.lvl = 0

            if self.startrect.colliderect(cursor.rect) == False:
                self.startchoice = True

            if self.creditrect.colliderect(cursor.rect):
                if self.creditchoice:
                    self.creditchoice = False
                    self.chschannel.play(self.chsound)

                if pygame.mouse.get_pressed()[0]:
                    self.cr = True

            if self.creditrect.colliderect(cursor.rect) == False:
                self.creditchoice = True

            if self.quitrect.colliderect(cursor.rect):
                if self.quitchoice:
                    self.quitchoice = False
                    self.chschannel.play(self.chsound)

                if pygame.mouse.get_pressed()[0]:
                    pygame.quit()

            if self.quitrect.colliderect(cursor.rect) == False:
                self.quitchoice = True

        if self.cr:
            if self.creditquitrect.colliderect(cursor.rect):
                if pygame.mouse.get_pressed()[0]:
                    self.cr = False

    def draw(self):
        if self.cr == False:
            win.blit(self.image, (0,0))

            '''
            pygame.draw.rect(win, (255, 255, 255), self.startrect, 5)
            '''
            if self.startchoice:
                win.blit(self.starttxt, (300, 400))

            if self.startchoice == False:
                win.blit(self.starttxtpressed, (300, 400))

            '''
            pygame.draw.rect(win, (255, 255, 255), self.creditrect, 5)
            '''
            if self.creditchoice:
                win.blit(self.credittxt, (300, 500))

            if self.creditchoice == False:
                win.blit(self.credittxtpressed, (300, 500))

            '''
            pygame.draw.rect(win, (255, 255, 255), self.quitrect, 5)
            '''
            if self.quitchoice:
                win.blit(self.quittxt, (290, 600))

            if self.quitchoice == False:
                win.blit(self.quittxtpressed, (305, 600))

        if self.cr:
            win.blit(self.creditimage, (0,0))

            win.blit(pygame.transform.scale(self.creditquitimage, (100, 100)), (0,0))

            win.blit(self.creditsr, (50, 300))
            win.blit(self.creditsr1, (50, 350))
            win.blit(self.creditsr2, (50, 400))
            win.blit(self.creditsr3, (50, 450))

class LevelsMap(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.chsound = pygame.mixer.Sound("ChoiceSound.wav")
        self.chschannel = pygame.mixer.Channel(19)

        self.chschannel.set_volume(0.3)
        
        self.image = pygame.image.load("tex\lvlmap_tex.png")

        self.quitbut = pygame.Rect(20, 680, 380, 80)
        self.quitchoice = True

        self.quittxt = pygame.image.load("tex\lvlmap_quit.png")

        self.quittxtpressed = pygame.image.load("tex\lvlmap_quit_pressed.png")

        self.lvl = 0

        self.lvlnumb = pygame.font.SysFont('Arial', 25)
        self.lvlnumbr = self.lvlnumb.render(" ", True,(255, 255, 255))

        self.lvlstatstxt = pygame.font.SysFont('Arial', 20)
        self.lvlstatstxtr = self.lvlstatstxt.render(" ", True,(255, 255, 255))

        self.lvl1complete = False
        self.lvl1rect = pygame.Rect(450, 540, 125, 200)
        self.lvl1icon_available = pygame.image.load("tex\lvl1\lvlmap_lvl1icon_available.png")
        self.lvl1icon_complete = pygame.image.load("tex\lvl1\lvlmap_lvl1icon_complete.png")
        self.lvl1stats = ["???", "???", "???", 0]
        
        self.lvl2complete = False
        self.lvl2rect = pygame.Rect(455, 320, 180, 160)
        self.lvl2icon_available = pygame.image.load("tex\lvl2\lvlmap_lvl2icon_available.png")
        self.lvl2icon_complete = pygame.image.load("tex\lvl2\lvlmap_lvl2icon_complete.png")
        self.lvl2stats = ["???", "???", "???", 0]
        
        self.lvl3complete = False
        self.lvl3rect = pygame.Rect(660, 500, 180, 160)
        self.lvl3icon_available = pygame.image.load("tex\lvl3\lvlmap_lvl3icon_available.png")
        self.lvl3icon_complete = pygame.image.load("tex\lvl3\lvlmap_lvl3icon_complete.png")
        self.lvl3stats = ["???", "???", "???", 0]
        
        self.lvl4complete = False
        self.lvl4rect = pygame.Rect(820, 340, 145, 150)
        self.lvl4icon_available = pygame.image.load("tex\lvl4\lvlmap_lvl4icon_available.png")
        self.lvl4icon_complete = pygame.image.load("tex\lvl4\lvlmap_lvl4icon_complete.png")
        self.lvl4stats = ["???", "???", "???", 0]
        
        self.lvl5complete = False
        self.lvl5rect = pygame.Rect(770, 180, 135, 100)
        self.lvl5icon_available = pygame.image.load("tex\lvl5\lvlmap_lvl5icon_available.png")
        self.lvl5icon_complete = pygame.image.load("tex\lvl5\lvlmap_lvl5icon_complete.png")
        self.lvl5stats = ["???", "???", "???", 0]
        
        self.lvl6complete = False
        self.lvl6rect = pygame.Rect(360, 130, 170, 130)
        self.lvl6icon_available = pygame.image.load("tex\lvl6\lvlmap_lvl6icon_available.png")
        self.lvl6icon_complete = pygame.image.load("tex\lvl6\lvlmap_lvl6icon_complete.png")
        self.lvl6stats = ["???", "???", "???", 0]
        
        self.lvl7complete = False
        self.lvl7rect = pygame.Rect(100, 130, 190, 160)
        self.lvl7icon_available = pygame.image.load("tex\lvl7\lvlmap_lvl7icon_available.png")
        self.lvl7icon_complete = pygame.image.load("tex\lvl7\lvlmap_lvl7icon_complete.png")
        self.lvl7stats = ["???", "???", "???", 0]

        self.onshop = False
        self.shoprect = pygame.Rect(200, 500, 150, 120)
        self.shopicon = pygame.image.load("tex\lvlmap_shopicon.png")

        self.comingsooncard = pygame.image.load("tex\lvlmap_comingsoon_card.png")

        self.lvlcompletioncard = pygame.image.load("tex\lvlmap_lvlcompletion_card.png")

        self.lvlcompletioncardflip = pygame.image.load("tex\lvlmap_lvlcompletion_card_flip.png")

        self.timeico = pygame.transform.scale(pygame.image.load("tex\game\TimeIcon.png"), (25, 25))
        self.moneyico = pygame.transform.scale(pygame.image.load("tex\game\MoneyIcon.png"), (25, 25))
        self.healthico = pygame.transform.scale(pygame.image.load("tex\game\healthicon.png"), (25, 25))
        self.resultico = pygame.transform.scale(pygame.image.load("tex\game\ResultIcon.png"), (30, 30))

    def col(self, cursor):
        if self.quitbut.colliderect(cursor.rect):
            if self.quitchoice:
                self.quitchoice = False
                self.chschannel.play(self.chsound)
            if pygame.mouse.get_pressed()[0]:
                self.lvl = -1

        if self.quitbut.colliderect(cursor.rect) == False:
            self.quitchoice = True
        
                
        if self.lvl1rect.colliderect(cursor.rect):
            if pygame.mouse.get_pressed()[0]:
                self.lvl = 1

        if self.lvl2rect.colliderect(cursor.rect):
            if self.lvl1complete:
                if pygame.mouse.get_pressed()[0]:
                    self.lvl = 2

        if self.lvl3rect.colliderect(cursor.rect):
            if self.lvl2complete:
                if pygame.mouse.get_pressed()[0]:
                    self.lvl = 3

        if self.lvl4rect.colliderect(cursor.rect):
            if self.lvl3complete:
                if pygame.mouse.get_pressed()[0]:
                    self.lvl = 4

        if self.lvl5rect.colliderect(cursor.rect):
            if self.lvl4complete:
                if pygame.mouse.get_pressed()[0]:
                    self.lvl = 5

        if self.lvl6rect.colliderect(cursor.rect):
            if self.lvl5complete:
                if pygame.mouse.get_pressed()[0]:
                    self.lvl = 6

        if self.lvl7rect.colliderect(cursor.rect):
            if self.lvl6complete:
                if pygame.mouse.get_pressed()[0]:
                    self.lvl = 7

    def draw(self):
        win.blit(self.image, (0,0))

        '''

        pygame.draw.rect(win, (255,0,0), self.quitbut, 5)
        '''
        if self.quitchoice:
            win.blit(self.quittxt, (20, 680))

        if self.quitchoice == False:
            win.blit(self.quittxtpressed, (20, 680))

        win.blit(self.shopicon, (0,0))

        if self.lvl1complete == False:
            win.blit(self.lvl1icon_available, (0,0))

        if self.lvl1complete:
            win.blit(self.lvl1icon_complete, (0,0))
            
            if self.lvl2complete == False:
                win.blit(self.lvl2icon_available, (0,0))

        if self.lvl2complete:
            win.blit(self.lvl2icon_complete, (0,0))
            
            if self.lvl3complete == False:
                win.blit(self.lvl3icon_available, (0,0))

        if self.lvl3complete:
            win.blit(self.lvl3icon_complete, (0,0))
            
            if self.lvl4complete == False:
                win.blit(self.lvl4icon_available, (0,0))

        if self.lvl4complete:
            win.blit(self.lvl4icon_complete, (0,0))
            
            if self.lvl5complete == False:
                win.blit(self.lvl5icon_available, (0,0))

        if self.lvl5complete:
            win.blit(self.lvl5icon_complete, (0,0))

        '''
            if self.lvl6complete == False:
                win.blit(self.lvl6icon_available, (0,0))

        if self.lvl6complete:
            win.blit(self.lvl6icon_complete, (0,0))
            
            if self.lvl7complete == False:
                win.blit(self.lvl7icon_available, (0,0))

        if self.lvl7complete:
            win.blit(self.lvl7icon_complete, (0,0))

        

        pygame.draw.rect(win, (255,0,0), self.lvl1rect, 5)

        pygame.draw.rect(win, (255,0,0), self.lvl2rect, 5)

        pygame.draw.rect(win, (255,0,0), self.lvl3rect, 5)

        pygame.draw.rect(win, (255,0,0), self.lvl4rect, 5)

        pygame.draw.rect(win, (255,0,0), self.lvl5rect, 5)

        pygame.draw.rect(win, (255,0,0), self.lvl6rect, 5)

        pygame.draw.rect(win, (255,0,0), self.lvl7rect, 5)

        pygame.draw.rect(win, (255,0,0), self.shoprect, 5)
        '''

    def carddraw(self, cursor):
        if self.lvl1rect.colliderect(cursor.rect):
            win.blit(self.lvlcompletioncard, (375, 420))

            self.lvlnumbr = self.lvlnumb.render("Уровень 1", True,(255, 255, 255))

            win.blit(self.lvlnumbr, (455, 423))

            for i in range(3):
                self.lvlstatstxtr = self.lvlstatstxt.render(str(self.lvl1stats[i]), True,(255, 255, 255))

                win.blit(self.lvlstatstxtr, (420 +81*i, 510))

            win.blit(self.timeico, (395, 505))
            win.blit(self.moneyico, (475, 505))
            win.blit(self.healthico, (556, 505))

            if self.lvl1stats[3] == 1:
                win.blit(self.resultico, (500, 460))

            if self.lvl1stats[3] == 2:
                win.blit(self.resultico, (485, 460))
                win.blit(self.resultico, (515, 460))

            if self.lvl1stats[3] == 3:
                win.blit(self.resultico, (455, 460))
                win.blit(self.resultico, (495, 460))
                win.blit(self.resultico, (535, 460))

            if self.lvl1stats[3] == 4:
                win.blit(self.resultico, (435, 460))
                win.blit(self.resultico, (475, 460))
                win.blit(self.resultico, (515, 460))
                win.blit(self.resultico, (555, 460))

            if self.lvl1stats[3] == 5:
                win.blit(self.resultico, (415, 460))
                win.blit(self.resultico, (455, 460))
                win.blit(self.resultico, (495, 460))
                win.blit(self.resultico, (535, 460))
                win.blit(self.resultico, (575, 460))
            
        if self.lvl2rect.colliderect(cursor.rect):
            win.blit(self.lvlcompletioncard, (400, 200))

            self.lvlnumbr = self.lvlnumb.render("Уровень 2", True,(255, 255, 255))

            win.blit(self.lvlnumbr, (480, 203))

            for i in range(3):
                self.lvlstatstxtr = self.lvlstatstxt.render(str(self.lvl2stats[i]), True,(255, 255, 255))

                win.blit(self.lvlstatstxtr, (445 +81*i, 290))

            win.blit(self.timeico, (420, 285))
            win.blit(self.moneyico, (500, 285))
            win.blit(self.healthico, (581, 285))

            if self.lvl2stats[3] == 1:
                win.blit(self.resultico, (525, 240))

            if self.lvl2stats[3] == 2:
                win.blit(self.resultico, (505, 240))
                win.blit(self.resultico, (540, 240))

            if self.lvl2stats[3] == 3:
                win.blit(self.resultico, (480, 240))
                win.blit(self.resultico, (520, 240))
                win.blit(self.resultico, (560, 240))

            if self.lvl2stats[3] == 4:
                win.blit(self.resultico, (460, 240))
                win.blit(self.resultico, (500, 240))
                win.blit(self.resultico, (540, 240))
                win.blit(self.resultico, (580, 240))

            if self.lvl2stats[3] == 5:
                win.blit(self.resultico, (440, 240))
                win.blit(self.resultico, (480, 240))
                win.blit(self.resultico, (520, 240))
                win.blit(self.resultico, (560, 240))
                win.blit(self.resultico, (600, 240))

        if self.lvl3rect.colliderect(cursor.rect):
            win.blit(self.lvlcompletioncard, (610, 380))

            self.lvlnumbr = self.lvlnumb.render("Уровень 3", True,(255, 255, 255))

            win.blit(self.lvlnumbr, (690, 383))

            for i in range(3):
                self.lvlstatstxtr = self.lvlstatstxt.render(str(self.lvl3stats[i]), True,(255, 255, 255))

                win.blit(self.lvlstatstxtr, (655 +81*i, 470))

            win.blit(self.timeico, (630, 465))
            win.blit(self.moneyico, (710, 465))
            win.blit(self.healthico, (791, 465))

            if self.lvl3stats[3] == 1:
                win.blit(self.resultico, (735, 420))

            if self.lvl3stats[3] == 2:
                win.blit(self.resultico, (720, 420))
                win.blit(self.resultico, (750, 420))

            if self.lvl3stats[3] == 3:
                win.blit(self.resultico, (690, 420))
                win.blit(self.resultico, (730, 420))
                win.blit(self.resultico, (770, 420))

            if self.lvl3stats[3] == 4:
                win.blit(self.resultico, (670, 420))
                win.blit(self.resultico, (710, 420))
                win.blit(self.resultico, (750, 420))
                win.blit(self.resultico, (790, 420))

            if self.lvl3stats[3] == 5:
                win.blit(self.resultico, (650, 420))
                win.blit(self.resultico, (690, 420))
                win.blit(self.resultico, (730, 420))
                win.blit(self.resultico, (770, 420))
                win.blit(self.resultico, (810, 420))

        if self.lvl4rect.colliderect(cursor.rect):
            win.blit(self.lvlcompletioncard, (710, 180))

            self.lvlnumbr = self.lvlnumb.render("Уровень 4", True,(255, 255, 255))

            win.blit(self.lvlnumbr, (790, 183))

            for i in range(3):
                self.lvlstatstxtr = self.lvlstatstxt.render(str(self.lvl4stats[i]), True,(255, 255, 255))

                win.blit(self.lvlstatstxtr, (755 +81*i, 270))

            win.blit(self.timeico, (730, 265))
            win.blit(self.moneyico, (810, 265))
            win.blit(self.healthico, (891, 265))

            if self.lvl4stats[3] == 1:
                win.blit(self.resultico, (835, 220))

            if self.lvl4stats[3] == 2:
                win.blit(self.resultico, (820, 220))
                win.blit(self.resultico, (850, 220))

            if self.lvl4stats[3] == 3:
                win.blit(self.resultico, (790, 220))
                win.blit(self.resultico, (830, 220))
                win.blit(self.resultico, (870, 220))

            if self.lvl4stats[3] == 4:
                win.blit(self.resultico, (770, 220))
                win.blit(self.resultico, (810, 220))
                win.blit(self.resultico, (850, 220))
                win.blit(self.resultico, (890, 220))

            if self.lvl4stats[3] == 5:
                win.blit(self.resultico, (750, 220))
                win.blit(self.resultico, (790, 220))
                win.blit(self.resultico, (830, 220))
                win.blit(self.resultico, (870, 220))
                win.blit(self.resultico, (910, 220))

        if self.lvl5rect.colliderect(cursor.rect):
            win.blit(self.lvlcompletioncard, (690, 20))

            self.lvlnumbr = self.lvlnumb.render("Уровень 5", True,(255, 255, 255))

            win.blit(self.lvlnumbr, (770, 23))

            for i in range(3):
                self.lvlstatstxtr = self.lvlstatstxt.render(str(self.lvl5stats[i]), True,(255, 255, 255))

                win.blit(self.lvlstatstxtr, (735 +81*i, 110))

            win.blit(self.timeico, (710, 105))
            win.blit(self.moneyico, (790, 105))
            win.blit(self.healthico, (871, 105))

            if self.lvl5stats[3] == 1:
                win.blit(self.resultico, (815, 60))

            if self.lvl5stats[3] == 2:
                win.blit(self.resultico, (800, 60))
                win.blit(self.resultico, (830, 60))

            if self.lvl5stats[3] == 3:
                win.blit(self.resultico, (770, 60))
                win.blit(self.resultico, (810, 60))
                win.blit(self.resultico, (850, 60))

            if self.lvl5stats[3] == 4:
                win.blit(self.resultico, (750, 60))
                win.blit(self.resultico, (790, 60))
                win.blit(self.resultico, (830, 60))
                win.blit(self.resultico, (870, 60))

            if self.lvl5stats[3] == 5:
                win.blit(self.resultico, (730, 60))
                win.blit(self.resultico, (770, 60))
                win.blit(self.resultico, (810, 60))
                win.blit(self.resultico, (850, 60))
                win.blit(self.resultico, (890, 60))

        if self.lvl6rect.colliderect(cursor.rect):
            win.blit(self.comingsooncard, (315, 70))
            
            '''
            win.blit(self.lvlcompletioncardflip, (315, 220))

            self.lvlnumbr = self.lvlnumb.render("Уровень 6", True,(255, 255, 255))

            win.blit(self.lvlnumbr, (395, 248))

            for i in range(3):
                self.lvlstatstxtr = self.lvlstatstxt.render(str(self.lvl6stats[i]), True,(255, 255, 255))

                win.blit(self.lvlstatstxtr, (360 +81*i, 335))

            win.blit(self.timeico, (335, 330))
            win.blit(self.moneyico, (415, 330))
            win.blit(self.healthico, (496, 330))

            if self.lvl6stats[3] == 1:
                win.blit(self.resultico, (440, 285))

            if self.lvl6stats[3] == 2:
                win.blit(self.resultico, (425, 285))
                win.blit(self.resultico, (455, 285))

            if self.lvl6stats[3] == 3:
                win.blit(self.resultico, (395, 285))
                win.blit(self.resultico, (435, 285))
                win.blit(self.resultico, (475, 285))

            if self.lvl6stats[3] == 4:
                win.blit(self.resultico, (375, 285))
                win.blit(self.resultico, (415, 285))
                win.blit(self.resultico, (455, 285))
                win.blit(self.resultico, (495, 285))

            if self.lvl6stats[3] == 5:
                win.blit(self.resultico, (355, 285))
                win.blit(self.resultico, (395, 285))
                win.blit(self.resultico, (435, 285))
                win.blit(self.resultico, (475, 285))
                win.blit(self.resultico, (515, 285))

            '''

        if self.lvl7rect.colliderect(cursor.rect):
            win.blit(self.comingsooncard, (60, 100))
            
            '''
            win.blit(self.lvlcompletioncardflip, (60, 250))

            self.lvlnumbr = self.lvlnumb.render("Уровень 7", True,(255, 255, 255))

            win.blit(self.lvlnumbr, (140, 278))

            for i in range(3):
                self.lvlstatstxtr = self.lvlstatstxt.render(str(self.lvl7stats[i]), True,(255, 255, 255))

                win.blit(self.lvlstatstxtr, (105 +81*i, 365))

            win.blit(self.timeico, (80, 360))
            win.blit(self.moneyico, (160, 360))
            win.blit(self.healthico, (241, 360))

            if self.lvl7stats[3] == 1:
                win.blit(self.resultico, (185, 315))

            if self.lvl7stats[3] == 2:
                win.blit(self.resultico, (170, 315))
                win.blit(self.resultico, (200, 315))

            if self.lvl7stats[3] == 3:
                win.blit(self.resultico, (140, 315))
                win.blit(self.resultico, (180, 315))
                win.blit(self.resultico, (220, 315))

            if self.lvl7stats[3] == 4:
                win.blit(self.resultico, (120, 315))
                win.blit(self.resultico, (160, 315))
                win.blit(self.resultico, (200, 315))
                win.blit(self.resultico, (240, 315))

            if self.lvl7stats[3] == 5:
                win.blit(self.resultico, (100, 315))
                win.blit(self.resultico, (140, 315))
                win.blit(self.resultico, (180, 315))
                win.blit(self.resultico, (220, 315))
                win.blit(self.resultico, (260, 315))

            '''

        if self.shoprect.colliderect(cursor.rect):
            win.blit(self.comingsooncard, (135, 430))



class SoundControl:
    def __init__(self):
        self.sounds = True
        self.music = True

        self.a = 1

        self.b = 1

        self.mix = pygame.mixer.music
        
        self.mix.load("MenuMusic.wav")

        pygame.mixer.music.set_volume(0.2)

    def menubgmus(self):
        if self.a == 1:
            self.a = 0
            self.mix.stop()
            self.mix.load("MenuMusic.wav")
            
        if self.mix.get_busy() == False:
            self.mix.play()

    def backgroundmus(self, alert, pause):
        if self.b == 1:
            self.b = 0
            self.mix.stop()

        if alert.activeonce == -1:
            self.mix.stop()
            if self.mix.get_busy() == False:
                self.mix.load("playingMusic.wav")
            
        if self.mix.get_busy() == False:
            self.mix.play()
                
        if alert.activeonce == 1:
            self.mix.stop()
            if self.mix.get_busy() == False:
                self.mix.load("AlertMusic.wav")

        if pause.once == 1:
            self.mix.pause()
            for i in range(20):
                pygame.mixer.Channel(i).pause()

        if pause.once == -1:
            self.mix.unpause()
            for i in range(20):
                pygame.mixer.Channel(i).unpause()

    def mute(self, sound, music):
        if music.icooffdraw:
            self.mix.set_volume(0)

        if music.icooffdraw == False:
            self.mix.set_volume(0.2)

        if sound.icooffdraw:
            self.sounds = False
            for i in range(20):
                pygame.mixer.Channel(i).stop()

        if sound.icooffdraw == False:
            self.sounds = True
    
    def update(self, alert, pause, sound, music):
        self.mute(sound, music)
        self.backgroundmus(alert, pause)

class Alert:
    def __init__(self):
        self.sound = pygame.mixer.Sound("AlertSound.wav")
        self.schannel = pygame.mixer.Channel(0)

        self.schannel.set_volume(0.2)
        
        self.active = False
        self.activeonce = 1

        self.image1 = pygame.image.load("tex\game\SirenFrames\SirenFrame1.png")
        self.image2 = pygame.image.load("tex\game\SirenFrames\SirenFrame2.png")
        self.image3 = pygame.image.load("tex\game\SirenFrames\SirenFrame3.png")
        self.image4 = pygame.image.load("tex\game\SirenFrames\SirenFrame4.png")
        self.image5 = pygame.image.load("tex\game\SirenFrames\SirenFrame5.png")
        self.image6 = pygame.image.load("tex\game\SirenFrames\SirenFrame6.png")
        self.image7 = pygame.image.load("tex\game\SirenFrames\SirenFrame7.png")
        self.image8 = pygame.image.load("tex\game\SirenFrames\SirenFrame8.png")

        self.images = [self.image1, self.image2, self.image3, self.image4, self.image5, self.image6, self.image7, self.image8]
        self.imc = 8

        self.count = 0
        
        self.secs = 19
        
        self.secstxt = pygame.font.SysFont('Arial', 35)
        self.secstxtr = self.secstxt.render(str(self.secs), True,(155, 0, 0))
        
        self.misecs = 99

        self.misecstxt = pygame.font.SysFont('Arial', 35)
        self.misecstxtr = self.misecstxt.render(": "+str(self.misecs), True,(155, 0, 0))

        self.once = True

    def playsound(self, soundcontrol):
        if self.active:
            if soundcontrol.sounds:
                if self.schannel.get_busy() == False:
                    self.schannel.play(self.sound)

        else:
            self.schannel.stop()

    def counting(self):
        if self.active:
            if self.activeonce<2:
                self.activeonce +=1
            self.misecs -= 1
            if self.misecs == 0:
                if self.secs == 0:
                    self.active = False
                    self.secs =19
                    self.misecs = 99
                    
                elif self.secs >0:
                    self.misecs = 99
                    self.secs -=1

        if self.active == False:
            if self.activeonce > -2:
                self.activeonce -=1

    def healthkill(self, health):
        if self.active:
            if self.once:
                health.health -= 1
                
                self.once = False

        else:
            self.once = True
                
    def draw(self):
        self.secstxtr = self.secstxt.render(str(self.secs), True,(155, 0, 0))
        self.misecstxtr = self.misecstxt.render(": "+str(self.misecs), True,(155, 0, 0))
        
        if self.active:
            win.blit(self.images[self.imc//8], (25, 75))
            self.imc += 1

            if self.imc == 64:
                self.imc = 1

            win.blit(self.secstxtr, (20, 180))

            win.blit(self.misecstxtr, (70, 180))

    def update(self):
        self.counting()

class AlertWall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y
        self.w = 10
        self.h = 94

        self.ys = 0

        self.rect = pygame.Rect(self.x, self.ys, self.w, self.h)
        self.image = pygame.image.load("tex\game\AlertWallImage.png")

    def comeup(self, alert):
        if alert.active:
            if self.ys <100:
                self.ys += 1

        if alert.active == False:
            if self.ys> 0:
                self.ys -= 1

    def draw(self):
        pygame.draw.rect(win, (30, 30, 30), (self.x, self.y, 2, self.ys - 6))

        pygame.draw.rect(win, (30, 30, 30), (self.x+3, self.y, 2, self.ys - 6))

        pygame.draw.rect(win, (30, 30, 30), (self.x+6, self.y, 2, self.ys - 6))

class Hud:
    def __init__(self):
        self.image = pygame.image.load("tex\game\BarImage.png")

    def draw(self):
        win.blit(self.image, (0,0))

class Health:
    def __init__(self):
        self.x = 10
        self.y = 5

        self.ima = pygame.image.load("tex\game\healthicon.png")
        self.image = pygame.transform.scale(self.ima, (55,55))

        self.health = 3
        self.c = 0

    def draw(self):
        if self.health == 3:
            for i in range(3):
                self.c = i*70
                win.blit(self.image, (self.x+self.c, self.y))

        if self.health == 2:
            for i in range(2):
                self.c = i*70
                win.blit(self.image, (self.x+self.c, self.y))

        if self.health == 1:
            win.blit(self.image, (self.x, self.y))

        self.c = 0

        

class Time:
    def __init__(self):
        self.iimage = pygame.transform.scale(pygame.image.load("tex\game\TimeIcon.png"), (50, 50))

        self.tx = 245
        self.tw = 155

        self.timage = 0
        self.timerect = pygame.Rect(self.tx, 10, self.tw, 45)

        self.c = 0
        self.time = 0

        self.timetxt = pygame.font.SysFont('Arial', 35)
        self.timetxtr = self.timetxt.render(str(self.time), True,(0, 0, 0))

    def count(self):
        self.c += 1
        if self.c == 125:
            self.c = 0
            self.time += 1

    def draw(self):
        self.timetxtr = self.timetxt.render(str(self.time), True,(0, 0, 0))
        pygame.draw.rect(win, (205, 205, 100), self.timerect)
        
        win.blit(self.iimage, (247, 7))

        win.blit(self.timetxtr, (310, 15))

class Moneycount(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.iimage = pygame.transform.scale(pygame.image.load("tex\game\MoneyIcon.png"), (50, 50))

        self.mx = 440
        self.mw = 160

        self.money = 0

        self.mimage = 0
        self.moneyrect = pygame.Rect(self.mx, 10, self.mw, 45)

        self.rect = pygame.Rect(self.mx+50, 0, self.mw-100, 30)

        self.moneytxt = pygame.font.SysFont('Arial', 35)
        self.moneytxtr = self.moneytxt.render(str(self.money), True,(0, 0, 0))

    def moneyadd(self, player):
        self.money = player.money

    def draw(self):
        self.moneytxtr = self.moneytxt.render(str(self.money), True,(0, 0, 0))
        pygame.draw.rect(win, (100, 255, 100), self.moneyrect)
        
        win.blit(self.iimage, (442, 7))

        win.blit(self.moneytxtr, (510, 15))

class Sounds(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.x = 905
        self.y = 15
        self.wh = 35

        self.rect = pygame.Rect(self.x, self.y, self.wh, self.wh)
        self.image = pygame.transform.scale(pygame.image.load("tex\game\SoundsIcon.png"), (45, 45))

        self.icooffimage = pygame.transform.scale(pygame.image.load("tex\game\OffIcon.png"), (45, 45))
        self.icooffdraw = False

        self.click = False

        self.choice = False

    def col(self, cursor):
        if self.rect.colliderect(cursor.rect):
                
            if pygame.mouse.get_pressed()[0]:
                if self.click == False:
                    if self.icooffdraw == False:
                        self.icooffdraw = True

                    elif self.icooffdraw == True:
                        self.icooffdraw = False
                self.click = True

            if pygame.mouse.get_pressed()[0] == False:
                self.click = False

    def draw(self):
        win.blit(self.image, (902, 10))

        if self.icooffdraw:
            win.blit(self.icooffimage, (900, 10))

class Music(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.x = 955
        self.y = 15
        self.wh = 35

        self.rect = pygame.Rect(self.x, self.y, self.wh, self.wh)
        self.image = pygame.transform.scale(pygame.image.load("tex\game\MusicIcon.png"), (35, 35))

        self.icooffimage = pygame.transform.scale(pygame.image.load("tex\game\OffIcon.png"), (45, 45))
        self.icooffdraw = False

        self.click = False

    def col(self, cursor):
        if self.rect.colliderect(cursor.rect):
            if pygame.mouse.get_pressed()[0]:
                if self.click == False:
                    if self.icooffdraw == False:
                        self.icooffdraw = True

                    elif self.icooffdraw == True:
                        self.icooffdraw = False
                self.click = True

            if pygame.mouse.get_pressed()[0] == False:
                self.click = False

    def draw(self):
        win.blit(self.image, (955, 15))

        if self.icooffdraw:
            win.blit(self.icooffimage, (950, 10))

class Retry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.x = 805
        self.y = 15
        self.wh = 35

        self.rect = pygame.Rect(self.x, self.y, self.wh, self.wh)
        self.image = pygame.transform.scale(pygame.image.load("tex\game\RetryIcon.png"), (35, 35))

        self.retry = False

    def use(self, cursor):
        if self.rect.colliderect(cursor.rect):
            if pygame.mouse.get_pressed()[0]:
                self.retry = True

        if pygame.key.get_pressed()[pygame.K_r]:
            self.retry = True

    def draw(self):
        win.blit(self.image, (805, 15))

class Pause(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sound = pygame.mixer.Sound("Pause.wav")
        self.schannel = pygame.mixer.Channel(1)

        self.schannel.set_volume(0.6)

        
        self.chsound = pygame.mixer.Sound("ChoiceSound.wav")
        self.chschannel = pygame.mixer.Channel(19)

        self.chschannel.set_volume(0.3)
        
        self.x = 855
        self.y = 15
        self.wh = 35

        self.rect = pygame.Rect(self.x, self.y, self.wh, self.wh)
        self.image = pygame.transform.scale(pygame.image.load("tex\game\PauseIcon.png"), (35, 35))

        self.prect = pygame.Rect(250, 265, 500, 450)
        self.pimage = pygame.image.load("tex\game\PauseImage.png")

        self.maintxt = pygame.image.load("tex\game\PauseTxt.png")

        self.crect = pygame.Rect(300, 365, 400, 80)

        self.continuetxt = pygame.image.load("tex\game\PauseContinue.png")

        self.continuetxtpressed = pygame.image.load("tex\game\PauseContinuePressed.png")

        self.qrect = pygame.Rect(300, 515, 400, 70)

        self.quittxt = pygame.image.load("tex\game\PauseQuit.png")

        self.quittxtpressed = pygame.image.load("tex\game\PauseQuitPressed.png")

        self.pause = False

        self.once = 0

        self.achoice = False

        self.bchoice = False

        self.lvl = 1

    def playsound(self, soundcontrol):
        if self.once == 1:
            if soundcontrol.sounds:
                self.schannel.play(self.sound)

    def use(self, cursor):
        if self.rect.colliderect(cursor.rect):
            if pygame.mouse.get_pressed()[0]:
                self.pause = True
                if self.once == -2:
                    self.once = 1
                
                elif self.once < 1:
                    self.once += 1

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.pause = True
            if self.once == -2:
                self.once = 1

            elif self.once < 1:
                self.once += 1

    def onpause(self, cursor, soundcontrol):
        if self.pause == True:
            if self.crect.colliderect(cursor.rect):
                if soundcontrol.sounds:
                    if self.achoice:
                        self.chschannel.play(self.chsound)
                        self.achoice = False
                    
                if pygame.mouse.get_pressed()[0]:
                    self.pause = False
                    if self.once > -2:
                        self.once -= 1

            if self.crect.colliderect(cursor.rect) == False:
                self.achoice = True

            if self.qrect.colliderect(cursor.rect):
                if soundcontrol.sounds:
                    if self.bchoice:
                        self.chschannel.play(self.chsound)
                        self.bchoice = False
                    
                if pygame.mouse.get_pressed()[0]:
                    self.lvl = 0

            if self.qrect.colliderect(cursor.rect) == False:
                self.bchoice = True

    def draw(self):
        win.blit(self.image, (855, 15))

    def windraw(self):
        if self.pause:
            win.blit(self.pimage, (200, 215))

            win.blit(self.maintxt, (300, 150))

            '''

            pygame.draw.rect(win, (255, 255, 255), self.crect, 5)

            '''
            if self.achoice:
                win.blit(self.continuetxt, (300, 365))

            if self.achoice == False:
                win.blit(self.continuetxtpressed, (295, 369))

            '''

            pygame.draw.rect(win, (255, 255, 255), self.qrect, 5)

            '''
            if self.bchoice:
                win.blit(self.quittxt, (290, 515))

            if self.bchoice == False:
                win.blit(self.quittxtpressed, (300, 515))

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.xy = pygame.mouse.get_pos()
        self.rect = pygame.Rect(int(self.xy[0]), int(self.xy[1]), 1, 1)

    def draw(self):
        pygame.draw.rect(win, (0,0,150), self.rect)

    def update(self):
        self.xy = pygame.mouse.get_pos()
        self.rect = pygame.Rect(int(self.xy[0]), int(self.xy[1]), 1, 1)

class PlaceOut(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()   

        self.x = x
        self.y = y
        self.w = 30
        self.h = 94

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.image = pygame.image.load("tex\game\PlaceOutImage.png")

        self.active = False

        self.ready = False

    def col(self, player):
        if self.active:
            if self.rect.colliderect(player.rect):
                self.ready = True

    def draw(self):
        if self.active and self.ready == False:
            win.blit(self.image, (self.x, self.y))

    def update(self, player):
        self.col(player)

class RobMission(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.dsound = pygame.mixer.Sound("RobMissionDoing.wav")
        self.csound = pygame.mixer.Sound("RobMissionComplete.wav")
        
        self.schannel = pygame.mixer.Channel(18)

        self.schannel.set_volume(0.8)

        self.x = x
        self.y = y
        self.w = 100
        self.h = 94

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.image = pygame.image.load("tex\game\RobPlace.png")

        self.count = 0

        self.ready = False

        self.attention = False

    def rob(self, player, alert):
        self.attention = False
        if self.ready == False:
            if alert.active == False:
                if self.rect.colliderect(player.rect):
                    if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                        player.using = True
                        
                        if player.moving:
                            self.count = 0
                            player.using = False
                            
                        self.count +=1

                        if player.moving == False:
                            if self.schannel.get_busy() == False:
                                self.schannel.play(self.dsound)
                        
                        if self.count == 400:
                            self.ready = True
                            self.schannel.stop()
                            
                            self.schannel.play(self.csound)

                    else:
                        self.count = 0
                        
                        self.schannel.stop()

                else:
                    self.count = 0

                    self.schannel.stop()

            if alert.active:
                if self.rect.colliderect(player.rect):
                    if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                        self.attention = True

    def draw(self):
        if self.ready == False:
            win.blit(self.image, (self.x, self.y))

            if self.count>0:
                pygame.draw.rect(win, (0,0,0), (self.x+25, self.y +10, 50, 30))
                pygame.draw.rect(win, (0,255,0), (self.x+25, self.y +10, self.count//8, 30))

            if self.attention:
                pygame.draw.rect(win, (255,0,0), (self.x + 30, self.y +10, 40, 30))

    def update(self, player, alert):
        self.rob(player, alert)
        
class NpcHTBX(pygame.sprite.Sprite):
    def __init__(self, wallL, wallR):
        super().__init__()

        self.asound = pygame.mixer.Sound("NpcAttention.wav")
        self.aschannel = pygame.mixer.Channel(10)

        self.aschannel.set_volume(0.6)

        self.ssound = pygame.mixer.Sound("NpcAttentionAlert.wav")
        self.sschannel = pygame.mixer.Channel(10)

        self.shsound = pygame.mixer.Sound("NpcShooting.wav")

        self.ansound = pygame.mixer.Sound("NpcDashing.wav")

        self.sschannel.set_volume(0.3)

        self.lx = wallL.x +10
        self.rx = wallR.x 
        self.h = 30

        self.xs = 0
        self.ys = 0

        self.rect = 0

        self.waittillalarm = 0

        self.alarm = False

        self.attention = False

        self.stoppednpc = 0

        self.canshoot = False

        self.candash = False

        self.c = 0

        self.attentionicon = pygame.transform.scale(pygame.image.load("tex\game\AttentionIcon.png"), (30, 40))

        self.alerticon = pygame.image.load("tex\game\AlertIcon.png")

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.alarm == False:
                self.c = 1
                if self.waittillalarm == 1:
                    self.aschannel.play(self.asound)

            if self.alarm:
                if self.attention:
                    if self.stoppednpc == False:
                        if self.candash:
                            if self.candash:
                                if self.c == 1:
                                    self.c = 0
                                    self.sschannel.play(self.ansound)
                                    
                        else:
                            if self.sschannel.get_busy() == False:
                                self.sschannel.play(self.ssound)

                if self.attention == False:
                    self.c = 1

    def detection(self, npc, player, alert):
        self.candash = npc.candash

        self.canshoot = npc.canshoot
        
        npc.attention = False
        self.attention = False
        self.stoppednpc = npc.stopped
        
        if alert.active == False:
            npc.alert = False
            self.alarm = False

        if alert.active:
            self.alarm = True
            if npc.stopped == False:
                npc.alert = True

        self.xs = npc.x+15
        self.ys = npc.y- 30
            
        if self.rect.colliderect(player.rect) and player.active and player.hidden == False and player.visible:
            npc.attention = True
            self.attention = True
            
            if alert.active == False:
                if npc.stopped == False:

                    self.waittillalarm += 1

                    if self.waittillalarm >170:
                        alert.active = True
                        self.waittillalarm = 0

            if alert.active:
                if npc.stopped == False:
                    alert.secs = 19
                    alert.misecs = 99

        else:
            self.waittillalarm = 0

    def move(self, npc):
        if npc.left == 1:
            self.rect = pygame.Rect(self.lx, npc.y, npc.x - self.lx, self.h)

        if npc.right == 1:
            self.rect = pygame.Rect(npc.x +50, npc.y, self.rx - npc.x-50 , self.h)

    def draw(self):
        '''
        pygame.draw.rect(win, (255, 0, 0), self.rect, 5)
        '''
        
        if self.stoppednpc == False:
            if self.alarm and self.attention:
                win.blit(self.alerticon, (self.xs-5, self.ys-35))
            
            elif self.waittillalarm>0 or self.alarm:
                win.blit(self.attentionicon, (self.xs-5, self.ys-35))

    def update(self, npc, player, alert):
        self.move(npc)
        self.detection(npc, player, alert)

class Npc(pygame.sprite.Sprite):
    def __init__(self, x, y, wallL, wallR, mode):
        super().__init__()

        self.sound = pygame.mixer.Sound("NpcDamage.wav")
        self.schannel = pygame.mixer.Channel(11)

        self.schannel.set_volume(0.6)

        self.x = x
        self.y = y
        self.w = 50
        self.h = 60

        self.imageidle = pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcIdle.png"), (self.w-22, self.h+20))

        self.imagegoright1 = pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight1.png"), (self.w-15, self.h+20))
        self.imagegoright2 = pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight2.png"), (self.w-15, self.h+20))
        self.imagegoright3 = pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight3.png"), (self.w-15, self.h+20))
        self.imagegoright4 = pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight4.png"), (self.w-15, self.h+20))
        self.imagegoright5 = pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight5.png"), (self.w-15, self.h+20))
        self.imagegoright6 = pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight6.png"), (self.w-15, self.h+20))
        self.imagegoright7 = pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight7.png"), (self.w-15, self.h+20))
        self.imagegoright8 = pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight8.png"), (self.w-15, self.h+20))

        self.imagegorightframes = [self.imagegoright1, self.imagegoright2, self.imagegoright3, self.imagegoright4, self.imagegoright5, self.imagegoright6, self.imagegoright7, self.imagegoright8]
        self.imagegorightc = 0

        self.imagegoleft1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight1.png"), (self.w-15, self.h+20)), True, False)
        self.imagegoleft2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight2.png"), (self.w-15, self.h+20)), True, False)
        self.imagegoleft3 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight3.png"), (self.w-15, self.h+20)), True, False)
        self.imagegoleft4 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight4.png"), (self.w-15, self.h+20)), True, False)
        self.imagegoleft5 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight5.png"), (self.w-15, self.h+20)), True, False)
        self.imagegoleft6 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight6.png"), (self.w-15, self.h+20)), True, False)
        self.imagegoleft7 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight7.png"), (self.w-15, self.h+20)), True, False)
        self.imagegoleft8 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/Npc/NpcGoRight8.png"), (self.w-15, self.h+20)), True, False)

        self.imagegoleftframes = [self.imagegoleft1, self.imagegoleft2, self.imagegoleft3, self.imagegoleft4, self.imagegoleft5, self.imagegoleft6, self.imagegoleft7, self.imagegoleft8]
        self.imagegoleftc = 0

        self.imagestopped = pygame.image.load("tex/game/Npc/NpcStopped.png")

        

        self.shootimageidle = pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcIdle.png"), (self.w-22, self.h+20))

        self.shootimageshooting = pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcShooting.png"), (self.w, self.h+20))

        self.shootimagegoright1 = pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight1.png"), (self.w-15, self.h+20))
        self.shootimagegoright2 = pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight2.png"), (self.w-15, self.h+20))
        self.shootimagegoright3 = pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight3.png"), (self.w-15, self.h+20))
        self.shootimagegoright4 = pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight4.png"), (self.w-15, self.h+20))
        self.shootimagegoright5 = pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight5.png"), (self.w-15, self.h+20))
        self.shootimagegoright6 = pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight6.png"), (self.w-15, self.h+20))
        self.shootimagegoright7 = pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight7.png"), (self.w-15, self.h+20))
        self.shootimagegoright8 = pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight8.png"), (self.w-15, self.h+20))

        self.shootimagegorightframes = [self.shootimagegoright1, self.shootimagegoright2, self.shootimagegoright3, self.shootimagegoright4, self.shootimagegoright5, self.shootimagegoright6, self.shootimagegoright7, self.shootimagegoright8]
        self.shootimagegorightc = 0

        self.shootimagegoleft1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight1.png"), (self.w-15, self.h+20)), True, False)
        self.shootimagegoleft2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight2.png"), (self.w-15, self.h+20)), True, False)
        self.shootimagegoleft3 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight3.png"), (self.w-15, self.h+20)), True, False)
        self.shootimagegoleft4 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight4.png"), (self.w-15, self.h+20)), True, False)
        self.shootimagegoleft5 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight5.png"), (self.w-15, self.h+20)), True, False)
        self.shootimagegoleft6 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight6.png"), (self.w-15, self.h+20)), True, False)
        self.shootimagegoleft7 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight7.png"), (self.w-15, self.h+20)), True, False)
        self.shootimagegoleft8 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCanshoot/NpcGoRight8.png"), (self.w-15, self.h+20)), True, False)

        self.shootimagegoleftframes = [self.shootimagegoleft1, self.shootimagegoleft2, self.shootimagegoleft3, self.shootimagegoleft4, self.shootimagegoleft5, self.shootimagegoleft6, self.shootimagegoleft7, self.shootimagegoleft8]
        self.shootimagegoleftc = 0

        self.shootimagestopped = pygame.image.load("tex/game/NpcCanshoot/NpcStopped.png")



        

        self.dashimageidle = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcIdle.png"), (self.w-22, self.h+20))

        self.dashimagedashing = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcDashAttention.png"), (self.w, self.h+20))

        self.dashimagegoright1 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight1.png"), (self.w-15, self.h+20))
        self.dashimagegoright2 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight2.png"), (self.w-15, self.h+20))
        self.dashimagegoright3 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight3.png"), (self.w-15, self.h+20))
        self.dashimagegoright4 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight4.png"), (self.w-15, self.h+20))
        self.dashimagegoright5 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight5.png"), (self.w-15, self.h+20))
        self.dashimagegoright6 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight6.png"), (self.w-15, self.h+20))
        self.dashimagegoright7 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight7.png"), (self.w-15, self.h+20))
        self.dashimagegoright8 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight8.png"), (self.w-15, self.h+20))

        self.dashimagegorightframes = [self.dashimagegoright1, self.dashimagegoright2, self.dashimagegoright3, self.dashimagegoright4, self.dashimagegoright5, self.dashimagegoright6, self.dashimagegoright7, self.dashimagegoright8]
        self.dashimagegorightc = 0

        self.dashimagegoleft1 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight1.png"), (self.w-15, self.h+20)), True, False)
        self.dashimagegoleft2 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight2.png"), (self.w-15, self.h+20)), True, False)
        self.dashimagegoleft3 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight3.png"), (self.w-15, self.h+20)), True, False)
        self.dashimagegoleft4 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight4.png"), (self.w-15, self.h+20)), True, False)
        self.dashimagegoleft5 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight5.png"), (self.w-15, self.h+20)), True, False)
        self.dashimagegoleft6 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight6.png"), (self.w-15, self.h+20)), True, False)
        self.dashimagegoleft7 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight7.png"), (self.w-15, self.h+20)), True, False)
        self.dashimagegoleft8 = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcGoRight8.png"), (self.w-15, self.h+20)), True, False)

        self.dashimagegoleftframes = [self.dashimagegoleft1, self.dashimagegoleft2, self.dashimagegoleft3, self.dashimagegoleft4, self.dashimagegoleft5, self.dashimagegoleft6, self.dashimagegoleft7, self.dashimagegoleft8]
        self.dashimagegoleftc = 0

        self.dashimagestopped = pygame.image.load("tex/game/NpcCandash/NpcStopped.png")

        self.dashweaponimageright1 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcDashing1.png"), (self.w-15, self.h+20))
        self.dashweaponimageright2 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcDashing2.png"), (self.w-15, self.h+20))
        self.dashweaponimageright3 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcDashing3.png"), (self.w-15, self.h+20))
        self.dashweaponimageright4 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcDashing4.png"), (self.w-15, self.h+20))
        self.dashweaponimageright5 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcDashing5.png"), (self.w-15, self.h+20))
        self.dashweaponimageright6 = pygame.transform.scale(pygame.image.load("tex/game/NpcCandash/NpcDashing6.png"), (self.w-15, self.h+20))

        self.dashweaponimagerightframes = [self.dashweaponimageright1, self.dashweaponimageright2, self.dashweaponimageright3, self.dashweaponimageright4, self.dashweaponimageright5, self.dashweaponimageright6]
        self.dashweaponimagerightc = 0

        self.dashweaponimageleft1 = pygame.transform.flip(self.dashweaponimageright1, True, False)
        self.dashweaponimageleft2 = pygame.transform.flip(self.dashweaponimageright2, True, False)
        self.dashweaponimageleft3 = pygame.transform.flip(self.dashweaponimageright3, True, False)
        self.dashweaponimageleft4 = pygame.transform.flip(self.dashweaponimageright4, True, False)
        self.dashweaponimageleft5 = pygame.transform.flip(self.dashweaponimageright5, True, False)
        self.dashweaponimageleft6 = pygame.transform.flip(self.dashweaponimageright6, True, False)

        self.dashweaponimageleftframes = [self.dashweaponimageleft1, self.dashweaponimageleft2, self.dashweaponimageleft3, self.dashweaponimageleft4, self.dashweaponimageleft5, self.dashweaponimageleft6]
        self.dashweaponimageleftc = 0

        self.cangrabmoney = True

        self.alert = False

        self.mode = mode
        
        self.canshoot = False
        self.shooting = False
        
        self.candash = False
        self.dashing = False
        

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.image = 0

        self.borderL = wallL.x + 10
        self.borderR = wallR.x - 50

        self.f1 = 1
        self.f2 = 0

        self.left = 1
        self.mid = False
        self.midc = 0
        self.right = 0

        self.stopped = False
        self.stoppedc = 0

        self.attention = False

        self.alertc = 0

        self.moneycatch = False

        self.moneyimage = pygame.transform.scale(pygame.image.load("tex\game\MoneyIcon.png"), (50, 50))

        self.mc = 0

        self.mx = self.x+80

        self.my = self.y

        self.sp = 1

        self.icorect = pygame.Rect(self.mx, self.my, 50, 50)

        self.moneycame = False

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.stoppedc == 1:
                self.schannel.play(self.sound, 0, 400)

    def checkmode(self):
        if self.mode == 1:
            self.canshoot = True

        elif self.mode == 2:
            self.candash = True

    def inactive(self):
        if self.stopped:
        
            self.stoppedc += 1
            if self.stoppedc == 5000:
                self.stopped = False

    def counter(self):
        if self.alert == False:
            if self.f1 ==1:
                self.f1 = 0
                self.f2 = 1

            elif self.f2 == 1:
                self.f2 = 0
                self.f1 = 1

        if self.alert:
            self.alertc += 1

            if self.alertc == 50:
                self.alertc = 0
                if self.attention == False:
                    if self.right == 1:
                        self.right = 0
                        self.left = 1

                    elif self.left == 1:
                        self.left = 0
                        self.right = 1

                    elif self.mid:
                        self.mid = False
                        self.midc = 0
                        self.right = 1
                        self.left = 0

    def move(self):
        self.moving = False
        if self.alert == False:
            if self.stopped == False:
                if self.attention == False:
                    self.moving = True
                    if self.left== 1:
                        if self.x > self.borderL:
                            if self.f2 == 1:
                                self.x -= 1

                        if self.x == self.borderL:
                            self.mid = True
                            self.left = 2
                            self.right = 0

                    if self.mid:
                        self.midc += 1
                        if self.midc == 200:
                            self.midc = 0
                            self.mid = False
                            if self.right == 0:
                                self.right = 1

                            if self.left == 0:
                                self.left = 1

                    if self.right == 1:
                        if self.x < self.borderR:
                            if self.f2 == 1:
                                self.x += 1

                        if self.x == self.borderR:
                            self.mid = True
                            self.right = 2
                            self.left = 0

        if self.alert:
            self.dashing = False
            if self.stopped == False:
                if self.attention:
                    if self.canshoot:
                        self.shooting = True

                    if self.candash:
                        self.dashing = True

    def draw(self):
        if self.stopped == False:
            if self.canshoot or self.candash:
                if self.canshoot:
                    if self.alert == False:
                        if self.attention:
                            if self.right == 1:
                                win.blit(self.shootimageshooting, (self.x, self.y-20))

                            if self.left == 1:
                                win.blit(pygame.transform.flip(self.shootimageshooting, True, False), (self.x-19, self.y-20))

                        if self.attention == False:
                            if self.mid:
                                win.blit(self.shootimageidle, (self.x+ 8, self.y-20))

                            if self.right == 1:
                                win.blit(self.shootimagegorightframes[self.shootimagegorightc//10], (self.x + 8, self.y -20))

                                self.shootimagegorightc += 1

                                if self.shootimagegorightc == 70:
                                    self.shootimagegorightc = 0

                            if self.left == 1:
                                win.blit(self.shootimagegoleftframes[self.shootimagegoleftc//10], (self.x + 8, self.y -20))

                                self.shootimagegoleftc += 1

                                if self.shootimagegoleftc == 70:
                                    self.shootimagegoleftc = 0

                    if self.alert:
                        if self.right == 1:
                            win.blit(self.shootimageshooting, (self.x, self.y-20))

                        if self.left == 1:
                            win.blit(pygame.transform.flip(self.shootimageshooting, True, False), (self.x- 19, self.y-20))
                        

                if self.candash:
                    if self.alert == False:
                        if self.attention:
                            self.dashimagegoleftc = 0
                            self.dashimagegorightc = 0
                            
                            if self.right == 1:
                                win.blit(self.dashimagedashing, (self.x, self.y-20))

                            if self.left == 1:
                                win.blit(pygame.transform.flip(self.dashimagedashing, True, False), (self.x-19, self.y-20))

                        if self.attention == False:
                            if self.mid:
                                win.blit(self.dashimageidle, (self.x+ 8, self.y-20))

                            if self.right == 1:
                                win.blit(self.dashimagegorightframes[self.dashimagegorightc//10], (self.x + 8, self.y -20))

                                self.dashimagegorightc += 1

                                if self.dashimagegorightc == 70:
                                    self.dashimagegorightc = 0

                            if self.left == 1:
                                win.blit(self.dashimagegoleftframes[self.dashimagegoleftc//10], (self.x + 8, self.y -20))

                                self.dashimagegoleftc += 1

                                if self.dashimagegoleftc == 70:
                                    self.dashimagegoleftc = 0

                    if self.alert:
                        if self.dashing == False:
                            self.dashweaponimageleftc = 0
                            self.dashweaponimagerightc = 0
                            
                            if self.right == 1:
                                win.blit(self.dashimagedashing, (self.x, self.y-20))

                            if self.left == 1:
                                win.blit(pygame.transform.flip(self.dashimagedashing,  True, False), (self.x- 19, self.y-20))

                        if self.dashing:
                            if self.right == 1:
                                win.blit(self.dashweaponimagerightframes[self.dashweaponimagerightc//10], (self.x+8, self.y-20))

                                self.dashweaponimagerightc += 1

                                if self.dashweaponimagerightc == 50:
                                    self.dashweaponimagerightc = 0

                            if self.left == 1:
                                win.blit(pygame.transform.flip(self.dashweaponimagerightframes[self.dashweaponimageleftc//10], True, False), (self.x+8, self.y-20))

                                self.dashweaponimageleftc += 1

                                if self.dashweaponimageleftc == 50:
                                    self.dashweaponimageleftc = 0

            else:
                if self.alert == False:
                    if self.attention:
                        if self.right == 1:
                            win.blit(self.imageidle, (self.x+ 8, self.y-20))

                        if self.left == 1:
                            win.blit(pygame.transform.flip(self.imageidle, True, False), (self.x+ 8, self.y-20))

                    if self.attention == False:
                        if self.mid:
                            win.blit(self.imageidle, (self.x+ 8, self.y-20))

                        if self.right == 1:
                            win.blit(self.imagegorightframes[self.imagegorightc//10], (self.x + 8, self.y -20))

                            self.imagegorightc += 1

                            if self.imagegorightc == 70:
                                self.imagegorightc = 0

                        if self.left == 1:
                            win.blit(self.imagegoleftframes[self.imagegoleftc//10], (self.x + 8, self.y -20))

                            self.imagegoleftc += 1

                            if self.imagegoleftc == 70:
                                self.imagegoleftc = 0

                if self.alert:
                    if self.right == 1:
                        win.blit(self.imageidle, (self.x+ 8, self.y-20))

                    if self.left == 1:
                        win.blit(pygame.transform.flip(self.imageidle, True, False), (self.x+ 8, self.y-20))
        
        if self.stopped:
            if self.canshoot or self.candash:
                if self.canshoot:
                    win.blit(pygame.transform.scale(self.shootimagestopped, (40, 80)), (self.x+5, self.y-20))

                if self.candash:
                    win.blit(pygame.transform.scale(self.dashimagestopped, (40, 80)), (self.x+5, self.y-20))

            else:
                win.blit(pygame.transform.scale(self.imagestopped, (40, 80)), (self.x+5, self.y-20))
            
            pygame.draw.rect(win, (0,0,0), (self.x - 25, self.y -20, 100, 10))
            
            pygame.draw.rect(win, (0,255,0), (self.x - 25, self.y -20, self.stoppedc//50, 10))

    def anim(self, moneycount):
        self.mc += 1

        if self.mc == 10:
            self.mc = 0
            self.sp += 1
        
        self.icorect = pygame.Rect(self.mx, self.my, 50, 50)
        
        if moneycount.mx + 50 > self.mx:
            self.mx += self.sp

        if moneycount.mx + 50< self.mx:
            self.mx -= self.sp

        if self.my >0:
            self.my -= self.sp

        if self.icorect.colliderect(moneycount.rect):
            self.moneycame = True

        if self.moneycame == False:
            win.blit(self.moneyimage, (self.mx, self.my+30))

    def update(self):
        self.checkmode()
        
        self.counter()
        
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        self.inactive()
        
        self.move()
                

class Money(pygame.sprite.Sprite):
    def __init__(self, x, y, amount):
        super().__init__()

        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x, self.y, 5, 94)

        self.icorect = pygame.Rect(self.x, self.y +30, 50, 50)

        self.amount = amount

        self.sp = 1

        self.c = 0

        self.moneyimage = pygame.transform.scale(pygame.image.load("tex\game\MoneyIcon.png"), (50, 50))

        self.came = False

        self.catch = False

    def anim(self, moneycount):
        self.c += 1

        if self.c == 10:
            self.c = 0
            self.sp += 1
        
        self.icorect = pygame.Rect(self.x, self.y, 50, 50)
        
        if moneycount.mx +50 > self.x:
            self.x += self.sp

        if moneycount.mx +50 < self.x:
            self.x -= self.sp

        if self.y >0:
            self.y -= self.sp

        if self.icorect.colliderect(moneycount.rect):
            self.came = True

        win.blit(self.moneyimage, (self.x, self.y))

    def draw(self):
        pass
        '''
        pygame.draw.rect(win,(0,255,0),self.rect)
        '''

class Type1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sound = pygame.mixer.Sound("CodedDoorSoundTune1.wav")
        self.schannel = pygame.mixer.Channel(6)

        self.schannel.set_volume(0.2)

        self.x = 360
        self.y = 320

        self.rect = pygame.Rect(self.x, self.y, 80, 80)
        self.image = 0

        self.cnumb = (50, 50, 255)

        self.numb = pygame.font.SysFont('Lucida Console', 60)
        self.numbren = self.numb.render("1", False, self.cnumb)

        self.canpush = True

        self.pushed = False

        self.canplay = 0

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.canplay == 1:
                self.schannel.play(self.sound)

    def col(self, cursor, codeddoor):
        self.cnumb = (218, 218, 218)
        self.pushed = False

        if codeddoor.opening:
            if codeddoor.pressed4 == 1:
                self.canplay = 0
            
            if codeddoor.delay == 0:
                if self.rect.colliderect(cursor.rect):
                    self.cnumb = (100, 100, 100)
                    if pygame.mouse.get_pressed()[0]:
                        self.pushed = True
                        self.canplay += 1
                        if self.canpush:
                            if codeddoor.pressed1==-1:
                                codeddoor.pressed1 = 1

                            elif codeddoor.pressed2==-1:
                                codeddoor.pressed2 = 1

                            elif codeddoor.pressed3==-1:
                                codeddoor.pressed3 = 1

                            elif codeddoor.pressed4==-1:
                                codeddoor.pressed4 = 1

                    if self.pushed == True:
                        self.canpush = False

                    if self.pushed == False:
                        self.canpush = True
                        self.canplay = 0

    def draw(self, codeddoor):
        if codeddoor.opening:
            self.numbren = self.numb.render("1", False, self.cnumb)

            pygame.draw.rect(win, (31,31,31), self.rect)
            win.blit(self.numbren, (self.x + 10, self.y +10))

    def update(self, cursor, codeddoor):
        self.col(cursor, codeddoor)

class Type2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sound = pygame.mixer.Sound("CodedDoorSoundTune2.wav")
        self.schannel = pygame.mixer.Channel(6)

        self.schannel.set_volume(0.2)

        self.x = 460
        self.y = 320

        self.rect = pygame.Rect(self.x, self.y, 80, 80)
        self.image = 0

        self.cnumb = (50, 50, 255)

        self.numb = pygame.font.SysFont('Lucida Console', 60)
        self.numbren = self.numb.render("2", False, self.cnumb)

        self.canpush = True

        self.pushed = False

        self.canplay = 0

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.canplay == 1:
                self.schannel.play(self.sound)

    def col(self, cursor, codeddoor):
        self.cnumb = (218, 218, 218)
        self.pushed = False
        
        if codeddoor.opening:
            if codeddoor.pressed4 == 2:
                self.canplay = 0
                
            if codeddoor.delay == 0:
                if self.rect.colliderect(cursor.rect):
                    self.cnumb = (100, 100, 100)
                    if pygame.mouse.get_pressed()[0]:
                        self.pushed = True
                        self.canplay += 1
                        if self.canpush:
                            if codeddoor.pressed1==-1:
                                codeddoor.pressed1 = 2

                            elif codeddoor.pressed2==-1:
                                codeddoor.pressed2 = 2

                            elif codeddoor.pressed3==-1:
                                codeddoor.pressed3 = 2

                            elif codeddoor.pressed4==-1:
                                codeddoor.pressed4 = 2

                    if self.pushed == True:
                        self.canpush = False

                    if self.pushed == False:
                        self.canpush = True
                        self.canplay = 0

    def draw(self, codeddoor):
        if codeddoor.opening:
            self.numbren = self.numb.render("2", False, self.cnumb)

            pygame.draw.rect(win, (31,31,31), self.rect)
            win.blit(self.numbren, (self.x + 10, self.y +10))

    def update(self, cursor, codeddoor):
        self.col(cursor, codeddoor)
                
class Type3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sound = pygame.mixer.Sound("CodedDoorSoundTune3.wav")
        self.schannel = pygame.mixer.Channel(6)

        self.schannel.set_volume(0.2)

        self.x = 560
        self.y = 320

        self.rect = pygame.Rect(self.x, self.y, 80, 80)
        self.image = 0

        self.cnumb = (50, 50, 255)

        self.numb = pygame.font.SysFont('Lucida Console', 60)
        self.numbren = self.numb.render("3", False, self.cnumb)

        self.canpush = True

        self.pushed = False

        self.canplay = 0

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.canplay == 1:
                self.schannel.play(self.sound)

    def col(self, cursor, codeddoor):
        self.cnumb = (218, 218, 218)
        self.pushed = False
        if codeddoor.opening:
            if codeddoor.pressed4 == 3:
                self.canplay = 0
        
            if codeddoor.delay == 0:
                if self.rect.colliderect(cursor.rect):
                    self.cnumb = (100, 100, 100)
                    if pygame.mouse.get_pressed()[0]:
                        self.pushed = True
                        self.canplay += 1
                        if self.canpush:
                            if codeddoor.pressed1==-1:
                                codeddoor.pressed1 = 3

                            elif codeddoor.pressed2==-1:
                                codeddoor.pressed2 = 3

                            elif codeddoor.pressed3==-1:
                                codeddoor.pressed3 = 3

                            elif codeddoor.pressed4==-1:
                                codeddoor.pressed4 = 3

                    if self.pushed == True:
                        self.canpush = False

                    if self.pushed == False:
                        self.canpush = True
                        self.canplay = 0

    def draw(self, codeddoor):
        if codeddoor.opening:
            self.numbren = self.numb.render("3", False, self.cnumb)

            pygame.draw.rect(win, (31,31,31), self.rect)
            win.blit(self.numbren, (self.x + 10, self.y +10))

    def update(self, cursor, codeddoor):
        self.col(cursor, codeddoor)

class Type4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sound = pygame.mixer.Sound("CodedDoorSoundTune1.wav")
        self.schannel = pygame.mixer.Channel(6)

        self.schannel.set_volume(0.2)

        self.x = 360
        self.y = 420

        self.rect = pygame.Rect(self.x, self.y, 80, 80)
        self.image = 0

        self.cnumb = (50, 50, 255)

        self.numb = pygame.font.SysFont('Lucida Console', 60)
        self.numbren = self.numb.render("4", False, self.cnumb)

        self.canpush = True

        self.pushed = False

        self.canplay = 0

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.canplay == 1:
                self.schannel.play(self.sound)

    def col(self, cursor, codeddoor):
        self.cnumb = (218, 218, 218)
        self.pushed = False

        if codeddoor.opening:
            if codeddoor.pressed4 == 4:
                self.canplay = 0
                
            if codeddoor.delay == 0:
                if self.rect.colliderect(cursor.rect):
                    self.cnumb = (100, 100, 100)
                    if pygame.mouse.get_pressed()[0]:
                        self.pushed = True
                        self.canplay += 1
                        if self.canpush:
                            if codeddoor.pressed1==-1:
                                codeddoor.pressed1 = 4

                            elif codeddoor.pressed2==-1:
                                codeddoor.pressed2 = 4

                            elif codeddoor.pressed3==-1:
                                codeddoor.pressed3 = 4

                            elif codeddoor.pressed4==-1:
                                codeddoor.pressed4 = 4
                                
                    if self.pushed == True:
                        self.canpush = False

                    if self.pushed == False:
                        self.canpush = True
                        self.canplay = 0

    def draw(self, codeddoor):
        if codeddoor.opening:
            self.numbren = self.numb.render("4", False, self.cnumb)

            pygame.draw.rect(win, (31,31,31), self.rect)
            win.blit(self.numbren, (self.x + 10, self.y +10))

    def update(self, cursor, codeddoor):
        self.col(cursor, codeddoor)

class Type5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sound = pygame.mixer.Sound("CodedDoorSoundTune2.wav")
        self.schannel = pygame.mixer.Channel(6)

        self.schannel.set_volume(0.2)

        self.x = 460
        self.y = 420

        self.rect = pygame.Rect(self.x, self.y, 80, 80)
        self.image = 0

        self.cnumb = (50, 50, 255)

        self.numb = pygame.font.SysFont('Lucida Console', 60)
        self.numbren = self.numb.render("5", False, self.cnumb)

        self.canpush = True

        self.pushed = False

        self.canplay = 0

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.canplay == 1:
                self.schannel.play(self.sound)

    def col(self, cursor, codeddoor):
        self.cnumb = (218, 218, 218)
        self.pushed = False

        if codeddoor.opening:
            if codeddoor.pressed4 == 5:
                self.canplay = 0
                
            if codeddoor.delay == 0:
                if self.rect.colliderect(cursor.rect):
                    self.cnumb = (100, 100, 100)
                    if pygame.mouse.get_pressed()[0]:
                        self.pushed = True
                        self.canplay += 1
                        if self.canpush:
                            if codeddoor.pressed1==-1:
                                codeddoor.pressed1 = 5

                            elif codeddoor.pressed2==-1:
                                codeddoor.pressed2 = 5

                            elif codeddoor.pressed3==-1:
                                codeddoor.pressed3 = 5

                            elif codeddoor.pressed4==-1:
                                codeddoor.pressed4 = 5

                    if self.pushed == True:
                        self.canpush = False

                    if self.pushed == False:
                        self.canpush = True
                        self.canplay = 0

    def draw(self, codeddoor):
        if codeddoor.opening:
            self.numbren = self.numb.render("5", False, self.cnumb)

            pygame.draw.rect(win, (31,31,31), self.rect)
            win.blit(self.numbren, (self.x + 10, self.y +10))

    def update(self, cursor, codeddoor):
        self.col(cursor, codeddoor)

class Type6(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sound = pygame.mixer.Sound("CodedDoorSoundTune3.wav")
        self.schannel = pygame.mixer.Channel(6)

        self.schannel.set_volume(0.2)

        self.x = 560
        self.y = 420

        self.rect = pygame.Rect(self.x, self.y, 80, 80)
        self.image = 0

        self.cnumb = (50, 50, 255)

        self.numb = pygame.font.SysFont('Lucida Console', 60)
        self.numbren = self.numb.render("6", False, self.cnumb)

        self.canpush = True

        self.pushed = False

        self.canplay = 0

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.canplay == 1:
                self.schannel.play(self.sound)

    def col(self, cursor, codeddoor):
        self.cnumb = (218, 218, 218)
        self.pushed = False

        if codeddoor.opening:
            if codeddoor.pressed4 == 6:
                self.canplay = 0
                
            if codeddoor.delay == 0:
                if self.rect.colliderect(cursor.rect):
                    self.cnumb = (100, 100, 100)
                    if pygame.mouse.get_pressed()[0]:
                        self.pushed = True
                        self.canplay += 1
                        if self.canpush:
                            if codeddoor.pressed1==-1:
                                codeddoor.pressed1 = 6

                            elif codeddoor.pressed2==-1:
                                codeddoor.pressed2 = 6

                            elif codeddoor.pressed3==-1:
                                codeddoor.pressed3 = 6

                            elif codeddoor.pressed4==-1:
                                codeddoor.pressed4 = 6

                    if self.pushed == True:
                        self.canpush = False

                    if self.pushed == False:
                        self.canpush = True
                        self.canplay = 0

    def draw(self, codeddoor):
        if codeddoor.opening:
            self.numbren = self.numb.render("6", False, self.cnumb)

            pygame.draw.rect(win, (31,31,31), self.rect)
            win.blit(self.numbren, (self.x + 10, self.y +10))

    def update(self, cursor, codeddoor):
        self.col(cursor, codeddoor)

class Type7(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sound = pygame.mixer.Sound("CodedDoorSoundTune1.wav")
        self.schannel = pygame.mixer.Channel(6)

        self.schannel.set_volume(0.2)

        self.x = 360
        self.y = 520

        self.rect = pygame.Rect(self.x, self.y, 80, 80)
        self.image = 0

        self.cnumb = (50, 50, 255)

        self.numb = pygame.font.SysFont('Lucida Console', 60)
        self.numbren = self.numb.render("7", False, self.cnumb)

        self.canpush = True

        self.pushed = False

        self.canplay = 0

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.canplay == 1:
                self.schannel.play(self.sound)

    def col(self, cursor, codeddoor):
        self.cnumb = (218, 218, 218)
        self.pushed = False

        if codeddoor.opening:
            if codeddoor.pressed4 == 7:
                self.canplay = 0
                
            if codeddoor.delay == 0:
                if self.rect.colliderect(cursor.rect):
                    self.cnumb = (100, 100, 100)
                    if pygame.mouse.get_pressed()[0]:
                        self.pushed = True
                        self.canplay += 1
                        if self.canpush:
                            if codeddoor.pressed1==-1:
                                codeddoor.pressed1 = 7

                            elif codeddoor.pressed2==-1:
                                codeddoor.pressed2 = 7

                            elif codeddoor.pressed3==-1:
                                codeddoor.pressed3 = 7

                            elif codeddoor.pressed4==-1:
                                codeddoor.pressed4 = 7

                    if self.pushed == True:
                        self.canpush = False

                    if self.pushed == False:
                        self.canpush = True
                        self.canplay = 0

    def draw(self, codeddoor):
        if codeddoor.opening:
            self.numbren = self.numb.render("7", False, self.cnumb)

            pygame.draw.rect(win, (31,31,31), self.rect)
            win.blit(self.numbren, (self.x + 10, self.y +10))

    def update(self, cursor, codeddoor):
        self.col(cursor, codeddoor)

class Type8(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sound = pygame.mixer.Sound("CodedDoorSoundTune2.wav")
        self.schannel = pygame.mixer.Channel(6)

        self.schannel.set_volume(0.2)

        self.x = 460
        self.y = 520

        self.rect = pygame.Rect(self.x, self.y, 80, 80)
        self.image = 0

        self.cnumb = (50, 50, 255)

        self.numb = pygame.font.SysFont('Lucida Console', 60)
        self.numbren = self.numb.render("8", False, self.cnumb)

        self.canpush = True

        self.pushed = False

        self.canplay = 0

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.canplay == 1:
                self.schannel.play(self.sound)

    def col(self, cursor, codeddoor):
        self.cnumb = (218, 218, 218)
        self.pushed = False
        if codeddoor.opening:
            if codeddoor.pressed4 == 8:
                self.canplay = 0
                
            if codeddoor.delay == 0:
                if self.rect.colliderect(cursor.rect):
                    self.cnumb = (100, 100, 100)
                    if pygame.mouse.get_pressed()[0]:
                        self.pushed = True
                        self.canplay += 1
                        if self.canpush:
                            if codeddoor.pressed1==-1:
                                codeddoor.pressed1 = 8

                            elif codeddoor.pressed2==-1:
                                codeddoor.pressed2 = 8

                            elif codeddoor.pressed3==-1:
                                codeddoor.pressed3 = 8

                            elif codeddoor.pressed4==-1:
                                codeddoor.pressed4 = 8

                    if self.pushed == True:
                        self.canpush = False

                    if self.pushed == False:
                        self.canpush = True
                        self.canplay = 0

    def draw(self, codeddoor):
        if codeddoor.opening:
            self.numbren = self.numb.render("8", False, self.cnumb)

            pygame.draw.rect(win, (31,31,31), self.rect)
            win.blit(self.numbren, (self.x + 10, self.y +10))

    def update(self, cursor, codeddoor):
        self.col(cursor, codeddoor)

class Type9(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sound = pygame.mixer.Sound("CodedDoorSoundTune3.wav")
        self.schannel = pygame.mixer.Channel(6)

        self.schannel.set_volume(0.2)

        self.x = 560
        self.y = 520

        self.rect = pygame.Rect(self.x, self.y, 80, 80)
        self.image = 0

        self.cnumb = (50, 50, 255)

        self.numb = pygame.font.SysFont('Lucida Console', 60)
        self.numbren = self.numb.render("9", False, self.cnumb)

        self.canpush = True

        self.pushed = False

        self.canplay = 0

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.canplay == 1:
                self.schannel.play(self.sound)

    def col(self, cursor, codeddoor):
        self.cnumb = (218, 218, 218)
        self.pushed = False

        if codeddoor.opening:
            if codeddoor.pressed4 == 9:
                self.canplay = 0
                
            if codeddoor.delay == 0:
                if self.rect.colliderect(cursor.rect):
                    self.cnumb = (100, 100, 100)
                    if pygame.mouse.get_pressed()[0]:
                        self.pushed = True
                        self.canplay += 1
                        if self.canpush:
                            if codeddoor.pressed1==-1:
                                codeddoor.pressed1 = 9

                            elif codeddoor.pressed2==-1:
                                codeddoor.pressed2 = 9

                            elif codeddoor.pressed3==-1:
                                codeddoor.pressed3 = 9

                            elif codeddoor.pressed4==-1:
                                codeddoor.pressed4 = 9

                    if self.pushed == True:
                        self.canpush = False

                    if self.pushed == False:
                        self.canpush = True
                        self.canplay = 0

    def draw(self, codeddoor):
        if codeddoor.opening:
            self.numbren = self.numb.render("9", False, self.cnumb)

            pygame.draw.rect(win, (31,31,31), self.rect)
            win.blit(self.numbren, (self.x + 10, self.y +10))

    def update(self, cursor, codeddoor):
        self.col(cursor, codeddoor)

class Type0(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.sound = pygame.mixer.Sound("CodedDoorSoundTune1.wav")
        self.schannel = pygame.mixer.Channel(6)

        self.schannel.set_volume(0.2)

        self.x = 460
        self.y = 620

        self.rect = pygame.Rect(self.x, self.y, 80, 80)
        self.image = 0

        self.cnumb = (50, 50, 255)

        self.numb = pygame.font.SysFont('Lucida Console', 60)
        self.numbren = self.numb.render("0", False, self.cnumb)

        self.canpush = True

        self.pushed = False

        self.canplay = 0

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.canplay == 1:
                self.schannel.play(self.sound)

    def col(self, cursor, codeddoor):
        self.cnumb = (218, 218, 218)
        self.pushed = False

        if codeddoor.opening:
            if codeddoor.pressed4 == "0":
                self.canplay = 0
                
            if codeddoor.delay == 0:
                if self.rect.colliderect(cursor.rect):
                    self.cnumb = (100, 100, 100)
                    if pygame.mouse.get_pressed()[0]:
                        self.pushed = True
                        self.canplay += 1
                        if self.canpush:
                            if codeddoor.pressed1==-1:
                                codeddoor.pressed1 = "0"

                            elif codeddoor.pressed2==-1:
                                codeddoor.pressed2 = "0"

                            elif codeddoor.pressed3==-1:
                                codeddoor.pressed3 = "0"

                            elif codeddoor.pressed4==-1:
                                codeddoor.pressed4 = "0"

                    if self.pushed == True:
                        self.canpush = False

                    if self.pushed == False:
                        self.canpush = True
                        self.canplay = 0

    def draw(self, codeddoor):
        if codeddoor.opening:
            self.numbren = self.numb.render("0", False, self.cnumb)

            pygame.draw.rect(win, (31,31,31), self.rect)
            win.blit(self.numbren, (self.x + 10, self.y +10))

    def update(self, cursor, codeddoor):
        self.col(cursor, codeddoor)



class CodedDoor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.wsound = pygame.mixer.Sound("CodedDoorWinSound.wav")
        self.wschannel = pygame.mixer.Channel(9)

        self.wschannel.set_volume(0.5)

        self.lsound = pygame.mixer.Sound("CodedDoorLoseSound.wav")
        self.lschannel = pygame.mixer.Channel(9)

        self.lschannel.set_volume(0.5)

        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x+10, self.y+30, 10, 30)
        
        self.image = pygame.image.load("tex\game\CodedlockImage.png")

        self.pressed1 = -1
        self.pressed2 = -1
        self.pressed3 = -1
        self.pressed4 = -1

        self.code = ""
        self.codeint = 0

        self.opening = False

        self.blocking = True

        self.bl = 0

        self.b2 = 0

        self.typed = pygame.font.SysFont('Lucida Console', 90)
        self.typedren = self.typed.render(str(self.code), True,(218, 218, 218))

        self.delay = False
        self.delayc = 0

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.blocking == False and self.bl == 0:
                self.bl = 1
                self.wschannel.play(self.wsound)

            if self.blocking and self.delayc == 50:
                self.lschannel.play(self.lsound)

    def pressedupdate(self):
        if self.opening == False:
            self.pressed1 = -1
            self.pressed2 = -1
            self.pressed3 = -1
            self.pressed4 = -1
            self.code = ""

        if self.opening:
            self.b2 = 1
            if int(self.pressed4) != -1:
                self.code = str(self.pressed1)+str(self.pressed2)+str(self.pressed3)+str(self.pressed4)
                self.codeint = int(self.code)

            elif int(self.pressed3) != -1:
                self.code = str(self.pressed1)+str(self.pressed2)+str(self.pressed3)
                self.codeint = int(self.code)

            elif int(self.pressed2) != -1:
                self.code = str(self.pressed1)+str(self.pressed2)
                self.codeint = int(self.code)

            elif int(self.pressed1) != -1:
                self.code = str(self.pressed1)
                self.codeint = int(self.code)

            self.typedren = self.typed.render(str(self.code), False,(218, 218, 218))

        if int(self.pressed1) !=-1 and int(self.pressed2) !=-1 and int(self.pressed3) !=-1 and int(self.pressed4) !=-1:
            self.delay = True

    def wait(self):
        if self.delay:
            self.delayc += 1
            if self.delayc == 50:
                self.opening = False
                player.using = False

            if self.delayc == 51:
                self.delayc = 0
                self.delay = False
            

    def col(self, player):
        if self.rect.colliderect(player.rect):
            if self.blocking:
                if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                    if self.delay == 0:
                        self.opening = True

        if self.opening:
            player.using = True

        if player.moving:
            self.opening = False
            player.using = False
                        
    def check(self, password, goupdown):
        if self.opening == False:
            if self.codeint == password.password:
                goupdown.blocking = False
                self.blocking = False

    def draw(self):
        win.blit(pygame.transform.scale(self.image, (36, 40)), (self.x-6, self.y + 20))
                
    def windraw(self):
        if self.opening:
            win.blit(self.image, (250, 80))

            win.blit(self.typedren, (385, 213))

    def update(self, player, password, goupdown):
        self.pressedupdate()
        self.col(player)
        self.wait()
        self.check(password, goupdown)

class Password(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.sound = pygame.mixer.Sound("PasswordSound.wav")
        self.schannel = pygame.mixer.Channel(8)

        self.schannel.set_volume(0.8)

        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x+10, self.y+30, 10, 30)
        self.image = pygame.image.load("tex\game\PasswordImageGm.png")
        self.winimage = pygame.image.load("tex\game\PasswordImage.png")

        self.a = random.randint(0,9)
        self.b = random.randint(0,9)
        self.c = random.randint(0,9)
        self.d = random.randint(0,9)

        self.opening = False

        self.showpassword = str(self.a)+str(self.b)+str(self.c)+str(self.d)
        self.password = int(str(self.a)+str(self.b)+str(self.c)+str(self.d))

        self.text = pygame.font.SysFont('Comic Sans MS', 36)
        self.textren = self.text.render("Код для открытия двери", True,(0, 0, 0))

        self.passwordtext = pygame.font.SysFont('Comic Sans MS', 48)
        self.passwordtextren = self.passwordtext.render(self.showpassword, True,(0, 0, 0))

        self.delay = 0

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.delay == 2:
                self.schannel.play(self.sound, 0, 500)

    def col(self, player):
        if self.rect.colliderect(player.rect):
            if self.opening == False:
                if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                    if self.delay == 0:
                        self.opening = True
                        self.delay = 1
                        player.using = True

            elif self.opening:
                player.hidden = False
                
                if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                    if self.delay == 0:
                        self.opening = False
                        self.delay = 1
                        player.using = False

            if self.delay>0:
                self.delay +=1

            if self.delay == 30:
                self.delay = 0

        if player.moving:
            self.opening = False
            self.delay = 0

    def draw(self):
        win.blit(pygame.transform.scale(self.image, (40, 40)), (self.x-10, self.y+ 30))

    def windraw(self):
        if self.opening:
            win.blit(self.winimage, (240, 80))

            win.blit(self.textren, (290, 200))
            win.blit(self.passwordtextren, (450, 400))

    def update(self, player):
        self.col(player)

class Hint(pygame.sprite.Sprite):
    def __init__(self, x, y, text, text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11):
        super().__init__()

        self.sound = pygame.mixer.Sound("PasswordSound.wav")
        self.schannel = pygame.mixer.Channel(8)

        self.schannel.set_volume(0.8)

        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x+10, self.y+30, 10, 30)
        self.image = pygame.image.load("tex\game\PasswordImageGm.png")
        self.winimage = pygame.image.load("tex\game\PasswordImage.png")

        self.opening = False

        self.text = pygame.font.SysFont('Comic Sans MS', 20)
        
        self.textren = self.text.render(text, True,(0, 0, 0))
        self.textren1 = self.text.render(text1, True,(0, 0, 0))
        self.textren2 = self.text.render(text2, True,(0, 0, 0))
        self.textren3 = self.text.render(text3, True,(0, 0, 0))
        self.textren4 = self.text.render(text4, True,(0, 0, 0))
        self.textren5 = self.text.render(text5, True,(0, 0, 0))
        self.textren6 = self.text.render(text6, True,(0, 0, 0))
        self.textren7 = self.text.render(text7, True,(0, 0, 0))
        self.textren8 = self.text.render(text8, True,(0, 0, 0))
        self.textren9 = self.text.render(text9, True,(0, 0, 0))
        self.textren10 = self.text.render(text10, True,(0, 0, 0))
        self.textren11 = self.text.render(text11, True,(0, 0, 0))

        self.delay = 0

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.delay == 2:
                self.schannel.play(self.sound, 0, 500)

    def col(self, player):
        if self.rect.colliderect(player.rect):
            if self.opening == False:
                if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                    if self.delay == 0:
                        self.opening = True
                        self.delay = 1
                        player.using = True

            elif self.opening:
                player.hidden = False
                
                if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                    if self.delay == 0:
                        self.opening = False
                        self.delay = 1
                        player.using = False

            if self.delay>0:
                self.delay +=1

            if self.delay == 30:
                self.delay = 0

        if player.moving:
            self.opening = False
            self.delay = 0

    def draw(self):
        win.blit(pygame.transform.scale(self.image, (40, 40)), (self.x-10, self.y+ 30))

    def windraw(self):
        if self.opening:
            win.blit(self.winimage, (240, 80))

            win.blit(self.textren, (280, 200))
            win.blit(self.textren1, (280, 220))
            win.blit(self.textren2, (280, 240))
            win.blit(self.textren3, (280, 260))
            win.blit(self.textren4, (280, 280))
            win.blit(self.textren5, (280, 300))
            win.blit(self.textren6, (280, 320))
            win.blit(self.textren7, (280, 340))
            win.blit(self.textren8, (280, 360))
            win.blit(self.textren9, (280, 380))
            win.blit(self.textren10, (280, 400))
            win.blit(self.textren11, (277, 420))

    def update(self, player):
        self.col(player)

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y
        self.w = 10
        self.h = 94

        self.image = pygame.image.load("tex\game\Laser\LaserImage.png")
        self.rect = pygame.Rect(self.x-20, self.y, self. w, self.h)

        self.active = True

    def col(self, player, alert):
        if self.active:
            if self.rect.colliderect(player.rect):
                alert.active = True
                
                alert.secs = 19
                alert.misecs = 99

    def draw(self):
        if self.active:
            win.blit(self.image, (self.x-20, self.y))

    def update(self, player, alert):
        self.col(player, alert)

class LaserTerminal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x-10
        self.y = y+110
        self.w = 40
        self.h = 60

        self.winnumb = random.randint(0,2)
        
        self.image = pygame.image.load("tex\game\Laser\LaserTerminal.png")
        self.imageopened = pygame.image.load("tex\game\Laser\LaserTerminalOpened.png")
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        self.opened = False

        self.opening = False

    def plrcol(self, player, lasergame):
        if self.opened == False:
            if self.rect.colliderect(player.rect):
                if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                    lasergame.opening = True
                    self.opening = True
                    lasergame.open = True
                    player.using = True

        if self.opened:
            player.using = False


    def draw(self):
        if self.opened == False:
            win.blit(self.image, (self.x, self.y))

        if self.opened:
            win.blit(self.imageopened, (self.x, self.y))

    def update(self, player, lasergame):
        self.plrcol(player, lasergame)

class LaserGame:
    def __init__(self):

        self.osound = pygame.mixer.Sound("LaserOpenSound.wav")
        self.csound = pygame.mixer.Sound("LaserCutSound.wav")
        
        self.schannel = pygame.mixer.Channel(12)

        self.schannel.set_volume(0.8)
        
        self.x = 275
        self.y = 100
        self.w = 450
        self.h = 565

        self.numb = [0,1]
        self.numbr = random.choice(self.numb)
        self.numb.remove(self.numbr)

        self.numb1 = [1,2]
        self.numb1r = random.choice(self.numb1)
        self.numb1.remove(self.numb1r)

        self.numb2 = [0,2]
        self.numb2r = random.choice(self.numb2)
        self.numb2.remove(self.numb2r)

        self.winnumb = 0

        self.pathrandom = random.randint(0,2)

        self.path1images = [[pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path1var1Safe.png"), pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path1var1Alert.png")],
                            [pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path1var2Safe.png"), pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path1var2Alert.png")],
                            [pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path1var3Safe.png"), pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path1var3Alert.png")]]

        self.path2images = [[pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path2var1Safe.png"), pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path2var1Alert.png")],
                            [pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path2var2Safe.png"), pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path2var2Alert.png")],
                            [pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path2var3Safe.png"), pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path2var3Alert.png")]]

        self.path3images = [[pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path3var1Safe.png"), pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path3var1Alert.png")],
                            [pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path3var2Safe.png"), pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path3var2Alert.png")],
                            [pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path3var3Safe.png"), pygame.image.load("tex\game\Laser\LaserTerminalPaths\Path3var3Alert.png")]]

        self.opening = False

        self.open = False
        
        self.image = pygame.image.load("tex\game\Laser\LaserTerminalInside.png")
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        self.pathimage1 = 0
        self.pathimage2 = 0
        self.pathimage3 = 0

        self.scisx = 240
        self.scissors = pygame.transform.flip(pygame.transform.scale(pygame.image.load("tex\game\Laser\Kusachki.png"), (160, 160)), True, False)

        self.choose = 0

        self.delay = 0

        self.canupdate = True

        self.cut = False

    def pathupdate(self, laserterminal):
        self.winnumb = laserterminal.winnumb
        
        if self.canupdate == True:
            if self.winnumb == 0:
                if self.pathrandom == 0:
                    self.pathimage1 = self.path1images[0][0]
                    self.pathimage2 = self.path2images[2][1]
                    self.pathimage3 = self.path3images[1][1]

                if self.pathrandom == 1:
                    self.pathimage1 = self.path1images[2][0]
                    self.pathimage2 = self.path2images[1][1]
                    self.pathimage3 = self.path3images[0][1]

                if self.pathrandom == 2:
                    self.pathimage1 = self.path1images[1][0]
                    self.pathimage2 = self.path2images[2][1]
                    self.pathimage3 = self.path3images[0][1]

            if self.winnumb == 1:
                if self.pathrandom == 0:
                    self.pathimage1 = self.path1images[1][1]
                    self.pathimage2 = self.path2images[0][0]
                    self.pathimage3 = self.path3images[2][1]

                if self.pathrandom == 1:
                    self.pathimage1 = self.path1images[0][1]
                    self.pathimage2 = self.path2images[1][0]
                    self.pathimage3 = self.path3images[2][1]

                if self.pathrandom == 2:
                    self.pathimage1 = self.path1images[2][1]
                    self.pathimage2 = self.path2images[1][0]
                    self.pathimage3 = self.path3images[0][1]

            if self.winnumb == 2:
                if self.pathrandom == 0:
                    self.pathimage1 = self.path1images[1][1]
                    self.pathimage2 = self.path2images[2][1]
                    self.pathimage3 = self.path3images[0][0]

                if self.pathrandom == 1:
                    self.pathimage1 = self.path1images[0][1]
                    self.pathimage2 = self.path2images[2][1]
                    self.pathimage3 = self.path3images[1][0]

                if self.pathrandom == 2:
                    self.pathimage1 = self.path1images[2][1]
                    self.pathimage2 = self.path2images[1][1]
                    self.pathimage3 = self.path3images[0][0]

            

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.open:
                self.open = False
                self.schannel.play(self.osound)

            if self.cut:
                self.cut = False
                self.schannel.play(self.csound)

    def game(self):
        if self.opening:
            if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
                if self.delay==0:
                    if self.choose>0:
                        self.choose -=1
                        self.scisx -=115
                        self.delay = 1

            if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
                if self.delay==0:
                    if self.choose<2:
                        self.choose +=1
                        self.scisx +=115
                        self.delay = 1

            if pygame.key.get_pressed()[pygame.K_a] == False and pygame.key.get_pressed()[pygame.K_LEFT] == False and pygame.key.get_pressed()[pygame.K_d] == False and pygame.key.get_pressed()[pygame.K_RIGHT] == False:
                self.delay = 0
                
            if self.delay > 0:
                self.delay += 1

            if self.delay == 200:
                self.delay = 0
                    
    def numbcheck(self, laserterminal, laser, alert):
        if self.opening:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                if self.choose != self.winnumb:
                    alert.active = True
                
                laserterminal.opened = True
                laserterminal.opening = False
                laser.active = False
                self.opening = False
                self.cut = True


    def draw(self):
        if self.opening:
            win.blit(self.image, (275, 100))

            win.blit(self.pathimage1, (275, 100))
            win.blit(self.pathimage2, (275, 100))
            win.blit(self.pathimage3, (275, 100))

            win.blit(self.scissors, (self.scisx, 580))

    def update(self, laserterminal, laser, alert):
        self.game()
        self.numbcheck(laserterminal, laser, alert)
            
class Ladder(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.image = pygame.image.load("tex\game\LadderImage.png")
        self.rect = pygame.Rect(self.x+28, self.y, 4, 194)

        self.onladder = False

    def draw(self):
        win.blit(self.image, (self.x, self.y + 100))

        '''
        pygame.draw.rect(win, (255,0,0), self.rect, 5)
        '''

    def go_up_down(self, player):
        if self.rect.colliderect(player.rect):
            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                self.onladder = True
                
                if player.y > self.y+32:
                    player.climbingDown = False
                    player.climbingUp = True
                    
                    player.active = False
                    player.y -= 1
                    

            if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
                self.onladder = True
                
                if player.y < self.y+132:
                    player.climbingDown = True
                    player.climbingUp = False
                    
                    player.active = False
                    player.x = self.x + 5
                    player.y += 1

            if player.y == self.y+32 or player.y == self.y+132:
                player.active = True
                self.onladder = False
                player.climbing = False
                player.climbingDown = False
                player.climbingUp = False
                player.imageclimbc = 0
                
            if self.onladder:
                player.climbing = True
                player.hidden = False
                player.hiding = False
                player.imagehiddenc = 0
                player.x = self.x + 5

    def update(self, player):
        self.go_up_down(player)

class Shadow(pygame.sprite.Sprite):
    def __init__(self, x, y, w):
        super().__init__()

        self.x = x
        self.y = y
        self.w = w

        self.image = pygame.Rect(self.x, self.y, self.w+40, 94)
        self.rect = pygame.Rect(self.x, self.y, self.w, 94)

        self.c = 0

    def checkcollision(self, player):
        if self.rect.colliderect(player.rect) and player.active and player.visible:
            if player.moving == False:
                self.c +=1
                player.hiding = True
                if self.c == 40:
                    self.c = 0
                    player.hidden = True
            
            if player.moving:
                self.c = 0
                player.hidden = False
                player.imagehiddenc = 0
                player.hiding = False

            if player.using:
                player.hidden = False

        elif player.active==False:
            player.hidden = False

    def draw(self):
        pass
        '''
        pygame.draw.rect(win, (255,255,0), self.rect, 5)
        '''

    def update(self, player):
        self.checkcollision(player)
        

class Camera(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.x = x
        self.y = y

class Camerahitbox(pygame.sprite.Sprite):
    def __init__(self, wallcoords1, wallcoords2, camera):
        super().__init__()

        self.sound = pygame.mixer.Sound("CameraSound.wav")
        self.schannel = pygame.mixer.Channel(7)

        self.schannel.set_volume(0.3)

        self.cameraimage = pygame.image.load("tex\game\Camera\CameraLeft.png")

        self.beamnothing = pygame.image.load("tex\game\Camera\CameraBeamNothing.png")
        self.beamattention = pygame.image.load("tex\game\Camera\CameraBeamAttention.png")
        self.beamalert = pygame.image.load("tex\game\Camera\CameraBeamAlert.png")
        
        self.x = wallcoords1.x + 10
        self.camx = camera.x
        self.y = camera.y
        self.rx = wallcoords2.x

        self.left = 1
        self.leftc = 0

        self.right = 0
        self.rightc = 0

        self.mid = 0
        self.midc = 0

        self.waittillalarm = 0

        self.rect = pygame.Rect(0,0,0,0)

        self.alert = False
        self.alertc = 0

        self.attention = False

        self.attentionicon = pygame.transform.scale(pygame.image.load("tex\game\AttentionIcon.png"), (30, 40))

        self.alerticon = pygame.image.load("tex\game\AlertIcon.png")

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.attention:
                if self.waittillalarm == 1:
                    self.schannel.play(self.sound, 0, 300)

    def count(self):
        if self.alert == False:
            if self.left:
                self.leftc+=1
                if self.leftc==195:
                    self.rightc=0
                    self.left=0
                    self.mid=1

            if self.mid:
                self.midc+=1
                if self.midc==50:
                    self.midc=0
                    self.mid=0
                    if self.leftc==0:
                        self.left=1

                    if self.rightc==0:
                        self.right=1

            if self.right:
                self.rightc+=1
                if self.rightc==195:
                    self.leftc=0
                    self.right=0
                    self.mid=1

        if self.alert:
            self.midc = 0
            self.mid = False
            self.alertc += 1

            if self.alertc == 50:
                self.alertc = 0
                if self.attention == False:
                    if self.right == 1:
                        self.right = 0
                        self.left = 1
                        self.leftc = 0
                        self.rightc = 195

                    elif self.left == 1:
                        self.left = 0
                        self.right = 1
                        self.leftc = 195
                        self.rightc = 0

                    elif self.mid:
                        self.right = 1
                        self.left = 0
                        self.rightc = 0
                        self.leftc = 195

    def changepos(self):
        if self.left == 1:
            self.rect = pygame.Rect(self.x, self.y, self.camx-30-self.x, 94)

        if self.right == 1:
            self.rect = pygame.Rect(self.camx+60, self.y, self.rx-self.camx-60, 94)

        if self.mid:
            self.rect = pygame.Rect(-100, -100, 1, 1)

    def checkcollide(self, player, alert):
        self.attention = False
        if alert.active == False:
            self.alert = False

        if alert.active:
            self.alert = True
            
        if self.rect.colliderect(player.rect) and player.active and player.hidden == False and player.visible:
            self.attention = True
            if alert.active == False:
                if self.left == 1:
                    self.leftc = 0

                if self.right == 1:
                    self.rightc = 0

                self.waittillalarm += 1

                if self.waittillalarm > 170:
                    alert.active = True
                    self.waittillalarm = 0

            if alert.active:
                alert.secs = 19
                alert.misecs = 99

        else:
            self.waittillalarm = 0

    def draw(self):
        if self.left == 1:
            win.blit(self.cameraimage, (self.camx-10, self.y))

        if self.mid:
            if self.leftc == 0:
                if self.midc < 26:
                    win.blit(pygame.transform.scale(pygame.transform.flip(self.cameraimage, True, False), (25, 32)), (self.camx+10, self.y))

                else:
                    win.blit(pygame.transform.scale(self.cameraimage, (25, 32)), (self.camx+5, self.y))

            if self.rightc == 0:
                if self.midc < 26:
                    win.blit(pygame.transform.scale(self.cameraimage, (25, 32)), (self.camx+5, self.y))

                else:
                    win.blit(pygame.transform.scale(pygame.transform.flip(self.cameraimage, True, False), (25, 32)), (self.camx+10, self.y))

        if self.right == 1:
            win.blit(pygame.transform.flip(self.cameraimage, True, False), (self.camx-5, self.y))
        '''
        pygame.draw.rect(win,(255,0,0), self.rect, 5)
        '''

        if self.alert == False and self.waittillalarm == 0:
            if self.left == 1:
                win.blit(self.beamnothing, (self.camx -80, self.y+10))

            if self.right == 1:
                win.blit(pygame.transform.flip(self.beamnothing, True, False), (self.camx+20, self.y+10))

        if self.alert and self.attention:
            win.blit(self.alerticon, (self.camx, self.y-47))

            if self.left == 1:
                win.blit(self.beamalert, (self.camx -80, self.y+10))

            if self.right == 1:
                win.blit(pygame.transform.flip(self.beamalert, True, False), (self.camx+20, self.y+10))

        elif self.waittillalarm>0 or self.alert:
            win.blit(self.attentionicon, (self.camx, self.y - 47))

            if self.left == 1:
                win.blit(self.beamattention, (self.camx -80, self.y+10))

            if self.right == 1:
                win.blit(pygame.transform.flip(self.beamattention, True, False), (self.camx+20, self.y+10))

    def update(self, player, alert):
        self.checkcollide(player, alert)
        self.count()
        self.changepos()

class Lift1(pygame.sprite.Sprite):
    def __init__(self, x, y, blocking):
        super().__init__()

        self.nsound = pygame.mixer.Sound("LiftNoise.wav")
        self.nschannel = pygame.mixer.Channel(13)

        self.nschannel.set_volume(0.5)

        self.csound = pygame.mixer.Sound("LiftCame.wav")
        self.cschannel = pygame.mixer.Channel(14)
        
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x+28, self.y, 4, 94)

        self.imageclosed = pygame.image.load("tex\game\Lift\LiftClosed.png")

        self.imageopened1 = pygame.image.load("tex\game\Lift\LiftOpened1.png")
        self.imageopened2 = pygame.image.load("tex\game\Lift\LiftOpened2.png")
        self.imageopened3 = pygame.image.load("tex\game\Lift\LiftOpened3.png")
        self.imageopened4 = pygame.image.load("tex\game\Lift\LiftOpened4.png")
        self.imageopened5 = pygame.image.load("tex\game\Lift\LiftOpened5.png")
        self.imageopened6 = pygame.image.load("tex\game\Lift\LiftOpened6.png")
        self.imageopened7 = pygame.image.load("tex\game\Lift\LiftOpened7.png")
        self.imageopened8 = pygame.image.load("tex\game\Lift\LiftOpened.png")

        self.imageopenedframes = [self.imageopened1, self.imageopened2, self.imageopened3, self.imageopened4, self.imageopened5, self.imageopened6, self.imageopened7, self.imageopened8]
        self.imageopenedc = 0

        self.godownlvl = 0
        self.count = 0

        self.plrshadow = pygame.image.load("tex\game\Player\PlayerShadow.png")

        self.blockimage = pygame.image.load("tex\game\Staircase\StaircaseBlockedImage.png")

        self.plrshadowx = 0
        self.plrshadowy = 0

        self.blocking = blocking

        self.col = False

        self.came = False

        self.mycame = False

    def godown(self, player):
        if self.godownlvl == 1:
            self.count += 1
            player.y += 1
            if self.nschannel.get_busy() == False:
                self.nschannel.play(self.nsound)
                
            if self.count == 100:
                self.nschannel.stop()
                self.cschannel.play(self.csound)
                
                self.godownlvl = 0
                self.count = 0
                player.active = True
                player.visible = True
                self.came = True

        if self.godownlvl == 2:
            self.count += 1
            player.y += 1
            if self.nschannel.get_busy() == False:
                self.nschannel.play(self.nsound)
                
            if self.count == 200:
                self.nschannel.stop()
                self.cschannel.play(self.csound)
                
                self.godownlvl = 0
                self.count = 0
                player.active = True
                player.visible = True
                self.came = True

        if self.godownlvl == 3:
            self.count += 1
            player.y += 1
            if self.nschannel.get_busy() == False:
                self.nschannel.play(self.nsound)
                
            if self.count == 300:
                self.nschannel.stop()
                self.cschannel.play(self.csound)
                
                self.godownlvl = 0
                self.count = 0
                player.active = True
                player.visible = True
                self.came = True

        if self.godownlvl == 4:
            self.count += 1
            player.y += 1
            if self.nschannel.get_busy() == False:
                self.nschannel.play(self.nsound)
                
            if self.count == 400:
                self.nschannel.stop()
                self.cschannel.play(self.csound)
                
                self.godownlvl = 0
                self.count = 0
                player.active = True
                player.visible = True
                self.came = True

        if self.godownlvl == 5:
            self.count += 1
            player.y += 1
            if self.nschannel.get_busy() == False:
                self.nschannel.play(self.nsound)
                
            if self.count == 500:
                self.nschannel.stop()
                self.cschannel.play(self.csound)
                
                self.godownlvl = 0
                self.count = 0
                player.active = True
                player.visible = True
                self.came = True

        if self.godownlvl == 6:
            self.count += 1
            player.y += 1
            if self.nschannel.get_busy() == False:
                self.nschannel.play(self.nsound)
                
            if self.count == 600:
                self.nschannel.stop()
                self.cschannel.play(self.csound)
                
                self.godownlvl = 0
                self.count = 0
                player.active = True
                player.visible = True
                self.came = True

        self.plrshadowx = player.x
        self.plrshadowy = player.y

    def drawplrshadows(self):
        if self.godownlvl == 1 or self.godownlvl == 2 or self.godownlvl == 3 or self.godownlvl == 4 or self.godownlvl == 5 or self.godownlvl == 6:
            win.blit(self.plrshadow, (self.plrshadowx, self.plrshadowy))
    
    def draw(self):
        if self.mycame:
            self.mycame = False
            self.imageopenedc = 70
            
        if self.imageopenedc >0:
            win.blit(self.imageopenedframes[self.imageopenedc//10], (self.x - 15, self.y))
        
        if self.col == False:
            if self.imageopenedc == 0 or self.godownlvl >0:
                win.blit(self.imageclosed, (self.x - 15, self.y))
                
            if self.imageopenedc >0:
                self.imageopenedc -= 1

        if self.col:
            if self.imageopenedc <70:
                self.imageopenedc += 1

        '''
        
        pygame.draw.rect(win,(255,0,0), self.rect,5)
        '''

        if self.blocking:
            win.blit(self.blockimage, (self.x, self.y))

    def going_down(self, player, lift2):
        if self.came:
            self.came = False
            lift2.mycame = True
            
        self.col = False
        if self.rect.colliderect(player.rect) and player.active and player.visible:
            self.col = True
            
            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                if self.blocking == False:
                    player.imagehiddenc = 0
                    player.active = False
                    player.visible = False
                    player.x = self.x + 5
                    if lift2.y - self.y == 100:
                        self.godownlvl = 1

                    if lift2.y - self.y == 200:
                        self.godownlvl = 2

                    if lift2.y - self.y == 300:
                        self.godownlvl = 3

                    if lift2.y - self.y == 400:
                        self.godownlvl = 4

                    if lift2.y - self.y == 500:
                        self.godownlvl = 5

                    if lift2.y - self.y == 600:
                        self.godownlvl = 6
    
    def update(self, player, lift2):
        self.going_down(player, lift2)
        self.godown(player)

class Lift2(pygame.sprite.Sprite):
    def __init__(self, x, y, blocking):
        super().__init__()

        self.nsound = pygame.mixer.Sound("LiftNoise.wav")
        self.nschannel = pygame.mixer.Channel(13)

        self.nschannel.set_volume(0.3)

        self.csound = pygame.mixer.Sound("LiftCame.wav")
        self.cschannel = pygame.mixer.Channel(14)
        
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x+28, self.y, 4, 94)

        self.imageclosed = pygame.image.load("tex\game\Lift\LiftClosed.png")

        self.imageopened1 = pygame.image.load("tex\game\Lift\LiftOpened1.png")
        self.imageopened2 = pygame.image.load("tex\game\Lift\LiftOpened2.png")
        self.imageopened3 = pygame.image.load("tex\game\Lift\LiftOpened3.png")
        self.imageopened4 = pygame.image.load("tex\game\Lift\LiftOpened4.png")
        self.imageopened5 = pygame.image.load("tex\game\Lift\LiftOpened5.png")
        self.imageopened6 = pygame.image.load("tex\game\Lift\LiftOpened6.png")
        self.imageopened7 = pygame.image.load("tex\game\Lift\LiftOpened7.png")
        self.imageopened8 = pygame.image.load("tex\game\Lift\LiftOpened.png")

        self.imageopenedframes = [self.imageopened1, self.imageopened2, self.imageopened3, self.imageopened4, self.imageopened5, self.imageopened6, self.imageopened7, self.imageopened8]
        self.imageopenedc = 0

        self.gouplvl = 0
        self.count = 0

        self.plrshadow = pygame.image.load("tex\game\Player\PlayerShadow.png")

        self.blockimage = pygame.image.load("tex\game\Staircase\StaircaseBlockedImage.png")
        
        self.plrshadowx = 0
        self.plrshadowy = 0

        self.blocking = blocking

        self.col = False

        self.came = False

        self.mycame = False

    def goup(self, player):
        if self.gouplvl == 1:
            self.count += 1
            player.y -= 1
            if self.nschannel.get_busy() == False:
                self.nschannel.play(self.nsound)
                
            if self.count == 100:
                self.cschannel.play(self.csound)
                self.nschannel.stop()
                
                self.gouplvl = 0
                self.count = 0
                player.active = True
                player.visible = True
                self.came = True

        if self.gouplvl == 2:
            self.count += 1
            player.y -= 1
            if self.nschannel.get_busy() == False:
                self.nschannel.play(self.nsound)
                
            if self.count == 200:
                self.nschannel.stop()
                self.cschannel.play(self.csound)
                
                self.gouplvl = 0
                self.count = 0
                player.active = True
                player.visible = True
                self.came = True

        if self.gouplvl == 3:
            self.count += 1
            player.y -= 1
            if self.nschannel.get_busy() == False:
                self.nschannel.play(self.nsound)
                
            if self.count == 300:
                self.nschannel.stop()
                self.cschannel.play(self.csound)
                
                self.gouplvl = 0
                self.count = 0
                player.active = True
                player.visible = True
                self.came = True

        if self.gouplvl == 4:
            self.count += 1
            player.y -= 1
            if self.nschannel.get_busy() == False:
                self.nschannel.play(self.nsound)
                
            if self.count == 400:
                self.nschannel.stop()
                self.cschannel.play(self.csound)
                
                self.gouplvl = 0
                self.count = 0
                player.active = True
                player.visible = True
                self.came = True

        if self.gouplvl == 5:
            self.count += 1
            player.y -= 1
            if self.nschannel.get_busy() == False:
                self.nschannel.play(self.nsound)
                
            if self.count == 500:
                self.nschannel.stop()
                self.cschannel.play(self.csound)
                
                self.gouplvl = 0
                self.count = 0
                player.active = True
                player.visible = True
                self.came = True

        if self.gouplvl == 6:
            self.count += 1
            player.y -= 1
            if self.nschannel.get_busy() == False:
                self.nschannel.play(self.nsound)
                
            if self.count == 600:
                self.nschannel.stop()
                self.cschannel.play(self.csound)
                
                self.gouplvl = 0
                self.count = 0
                player.active = True
                player.visible = True
                self.came = True

        self.plrshadowx = player.x
        self.plrshadowy = player.y

    def drawplrshadows(self):
        if self.gouplvl == 1 or self.gouplvl == 2 or self.gouplvl == 3 or self.gouplvl == 4 or self.gouplvl == 5 or self.gouplvl == 6:
            win.blit(self.plrshadow, (self.plrshadowx, self.plrshadowy))
    
    def draw(self):
        if self.mycame:
            self.mycame = False
            self.imageopenedc = 70
            
        if self.imageopenedc >0:
            win.blit(self.imageopenedframes[self.imageopenedc//10], (self.x - 15, self.y))
        
        if self.col == False:
            if self.imageopenedc == 0 or self.gouplvl >0:
                win.blit(self.imageclosed, (self.x - 15, self.y))
                
            if self.imageopenedc >0:
                self.imageopenedc -= 1

        if self.col:
            if self.imageopenedc <70:
                self.imageopenedc += 1

        if self.blocking:
            win.blit(self.blockimage, (self.x, self.y))

        '''
        
        pygame.draw.rect(win,(255,0,0), self.rect,5)
        '''

    def going_up(self, player, lift1):
        if self.came:
            self.came = False
            lift1.mycame = True

        self.col = False
        if self.rect.colliderect(player.rect) and player.active and player.visible:
            self.col = True
            
            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                if self.blocking == False:
                    player.imagehiddenc = 0
                    player.active = False
                    player.visible = False
                    player.x = self.x + 5
                    if self.y - lift1.y == 100:
                        self.gouplvl = 1

                    if self.y - lift1.y == 200:
                        self.gouplvl = 2

                    if self.y - lift1.y == 300:
                        self.gouplvl = 3

                    if self.y - lift1.y == 400:
                        self.gouplvl = 4

                    if self.y - lift1.y == 500:
                        self.gouplvl = 5

                    if self.y - lift1.y == 600:
                        self.gouplvl = 6
    
    def update(self, player, lift1):
        self.going_up(player, lift1)
        self.goup(player)



class Staircase1(pygame.sprite.Sprite):
    def __init__(self, x, y, blocking):
        pygame.sprite.Sprite.__init__(self)

        self.sound = pygame.mixer.Sound("StaircaseSound.wav")
        self.schannel = pygame.mixer.Channel(4)

        self.schannel.set_volume(0.2)
        
        self.x = x
        self.y = y
        self.image = pygame.image.load("tex\game\Staircase\StaircaseUpImage.png")

        self.blockimage = pygame.image.load("tex\game\Staircase\StaircaseBlockedImage.png")

        self.imagegodown1 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingDown1.png")
        self.imagegodown2 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingDown2.png")
        self.imagegodown3 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingDown3.png")
        self.imagegodown4 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingDown4.png")
        self.imagegodown5 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingDown5.png")
        self.imagegodown6 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingDown6.png")
        self.imagegodown7 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingDown7.png")
        self.imagegodown8 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingDown8.png")
        self.imagegodown9 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingDown9.png")
        self.imagegodown10 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingDown10.png")
        self.imagegodown11 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingDown11.png")
        self.imagegodown12 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingDown12.png")

        self.imagegodownframes = [self.imagegodown1, self.imagegodown2, self.imagegodown3, self.imagegodown4, self.imagegodown5, self.imagegodown6, self.imagegodown7, self.imagegodown8, self.imagegodown9, self.imagegodown10, self.imagegodown11, self.imagegodown12]
        self.imagegodownc = 0
        
        self.rect = pygame.Rect(self.x+28, self.y, 4, 94)

        self.delay = 0

        self.delayfor = 0

        self.blocking = blocking

    def playsound(self, soundcontrol):
        if self.delay == 1:
            if self.delayfor == 1:
                if soundcontrol.sounds:
                    self.schannel.play(self.sound)

    def count(self, player):
        if self.delay==1:
            self.delayfor +=1
            if self.delayfor == 160:
                self.delayfor = 0
                self.delay = 0
                player.active = True
                player.visible = True

    def drawgoing(self):
        if self.delay == 0:
            self.imagegodownc = 0

        if self.delay == 1:
            if self.imagegodownc < 90:
                win.blit(self.imagegodownframes[self.imagegodownc//15], (self.x, self.y))

            if self.imagegodownc > 90:
                win.blit(self.imagegodownframes[self.imagegodownc//15], (self.x, self.y+100))
                
            if self.imagegodownc < 170:
                self.imagegodownc+=1
    
    def draw(self):
        win.blit(self.image, (self.x, self.y))

        if self.blocking:
            win.blit(self.blockimage, (self.x, self.y))

        '''
        
        pygame.draw.rect(win,(255,0,0), self.rect,5)
        '''

    def going_down(self, player):
        if self.rect.colliderect(player.rect) and player.active and player.visible:
            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                if self.blocking == False:
                    player.imagehiddenc = 0
                    player.hidden = False
                    player.hiding = False
                    player.active = False
                    player.visible = False
                    player.y += 100
                    player.x = self.x + 5
                    self.delay=1
    
    def update(self, player):
        self.count(player)
        if self.delay==0:
            self.going_down(player)
            
class Staircase2(pygame.sprite.Sprite):
    def __init__(self, x, y, blocking):
        pygame.sprite.Sprite.__init__(self)

        self.sound = pygame.mixer.Sound("StaircaseSound.wav")
        self.schannel = pygame.mixer.Channel(4)

        self.schannel.set_volume(0.2)
        
        self.x = x
        self.y = y
        self.image = pygame.image.load("tex\game\Staircase\StaircaseDownImage.png")
        self.rect = pygame.Rect(self.x+28, self.y, 4, 94)

        self.blockimage = pygame.image.load("tex\game\Staircase\StaircaseBlockedImage.png")

        self.imagegoup1 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingUp1.png")
        self.imagegoup2 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingUp2.png")
        self.imagegoup3 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingUp3.png")
        self.imagegoup4 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingUp4.png")
        self.imagegoup5 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingUp5.png")
        self.imagegoup6 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingUp6.png")
        self.imagegoup7 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingUp7.png")
        self.imagegoup8 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingUp8.png")
        self.imagegoup9 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingUp9.png")
        self.imagegoup10 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingUp10.png")
        self.imagegoup11 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingUp11.png")
        self.imagegoup12 = pygame.image.load("tex\game\Staircase\StaircasePlrGoingUp12.png")

        self.imagegoupframes = [self.imagegoup1, self.imagegoup2, self.imagegoup3, self.imagegoup4, self.imagegoup5, self.imagegoup6, self.imagegoup7, self.imagegoup8, self.imagegoup9, self.imagegoup10, self.imagegoup11, self.imagegoup12]
        self.imagegoupc = 0

        self.delay = 0

        self.delayfor = 0

        self.blocking = blocking

    def playsound(self, soundcontrol):
        if self.delay == 1:
            if self.delayfor == 1:
                if soundcontrol.sounds:
                    self.schannel.play(self.sound)

    def count(self, player):
        if self.delay==1:
            self.delayfor +=1
            if self.delayfor == 160:
                self.delayfor = 0
                self.delay = 0
                player.active = True
                player.visible = True

    def drawgoing(self):      
        if self.delay == 0:
            self.imagegoupc = 0

        if self.delay == 1:
            if self.imagegoupc < 90:
                win.blit(self.imagegoupframes[self.imagegoupc//15], (self.x, self.y))

            if self.imagegoupc > 90:
                win.blit(self.imagegoupframes[self.imagegoupc//15], (self.x, self.y-100))
                
            if self.imagegoupc < 170:
                self.imagegoupc+=1
    
    def draw(self):
        win.blit(self.image, (self.x, self.y))

        if self.blocking:
            win.blit(self.blockimage, (self.x, self.y))

        '''
        
        pygame.draw.rect(win,(255,0,0), self.rect,5)
        '''

    def going_up(self, player):
        if self.rect.colliderect(player.rect) and player.active and player.visible:
            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                if self.blocking == False:
                    player.imagehiddenc = 0
                    player.hidden = False
                    player.hiding = False
                    player.active = False
                    player.visible = False
                    player.y -= 100
                    player.x = self.x + 5
                    self.delay=1

    def update(self, player):
        self.count(player)
        if self.delay==0:
            self.going_up(player)

class AttackHitbox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.rx = 0
        self.lx = 0
        self.y = player.y +10
        self.w = 0
        self.h = 45

        self.rect = 0

        self.use = False
        self.side = 0

        self.delay = 0

        self.stopped = False

    def idle(self, player):
        self.rect = pygame.Rect(-100, -100, 0, 0)
        
        self.rx = player.x + 35
        self.lx = player.x+15
        self.y = player.y +10

        if player.movingR:
            self.side = 1

        if player.movingL:
            self.side = 0

    def attacking(self):
        if self.use:
            if self.side == 0:
                if self.delay<20:
                    self.delay += 1
                    self.w += 2
                    self.lx -= self.delay*2

                if self.delay == 20:
                    self.delay = 0
                    self.w = 0
                    self.lx = 0
                    self.use = False

                self.rect = pygame.Rect(self.lx, self.y, self.w, self.h)
                    
            if self.side == 1:
                if self.delay<20:
                    self.delay += 1
                    self.w += 2

                if self.delay == 20:
                    self.delay = 0
                    self.w = 0
                    self.use = False
                
                self.rect = pygame.Rect(self.rx, self.y, self.w, self.h)

    def damage(self, npc):
        self.stopped = False
        if self.rect.colliderect(npc.rect):
            if npc.canshoot == False:
                npc.stopped = True
                npc.stoppedc = 0

    def draw(self):
        '''
        pygame.draw.rect(win, (255,0,255), self.rect, 5)
        '''

    def update(self, player):
        self.idle(player)
        self.attacking()
        

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.gosound = pygame.mixer.Sound("GoSound.wav")
        self.goschannel = pygame.mixer.Channel(2)

        self.hitsound = pygame.mixer.Sound("HitSound.wav")
        self.hitschannel = pygame.mixer.Channel(3)

        self.hitschannel.set_volume(0.2)

        self.moneysound = pygame.mixer.Sound("MoneySound.wav")
        self.moneyschannel = pygame.mixer.Channel(5)

        self.moneyschannel.set_volume(0.6)

        self.psound = pygame.mixer.Sound("PlayerLaugh.wav")
        self.pschannel = pygame.mixer.Channel(16)

        self.pschannel.set_volume(0.5)
        
        self.w=50
        self.h=60
        self.x=x
        self.y=y
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        self.imageidle = pygame.image.load("tex\game\Player\PlayerIdle.png")

        self.imagehidden1 = pygame.image.load("tex\game\Player\PlayerHiding1.png")
        self.imagehidden2 = pygame.image.load("tex\game\Player\PlayerHiding2.png")
        self.imagehidden3 = pygame.image.load("tex\game\Player\PlayerHiding3.png")
        self.imagehidden4 = pygame.image.load("tex\game\Player\PlayerHiding4.png")

        self.imagehiddenframes = [self.imagehidden1, self.imagehidden2, self.imagehidden3, self.imagehidden4]
        self.imagehiddenc = 0

        self.imagebackwards = pygame.image.load("tex\game\Player\PlayerBackwards.png")

        self.imagegoleft1 = pygame.image.load("tex\game\Player\PlayerGoLeft1.png")
        self.imagegoleft2 = pygame.image.load("tex\game\Player\PlayerGoLeft2.png")
        self.imagegoleft3 = pygame.image.load("tex\game\Player\PlayerGoLeft3.png")
        self.imagegoleft4 = pygame.image.load("tex\game\Player\PlayerGoLeft4.png")
        self.imagegoleft5 = pygame.image.load("tex\game\Player\PlayerGoLeft5.png")
        self.imagegoleft6 = pygame.image.load("tex\game\Player\PlayerGoLeft6.png")
        self.imagegoleft7 = pygame.image.load("tex\game\Player\PlayerGoLeft7.png")
        self.imagegoleft8 = pygame.image.load("tex\game\Player\PlayerGoLeft8.png")
        self.imagegoleft9 = pygame.image.load("tex\game\Player\PlayerGoLeft9.png")

        self.imagegoleftframes = [self.imagegoleft1, self.imagegoleft2, self.imagegoleft3, self.imagegoleft4, self.imagegoleft5, self.imagegoleft6, self.imagegoleft7, self.imagegoleft8, self.imagegoleft9]
        self.imagegoleftc = 0

        self.imagegoright1 = pygame.image.load("tex\game\Player\PlayerGoRight1.png")
        self.imagegoright2 = pygame.image.load("tex\game\Player\PlayerGoRight2.png")
        self.imagegoright3 = pygame.image.load("tex\game\Player\PlayerGoRight3.png")
        self.imagegoright4 = pygame.image.load("tex\game\Player\PlayerGoRight4.png")
        self.imagegoright5 = pygame.image.load("tex\game\Player\PlayerGoRight5.png")
        self.imagegoright6 = pygame.image.load("tex\game\Player\PlayerGoRight6.png")
        self.imagegoright7 = pygame.image.load("tex\game\Player\PlayerGoRight7.png")
        self.imagegoright8 = pygame.image.load("tex\game\Player\PlayerGoRight8.png")
        self.imagegoright9 = pygame.image.load("tex\game\Player\PlayerGoRight9.png")

        self.imagegorightframes = [self.imagegoright1, self.imagegoright2, self.imagegoright3, self.imagegoright4, self.imagegoright5, self.imagegoright6, self.imagegoright7, self.imagegoright8, self.imagegoright9]
        self.imagegorightc = 0

        self.imageclimb1 = pygame.image.load("tex\game\Player\PlayerClimbing1.png")
        self.imageclimb2 = pygame.image.load("tex\game\Player\PlayerClimbing2.png")
        self.imageclimb3 = pygame.image.load("tex\game\Player\PlayerClimbing3.png")
        self.imageclimb4 = pygame.image.load("tex\game\Player\PlayerClimbing4.png")
        self.imageclimb5 = pygame.image.load("tex\game\Player\PlayerClimbing5.png")
        self.imageclimb6 = pygame.image.load("tex\game\Player\PlayerClimbing6.png")
        self.imageclimb7 = pygame.image.load("tex\game\Player\PlayerClimbing7.png")
        self.imageclimb8 = pygame.image.load("tex\game\Player\PlayerClimbing8.png")

        self.imageclimbframes = [self.imageclimb1, self.imageclimb2, self.imageclimb3, self.imageclimb4, self.imageclimb5, self.imageclimb6, self.imageclimb7, self.imageclimb8]
        self.imageclimbc = 1

        self.imageattackleft1 = pygame.image.load("tex\game\Player\PlayerAttackLeft1.png")
        self.imageattackleft2 = pygame.image.load("tex\game\Player\PlayerAttackLeft2.png")
        self.imageattackleft3 = pygame.image.load("tex\game\Player\PlayerAttackLeft3.png")
        self.imageattackleft4 = pygame.image.load("tex\game\Player\PlayerAttackLeft4.png")
        self.imageattackleft5 = pygame.image.load("tex\game\Player\PlayerAttackLeft5.png")
        self.imageattackleft6 = pygame.image.load("tex\game\Player\PlayerAttackLeft6.png")

        self.imageattackleftframes = [self.imageattackleft1, self.imageattackleft2, self.imageattackleft3, self.imageattackleft4, self.imageattackleft5, self.imageattackleft6]
        self.imageattackc = 0

        self.active = True

        self.visible = True

        self.hidden = False

        self.hiding = False

        self.moving = False
        self.movingR = False
        self.movingL = False

        self.using = False

        self.climbing = False
        self.climbingUp = False
        self.climbingDown = False

        self.cangoright = True

        self.cangoleft = True

        self.money = 0

        self.attacking = False

        self.attackdel = 0

        self.death = False

        self.random = random.randint(0,10)

    def healthchk(self, health):
        if health.health == 0:
            self.death = True

    def playsound(self, soundcontrol):
        if self.moving:
            if soundcontrol.sounds:
                if self.goschannel.get_busy() == False:
                    self.goschannel.play(self.gosound, 0, 400)

        if self.moving == False:
            self.goschannel.stop()

        if self.attacking:
            if soundcontrol.sounds:
                self.hitschannel.play(self.hitsound)

    def npccol(self, npc):
        if self.rect.colliderect(npc.rect):
            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                if npc.stopped:
                    if self.visible:
                        if npc.cangrabmoney:
                            npc.cangrabmoney = False

                            npc.moneycatch = True

                            self.moneyschannel.play(self.moneysound)

                            self.pschannel.play(self.psound, 0, 560)

        if npc.moneycame:
            self.money += 10
                
        if npc.shooting:
            self.death = True
            
            
        if npc.dashing:
            if self.death == False:
                if npc.x> player.x:
                    npc.x -=2

                if npc.x<player.x:
                    npc.x += 2

                if self.rect.colliderect(npc.rect):
                    self.death = True

    def attack(self, attackhtbx, lasergame):
        if player.active and player.visible:
            if self.climbing == False:
                if lasergame.opening == False:
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        if self.attackdel == 0:
                            attackhtbx.use = True
                            attackhtbx.w = -2
                            attackhtbx.delay = 0
                            self.attacking = True
                            self.attackdel =1

                    if self.attackdel == 30:
                        self.attackdel = 0

                    if self.attackdel == 2:
                        self.attacking = False

                    if self.attackdel >0:
                        self.attackdel += 1
            

    def moneycol(self, money):
        if self.rect.colliderect(money.rect):
            if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                if self.visible:
                    money.rect = pygame.Rect(-100, -100, 0, 0)

                    money.catch = True

                    self.moneyschannel.play(self.moneysound)

                    if self.random == 1:
                        self.pschannel.play(self.psound, 0, 560)

        if money.came:
            self.money += money.amount   
            money.kill()

    def lockscol(self, lock):
        if self.rect.colliderect(lock.rect):
            if lock.opening == False and lock.open == False:
                if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                    lock.open = True
                    
                if lock.active:
                    lock.kill()
    
    def draw(self):
        if self.visible:
            if self.using:
                win.blit(self.imagebackwards, (self.x, self.y))
                self.hidden = False

            if self.attackdel >0:
                if self.movingL:
                    win.blit(self.imageattackleftframes[self.imageattackc//5], (self.x-15, self.y))

                if self.movingR:
                    win.blit(pygame.transform.flip(self.imageattackleftframes[self.imageattackc//5], True, False), (self.x+15, self.y))

                if self.movingL == False and self.movingR == False:
                    win.blit(self.imageattackleftframes[self.imageattackc//5], (self.x-15, self.y))

                if self.imageattackc < 25:
                    self.imageattackc += 1

            if self.attackdel == 0:
                self.imageattackc = 0
                
            if self.climbing:
                self.moving = False
                self.movingR = False
                self.movingL = False
                
                win.blit(self.imageclimbframes[self.imageclimbc//10], (self.x, self.y))

                if self.climbingUp:
                    self.climbingUp = False
                    
                    self.imageclimbc += 1
                    if self.imageclimbc == 70:
                        self.imageclimbc = 0

                if self.climbingDown:
                    self.climbingDown = False
                    
                    if self.imageclimbc >0:
                        self.imageclimbc -= 1
                        
                    if self.imageclimbc == 0:
                        self.imageclimbc = 70

                if self.imageclimbc >70 or self.imageclimbc <0:
                    self.imageclimbc = 0
                        
            if self.hiding == False:
                if self.moving == False and self.hidden == False and self.climbing == False and self.using == False:
                    self.imagegoleftc = 0
                    self.imagegorightc = 0
                    
                    win.blit(self.imageidle, (self.x, self.y))

                if self.moving:
                    if self.movingL:
                        win.blit(self.imagegoleftframes[self.imagegoleftc//8], (self.x, self.y))
                        self.imagegoleftc += 1
                        if self.imagegoleftc == 72:
                            self.imagegoleftc = 0

                    if self.movingL == False:
                        self.imagegoleftc = 0

                    if self.movingR:
                        win.blit(self.imagegorightframes[self.imagegorightc//8], (self.x, self.y))
                        self.imagegorightc += 1
                        if self.imagegorightc == 72:
                            self.imagegorightc = 0

                    if self.movingR == False:
                        self.imagegorightc = 0

            if self.hiding and self.using == False:
                if self.imagehiddenc < 30:
                    self.imagehiddenc += 1
                    if self.imagehiddenc == 30:
                        self.hiding = False

            if self.using == False:
                if self.attackdel == 0:
                    if self.imagehiddenc> 0:
                        win.blit(self.imagehiddenframes[self.imagehiddenc//10], (self.x, self.y-self.imagehiddenc//10))

                if self.attackdel >0:
                    if self.imagehiddenc > 0:
                        self.imagehiddenc = 0
                        
                        win.blit(self.imageidle, (self.x, self.y))

                        self.hidden = False
                
    def checkcolL(self, wall):
        if self.rect.colliderect(wall.rect):
            if wall.cancollide:
                self.cangoright = False

    def checkcolR(self, wall):
        if self.rect.colliderect(wall.rect):
            if wall.cancollide:
                self.cangoleft = False

    def moveidle(self):
        self.moving = False

    def cango(self):
        self.cangoleft = True
        self.cangoright = True

    def move(self):
        if self.active and self.visible:
            if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.moving = True
                self.movingR = True
                self.movingL = False
                if self.cangoright:
                    self.x+=1
            
            if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
                self.moving = True
                self.movingL = True
                self.movingR = False
                if self.cangoleft:
                    self.x-=1

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.random = random.randint(0,10)
        self.moveidle()
        self.move()
        self.cango()

class Floor:
    def __init__(self,x, y, w):
        self.x = x
        self.y=y
        self.w = w

    def draw(self):
        pygame.draw.rect(win,(50,50,50),(self.x,self.y,self.w,8))



class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(win, (50,50,50), (self.x, self.y, 10, 100))

class WallBlockedL(pygame.sprite.Sprite):
    def __init__(self, x, y, islocked, canopen):
        super().__init__()
        
        self.x = x
        self.y=y

        self.islocked = islocked

        self.cancollide = True

        self.canopen = canopen

        self.rect = pygame.Rect(self.x-4,self.y+4,4,92)

    def lockstatus(self):
        if self.islocked == True:
            self.cancollide = True

        else:
            self.cancollide = False

    def draw(self):
        pass
        '''
        pygame.draw.rect(win,(255, 0,255), self.rect)
        '''

class WallBlockedR(pygame.sprite.Sprite):
    def __init__(self, x, y, islocked, canopen):
        super().__init__()
        
        self.x = x
        self.y=y

        self.islocked = islocked

        self.cancollide = True

        self.canopen = canopen

        self.rect = pygame.Rect(self.x+10,self.y+4,4,92)

    def lockstatus(self):
        if self.islocked == True:
            self.cancollide = True

        else:
            self.cancollide = False

    def draw(self):
        pass

        '''
        pygame.draw.rect(win,(255, 0,255), self.rect)
        '''

class Lock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.wsound = pygame.mixer.Sound("LockOpened.wav")
        self.schannel = pygame.mixer.Channel(15)

        self.lsound = pygame.mixer.Sound("LockOpenedFail.wav")

        self.x = x
        self.y = y

        self.w = 30
        self.h = 30

        self.visible = True

        self.opening = False
        self.active = False

        self.rect = pygame.Rect(self.x, self.y+10, self.w, self.h-20)
        self.imageoutside = pygame.image.load("tex\game\Lock\LockImageOutside.png")

        self.winimage = pygame.image.load("tex\game\Lock\LockImageInside.png")

        self.imageopening1 = pygame.image.load("tex\game\Lock\LockImageInsideOpening1.png")
        self.imageopening2 = pygame.image.load("tex\game\Lock\LockImageInsideOpening2.png")
        self.imageopening3 = pygame.image.load("tex\game\Lock\LockImageInsideOpening3.png")
        self.imageopening4 = pygame.image.load("tex\game\Lock\LockImageInsideOpening4.png")
        self.imageopening5 = pygame.image.load("tex\game\Lock\LockImageInsideOpening5.png")
        self.imageopening6 = pygame.image.load("tex\game\Lock\LockImageInsideOpening6.png")
        self.imageopening7 = pygame.image.load("tex\game\Lock\LockImageInsideOpening7.png")

        self.imageopeningframes = [self.imageopening1, self.imageopening2, self.imageopening3, self.imageopening4, self.imageopening5, self.imageopening6, self.imageopening7]
        self.imageopeningc = 0
        
        self.delay = False
        self.delayc = 0

        self.delayend = False
        self.delaycend = 0

        self.success = False

        self.successc = 0

        self.onetime = 0

        self.open = False

    def playsound(self, soundcontrol):
        if soundcontrol.sounds:
            if self.success:
                if self.delaycend == 1:
                    self.schannel.play(self.wsound, 0, 800)

            if self.success == False:
                if self.delaycend == 1:
                    self.schannel.play(self.lsound)
        
    def cooldown(self):
        if self.delay:
            self.delayc += 1
            if self.delayc == 50:
                self.delayc = 0
                self.delay = False

    def activate(self, wall1, wall2):
        if wall1.cancollide and wall2.cancollide:
            if self.open:
                self.open = False
                self.opening = True
                self.delay = True
                player.active = False

    def game(self, lockhitbox, lockmovingpart, wall1, wall2):
        if self.opening:
            
            if self.delay == False:
                if self.delayend == False:
                    if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
                        if lockhitbox.rect.colliderect(lockmovingpart.rect):
                            self.success = True
                            self.delayend = True

                        else:
                            self.success = False
                            self.delayend = True
                            if self.onetime == 0:
                                lockhitbox.y -= 10
                                self.onetime = 1

    def ending(self, lockhitbox, lockmovingpart):
        if self.delayend:
            lockmovingpart.canmove = False
            self.delaycend += 1
            if self.success:
                self.successc += 1
                if self.successc<19:
                    lockhitbox.y -= 10
                    
            if self.delaycend == 100:
                self.opening = False
                self.delaycend = 0
                self.delayend = False
                self.successc = 0

    def deactivate(self, wall1, wall2, player, lockmovingpart, lockhitbox):
        if self.opening == False:
            self.imageopeningc = 0
            
            player.active  = True
            
            lockmovingpart.canmove = True
            
            self.onetime = 0
            
            if self.success:
                wall1.cancollide = False
                wall2.cancollide = False
                self.success = False
                self.visible = False
                self.active = True
        
    def draw(self):
        if self.visible:
            '''
            pygame.draw.rect(win, (255,0,0), self.rect, 5)
            '''
            
            win.blit(self.imageoutside, (self.x, self.y))

    def drawwin(self):
        if self.opening:
            if self.success == False or self.delaycend <21:
                win.blit(self.winimage, (300, 50))

            if self.delaycend > 20 and self.success:
                if self.delaycend < 55:
                    self.imageopeningc += 1
                    
                win.blit(self.imageopeningframes[self.imageopeningc//5], (300, 50))

            

    def update(self, wall1, wall2, player, lockmovingpart, lockhitbox):
        self.activate(wall1, wall2)
        self.cooldown()
        self.game(lockhitbox, lockmovingpart, wall1, wall2)
        self.ending(lockhitbox, lockmovingpart)
        self.deactivate(wall1, wall2, player, lockmovingpart, lockhitbox)
        


class LockHTBX(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 495
        self.y = 320
        self.w = 10
        self.h = 300

        self.image = pygame.image.load("tex\game\Lock\LockStickImage.png")
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h-160)

    def rectupdate(self):
        self.y = 320
        self.x = 495

    def draw(self):
        win.blit(self.image, (self.x, self.y+140))

        '''

        pygame.draw.rect(win, (255,0,0), self.rect, 3)
        '''

class LockMovingPart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.x = 530
        self.y = 320
        self.w = 60
        self.h = 140

        self.c = 0

        self.counts = [[1,0],[1,1],[2,0],[2,1]]

        self.choosen = [1,0]

        self.rect = pygame.Rect(self.x+10, self.y, self.w-20, self.h)

        self.image = pygame.image.load("tex\game\Lock\LockMovingPartImage.png")

        self.canmove = True

    def count(self):
        self.c +=1
        if self.c == 20:
            self.c = 0
            self.choosen = random.choice(self.counts)
        
    def move(self):
        if self.canmove:
            if self.choosen[1]==0:
                if self.x>314:
                    self.x -= self.choosen[0]

            if self.choosen[1]==1:
                if self.x<624:
                    self.x += self.choosen[0]

            if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
                if self.x<624:
                    self.x += 3

            elif pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
                if self.x>314:
                    self.x -= 3

    def rectupdate(self):
        self.rect = pygame.Rect(self.x+10, self.y, self.w-20, self.h)

    def draw(self):
        win.blit(self.image, (self.x, self.y))
        '''
            
        pygame.draw.rect(win, (150,0,0), self.rect, 3)
        '''

    def update(self):
        self.count()
        self.move()
        self.rectupdate()

cursor = Cursor()

walls = pygame.sprite.Group()

wallsBlockedL=pygame.sprite.Group()

wallsBlockedR=pygame.sprite.Group()

SpecwallsBlockedL=pygame.sprite.Group()

SpecwallsBlockedR=pygame.sprite.Group()

strcase1=pygame.sprite.Group()

strcase2=pygame.sprite.Group()

lifts1 = pygame.sprite.Group()

lifts2 = pygame.sprite.Group()

cameras = pygame.sprite.Group()

cameras_hitbox = pygame.sprite.Group()

shadows = pygame.sprite.Group()

ladders = pygame.sprite.Group()

locks = pygame.sprite.Group()

npcs = pygame.sprite.Group()

npchitboxes = pygame.sprite.Group()

lasers = pygame.sprite.Group()

laserterminals = pygame.sprite.Group()

passwords = pygame.sprite.Group()

codedlock = pygame.sprite.Group()

moneys = pygame.sprite.Group()

alertwalls = pygame.sprite.Group()

hints = pygame.sprite.Group()

sounds = Sounds()

music = Music()

soundcontrol = SoundControl()

#ОСНОВНЫЕ ПЕРЕМЕННЫЕ

loadingimage = pygame.image.load("tex\CreditImage.png")

transitionc = 0

loadingtxt = pygame.font.SysFont('Comic Sans MS', 50)
loadingtxtr = loadingtxt.render("Загрузка...", True,(255, 255, 255))

wait = False

welcome = Welcome()

levelsmap = LevelsMap()

#LVL 1############################################################

lvl1gameimage = pygame.image.load("tex\lvl1\Lvl1GameImage.png")

#LVL 2############################################################

lvl2gameimage1 = pygame.image.load("tex\lvl2\Lvl2GameImage1.png")

lvl2gameimage2 = pygame.image.load("tex\lvl2\Lvl2GameImage2.png")

lvl2gameimage3 = pygame.image.load("tex\lvl2\Lvl2GameImage3.png")

lvl2gameimage4 = pygame.image.load("tex\lvl2\Lvl2GameImage4.png")

lvl2gameimage5 = pygame.image.load("tex\lvl2\Lvl2GameImage5.png")

lvl2gameimage6 = pygame.image.load("tex\lvl2\Lvl2GameImage6.png")

lvl2gameimage7 = pygame.image.load("tex\lvl2\Lvl2GameImage7.png")

lvl2gameimage8 = pygame.image.load("tex\lvl2\Lvl2GameImage8.png")

lvl2gameimage9 = pygame.image.load("tex\lvl2\Lvl2GameImage9.png")

lvl2gameimage10 = pygame.image.load("tex\lvl2\Lvl2GameImage10.png")

lvl2gameimage11 = pygame.image.load("tex\lvl2\Lvl2GameImage11.png")

lvl2gameimage12 = pygame.image.load("tex\lvl2\Lvl2GameImage12.png")

lvl2gameimage13 = pygame.image.load("tex\lvl2\Lvl2GameImage13.png")

lvl2gameimage14 = pygame.image.load("tex\lvl2\Lvl2GameImage14.png")

lvl2gameimage15 = pygame.image.load("tex\lvl2\Lvl2GameImage15.png")

lvl2gameimage16 = pygame.image.load("tex\lvl2\Lvl2GameImage16.png")

#LVL 3############################################################

lvl3gameimage1 = pygame.image.load("tex\lvl3\Lvl3GameImage1.png")

lvl3gameimage2 = pygame.image.load("tex\lvl3\Lvl3GameImage2.png")

lvl3gameimage3 = pygame.image.load("tex\lvl3\Lvl3GameImage3.png")

lvl3gameimage4 = pygame.image.load("tex\lvl3\Lvl3GameImage4.png")

lvl3gameimage5 = pygame.image.load("tex\lvl3\Lvl3GameImage5.png")

lvl3gameimage6 = pygame.image.load("tex\lvl3\Lvl3GameImage6.png")

lvl3gameimage7 = pygame.image.load("tex\lvl3\Lvl3GameImage7.png")

lvl3gameimage8 = pygame.image.load("tex\lvl3\Lvl3GameImage8.png")

lvl3gameimage9 = pygame.image.load("tex\lvl3\Lvl3GameImage9.png")

lvl3gameimage10 = pygame.image.load("tex\lvl3\Lvl3GameImage10.png")

lvl3gameimage11 = pygame.image.load("tex\lvl3\Lvl3GameImage11.png")

lvl3gameimage12 = pygame.image.load("tex\lvl3\Lvl3GameImage12.png")

lvl3gameimage13 = pygame.image.load("tex\lvl3\Lvl3GameImage13.png")

lvl3gameimage14 = pygame.image.load("tex\lvl3\Lvl3GameImage14.png")

lvl3gameimage15 = pygame.image.load("tex\lvl3\Lvl3GameImage15.png")

#LVL 4############################################################

lvl4gameimage1 = pygame.image.load("tex\lvl4\Lvl3GameImage1.png")

lvl4gameimage2 = pygame.image.load("tex\lvl4\Lvl3GameImage2.png")

lvl4gameimage3 = pygame.image.load("tex\lvl4\Lvl3GameImage3.png")

lvl4gameimage4 = pygame.image.load("tex\lvl4\Lvl3GameImage4.png")

lvl4gameimage5 = pygame.image.load("tex\lvl4\Lvl3GameImage5.png")

lvl4gameimage6 = pygame.image.load("tex\lvl4\Lvl3GameImage6.png")

lvl4gameimage7 = pygame.image.load("tex\lvl4\Lvl3GameImage7.png")

lvl4gameimage8 = pygame.image.load("tex\lvl4\Lvl3GameImage8.png")

lvl4gameimage9 = pygame.image.load("tex\lvl4\Lvl3GameImage9.png")

lvl4gameimage10 = pygame.image.load("tex\lvl4\Lvl3GameImage10.png")

lvl4gameimage11 = pygame.image.load("tex\lvl4\Lvl3GameImage11.png")

lvl4gameimage12 = pygame.image.load("tex\lvl4\Lvl3GameImage12.png")

lvl4gameimage13 = pygame.image.load("tex\lvl4\Lvl3GameImage13.png")

lvl4gameimage14 = pygame.image.load("tex\lvl4\Lvl3GameImage14.png")

lvl4gameimage15 = pygame.image.load("tex\lvl4\Lvl3GameImage15.png")

lvl4gameimage16 = pygame.image.load("tex\lvl4\Lvl3GameImage16.png")

lvl4gameimage17 = pygame.image.load("tex\lvl4\Lvl3GameImage17.png")

lvl4gameimage18 = pygame.image.load("tex\lvl4\Lvl3GameImage18.png")

lvl4gameimage19 = pygame.image.load("tex\lvl4\Lvl3GameImage19.png")

#LVL 5############################################################

lvl5gameimage1 = pygame.image.load("tex\lvl5\Lvl3GameImage1.png")

lvl5gameimage2 = pygame.image.load("tex\lvl5\Lvl3GameImage2.png")

lvl5gameimage3 = pygame.image.load("tex\lvl5\Lvl3GameImage3.png")

lvl5gameimage4 = pygame.image.load("tex\lvl5\Lvl3GameImage4.png")

lvl5gameimage5 = pygame.image.load("tex\lvl5\Lvl3GameImage5.png")

lvl5gameimage6 = pygame.image.load("tex\lvl5\Lvl3GameImage6.png")

lvl5gameimage7 = pygame.image.load("tex\lvl5\Lvl3GameImage7.png")

lvl5gameimage8 = pygame.image.load("tex\lvl5\Lvl3GameImage8.png")

lvl5gameimage9 = pygame.image.load("tex\lvl5\Lvl3GameImage9.png")

lvl5gameimage10 = pygame.image.load("tex\lvl5\Lvl3GameImage10.png")

lvl5gameimage11 = pygame.image.load("tex\lvl5\Lvl3GameImage11.png")

lvl5gameimage12 = pygame.image.load("tex\lvl5\Lvl3GameImage12.png")

lvl=-1

lvl_chk=1

quitlvl = False

floors=[]

lvlcomplete = False

moneyall = 0

lvlcompletec = 0

WinSound = pygame.mixer.Sound("GameWinSound.wav")
WinChannel = pygame.mixer.Channel(17)

LoseSound = pygame.mixer.Sound("GameLoseSound.wav")
LoseChannel = pygame.mixer.Channel(17)

playing = False

lvlreload = False

lose = False

losec = 0

game = True

run = True

once = 1    

while run:
    for  eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            run = False

    pygame.time.delay(3)
    win.fill((0,0,0))

    cursor.update()
            
    if lvl == -1:
        soundcontrol.menubgmus()
        
        if wait == False:
            welcome.col(cursor)

            soundcontrol.b = 1

            sounds.col(cursor)

            music.col(cursor)

            soundcontrol.mute(sounds, music)

        welcome.draw()

        sounds.draw()

        music.draw()

        if welcome.lvl == 0:
            wait = True

    if lvl == 0:
        soundcontrol.menubgmus()

        if wait == False:
            levelsmap.col(cursor)

            sounds.col(cursor)

            music.col(cursor)

            soundcontrol.mute(sounds, music)

            soundcontrol.b = 1

        levelsmap.draw()

        levelsmap.carddraw(cursor)

        sounds.draw()
        music.draw()

        if levelsmap.lvl == -1:
            wait = True

        if levelsmap.lvl == 1 or levelsmap.lvl == 2 or levelsmap.lvl == 3 or levelsmap.lvl == 4 or levelsmap.lvl == 5 or levelsmap.lvl == 6 or levelsmap.lvl == 7:
            wait = True

        lvl_chk = 1

    if lvlreload:
        if quitlvl == False:
            lvl_chk = 1

        if quitlvl:
            quitlvl = False

        lvlreload = False

        floors = []

        for i in walls:
            i.kill()
        
        del player

        del attackhtbx

        del lasergame

        del lockhitbox

        del lockmovingpart

        del type1
        del type2
        del type3
        del type4
        del type5
        del type6
        del type7
        del type8
        del type9
        del type0

        del hud

        del health

        del time

        del moneyc

        del retry

        del pause

        del alert

        for i in wallsBlockedL:
            i.kill()

        for i in wallsBlockedR:
            i.kill()

        for i in strcase1:
            i.kill()

        for i in strcase2:
            i.kill()

        for i in lifts1:
            i.kill()

        for i in lifts2:
            i.kill()

        for i in shadows:
            i.kill()

        for i in cameras:
            i.kill()

        for i in cameras_hitbox:
            i.kill()

        for i in ladders:
            i.kill()

        for i in locks:
            i.kill()

        for i in lasers:
            i.kill()

        for i in laserterminals:
            i.kill()

        for i in passwords:
            i.kill()

        for i in hints:
            i.kill()

        for i in codedlock:
            i.kill()

        for i in moneys:
            i.kill()

        for i in npcs:
            i.kill()

        for i in npchitboxes:
            i.kill()

        del robmission

        del placeout

        for i in alertwalls:
            i.kill()

    if lvl==1 and lvl_chk==1:
        levelsmap.lvl = 0

        soundcontrol.a = 1

        playing = True

        #ОСНОВНЫЕ

        player = Player(870, 300)

        attackhtbx = AttackHitbox()

        lasergame = LaserGame()

        lockhitbox = LockHTBX()

        lockmovingpart = LockMovingPart()

        type1 = Type1()

        type2 = Type2()

        type3 = Type3()

        type4 = Type4()

        type5 = Type5()

        type6 = Type6()

        type7 = Type7()

        type8 = Type8()

        type9 = Type9()

        type0 = Type0()

        hud = Hud()

        health = Health()

        time = Time()

        moneyc = Moneycount()

        retry = Retry()

        pause = Pause()

        alert = Alert()

        #ПОЛ

        for i in range(7):
            sumif=i*100

            if i>1 and i<7:
                floors.append(Floor(0,61+sumif, 1000))

        #СТЕНЫ

        for i in range(7):
            sumiw=i*100
                    
            if i==2:
                walls.add(Wall(0,65+sumiw))

                walls.add(Wall(255,65+sumiw))

                walls.add(Wall(715,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            if i==3:
                walls.add(Wall(415,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            if i==4:
                walls.add(Wall(0,65+sumiw))

                walls.add(Wall(235,65+sumiw))

                walls.add(Wall(515,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            if i==5:
                walls.add(Wall(0,65+sumiw))

                walls.add(Wall(315,65+sumiw))

                walls.add(Wall(755,65+sumiw))

                walls.add(Wall(990,65+sumiw))


        for i in range(7):
            sumiw = i*100
            if i == 2:
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 3:
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 4:
                wallsBlockedL.add(WallBlockedL(235, 65+sumiw, True, True))

                wallsBlockedL.add(WallBlockedL(515, 65+sumiw, False, False))
                    
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 5:
                wallsBlockedL.add(WallBlockedL(755, 65+sumiw, False, False))

                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

        for i in range(7):
            sumiw = i*100
            if i == 2:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

            if i == 3:
                wallsBlockedR.add(WallBlockedR(-10, 65+sumiw, False, False))

            if i == 4:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(235, 65+sumiw, True, False))
                    
                wallsBlockedR.add(WallBlockedR(515, 65+sumiw, False, False))

            if i == 5:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(755, 65+sumiw, False, False))

        #ЛЕСТНИЧНЫЕ ПРОЕМЫ

        for i in range(7):
            sumi=i*100
            if i == 3:
                strcase1.add(Staircase1(820,68+sumi, False))

            if i == 4:
                strcase1.add(Staircase1(660,68+sumi, False))

                strcase2.add(Staircase2(820,68+sumi, False))

            if i == 5:
                strcase2.add(Staircase2(660,68+sumi, True))

        #ЛИФТЫ

        for i in range(7):
            sumi = i*100
            if i == 2:
                lifts1.add(Lift1(50,68+sumi, False))

        for i in range(7):
            sumi = i*100
            if i == 4:
                lifts2.add(Lift2(50,68+sumi, False))

        #ТЕНИ

        shadows.add(Shadow(200, 268, 240))

        shadows.add(Shadow(630, 268, 160))

            

        shadows.add(Shadow(10, 368, 170))

        shadows.add(Shadow(330, 368, 360))

        shadows.add(Shadow(900, 368, 90))
        

        shadows.add(Shadow(150, 468, 260))

        shadows.add(Shadow(525, 468, 95))


        shadows.add(Shadow(10, 568, 50))

        shadows.add(Shadow(250, 568, 140))

        shadows.add(Shadow(690, 568, 65))

        #КАМЕРА

        cameras.add(Camera(500, 268))
        cameras_hitbox.add(Camerahitbox(walls.sprites()[1], walls.sprites()[2], cameras.sprites()[0]))

        #ЛЕСТНИЦА

        ladders.add(Ladder(420, 468))

        ladders.add(Ladder(940, 468))

        #ЗАМКИ
        
        locks.add(Lock(207, 510))
            
        #ЛАЗЕРЫ

        lasers.add(Laser(540, 368))

        laserterminals.add(LaserTerminal(540, 368))

        #ПАРОЛИ

        passwords.add(Password(70, 568))

        codedlock.add(CodedDoor(630, 568))

        #ЗАПИСКИ

        hints.add(Hint(730, 268, "Приветствую, дружище! Это пробная миссия,", "по результатам которой мы сможем определить,", "подойдешь ли ты к нам в отряд. В комнатах", "есть слепые зоны для камер и охранников.",
                       "Стой на месте, чтобы пропасть из их поля зрения.", "Камеры смотрят сначала вправо, потом влево", "и так далее. Если успеешь поймать момент для", "перебежки, то они тебя не заметят. И даже если",
                       "заметят, знай, что они перешлют сигнал проис-", "шествия только через некоторое время. Удачи!", "Чуть не забыл, в шкафах есть деньги!", "Чтобы их собрать, нажми на 'w' или стрелочку вверх."))

        hints.add(Hint(150, 268, "Чтож, недурно для первого раза! (надеюсь ты ", "обошёлся без сигнализации) Теперь тебе нужно", "попасть на другие этажи. В этом тебе поможет", "cтарый добрый лифт. Он может перевезти тебя",
                       "на любой этаж какой тебе надо. Тут я думаю", " и так все ясно.", "Нажми на 'w' или стрелочку вверх, чтобы зайти", " в лифт", "", "", "", ""))

        hints.add(Hint(20, 468, "А вот и первая сложная задача - замок.", "Тут тебе потребуется подвинуть деталь замка", "так, чтобы отмычка, находящаяся снизу, могла", "свободно пройти сквозь неё, и вуаля - дверь ",
                       "открыта! Нажми на 'a' или стрелочку влево, ", "чтобы двигать деталь замка влево, а 'd' или ", "стрелочку вправо, чтобы двигать вправо. Если ", "считаешь, что деталь совпадает с отмычкой, ",
                       "нажми на 'w' или стрелочку вверх, чтобы открыть ", "замок.", "", ""))

        hints.add(Hint(320, 468, "Вижу ты справился с замком, но это не все", "испытания, которые тебе придётся пройти.", "По всей видимости, у арендодателя дома не ",
                       "хватило денег на несколько лифтов! Но это ", "вовсе не проблема, ведь есть лестница!", "Чтобы спускаться зажми 's' или стрелочку ",
                       "вниз, чтобы подниматься зажми 'w' ", "или стрелочку вверх.", "", "", "", ""))

        hints.add(Hint(400, 568, "Вот тут и начинаются проблемы! Охранники,", "в отличие, от камер могут и покалечить!", "Только не волнуйся, этот так не умеет!",
                       "Если пройдёшь эту миссию, то узнаешь и о ", "других, но об этом потом. Ты можешь прятаться", "от охранников, как и от камер. Но если тебе не",
                       "по нраву их физиономии, ты можешь навалять им!", "Для этого у тебя была палка (но как она там", "оказалась?). Чтобы её использовать, нажми на",
                       "пробел. Кстати, охранникам тоже платят,", "потому ты можешь забрать у них деньги!", "Для этого нажми на 'w' или стрелочку вверх."))

        hints.add(Hint(730, 568, "Если ты был достаточно внимателен, то ты,", "вероятно, прочитал ту записку с цифрами. Теп-", "ерь подумай, для чего же она нужна, видя кодов-", "ый замок? Разумеется это код от запертой двери!",
                       "Чтобы его ввести нажми 'w' или стрелочку", "вверх, а дальше все проще некуда. Главное", "не забудь код! Он не всегда будет находиться", "так близко к двери!", "", "", "", ""))

        hints.add(Hint(610, 468, "Судя по всему, ты догадался как войти в", "дверь. Смекалка в этом деле тоже важна!", "Прибор, находящийся слева, найдёт в тебе", "навыки электрика. Когда откроешь щиток,",
                       "Тебе всего лишь надо будет выбрать провод,", "который не вызовет сигнализацию. Для этого", "нужно внимательно осмотреть каждый провод и", "выбрать тот, на конце которого нарисован желтый",
                       "значок. Он просто отключит лазеры сверху.", "Для выбора между проводами используй тe", "же кнопки, что и для движения игрока.", "Чтобы отрезать провод, нажми пробел."))

        hints.add(Hint(900, 468, "Надеюсь, что ты это прочтёшь, ведь", "в ином случае ты можешь пропустить то,", "за чем тебя сюда прислали! Внизу находится", "мешок с деньгами. Забери его и прийди",
                       "к точке назначения. Там мы с командой тебя", "заберём. Если ты ещё дойдёшь.. На этом", "подсказки заканчиваются. Пока!", "", "", "", "", ""))

        #ДЕНЬГИ

        moneys.add(Money(150, 268, 10))

        moneys.add(Money(300, 268, 15))

        moneys.add(Money(565, 268, 15))

        moneys.add(Money(678, 268, 5))

        moneys.add(Money(832, 268, 10))

        moneys.add(Money(125, 368, 15))

        moneys.add(Money(248, 368, 10))

        moneys.add(Money(384, 368, 5))

        moneys.add(Money(466, 368, 10))

        moneys.add(Money(610, 368, 5))

        moneys.add(Money(942, 368, 15))

        moneys.add(Money(282, 468, 10))

        moneys.add(Money(386, 468, 10))

        moneys.add(Money(770, 468, 15))

        moneys.add(Money(360, 568, 15))

        moneys.add(Money(590, 568, 5))

        moneys.add(Money(790, 568, 15))

        #ВРАГИ

        npcs.add(Npc(100, 600, walls.sprites()[10], walls.sprites()[11], 0))
        npchitboxes.add(NpcHTBX(walls.sprites()[10], walls.sprites()[11]))

        #МЕСТО КРАЖИ

        robmission = RobMission(810, 568)

        #МЕСТО ПОБЕГА
        
        placeout = PlaceOut(50, 368)



        alert.activeonce = 0

        

        lvl_chk=0

    if lvl==2 and lvl_chk==1:
        levelsmap.lvl = 0

        soundcontrol.a = 1

        playing = True

        #ОСНОВНЫЕ

        player = Player(100, 200)

        attackhtbx = AttackHitbox()

        lasergame = LaserGame()

        lockhitbox = LockHTBX()

        lockmovingpart = LockMovingPart()

        type1 = Type1()

        type2 = Type2()

        type3 = Type3()

        type4 = Type4()

        type5 = Type5()

        type6 = Type6()

        type7 = Type7()

        type8 = Type8()

        type9 = Type9()

        type0 = Type0()

        hud = Hud()

        health = Health()

        time = Time()

        moneyc = Moneycount()

        retry = Retry()

        pause = Pause()

        alert = Alert()

    #ПОЛ

        for i in range(7):
            sumif=i*100
            if i==1:
                floors.append(Floor(300,61+sumif, 360))
            elif i > 1 and i <7:
                floors.append(Floor(0,61+sumif, 1000))

    #СТЕНЫ

        for i in range(7):
            sumiw=i*100
            if i==1:
                walls.add(Wall(300,65+sumiw))
                    
                walls.add(Wall(650,65+sumiw))
                    
            if i==2:
                walls.add(Wall(0,65+sumiw))
                walls.add(Wall(140,65+sumiw))
                walls.add(Wall(420,65+sumiw))
                walls.add(Wall(990,65+sumiw))

            if i==3:
                walls.add(Wall(0,65+sumiw))
                
                walls.add(Wall(500,65+sumiw))
        
                walls.add(Wall(710,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            if i==4:
                walls.add(Wall(0,65+sumiw))
                    
                walls.add(Wall(280,65+sumiw))
                    
                walls.add(Wall(620,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            if i==5:
                walls.add(Wall(0,65+sumiw))
                    
                walls.add(Wall(320,65+sumiw))

                walls.add(Wall(770,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            
        for i in range(7):
            sumiw = i*100
            if i == 1:
                wallsBlockedL.add(WallBlockedL(300, 65+sumiw, True, True))

                wallsBlockedL.add(WallBlockedL(650, 65+sumiw, False, False))

            if i == 2:
                wallsBlockedL.add(WallBlockedL(140, 65+sumiw, True, False))

                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 3:
                wallsBlockedL.add(WallBlockedL(500, 65+sumiw, True, True))

                wallsBlockedL.add(WallBlockedL(710, 65+sumiw, False, False))
                
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 4:
                wallsBlockedL.add(WallBlockedL(280, 65+sumiw, False, False))
                    
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 5:
                wallsBlockedL.add(WallBlockedL(320, 65+sumiw, True, False))

                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))


        for i in range(7):
            sumiw = i*100
            if i == 1:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(300, 65+sumiw, True, False))

            if i == 2:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(140, 65+sumiw, True, True))

            if i == 3:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(500, 65+sumiw, True, False))

                wallsBlockedR.add(WallBlockedR(710, 65+sumiw, True, False))

            if i == 4:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))
                    
                wallsBlockedR.add(WallBlockedR(280, 65+sumiw, False, False))

            if i == 5:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(320, 65+sumiw, True, True))

        #ЛЕСТНИЧНЫЕ ПРОЕМЫ

        for i in range(7):
            sumi=i*100
            if i == 1:
                strcase1.add(Staircase1(500,68+sumi, False))

            if i == 2:
                strcase2.add(Staircase2(500,68+sumi, False))

            if i == 3:
                strcase1.add(Staircase1(740,68+sumi, False))

            if i == 4:
                strcase1.add(Staircase1(20,68+sumi, False))
                
                strcase2.add(Staircase2(740,68+sumi, False))

            if i == 5:
                strcase2.add(Staircase2(20,68+sumi, False))

        #ЛИФТЫ

        for i in range(7):
            sumi = i*100
            if i == 2:
                lifts1.add(Lift1(870,68+sumi, True))

        for i in range(7):
            sumi = i*100
            if i == 5:
                lifts2.add(Lift2(870,68+sumi, False))

        #ТЕНИ

        shadows.add(Shadow(310, 168, 60))

        shadows.add(Shadow(560, 168, 650))
        

        shadows.add(Shadow(430, 268, 160))

        shadows.add(Shadow(910, 268, 990))
        
        
        shadows.add(Shadow(0, 368, 40))

        shadows.add(Shadow(420, 368, 80))

        shadows.add(Shadow(510, 368, 40))
        

        shadows.add(Shadow(210, 468, 70))

        shadows.add(Shadow(290, 468, 90))

        shadows.add(Shadow(630, 468, 50))


        shadows.add(Shadow(10, 568, 40))

        shadows.add(Shadow(260, 568, 60))

        shadows.add(Shadow(330, 568, 60))

        shadows.add(Shadow(710, 568, 60))

        #КАМЕРА

        cameras.add(Camera(420, 168))
        cameras_hitbox.add(Camerahitbox(walls.sprites()[0], walls.sprites()[1], cameras.sprites()[0]))

        cameras.add(Camera(810, 468))
        cameras_hitbox.add(Camerahitbox(walls.sprites()[12], walls.sprites()[13], cameras.sprites()[1]))

        cameras.add(Camera(460, 568))
        cameras_hitbox.add(Camerahitbox(walls.sprites()[15], walls.sprites()[16], cameras.sprites()[2]))

        #ЛЕСТНИЦА

        ladders.add(Ladder(230, 268))

        ladders.add(Ladder(410, 468))

        #ЗАМКИ
        
        locks.add(Lock(270, 210))

        locks.add(Lock(150, 310))

        locks.add(Lock(470, 410))

        locks.add(Lock(330, 610))
            
        #ЛАЗЕРЫ

        lasers.add(Laser(620, 268))

        laserterminals.add(LaserTerminal(620, 268))

        lasers.add(Laser(580, 468))

        laserterminals.add(LaserTerminal(580, 468))

        #ПАРОЛИ

        passwords.add(Password(20, 268))

        codedlock.add(CodedDoor(840, 268))

        #ЗАПИСКИ

        hints.add(Hint(560, 268, "Отлично! Ты справился с проверочным", "заданием! Мы тут подумали и решили принять", "тебя к нам! Поздравляю!", "Кстати, помнишь как я тебе обещал рассказать", "о других охранниках? Так вот за дверью",
                       "слева стоит действительно опасный тип. Если", "он тебя заметит - БЕГИ! Иначе он прибьёт тебя", "дубинкой и мы останемся без денег! Он", "достаточно шустрый, поэтому не советую",
                       "попадаться ему на глаза вообще. Желаю удачи!", "", ""))
        
        hints.add(Hint(950, 268, "Так, к слову. Лифты тоже умеют запирать..", "Дальше без подсказок, окей? Тут все просто.", "", "", "", "", "", "", "", "", "", ""))
        
        #ДЕНЬГИ

        moneys.add(Money(365, 168, 10))

        moneys.add(Money(592, 168, 10))

        moneys.add(Money(70, 268, 15))

        moneys.add(Money(120, 268, 10))

        moneys.add(Money(310, 268, 15))

        moneys.add(Money(380, 268, 10))

        moneys.add(Money(460, 268, 10))

        moneys.add(Money(670, 268, 5))

        moneys.add(Money(800, 268, 15))

        moneys.add(Money(400, 368, 15))

        moneys.add(Money(540, 368, 10))

        moneys.add(Money(580, 368, 10))

        moneys.add(Money(840, 368, 10))

        moneys.add(Money(110, 468, 10))

        moneys.add(Money(140, 468, 10))

        moneys.add(Money(170, 468, 10))

        moneys.add(Money(230, 468, 15))

        moneys.add(Money(380, 468, 10))

        moneys.add(Money(500, 468, 15))

        moneys.add(Money(680, 468, 10))

        moneys.add(Money(890, 468, 10))

        moneys.add(Money(120, 568, 10))

        moneys.add(Money(735, 568, 15))

        moneys.add(Money(840, 568, 10))

        #ВРАГИ

        npcs.add(Npc(200, 300, walls.sprites()[3], walls.sprites()[4], 2))
        npchitboxes.add(NpcHTBX(walls.sprites()[3], walls.sprites()[4]))

        npcs.add(Npc(300, 400, walls.sprites()[6], walls.sprites()[7], 0))
        npchitboxes.add(NpcHTBX(walls.sprites()[6], walls.sprites()[7]))

        npcs.add(Npc(150, 600, walls.sprites()[14], walls.sprites()[15], 0))
        npchitboxes.add(NpcHTBX(walls.sprites()[14], walls.sprites()[15]))

        #МЕСТО КРАЖИ

        robmission = RobMission(860, 368)

        #МЕСТО ПОБЕГА
        
        placeout = PlaceOut(20, 368)

        

        alert.activeonce = 0

        lvl_chk=0

    if lvl==3 and lvl_chk==1:
        levelsmap.lvl = 0

        soundcontrol.a = 1

        playing = True

        #ОСНОВНЫЕ

        player = Player(20, 600)

        attackhtbx = AttackHitbox()

        lasergame = LaserGame()

        lockhitbox = LockHTBX()

        lockmovingpart = LockMovingPart()

        type1 = Type1()

        type2 = Type2()

        type3 = Type3()

        type4 = Type4()

        type5 = Type5()

        type6 = Type6()

        type7 = Type7()

        type8 = Type8()

        type9 = Type9()

        type0 = Type0()

        hud = Hud()

        health = Health()

        time = Time()

        moneyc = Moneycount()

        retry = Retry()

        pause = Pause()

        alert = Alert()

    #ПОЛ

        for i in range(7):
            sumif=i*100
            if i > 1 and i <5:
                floors.append(Floor(94,61+sumif, 906))
            elif i > 4 and i <7:
                floors.append(Floor(0,61+sumif, 1000))

    #СТЕНЫ

        for i in range(7):
            sumiw=i*100
            if i==2:
                walls.add(Wall(94,65+sumiw))
                walls.add(Wall(410,65+sumiw))
                walls.add(Wall(780,65+sumiw))
                walls.add(Wall(990,65+sumiw))

            if i==3:
                walls.add(Wall(94,65+sumiw))
                
                walls.add(Wall(300,65+sumiw))
        
                walls.add(Wall(740,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            if i==4:
                walls.add(Wall(94,65+sumiw))
                    
                walls.add(Wall(350,65+sumiw))
                    
                walls.add(Wall(700,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            if i==5:
                walls.add(Wall(280,65+sumiw))

                walls.add(Wall(750,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            
        for i in range(7):
            sumiw = i*100
            if i == 2:
                wallsBlockedL.add(WallBlockedL(780, 65+sumiw, True, True))

                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 3:
                wallsBlockedL.add(WallBlockedL(300, 65+sumiw, False, False))

                wallsBlockedL.add(WallBlockedL(740, 65+sumiw, False, False))
                
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 4:
                wallsBlockedL.add(WallBlockedL(94, 65+sumiw, True, False))
                
                wallsBlockedL.add(WallBlockedL(350, 65+sumiw, False, False))

                wallsBlockedL.add(WallBlockedL(700, 65+sumiw, True, False))
                    
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 5:
                wallsBlockedL.add(WallBlockedL(750, 65+sumiw, True, True))

                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))


        for i in range(7):
            sumiw = i*100
            if i == 2:
                wallsBlockedR.add(WallBlockedR(94, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(780, 65+sumiw, True, False))

            if i == 3:
                wallsBlockedR.add(WallBlockedR(94, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(300, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(740, 65+sumiw, False, False))

            if i == 4:
                wallsBlockedR.add(WallBlockedR(-10, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(94, 65+sumiw, True, True))

                wallsBlockedR.add(WallBlockedR(350, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(700, 65+sumiw, True, True))

            if i == 5:
                wallsBlockedR.add(WallBlockedR(-10, 65+sumiw, False, False))
                    
                wallsBlockedR.add(WallBlockedR(750, 65+sumiw, True, False))

        #ЛЕСТНИЧНЫЕ ПРОЕМЫ

        for i in range(7):
            sumi=i*100
            if i == 3:
                strcase1.add(Staircase1(230,68+sumi, True))

                strcase1.add(Staircase1(770,68+sumi, False))

            if i == 4:
                strcase2.add(Staircase2(230,68+sumi, False))

                strcase2.add(Staircase2(770,68+sumi, False))
                
                strcase1.add(Staircase1(910,68+sumi, False))

            if i == 5:
                strcase2.add(Staircase2(910,68+sumi, False))

        #ЛИФТЫ

        for i in range(7):
            sumi = i*100
            if i == 2:
                lifts1.add(Lift1(480,68+sumi, False))

        for i in range(7):
            sumi = i*100
            if i == 4:
                lifts2.add(Lift2(480,68+sumi, False))

        #ТЕНИ

        shadows.add(Shadow(104, 268, 60))

        shadows.add(Shadow(790, 268, 60))
        
        
        shadows.add(Shadow(250, 368, 50))

        shadows.add(Shadow(640, 368, 100))

        shadows.add(Shadow(750, 368, 60))
        

        shadows.add(Shadow(104, 468, 70))

        shadows.add(Shadow(710, 468, 60))

        shadows.add(Shadow(930, 468, 60))


        shadows.add(Shadow(0, 568, 100))

        shadows.add(Shadow(220, 568, 60))

        shadows.add(Shadow(760, 568, 60))

        shadows.add(Shadow(940, 568, 50))

        #КАМЕРА

        cameras.add(Camera(490, 368))
        cameras_hitbox.add(Camerahitbox(walls.sprites()[5], walls.sprites()[6], cameras.sprites()[0]))

        cameras.add(Camera(470, 568))
        cameras_hitbox.add(Camerahitbox(walls.sprites()[12], walls.sprites()[13], cameras.sprites()[1]))

        #ЛЕСТНИЦА

        ladders.add(Ladder(120, 268))

        ladders.add(Ladder(680, 268))

        ladders.add(Ladder(590, 468))

        #ЗАМКИ
        
        locks.add(Lock(750, 310))

        locks.add(Lock(104, 510))

        locks.add(Lock(710, 510))

        locks.add(Lock(720, 610))
            
        #ЛАЗЕРЫ

        lasers.add(Laser(340, 268))

        laserterminals.add(LaserTerminal(340, 268))

        lasers.add(Laser(840, 468))

        laserterminals.add(LaserTerminal(840, 468))

        #ПАРОЛИ

        passwords.add(Password(950, 268))

        codedlock.add(CodedDoor(200, 368))

        #ДЕНЬГИ

        moneys.add(Money(205, 268, 15))

        moneys.add(Money(260, 268, 10))

        moneys.add(Money(310, 268, 10))

        moneys.add(Money(250, 268, 10))

        moneys.add(Money(590, 268, 15))

        moneys.add(Money(915, 268, 5))

        moneys.add(Money(415, 368, 10))

        moneys.add(Money(560, 368, 10))

        moneys.add(Money(625, 368, 10))

        moneys.add(Money(840, 368, 10))

        moneys.add(Money(175, 468, 5))

        moneys.add(Money(320, 468, 15))

        moneys.add(Money(390, 468, 15))

        moneys.add(Money(445, 468, 5))

        moneys.add(Money(885, 468, 10))

        moneys.add(Money(150, 568, 10))

        moneys.add(Money(180, 568, 15))

        moneys.add(Money(320, 568, 10))

        moneys.add(Money(390, 568, 15))

        moneys.add(Money(470, 568, 5))

        moneys.add(Money(675, 568, 15))

        moneys.add(Money(800, 568, 10))

        #ВРАГИ

        npcs.add(Npc(620, 300, walls.sprites()[1], walls.sprites()[2], 2))
        npchitboxes.add(NpcHTBX(walls.sprites()[1], walls.sprites()[2]))

        npcs.add(Npc(500, 500, walls.sprites()[9], walls.sprites()[10], 2))
        npchitboxes.add(NpcHTBX(walls.sprites()[9], walls.sprites()[10]))

        #МЕСТО КРАЖИ

        robmission = RobMission(900, 368)

        #МЕСТО ПОБЕГА
        
        placeout = PlaceOut(120, 468)

        

        alert.activeonce = 0

        lvl_chk=0

        

    if lvl==4 and lvl_chk==1:
        levelsmap.lvl = 0

        soundcontrol.a = 1

        playing = True

        #ОСНОВНЫЕ

        player = Player(450, 100)

        attackhtbx = AttackHitbox()

        lasergame = LaserGame()

        lockhitbox = LockHTBX()

        lockmovingpart = LockMovingPart()

        type1 = Type1()

        type2 = Type2()

        type3 = Type3()

        type4 = Type4()

        type5 = Type5()

        type6 = Type6()

        type7 = Type7()

        type8 = Type8()

        type9 = Type9()

        type0 = Type0()

        hud = Hud()

        health = Health()

        time = Time()

        moneyc = Moneycount()

        retry = Retry()

        pause = Pause()

        alert = Alert()
        
        #ПОЛ

        for i in range(7):
            sumif=i*100
            if i==0:
                floors.append(Floor(0,61+sumif, 300))
            else:
                floors.append(Floor(0,61+sumif, 1000))

        #СТЕНЫ

        for i in range(7):
            sumiw=i*100
            if i==0:
                walls.add(Wall(0,65+sumiw))
                    
                walls.add(Wall(290,65+sumiw))
                    
            if i==1:
                walls.add(Wall(0,65+sumiw))

                walls.add(Wall(395,65+sumiw))
                    
                walls.add(Wall(990,65+sumiw))
                    
            if i==2:
                walls.add(Wall(0,65+sumiw))
                walls.add(Wall(165,65+sumiw))
                walls.add(Wall(595,65+sumiw))
                walls.add(Wall(890,65+sumiw))

            if i==3:
                walls.add(Wall(0,65+sumiw))
        
                walls.add(Wall(595,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            if i==4:
                walls.add(Wall(0,65+sumiw))
                    
                walls.add(Wall(345,65+sumiw))
                    
                walls.add(Wall(745,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            if i==5:
                walls.add(Wall(0,65+sumiw))
                    
                walls.add(Wall(295,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            
        for i in range(7):
            sumiw = i*100
            if i == 0:
                wallsBlockedL.add(WallBlockedL(1000, 65+sumiw, False, False))

            if i == 1:
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 2:
                wallsBlockedL.add(WallBlockedL(1000, 65+sumiw, False, False))

                wallsBlockedL.add(WallBlockedL(595, 65+sumiw, True, False))

            if i == 3:
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 4:
                wallsBlockedL.add(WallBlockedL(345, 65+sumiw, False, False))

                wallsBlockedL.add(WallBlockedL(745, 65+sumiw, True, True))
                    
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 5:
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

                wallsBlockedL.add(WallBlockedL(295, 65+sumiw, True, False))

        wallsBlockedL.add(WallBlockedL(550, 365, False, False))


        for i in range(7):
            sumiw = i*100
            if i == 0:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

            if i == 1:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

            if i == 2:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(595, 65+sumiw, True, True))

            if i == 3:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

            if i == 4:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))
                    
                wallsBlockedR.add(WallBlockedR(345, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(745, 65+sumiw, True, False))

            if i == 5:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(295, 65+sumiw, True, True))

        wallsBlockedR.add(WallBlockedR(550, 365, False, False))

                

        #ЛЕСТНИЧНЫЕ ПРОЕМЫ

        for i in range(4):
            sumi=i*100
            if i == 0:
                strcase1.add(Staircase1(100,68+sumi, False))

            if i == 1:
                strcase2.add(Staircase2(100,68+sumi, False))
                    
                strcase1.add(Staircase1(795,68+sumi, False))

            if i == 2:
                strcase2.add(Staircase2(795,68+sumi, False))
                    
                strcase1.add(Staircase1(45,68+sumi, True))

            if i == 3:
                strcase2.add(Staircase2(45,68+sumi, False))

        #ЛИФТЫ

        for i in range(5):
            sumi = i*100
            if i == 3:
                lifts1.add(Lift1(900,68+sumi, False))

        for i in range(5):
            sumi = i*100
            if i == 4:
                lifts2.add(Lift2(900,68+sumi, False))


        #ТЕНИ

        shadows.add(Shadow(230, 68, 60))

            

        shadows.add(Shadow(10, 168, 40))

        shadows.add(Shadow(380, 168, 230))

        shadows.add(Shadow(960, 168, 50))



        #---

            

        shadows.add(Shadow(10, 368, 40))

        shadows.add(Shadow(590, 368, 40))



        #---



        shadows.add(Shadow(290, 568, 40))

        shadows.add(Shadow(960, 568, 50))

        #КАМЕРА

        cameras.add(Camera(650, 168))
        cameras_hitbox.add(Camerahitbox(walls.sprites()[3], walls.sprites()[4], cameras.sprites()[0]))

        cameras.add(Camera(370, 268))
        cameras_hitbox.add(Camerahitbox(walls.sprites()[6], walls.sprites()[7], cameras.sprites()[1]))

        #ЛЕСТНИЦА

        ladders.add(Ladder(150, 368))

        ladders.add(Ladder(400, 468))

        ladders.add(Ladder(800, 468))

        #ЗАМКИ
        
        locks.add(Lock(605, 310))
            
        locks.add(Lock(715, 510))
            
        locks.add(Lock(305, 610))
            
        #ЛАЗЕРЫ

        lasers.add(Laser(270, 368))

        laserterminals.add(LaserTerminal(270, 368))

        #ПАРОЛИ

        passwords.add(Password(950, 168))

        codedlock.add(CodedDoor(110, 268))

        #ЗАПИСКИ

        hints.add(Hint(850, 468, "Ого! Да ты неплохо влился в нашу компанию!", "Тут казалось бы легкая миссия, но", "охранник внизу уже действительно опасен.", "Если ты попадёшься к нему на глаза,", "он может достать оружие и обезвредить",
                       "тебя моментально! НИ В КОЕМ СЛУЧАЕ НЕ", "ХОДИ ВОЗЛЕ НЕГО ВО ВРЕМЯ СИГНАЛИЗАЦИИ!!", "Как только он тебя увидет - тебе крышка!", "так что будь с ним особо внимателен.",
                       "постарайся не подвести меня и свою шкуру", "заодно! Чуть не забыл, этот тип достаточно силён,", "так что вырубить его обычной палкой не выйдет"))

        #ДЕНЬГИ

        moneys.add(Money(50, 68, 10))

        moneys.add(Money(200, 68, 5))

        moneys.add(Money(50, 168, 15))

        moneys.add(Money(200, 168, 5))

        moneys.add(Money(450, 168, 5))

        moneys.add(Money(550, 168, 10))

        moneys.add(Money(750, 168, 5))

        moneys.add(Money(925, 168, 15))

        moneys.add(Money(250, 268, 10))

        moneys.add(Money(350, 268, 15))

        moneys.add(Money(500, 268, 5))

        moneys.add(Money(700, 268, 10))

        moneys.add(Money(400, 368, 10))

        moneys.add(Money(500, 368, 15))

        moneys.add(Money(650, 368, 5))

        moneys.add(Money(800, 368, 10))

        moneys.add(Money(50, 468, 15))

        moneys.add(Money(500, 468, 10))

        moneys.add(Money(650, 468, 15))

        moneys.add(Money(50, 568, 15))

        moneys.add(Money(150, 568, 10))

        moneys.add(Money(200, 568, 10))

        moneys.add(Money(900, 568, 5))

        #ВРАГИ

        npcs.add(Npc(200, 200, walls.sprites()[2], walls.sprites()[3], 0))
        npchitboxes.add(NpcHTBX(walls.sprites()[2], walls.sprites()[3]))

        npcs.add(Npc(650, 600, walls.sprites()[17], walls.sprites()[18], 1))
        npchitboxes.add(NpcHTBX(walls.sprites()[17], walls.sprites()[18]))

        #МЕСТО КРАЖИ

        robmission = RobMission(525, 468)

        #МЕСТО ПОБЕГА
        
        placeout = PlaceOut(950, 268)

        #СТЕНЫ ТРЕВОГИ

        alertwalls.add(AlertWall(550, 368))



        alert.activeonce = 0

        

        lvl_chk=0



    if lvl==5 and lvl_chk==1:
        levelsmap.lvl = 0

        soundcontrol.a = 1

        playing = True

        #ОСНОВНЫЕ

        player = Player(40, 600)

        attackhtbx = AttackHitbox()

        lasergame = LaserGame()

        lockhitbox = LockHTBX()

        lockmovingpart = LockMovingPart()

        type1 = Type1()

        type2 = Type2()

        type3 = Type3()

        type4 = Type4()

        type5 = Type5()

        type6 = Type6()

        type7 = Type7()

        type8 = Type8()

        type9 = Type9()

        type0 = Type0()

        hud = Hud()

        health = Health()

        time = Time()

        moneyc = Moneycount()

        retry = Retry()

        pause = Pause()

        alert = Alert()

    #ПОЛ

        for i in range(7):
            sumif=i*100
            if i > -1 and i <4:
                floors.append(Floor(700,61+sumif, 300))
            elif i > 3 and i <8:
                floors.append(Floor(0,61+sumif, 1000))

    #СТЕНЫ

        for i in range(7):
            sumiw=i*100
            if i==0:
                walls.add(Wall(700,65+sumiw))

                walls.add(Wall(850,65+sumiw))
                
                walls.add(Wall(990,65+sumiw))

            if i==1:
                walls.add(Wall(700,65+sumiw))
                
                walls.add(Wall(990,65+sumiw))

            if i==2:
                walls.add(Wall(700,65+sumiw))
                
                walls.add(Wall(990,65+sumiw))

            if i==3:
                walls.add(Wall(700,65+sumiw))

                walls.add(Wall(850,65+sumiw))
                
                walls.add(Wall(990,65+sumiw))

            if i==4:
                walls.add(Wall(0,65+sumiw))
                
                walls.add(Wall(270,65+sumiw))
        
                walls.add(Wall(600,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            if i==5:
                walls.add(Wall(0,65+sumiw))
                    
                walls.add(Wall(350,65+sumiw))
                    
                walls.add(Wall(730,65+sumiw))

                walls.add(Wall(990,65+sumiw))

            
        for i in range(7):
            sumiw = i*100
            if i == 0:
                wallsBlockedL.add(WallBlockedL(850, 65+sumiw, True, True))

                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 1:
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))
            
            if i == 2:
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 3:
                wallsBlockedL.add(WallBlockedL(700, 65+sumiw, False, False))
                
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 4:
                wallsBlockedL.add(WallBlockedL(270, 65+sumiw, False, False))
                
                wallsBlockedL.add(WallBlockedL(600, 65+sumiw, True, True))
                    
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 5:
                wallsBlockedL.add(WallBlockedL(350, 65+sumiw, False, False))

                wallsBlockedL.add(WallBlockedL(730, 65+sumiw, True, False))

                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))

            if i == 6:
                wallsBlockedL.add(WallBlockedL(990, 65+sumiw, False, False))


        for i in range(7):
            sumiw = i*100
            if i == 0:
                wallsBlockedR.add(WallBlockedR(700, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(850, 65+sumiw, True, False))
                
            if i == 1:
                wallsBlockedR.add(WallBlockedR(700, 65+sumiw, False, False))
                
            if i == 2:
                wallsBlockedR.add(WallBlockedR(700, 65+sumiw, False, False))

            if i == 3:
                wallsBlockedR.add(WallBlockedR(-10, 65+sumiw, False, False))
                
                wallsBlockedR.add(WallBlockedR(700, 65+sumiw, False, False))

            if i == 4:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(270, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(600, 65+sumiw, True, False))

            if i == 5:
                wallsBlockedR.add(WallBlockedR(0, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(350, 65+sumiw, False, False))

                wallsBlockedR.add(WallBlockedR(730, 65+sumiw, True, True))

            if i == 6:
                wallsBlockedR.add(WallBlockedR(255, 65+sumiw, False, False))

        #ЛЕСТНИЧНЫЕ ПРОЕМЫ

        for i in range(7):
            sumi=i*100
            if i == 0:
                strcase1.add(Staircase1(900,68+sumi, False))

            if i == 1:
                strcase2.add(Staircase2(900,68+sumi, False))

            if i == 2:
                strcase1.add(Staircase1(720,68+sumi, False))

            if i == 3:
                strcase2.add(Staircase2(720,68+sumi, False))

            if i == 4:
                strcase1.add(Staircase1(140,68+sumi, False))

            if i == 5:
                strcase2.add(Staircase2(140,68+sumi, False))

        #ЛИФТЫ

        for i in range(7):
            sumi = i*100
            if i == 0:
                lifts1.add(Lift1(730,68+sumi, False))

        for i in range(7):
            sumi = i*100
            if i == 4:
                lifts2.add(Lift2(730,68+sumi, True))

        #ТЕНИ

        shadows.add(Shadow(710, 68, 60))

        shadows.add(Shadow(930, 68, 60))
        

        shadows.add(Shadow(930, 168, 60))
        


        
        shadows.add(Shadow(710, 368, 60))

        shadows.add(Shadow(940, 368, 50))
        

        shadows.add(Shadow(280, 468, 70))

        shadows.add(Shadow(570, 468, 140))


        shadows.add(Shadow(10, 568, 100))

        shadows.add(Shadow(280, 568, 70))

        shadows.add(Shadow(900, 568, 90))

        
        shadows.add(Shadow(270, 668, 700))

        #КАМЕРА

        cameras.add(Camera(810, 268))
        cameras_hitbox.add(Camerahitbox(walls.sprites()[5], walls.sprites()[6], cameras.sprites()[0]))

        cameras.add(Camera(330, 468))
        cameras_hitbox.add(Camerahitbox(walls.sprites()[11], walls.sprites()[12], cameras.sprites()[1]))

        cameras.add(Camera(570, 568))
        cameras_hitbox.add(Camerahitbox(walls.sprites()[15], walls.sprites()[16], cameras.sprites()[2]))

        #ЛЕСТНИЦА

        ladders.add(Ladder(30, 368))

        ladders.add(Ladder(940, 368))

        ladders.add(Ladder(410, 468))

        ladders.add(Ladder(269, 568))

        ladders.add(Ladder(915, 568))

        #ЗАМКИ
        
        locks.add(Lock(820, 110))

        locks.add(Lock(570, 510))

        locks.add(Lock(740, 610))
            
        #ЛАЗЕРЫ

        lasers.add(Laser(880, 268))

        laserterminals.add(LaserTerminal(880, 268))

        lasers.add(Laser(500, 468))

        laserterminals.add(LaserTerminal(500, 468))

        #ПАРОЛИ

        passwords.add(Password(950, 268))

        codedlock.add(CodedDoor(700, 468))

        #ДЕНЬГИ

        moneys.add(Money(875, 68, 10))
        

        moneys.add(Money(825, 168, 10))

        moneys.add(Money(870, 168, 15))
        

        moneys.add(Money(825, 268, 10))
        

        moneys.add(Money(810, 368, 15))


        moneys.add(Money(100, 468, 10))

        moneys.add(Money(230, 468, 30))

        moneys.add(Money(320, 468, 10))

        moneys.add(Money(390, 468, 5))

        moneys.add(Money(540, 468, 10))

        moneys.add(Money(650, 468, 15))

        moneys.add(Money(890, 468, 15))


        moneys.add(Money(215, 568, 10))

        moneys.add(Money(285, 568, 10))

        moneys.add(Money(610, 568, 15))

        moneys.add(Money(685, 568, 10))

        moneys.add(Money(915, 568, 10))

        

        #ВРАГИ

        npcs.add(Npc(100, 500, walls.sprites()[10], walls.sprites()[11], 0))
        npchitboxes.add(NpcHTBX(walls.sprites()[10], walls.sprites()[11]))

        npcs.add(Npc(820, 500, walls.sprites()[12], walls.sprites()[13], 1))
        npchitboxes.add(NpcHTBX(walls.sprites()[12], walls.sprites()[13]))

        #МЕСТО КРАЖИ

        robmission = RobMission(710, 168)

        #МЕСТО ПОБЕГА
        
        placeout = PlaceOut(10, 368)

        

        alert.activeonce = 0

        lvl_chk=0

                                                                                                                                                                                #####################################################

    if lvl == 1:
        win.blit(lvl1gameimage, (0,0))
    
    if lvl == 2:
        win.blit(lvl2gameimage14, (0, 65))
        
        win.blit(lvl2gameimage15, (500, 65))
        
        win.blit(lvl2gameimage1, (310,169))

        win.blit(lvl2gameimage2, (9, 268))

        win.blit(lvl2gameimage3, (150, 268))

        win.blit(lvl2gameimage4, (424, 268))

        win.blit(lvl2gameimage5, (0, 368))

        win.blit(lvl2gameimage6, (501, 368))

        win.blit(lvl2gameimage7, (719, 368))

        win.blit(lvl2gameimage8, (10, 468))

        win.blit(lvl2gameimage9, (290, 468))

        win.blit(lvl2gameimage10, (630, 468))

        win.blit(lvl2gameimage11, (10, 568))

        win.blit(lvl2gameimage12, (330, 568))

        win.blit(lvl2gameimage13, (780, 568))

        win.blit(lvl2gameimage16, (0, 667))

    if lvl == 3:
        win.blit(lvl3gameimage13, (0, 261))
        
        win.blit(lvl3gameimage14, (0, 65))
        
        win.blit(lvl3gameimage15, (500, 65))
        
        win.blit(lvl3gameimage1, (104,268))

        win.blit(lvl3gameimage2, (420, 268))

        win.blit(lvl3gameimage3, (790, 268))

        win.blit(lvl3gameimage4, (104, 368))

        win.blit(lvl3gameimage5, (310, 368))

        win.blit(lvl3gameimage6, (750, 368))

        win.blit(lvl3gameimage7, (104, 468))

        win.blit(lvl3gameimage8, (360, 468))

        win.blit(lvl3gameimage9, (710, 468))

        win.blit(lvl3gameimage10, (2, 568))

        win.blit(lvl3gameimage11, (290, 568))

        win.blit(lvl3gameimage12, (760, 568))

        win.blit(lvl2gameimage16, (0, 667))

    if lvl == 4:
        win.blit(lvl4gameimage18, (300, 65))
        
        win.blit(lvl4gameimage19, (650, 65))
        
        win.blit(lvl4gameimage1, (10, 68))

        win.blit(lvl4gameimage2, (10, 168))

        win.blit(lvl4gameimage3, (160, 168))

        win.blit(lvl4gameimage4, (405, 168))

        win.blit(lvl4gameimage5, (700, 168))

        win.blit(lvl4gameimage6, (9, 268))

        win.blit(lvl4gameimage7, (174, 268))

        win.blit(lvl4gameimage8, (605, 268))

        win.blit(lvl4gameimage9, (10, 368))

        win.blit(lvl4gameimage10, (300, 368))

        win.blit(lvl4gameimage11, (605, 368))

        win.blit(lvl4gameimage12, (10, 468))

        win.blit(lvl4gameimage13, (355, 468))
        
        win.blit(lvl4gameimage14, (755, 468))

        win.blit(lvl4gameimage15, (10, 568))

        win.blit(lvl4gameimage16, (305, 568))

        win.blit(lvl4gameimage17, (692, 568))

        win.blit(lvl2gameimage16, (0, 667))

    if lvl == 5:
        win.blit(lvl5gameimage12, (0, 65))
        
        win.blit(lvl5gameimage11, (710, 68))

        win.blit(lvl5gameimage10, (710, 168))

        win.blit(lvl5gameimage9, (710, 268))

        win.blit(lvl5gameimage8, (710, 368))

        win.blit(lvl5gameimage7, (610, 468))

        win.blit(lvl5gameimage6, (280, 468))

        win.blit(lvl5gameimage5, (10, 468))

        win.blit(lvl5gameimage4, (740, 568))

        win.blit(lvl5gameimage3, (360, 568))

        win.blit(lvl5gameimage2, (10, 568))

    if playing == True:
        
        levelsmap.lvl1stats[3] = 0

        levelsmap.lvl2stats[3] = 0

        levelsmap.lvl3stats[3] = 0

        levelsmap.lvl4stats[3] = 0

        levelsmap.lvl5stats[3] = 0

        levelsmap.lvl6stats[3] = 0

        levelsmap.lvl7stats[3] = 0
        
        if game == True:
            
            for i in strcase1:
                i.update(player)

            for i in strcase2:
                i.update(player)

            for i in shadows:
                i.update(player)

            for i in ladders:
                i.update(player)

            if lvl == 1:
                npchitboxes.sprites()[0].update(npcs.sprites()[0], player, alert)

                lifts1.sprites()[0].update(player, lifts2.sprites()[0])

                lifts1.sprites()[0].drawplrshadows()

                lifts2.sprites()[0].update(player, lifts1.sprites()[0])

                lifts2.sprites()[0].drawplrshadows()

                for i in locks:
                    if i.opening == False:
                        lockhitbox.rectupdate()

                player.active = True

                for i in locks:
                    player.lockscol(i)

                    if i.open:
                        i.update(wallsBlockedL.sprites()[2], wallsBlockedR.sprites()[3], player, lockmovingpart, lockhitbox)

                    if i.opening:
                        i.update(wallsBlockedL.sprites()[2], wallsBlockedR.sprites()[3], player, lockmovingpart, lockhitbox)
                        i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[2], wallsBlockedR.sprites()[3])

                        player.active = False

                if lasergame.opening:
                    player.active = False

            if lvl == 2:
                npchitboxes.sprites()[0].update(npcs.sprites()[0], player, alert)

                npchitboxes.sprites()[1].update(npcs.sprites()[1], player, alert)

                npchitboxes.sprites()[2].update(npcs.sprites()[2], player, alert)

                lifts1.sprites()[0].update(player, lifts2.sprites()[0])

                lifts1.sprites()[0].drawplrshadows()

                lifts2.sprites()[0].update(player, lifts1.sprites()[0])

                lifts2.sprites()[0].drawplrshadows()

                c = 0
                
                for i in locks:
                    if i.opening == False:
                        c += 1
                        if len(locks.sprites())==1:
                            lockhitbox.rectupdate()

                    if len(locks.sprites())==4:
                        if c == 4:
                            lockhitbox.rectupdate()

                    if len(locks.sprites())==3:
                        if c == 3:
                            lockhitbox.rectupdate()

                    if len(locks.sprites())==2:
                        if c == 2:
                            lockhitbox.rectupdate()


                c = 0

                player.active = True

                for i in locks:
                    player.lockscol(i)
                        
                    if i.open:
                        if i.x == 270 and i.y == 210:
                            i.update(wallsBlockedL.sprites()[0], wallsBlockedR.sprites()[1], player, lockmovingpart, lockhitbox)
                        
                        elif i.x == 150 and i.y == 310:
                            i.update(wallsBlockedL.sprites()[2], wallsBlockedR.sprites()[3], player, lockmovingpart, lockhitbox)

                        elif i.x == 470 and i.y == 410:
                            i.update(wallsBlockedL.sprites()[4], wallsBlockedR.sprites()[5], player, lockmovingpart, lockhitbox)

                        elif i.x == 330 and i.y == 610:
                            i.update(wallsBlockedL.sprites()[9], wallsBlockedR.sprites()[10], player, lockmovingpart, lockhitbox)

                    if i.opening:
                        if i.x == 270 and i.y == 210:
                            i.update(wallsBlockedL.sprites()[0], wallsBlockedR.sprites()[1], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[0], wallsBlockedR.sprites()[1])

                        elif i.x == 150 and i.y == 310:
                            i.update(wallsBlockedL.sprites()[2], wallsBlockedR.sprites()[3], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[2], wallsBlockedR.sprites()[3])

                        elif i.x == 470 and i.y == 410:
                            i.update(wallsBlockedL.sprites()[4], wallsBlockedR.sprites()[5], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[4], wallsBlockedR.sprites()[5])

                        elif i.x == 330 and i.y == 610:
                            i.update(wallsBlockedL.sprites()[9], wallsBlockedR.sprites()[10], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[9], wallsBlockedR.sprites()[10])

                        player.active = False

                if lasergame.opening:
                    player.active = False

            if lvl == 3:
                npchitboxes.sprites()[0].update(npcs.sprites()[0], player, alert)

                npchitboxes.sprites()[1].update(npcs.sprites()[1], player, alert)
                

                lifts1.sprites()[0].update(player, lifts2.sprites()[0])

                lifts1.sprites()[0].drawplrshadows()

                lifts2.sprites()[0].update(player, lifts1.sprites()[0])

                lifts2.sprites()[0].drawplrshadows()


                c = 0
                
                for i in locks:
                    if i.opening == False:
                        c += 1
                        if len(locks.sprites())==1:
                            lockhitbox.rectupdate()

                    if len(locks.sprites())==4:
                        if c == 4:
                            lockhitbox.rectupdate()

                    if len(locks.sprites())==3:
                        if c == 3:
                            lockhitbox.rectupdate()

                    if len(locks.sprites())==2:
                        if c == 2:
                            lockhitbox.rectupdate()


                c = 0

                player.active = True

                for i in locks:
                    player.lockscol(i)
                        
                    if i.open:
                        if i.x == 750 and i.y == 310:
                            i.update(wallsBlockedL.sprites()[0], wallsBlockedR.sprites()[1], player, lockmovingpart, lockhitbox)
                        
                        elif i.x == 104 and i.y == 510:
                            i.update(wallsBlockedL.sprites()[5], wallsBlockedR.sprites()[6], player, lockmovingpart, lockhitbox)

                        elif i.x == 710 and i.y == 510:
                            i.update(wallsBlockedL.sprites()[7], wallsBlockedR.sprites()[8], player, lockmovingpart, lockhitbox)

                        elif i.x == 720 and i.y == 610:
                            i.update(wallsBlockedL.sprites()[9], wallsBlockedR.sprites()[10], player, lockmovingpart, lockhitbox)

                    if i.opening:
                        if i.x == 750 and i.y == 310:
                            i.update(wallsBlockedL.sprites()[0], wallsBlockedR.sprites()[1], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[0], wallsBlockedR.sprites()[1])

                        elif i.x == 104 and i.y == 510:
                            i.update(wallsBlockedL.sprites()[5], wallsBlockedR.sprites()[6], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[5], wallsBlockedR.sprites()[6])

                        elif i.x == 710 and i.y == 510:
                            i.update(wallsBlockedL.sprites()[7], wallsBlockedR.sprites()[8], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[8], wallsBlockedR.sprites()[7])

                        elif i.x == 720 and i.y == 610:
                            i.update(wallsBlockedL.sprites()[9], wallsBlockedR.sprites()[10], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[9], wallsBlockedR.sprites()[10])

                        player.active = False



                if lasergame.opening:
                    player.active = False

            if lvl == 4:
                alertwalls.sprites()[0].comeup(alert)
                
                if alert.active == False:
                    wallsBlockedL.sprites()[-1].cancollide = False

                    wallsBlockedR.sprites()[-1].cancollide = False

                if alert.active:
                    wallsBlockedL.sprites()[-1].cancollide = True

                    wallsBlockedR.sprites()[-1].cancollide = True
                
                npchitboxes.sprites()[0].update(npcs.sprites()[0], player, alert)

                npchitboxes.sprites()[1].update(npcs.sprites()[1], player, alert)
                
                lifts1.sprites()[0].update(player, lifts2.sprites()[0])

                lifts1.sprites()[0].drawplrshadows()

                lifts2.sprites()[0].update(player, lifts1.sprites()[0])

                lifts2.sprites()[0].drawplrshadows()

                c = 0
                
                for i in locks:
                    if i.opening == False:
                        c += 1
                        if len(locks.sprites())==1:
                            lockhitbox.rectupdate()

                    if len(locks.sprites())==3:
                        if c == 3:
                            lockhitbox.rectupdate()

                    if len(locks.sprites())==2:
                        if c == 2:
                            lockhitbox.rectupdate()


                c = 0

                player.active = True

                for i in locks:
                    player.lockscol(i)
                        
                    if i.open:
                        if i.x == 605 and i.y == 310:
                            i.update(wallsBlockedL.sprites()[3], wallsBlockedR.sprites()[3], player, lockmovingpart, lockhitbox)
                        
                        elif i.x == 715 and i.y == 510:
                            i.update(wallsBlockedL.sprites()[6], wallsBlockedR.sprites()[7], player, lockmovingpart, lockhitbox)

                        elif i.x == 305 and i.y == 610:
                            i.update(wallsBlockedL.sprites()[9], wallsBlockedR.sprites()[9], player, lockmovingpart, lockhitbox)

                    if i.opening:
                        if i.x == 605 and i.y == 310:
                            i.update(wallsBlockedL.sprites()[3], wallsBlockedR.sprites()[3], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[3], wallsBlockedR.sprites()[3])

                        elif i.x == 715 and i.y == 510:
                            i.update(wallsBlockedL.sprites()[6], wallsBlockedR.sprites()[7], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[6], wallsBlockedR.sprites()[7])

                        elif i.x == 305 and i.y == 610:
                            i.update(wallsBlockedL.sprites()[9], wallsBlockedR.sprites()[9], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[9], wallsBlockedR.sprites()[9])

                        player.active = False

                


                if lasergame.opening:
                    player.active = False

            if lvl == 5:
                npchitboxes.sprites()[0].update(npcs.sprites()[0], player, alert)

                npchitboxes.sprites()[1].update(npcs.sprites()[1], player, alert)
                
                lifts1.sprites()[0].update(player, lifts2.sprites()[0])

                lifts1.sprites()[0].drawplrshadows()

                lifts2.sprites()[0].update(player, lifts1.sprites()[0])

                lifts2.sprites()[0].drawplrshadows()

                c = 0
                
                for i in locks:
                    if i.opening == False:
                        c += 1
                        if len(locks.sprites())==1:
                            lockhitbox.rectupdate()

                    if len(locks.sprites())==3:
                        if c == 3:
                            lockhitbox.rectupdate()

                    if len(locks.sprites())==2:
                        if c == 2:
                            lockhitbox.rectupdate()


                c = 0

                player.active = True

                for i in locks:
                    player.lockscol(i)
                        
                    if i.open:
                        if i.x == 820 and i.y == 110:
                            i.update(wallsBlockedL.sprites()[0], wallsBlockedR.sprites()[1], player, lockmovingpart, lockhitbox)
                        
                        elif i.x == 570 and i.y == 510:
                            i.update(wallsBlockedL.sprites()[7], wallsBlockedR.sprites()[8], player, lockmovingpart, lockhitbox)

                        elif i.x == 740 and i.y == 610:
                            i.update(wallsBlockedL.sprites()[10], wallsBlockedR.sprites()[11], player, lockmovingpart, lockhitbox)

                    if i.opening:
                        if i.x == 820 and i.y == 110:
                            i.update(wallsBlockedL.sprites()[0], wallsBlockedR.sprites()[1], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[0], wallsBlockedR.sprites()[1])

                        elif i.x == 570 and i.y == 510:
                            i.update(wallsBlockedL.sprites()[7], wallsBlockedR.sprites()[8], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[7], wallsBlockedR.sprites()[8])

                        elif i.x == 740 and i.y == 610:
                            i.update(wallsBlockedL.sprites()[10], wallsBlockedR.sprites()[11], player, lockmovingpart, lockhitbox)
                            i.game(lockhitbox, lockmovingpart, wallsBlockedL.sprites()[10], wallsBlockedR.sprites()[11])

                        player.active = False

                


                if lasergame.opening:
                    player.active = False

            for i in lasers:
                i.update(player, alert)

            for i in laserterminals:
                i.update(player, lasergame)

            for i in cameras_hitbox:
                i.update(player, alert)

            player.update()

            player.attack(attackhtbx, lasergame)

            attackhtbx.update(player)

            for i in npcs:
                attackhtbx.damage(i)

                player.npccol(i)
                
                i.update()

            for i in wallsBlockedL:
                player.checkcolL(i)

            for i in wallsBlockedR:
                player.checkcolR(i)

            robmission.update(player, alert)

            if robmission.ready:
                placeout.active = True

            placeout.update(player)

            for i in locks:
                if i.opening == True:
                    lockmovingpart.update()

            for i in passwords:
                i.update(player)

            for i in hints:
                i.update(player)

            if lvl == 1:
                codedlock.sprites()[0].update(player, passwords.sprites()[0], strcase2.sprites()[1])

            if lvl == 2:
                codedlock.sprites()[0].update(player, passwords.sprites()[0], lifts1.sprites()[0])

            if lvl == 3:
                codedlock.sprites()[0].update(player, passwords.sprites()[0], strcase1.sprites()[0])

            if lvl == 4:
                codedlock.sprites()[0].update(player, passwords.sprites()[0], strcase1.sprites()[2])

            if lvl == 5:
                codedlock.sprites()[0].update(player, passwords.sprites()[0], lifts2.sprites()[0])

            type1.update(cursor, codedlock.sprites()[0])

            type2.update(cursor, codedlock.sprites()[0])

            type3.update(cursor, codedlock.sprites()[0])

            type4.update(cursor, codedlock.sprites()[0])

            type5.update(cursor, codedlock.sprites()[0])

            type6.update(cursor, codedlock.sprites()[0])

            type7.update(cursor, codedlock.sprites()[0])

            type8.update(cursor, codedlock.sprites()[0])

            type9.update(cursor, codedlock.sprites()[0])

            type0.update(cursor, codedlock.sprites()[0])

            if lvl == 1:
                lasergame.pathupdate(laserterminals.sprites()[0])
                lasergame.update(laserterminals.sprites()[0], lasers.sprites()[0], alert)

            if lvl == 2:
                if laserterminals.sprites()[0].opening:
                    lasergame.pathupdate(laserterminals.sprites()[0])
                    lasergame.update(laserterminals.sprites()[0], lasers.sprites()[0], alert)

                if laserterminals.sprites()[1].opening:
                    lasergame.pathupdate(laserterminals.sprites()[1])
                    lasergame.update(laserterminals.sprites()[1], lasers.sprites()[1], alert)

            if lvl == 3:
                if laserterminals.sprites()[0].opening:
                    lasergame.pathupdate(laserterminals.sprites()[0])
                    lasergame.update(laserterminals.sprites()[0], lasers.sprites()[0], alert)

                if laserterminals.sprites()[1].opening:
                    lasergame.pathupdate(laserterminals.sprites()[1])
                    lasergame.update(laserterminals.sprites()[1], lasers.sprites()[1], alert)

            if lvl == 4:
                lasergame.pathupdate(laserterminals.sprites()[0])
                lasergame.update(laserterminals.sprites()[0], lasers.sprites()[0], alert)

            if lvl == 5:
                if laserterminals.sprites()[0].opening:
                    lasergame.pathupdate(laserterminals.sprites()[0])
                    lasergame.update(laserterminals.sprites()[0], lasers.sprites()[0], alert)

                if laserterminals.sprites()[1].opening:
                    lasergame.pathupdate(laserterminals.sprites()[1])
                    lasergame.update(laserterminals.sprites()[1], lasers.sprites()[1], alert)

            #HUD

            time.count()

            moneyc.moneyadd(player)
            
            sounds.col(cursor)

            music.col(cursor)

            retry.use(cursor)

            alert.update()

            alert.healthkill(health)

            player.healthchk(health)

            

            pause.use(cursor)

            

            #ЗВУКИ

            soundcontrol.update(alert, pause, sounds, music)

            alert.playsound(soundcontrol)

            pause.playsound(soundcontrol)

            player.playsound(soundcontrol)

            type1.playsound(soundcontrol)
            type2.playsound(soundcontrol)
            type3.playsound(soundcontrol)
            type4.playsound(soundcontrol)
            type5.playsound(soundcontrol)
            type6.playsound(soundcontrol)
            type7.playsound(soundcontrol)
            type8.playsound(soundcontrol)
            type9.playsound(soundcontrol)
            type0.playsound(soundcontrol)

            for i in strcase1:
                i.playsound(soundcontrol)

            for i in strcase2:
                i.playsound(soundcontrol)

            for i in cameras_hitbox:
                i.playsound(soundcontrol)

            passwords.sprites()[0].playsound(soundcontrol)

            for i in hints:
                i.playsound(soundcontrol)

            codedlock.sprites()[0].playsound(soundcontrol)

            for i in npchitboxes:
                i.playsound(soundcontrol)

            for i in npcs:
                i.playsound(soundcontrol)

            lasergame.playsound(soundcontrol)

            for i in locks:
                i.playsound(soundcontrol)





            if time.time == 9999:
                player.death = True

            if pause.pause:
                game = False

            if placeout.ready:
                lvlcomplete = True
                game = False
                pygame.mixer.music.pause()
                
                for i in range(20):
                    pygame.mixer.Channel(i).stop()
                    
                WinChannel.play(WinSound)

            if player.death:
                game = False
                lose = True
                pygame.mixer.music.pause()
                
                for i in range(20):
                        pygame.mixer.Channel(i).stop()
                
                LoseChannel.play(LoseSound)

                for i in npcs:
                    if i.shooting:
                        i.shooting = False
                        pygame.mixer.Channel(10).set_volume(1)
                        pygame.mixer.Channel(10).play(pygame.mixer.Sound("NpcShooting.wav"))

                



        pause.onpause(cursor, soundcontrol)

        if pause.pause == False and lvlcomplete == False and lose == False:
            game = True

        #РИСОВАНИЕ

        for i in strcase1:
            i.draw()

        for i in strcase2:
            i.draw()

        for i in strcase1:
            i.drawgoing()

        for i in strcase2:
            i.drawgoing()

        for i in shadows:
            i.draw()

        for i in ladders:
            i.draw()

        if lvl == 5:
            win.blit(lvl5gameimage1, (0, 667))

        for i in lifts1:
            i.draw()

        for i in lifts2:
            i.draw()

        for i in lifts1:
            i.drawplrshadows()

        for i in lifts2:
            i.drawplrshadows()

        for i in lasers:
            i.draw()

        for i in laserterminals:
            i.draw()

        for i in passwords:
            i.draw()

        for i in hints:
            i.draw()

        for i in codedlock:
            i.draw()

        for i in moneys:
            i.draw()

        codedlock.sprites()[0].draw()

        robmission.draw()

        placeout.draw()

        for i in locks:
            i.draw()

        player.draw()

        attackhtbx.draw()

        for i in npcs:
            i.draw()

        for i in wallsBlockedL:
            i.draw()

        for i in wallsBlockedR:
            i.draw()

        for i in alertwalls:
            i.draw()

        for i in floors:
            i.draw()

        for i in walls:
            i.draw()
            
        for i in npchitboxes:
            i.draw()

        for i in cameras_hitbox:
            i.draw()
            
        for i in locks:
            i.drawwin()

        for i in locks:
            if i.opening == True:
                lockmovingpart.draw()
                
                lockhitbox.draw()

        for i in passwords:
            i.windraw()

        for i in hints:
            i.windraw()

        for i in codedlock:
            i.windraw()

        type1.draw(codedlock.sprites()[0])
        type2.draw(codedlock.sprites()[0])
        type3.draw(codedlock.sprites()[0])
        type4.draw(codedlock.sprites()[0])
        type5.draw(codedlock.sprites()[0])
        type6.draw(codedlock.sprites()[0])
        type7.draw(codedlock.sprites()[0])
        type8.draw(codedlock.sprites()[0])
        type9.draw(codedlock.sprites()[0])
        type0.draw(codedlock.sprites()[0])

        lasergame.draw()

        hud.draw()

        health.draw()

        time.draw()

        moneyc.draw()

        sounds.draw()

        music.draw()

        retry.draw()

        pause.draw()

        alert.draw()

        pause.windraw()

        for i in moneys:
            if i.catch:
                i.anim(moneyc)
                
            player.moneycol(i)

            if i.came:
                i.came = False
                i.catch = False

        for i in npcs:
            if i.moneycatch:
                i.anim(moneyc)
                
            player.npccol(i)

            if i.moneycame:
                i.moneycame = False
                i.moneycatch = False

        if pause.lvl == 0:
            wait = True
            
            playing = False
            game = False
            quitlvl = True

        if retry.retry:
            wait = True

        if lose:
            losec += 1
            win.blit(pygame.image.load("tex\game\LoseImage.png"), (0,0))

            if losec == 200:
                lose = 0
                lvl = 0
                lvlreload = True
                playing = False
                game = False
                quitlvl = True

        if lvlcomplete:
            lvlcompletec += 1

            for i in moneys:
                if i.catch:
                    moneyc.money += i.amount
                    i.catch = 0

            for i in npcs:
                if i.moneycatch:
                    moneyc.money += 10
                    i.moneycatch = 0

            win.blit(pygame.transform.scale(pygame.image.load("tex\game\WinImage.jpg"), (1000, 765)), (0,0))
            
            if levelsmap.lvl1complete and levelsmap.lvl2complete and levelsmap.lvl3complete and levelsmap.lvl4complete and levelsmap.lvl5complete:
                win.blit(pygame.image.load("tex\EndGameImage.png"), (0,0))

            if lvlcompletec == 200:
                lvlcompletec = 0
                lvlcomplete = False
                
                if lvl == 1:
                    levelsmap.lvl1complete = True
                    
                    if moneyc.money == 195:
                        levelsmap.lvl1stats[3] += 1

                    if time.time <70:
                        levelsmap.lvl1stats[3] += 1

                    if health.health == 3:
                        levelsmap.lvl1stats[3] += 3

                    if health.health == 2:
                        levelsmap.lvl1stats[3] += 2

                    if health.health == 1:
                        levelsmap.lvl1stats[3] += 1
                        
                    levelsmap.lvl1stats[0] = time.time
                    levelsmap.lvl1stats[1] = moneyc.money
                    levelsmap.lvl1stats[2] = health.health

                if lvl == 2:
                    levelsmap.lvl2complete = True
                    
                    if moneyc.money == 300:
                        levelsmap.lvl2stats[3] += 1

                    if time.time <150:
                        levelsmap.lvl2stats[3] += 1

                    if health.health == 3:
                        levelsmap.lvl2stats[3] += 3

                    if health.health == 2:
                        levelsmap.lvl2stats[3] += 2

                    if health.health == 1:
                        levelsmap.lvl2stats[3] += 1
                        
                    levelsmap.lvl2stats[0] = time.time
                    levelsmap.lvl2stats[1] = moneyc.money
                    levelsmap.lvl2stats[2] = health.health

                if lvl == 3:
                    levelsmap.lvl3complete = True
                    
                    if moneyc.money == 265:
                        levelsmap.lvl3stats[3] += 1

                    if time.time <200:
                        levelsmap.lvl3stats[3] += 1

                    if health.health == 3:
                        levelsmap.lvl3stats[3] += 3

                    if health.health == 2:
                        levelsmap.lvl3stats[3] += 2

                    if health.health == 1:
                        levelsmap.lvl3stats[3] += 1
                        
                    levelsmap.lvl3stats[0] = time.time
                    levelsmap.lvl3stats[1] = moneyc.money
                    levelsmap.lvl3stats[2] = health.health

                if lvl == 4:
                    levelsmap.lvl4complete = True
                    
                    if moneyc.money == 240:
                        levelsmap.lvl4stats[3] += 1

                    if time.time <100:
                        levelsmap.lvl4stats[3] += 1

                    if health.health == 3:
                        levelsmap.lvl4stats[3] += 3

                    if health.health == 2:
                        levelsmap.lvl4stats[3] += 2

                    if health.health == 1:
                        levelsmap.lvl4stats[3] += 1
                        
                    levelsmap.lvl4stats[0] = time.time
                    levelsmap.lvl4stats[1] = moneyc.money
                    levelsmap.lvl4stats[2] = health.health

                if lvl == 5:
                    levelsmap.lvl5complete = True
                    
                    if moneyc.money == 240:
                        levelsmap.lvl5stats[3] += 1

                    if time.time <200:
                        levelsmap.lvl5stats[3] += 1

                    if health.health == 3:
                        levelsmap.lvl5stats[3] += 3

                    if health.health == 2:
                        levelsmap.lvl5stats[3] += 2

                    if health.health == 1:
                        levelsmap.lvl5stats[3] += 1
                        
                    levelsmap.lvl5stats[0] = time.time
                    levelsmap.lvl5stats[1] = moneyc.money
                    levelsmap.lvl5stats[2] = health.health
                
                lvl = 0
                lvlreload = True
                playing = False
                game = False
                quitlvl = True
            
    if wait:
        win.blit(loadingimage, (0,0))

        win.blit(loadingtxtr, (10, 10))

        if lvl >0:
            if retry.retry:
                lvlreload = True

            if pause.lvl == 0:
                lvl = 0
                lvlreload = True

        if lvl == -1:
            if welcome.lvl == 0:
                welcome.lvl = -1

                lvl = 0

        if lvl == 0:
            if levelsmap.lvl == -1:
                levelsmap.lvl = 0

                lvl = -1

            if levelsmap.lvl == 1 or levelsmap.lvl == 2 or levelsmap.lvl == 3 or levelsmap.lvl == 4 or levelsmap.lvl == 5 or levelsmap.lvl == 6 or levelsmap.lvl == 7:
                game = True
                
                lvl = levelsmap.lvl
        
        if transitionc <10:
            transitionc += 1

        if transitionc == 10:
            transitionc = 0
            wait = False


        
    pygame.display.flip()

pygame.quit()
