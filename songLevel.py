#Explicação do codigo:A maioria das funções aqui provavelmente não serão aproveitadas(provavelmente serão feitos ou 
#usados alguns modulos para fazer essas funcionalidades),as variaveis mais importantes são:
#buttonList,indexButtonDraw,Time,deltaTime,Notes,gameDisplay,background_surface.
#as classes mais importantes são:Image,imageNotes
#os metodos mais importantes fora dos que estão dentro das classes beginScene(),ButtonsToDraw(),drawScene(),Update()
#from colorName import *
import random
import math
import pygame
#import pygame
display_Width = 1240
display_Height = 720
FPS = 60
scene = 'main_menu'
gameName = "Carnice Hero"
gameExit = False
onLoad = False
#UI = Canvas()
buttonList = ([],[],[],[],[])#aqui tem a lista dos tempos que cada nota devera ser pressionada
indexButtonDraw = [0,0,0,0,0]#diz qual é o index da ultima nota a ser desenhada,para não ter que percorrer toda a buttonList
onPause = False
Time = 0.0#variavel de tempo
deltaTime = 4.0#diferença de tempo onde começa a ver as notas, para poder pressiona-las
Frame = 0
numberOfButtons = 0


#clock
gameDisplay = pygame.display.set_mode((display_Width, display_Height))
clock = pygame.time.Clock()
background_surface = pygame.Surface((display_Width, display_Height))
background_surface.fill((0, 0, 0))
def DrawDisplay(display_width,display_heigth,fps,Name):
    #global gameDisplay
    #gameDisplay = pygame.display.set_mode((display_width,display_heigth))
    pygame.display.set_caption(Name)
    global clock 
    clock = pygame.time.Clock()
    global FPS
    FPS = fps
    return pygame.display.set_mode((display_width,display_heigth))

def Event():
    return pygame.event.get()

def GameQuit():
    return pygame.QUIT

def Quit():
    pygame.quit()

class Image:#classe de imagens feito para desenhar,escalar imagem,e cortar imagem
    def __init__(self,local):
        self.Local = local
        self.Image = Image.scaleImage(pygame.image.load(local),(2.0,2.0)).convert_alpha()
        self.Rect =  self.Image.get_rect()
    #def drawImage(image,pos = (0.0,0.0)):
     #   rect = image.get_rect()
      #  global gameDisplay
       # gameDisplay.blit(image, (int(pos[0] - rect.center[0]),int(pos[1] - rect.center[1])))
    def scaleImage(image ,scale = (1.0,1.0)):
        ScaledImage = pygame.transform.smoothscale(image,(int(scale[0]*image.get_width()),int(scale[1]*image.get_height())))
        return ScaledImage
    def cutImage(image ,shown = (1.0,1.0)):
        CutImage = pygame.transform.chop(image, (0.0, 0.0, shown[0]*image.get_width(), shown[1]*image.get_height()))
        return CutImage
    def drawChangedImage(image , pos = (0.0,0.0)):
        rect = image.get_rect()
        global gameDisplay
        gameDisplay.blit(image, (int(pos[0] - rect.center[0]),int(pos[1] - rect.center[1])))



class imageNotes:#classe da lista de botões para instanciar as notas, sem ter que armazenar em todos as notas da tela
    def __init__(self):
        global display_Height
        global display_Width
        self.display_Height = display_Height
        self.display_Width = display_Width
    def loadImages(self,local):
        self.Images = []
        i = 0
        for loc in local:
            self.Images.append(Image(loc))
            i = i + 1
        self.i = i #numero de imagens armazenadas na variavel
    def isometricPositionDraw(self,index,time):#transforma a imagem dependendo da posição em que ela aparece,para se mostrar uma vista isometrica,para desenha-la
        global Time
        global deltaTime
        iniRatio = 0.20
        lastRatio = 0.95
        showNoteTime = 0.2
        #initialPosY = iniRatio*globalVar.display_Height
        #lastPosY = lastRatio*globalVar.display_Height
        r = (Time - time - deltaTime)
        if(r <= 0.0):
            return
        #print("r é " + str(r))
        ratio = r*(lastRatio-iniRatio)/deltaTime + iniRatio
        image = Image.scaleImage(self.Images[index].Image,(ratio,ratio))
        posY = ratio*self.display_Height

        posX = self.display_Width/2 + 1.5*(index-2)*image.get_width()
        if(r < showNoteTime):
            dy = image.get_height()
            image = Image.cutImage(image,(0.0,r/showNoteTime))
            dy = dy - image.get_height()/2
            Image.drawChangedImage(image,(posX,posY + int(dy)))
            return
        Image.drawChangedImage(image,(posX,posY))


    def drawNote(image = Image("green.png"),pos = (0,0)):#
        image.drawImage(pos)

class playNote():
    def __init__(self,nomallocal,pressDir,rightDir):
        global display_Height
        global display_Width
        global Notes
        self.posY = 0.95*display_Height
        self.posX = []

        for i in range(0,5):
            self.posX.append(display_Width/2 + 1.5*(i-2)*Notes.Images[i].Image.get_width())
        self.Images = []#imagem a ser desenhada
        self.NormalStateImage = []#imagem a ser desenhada quando os botões para pressionar as notas não forem ativados
        self.pressedImages = []#imagem a ser ativada quando os botões forem ativados e errarem
        self.rightImages = []#imagem a ser ativada quando as notas forem pressionadas corretamente
        i = 0
        for loc in nomallocal:
            self.NormalStateImage.append(Image(loc))
            self.Images.append(Image(loc))
            i = i + 1
        for loc in pressDir:
            self.pressedImages.append(Image(loc))
        for loc in rightDir:
            self.rightImages.append(Image(loc))
        self.i = i #numero de imagens armazenadas na variavel
    def notePressed(self,i,time,impresTime):
        global buttonList
        global deltaTime
        global indexButtonDraw
        if not buttonList[i]:
            self.Images[i] = self.pressedImages[i]
            return

        t = time - buttonList[i][0] - 2*deltaTime
        t = impresTime*2#garante que entra no porximo loop
        n = indexButtonDraw[i]
        j = -1
        while t >= impresTime and  j < n:
            j = j + 1
            t = time - buttonList[i][j] - 2*deltaTime
        if t < impresTime and t > -impresTime:
            self.Images[i] = self.rightImages[i]#troca a imagem a ser desenhada
            del buttonList[i][j]
            indexButtonDraw[i] = indexButtonDraw[i] - 1
            print('adcionar pontos')#adciona os pontos por ter acertado a nota
        else:
            self.Images[i] = self.pressedImages[i]
            print('Ativa o som do erro')#Ativa o som do erro
    def noteUnpress(self,i):
        self.Images[i] = self.NormalStateImage[i]

    def drawPlayNotes(self):
        i = 0
        while i < 5:
            pos = (self.posX[i],self.posY)
            Image.drawChangedImage(self.Images[i].Image,(self.posX[i],self.posY))
            i = i + 1

    def events(self,evt):
        
        global Time
        imprecisionTime = 0.1#intervalo de tempo em que o jogador pode ser impreciso
        i = 0
        for event in evt:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    i = 0
                elif event.key == pygame.K_s:
                    i = 1
                elif event.key == pygame.K_d:
                    i = 2
                elif event.key == pygame.K_j:
                    i = 3
                elif event.key == pygame.K_k:
                    i = 4
                self.notePressed(i,Time,imprecisionTime)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    i = 0
                elif event.key == pygame.K_s:
                    i = 1
                elif event.key == pygame.K_d:
                    i = 2
                elif event.key == pygame.K_j:
                    i = 3
                elif event.key == pygame.K_k:
                    i = 4
                self.noteUnpress(i)




Notes = imageNotes()
Notes.loadImages(("green.png","yellow.png","rednote.png","blue.png","orange.png"))
pressNotes = playNote(nomallocal = ("greenNormal.png","yellowNormal.png","redNormal.png","blueNormal.png","orangeNormal.png")
    ,pressDir = ("greenPressed.png","yellowPressed.png","redPressed.png","bluePressed.png","orangePressed.png")
    ,rightDir = ("greenPressed.png","yellowPressed.png","redPressed.png","bluePressed.png","orangePressed.png"))
#Notes.loadImages(("download1.jpg","download1.jpg","download1.jpg","download1.jpg","download1.jpg"))

def makesList():
    global buttonList
    lastTime = 0
    n = 0
    #dn = 1
    #flag = 0
    #print('flag' + str(flag))
    while n < 200:
        i = random.randint(0,4)
        if buttonList[i]:
            lastTime = buttonList[i][len(buttonList[i]) - 1]
        lastTime = lastTime + random.randint(0,40)/10
        buttonList[i].append(lastTime)
        n = n + 1
        #dn = dn - 1
    #return n



def beginScene():
    #global numberOfButtons
    #numberOfButtons = 0
    #numberOfButtons = makesList(numberOfButtons)
    global onPause
    global display_Width
    global display_Height
    global FPS
    global gameName
    global gameDisplay
    
    onPause = False
    global Time
    Time = 0.0
    gameDisplay.fill((0.0,0.0,0.0))

    #flag = 1
    #print('flag' + str(flag))
    gameDisplay = DrawDisplay(display_Width,display_Height,FPS,gameName)

beginScene()

def ButtonsToDraw():
    global buttonList
    global indexButtonDraw
    global Time
    global deltaTime
    global Notes
    global display_Width
    global pressNotes
    i = Notes.i - 1
    while i >= 0:
        if buttonList[i]:
            if Time - buttonList[i][0] - deltaTime > 2*deltaTime:
                del buttonList[i][0]
                indexButtonDraw[i] = indexButtonDraw[i] - 1
        i = i - 1
    i = Notes.i - 1
    leftLine = display_Width/2 - 2*45
    #flag = 2
    #print('flag' + str(flag))
    pressNotes.drawPlayNotes()
    while i >= 0:
        j = indexButtonDraw[i]
        if buttonList[i]:
            n = len(buttonList[i]) - j
            while n > 0:
                if buttonList[i][j] - Time > deltaTime:
                    break
                j = j + 1
                n = n - 1
                indexButtonDraw[i] = j
        while j > 0:
            j = j - 1
            #drawButton(color,(leftLine + i*45,(Time - buttonList[i][j] - deltaTime )*globalVar.display_Height/deltaTime))
            Notes.isometricPositionDraw(i,buttonList[i][j])
        i = i-1
    #flag = 3
    #print('flag' + str(flag)) 


#def drawTimingButton():
def drawScene():
    global gameDisplay
    global background_surface
    #gameDisplay.fill((0.0,0.0,0.0))
    gameDisplay.blit(background_surface,(0,0))
    ButtonsToDraw()
    


def Update():
    global Time
    global onPause
    global Frame
    global gameExit
    global FPS
    global pressNotes
    #global numberOfButtons
    #numberOfButtons = makesList(numberOfButtons)
    #flag = 4
    dt = clock.tick(FPS)/1000
    #print('flag' + str(flag))
    if onPause == False:
        Frame = Frame + 1
        Time = Time + dt
    #    if Frame % 30 == 0:
     #       print(Time)
      #      print("Frame: " + " " + str(Frame))
    evt = Event()
    for event in evt:
        if event.type == GameQuit():
            gameExit = True
        #elif event.type == pygame.MOUSEBUTTONDOWN:
         #   if event.button == 1: #botão esquerdo
               #eventos de cick de botão 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if onPause:
                    onPause = False
                elif not onPause:
                    onPause = True
    
        #elif event.type == pygame.KEYUP:
         #   break
    #flag = 5
    #print('flag' + str(flag))
    drawScene()
    pressNotes.events(evt)
    #flag = 6
    #print('flag' + str(flag))
    pygame.display.flip()

makesList()


while not gameExit:
    Update()
Quit()
print("fim")
