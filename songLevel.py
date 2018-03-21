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
isRunning = True
dt = 0.0

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
    def drawImage(pos = (0,0)):
        global gameDisplay
        gameDisplay.blit(self.Image, (pos[0] - self.Rect.center[0],pos[1] - self.Rect.center[1]))
    def scaleImage(image ,scale = (1.0,1.0)):
        ScaledImage = pygame.transform.scale(image,(int(scale[0]*image.get_width()),int(scale[1]*image.get_height())))
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


    def drawNote(image = Image("download.png"),pos = (0,0)):#
        image.drawImage(pos)


Notes = imageNotes()
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
    global tex
    #gameDisplay.fill((0.0,0.0,0.0))
    gameDisplay.blit(background_surface,(0,0))
    tex.draw_textures(gameDisplay)
    ButtonsToDraw()
    




#class texture para poder dezenhar no braço da "guitarra"
def Texturize(image,size=None):
    if size:
        (w,h) = size 
    else:
        (w,h) = image.get_size()
    texture = []
    for y in range(h): 
        row=pygame.Surface((w,1))
        row.blit(image,(0,-y))
        texture+=[row]
    return texture
class Texture:
    rotX,rotY = -18.5/180*math.pi,0;
    pos = [0,1.8,-1.2]
    def __init__(self,dir):
        global deltaTime
        global display_Height
        global display_Width
        self.image = pygame.image.load(dir);
        self.image = Image.scaleImage(self.image,(2.0,2.0))
        size = self.image.get_size()
        self.texture = [Texturize(self.image,size),size]
        self.fractions = [2*y/size[1] for y in range(size[1])]
        self.range = 6
        self.cx = display_Width/2
        self.cy = display_Height/2
        self.speed = (0.95-0.2)*display_Height/100
        self.z = 0
        
    def rotate2d(self,pos,rad): 
        x,y=pos
        s=math.sin(rad)
        c = math.cos(rad)
        return x*c-y*s,x*s+y*c

    def rotate3d(self,pos,rot):
        x,y,z = pos
        if rot[2]: 
            x,y = self.rotate2d((x,y),rot[2])
        if rot[1]: 
            z,x = self.rotate2d((z,x),rot[1])
        if rot[0]: 
            y,z = self.rotate2d((y,z),rot[0])
        return x,y,z
    def pos2d(self,x,z):
        X,Y,Z = self.pos
        x,y,z = self.rotate3d((x-X,-Y,z-Z),(self.rotX,self.rotY,0))
        f = 300/z if z>0 else 90000
        return int(self.cx+x*f),int(self.cy-y*f)
    def update(self):
        global dt
        global isRunning

        if self.speed: # if there's speed, let's move.
            s = dt*self.speed
            self.z+=s
            #for chord in self.chords: chord[1]-=s # move chords towards target

            if not isRunning:
                self.speed-=dt*1.7 # slow down
                if self.speed<0.2: self.speed = 0 # slow enough, let's just stop...

        #self.running = pygame.mixer.music.get_busy() # is the song still playing?

        #if not self.joysticks: self.init_joysticks()
    def draw_textures(self,screen):
        t,(w,h) = self.texture; 
        s = 2 # box size
        for Z in range(0,self.range,s):
            for y in range(h):
                f = self.fractions[y]
                z = (f+Z-self.z)%self.range
                a,b = self.pos2d(-1,z),self.pos2d(1,z) # left and right point of line (image to be drawn on)
                try: screen.blit(pygame.transform.scale(t[-y],(b[0]-a[0],s)),a) # not fixed for rotating cam left or right, only up and down so far
                except: pass # incase there's a problem
tex = Texture("texture.png")
def Update():
    global Time
    global onPause
    global Frame
    global gameExit
    global FPS
    global tex
    global gameDisplay
    global dt
    #global numberOfButtons
    #numberOfButtons = makesList(numberOfButtons)
    #flag = 4
    dt = clock.tick(FPS)/1000
    #print('flag' + str(flag))
    if onPause == False:
        Frame = Frame + 1
        Time = Time + dt
        if Frame % 30 == 0:
            print(Time)
            print("Frame: " + " " + str(Frame))
    for event in Event():
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
    tex.update()
    
    drawScene()

    #tex.draw_textures(gameDisplay)
    #flag = 6
    #print('flag' + str(flag))
    pygame.display.flip()

makesList()
Notes.loadImages(("download.png","download.png","download.png","download.png","download.png"))
while not gameExit:
    Update()
Quit()
print("fim")
