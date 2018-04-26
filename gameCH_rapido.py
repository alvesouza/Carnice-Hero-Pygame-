#Explicação do codigo:A maioria das funções aqui provavelmente não serão aproveitadas(provavelmente serão feitos ou 
#usados alguns modulos para fazer essas funcionalidades),as variaveis mais importantes são:
#buttonList,indexButtonDraw,Time,deltaTime,Notes,gameDisplay,background_surface.
#as classes mais importantes são:Image,imageNotes
#os metodos mais importantes fora dos que estão dentro das classes beginScene(),ButtonsToDraw(),drawScene(),Update()
#from colorName import *
import random, math, pygame, sys, os, time
from pygame.locals import *

last_frame_rect = []
atual_frame_rect = []

class Relogio:
    """ Classe com as informacoes do relogio do jogo. """
    def __init__(self, fps):
        self.fps = fps
        self.relogio = pygame.time.Clock()


class Audio:
    """ Classe com as informacoes dos audios do jogo. """
    def __init__(self, endereco, volume):
        self.audio = pygame.mixer.Sound(endereco)
        self.audio.set_volume(volume)

    def play(self):
        self.audio.play()
    def stop(self):
        self.audio.stop()


class Tela:
    """ Classe com as informacoes do display do jogo. """
    def __init__(self, largura, altura, titulo, enderecoImagemFundo):
        self.largura = largura
        self.altura = altura
        self.titulo = titulo
        self.imagemFundo = pygame.image.load(enderecoImagemFundo)
        self.imagemFundo = pygame.transform.scale(self.imagemFundo, (self.largura, self.altura))
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption(self.titulo)


class Menu:

    def game_menu(self):

        pygame.init()

        menu_inicial_iniciar = Tela(1115, 713, "CarniceHero", "menu_inicial_iniciar.jpg")
        menu_inicial_como_jogar = Tela(1115, 713, "CarniceHero", "menu_inicial_como_jogar.jpg")
        menu_inicial_creditos = Tela(1115, 713, "CarniceHero", "menu_inicial_creditos.jpg")

        menu_como_jogar = Tela(1115, 713, "CarniceHero", "menu_como_jogar.jpg")
        menu_creditos = Tela(1115, 713, "CarniceHero", "menu_creditos_2.jpg")

        menu_dificuldade_olodum = Tela(1115, 713, "CarniceHero", "menu_dificuldade_olodum.jpg")
        menu_dificuldade_samba_normal = Tela(1115, 713, "CarniceHero", "menu_dificuldade_samba_normal.jpg")
        menu_dificuldade_samba_frenetico = Tela(1115, 713, "CarniceHero", "menu_dificuldade_samba_frenetico.jpg")
        menu_dificuldade_voltar = Tela(1115, 713, "CarniceHero", "menu_dificuldade_voltar.jpg")

        audio_menu_navigate = Audio("menu_navigate_0.wav", 1)

        relogio_jogo = Relogio(60)

        fechar_jogo = False

        estado = "menu_inicial_iniciar"
        menu = True
        while menu:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    fechar_jogo = True
                    menu = False

                elif event.type == pygame.KEYDOWN:

                    if event.key == 13:  # 13 == botao ENTER:
                        if estado == "menu_inicial_iniciar":
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_olodum"
                        elif estado == "menu_dificuldade_voltar":
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_iniciar"
                        elif estado == "menu_inicial_como_jogar":
                            audio_menu_navigate.audio.play()
                            estado = "menu_como_jogar"
                        elif estado == "menu_inicial_creditos":
                            audio_menu_navigate.audio.play()
                            estado = "menu_creditos"
                        elif estado == "menu_como_jogar":
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_como_jogar"
                        elif estado == "menu_creditos":
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_creditos"
                        else:
                            audio_menu_navigate.audio.play()
                            menu = False

                    elif estado == "menu_inicial_iniciar":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_como_jogar"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_creditos"

                    elif estado == "menu_inicial_como_jogar":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_creditos"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_iniciar"

                    elif estado == "menu_inicial_creditos":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_iniciar"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_inicial_como_jogar"

                    elif estado == "menu_dificuldade_olodum":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_samba_normal"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_voltar"

                    elif estado == "menu_dificuldade_samba_normal":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_samba_frenetico"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_olodum"

                    elif estado == "menu_dificuldade_samba_frenetico":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_voltar"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_samba_normal"

                    elif estado == "menu_dificuldade_voltar":
                        if event.key == pygame.K_DOWN:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_olodum"
                        elif event.key == pygame.K_UP:
                            audio_menu_navigate.audio.play()
                            estado = "menu_dificuldade_samba_frenetico"

            if estado == "menu_inicial_iniciar":
                menu_inicial_iniciar.tela.blit(menu_inicial_iniciar.imagemFundo, (0, 0))
            elif estado == "menu_inicial_como_jogar":
                menu_inicial_como_jogar.tela.blit(menu_inicial_como_jogar.imagemFundo, (0, 0))
            elif estado == "menu_inicial_creditos":
                menu_inicial_creditos.tela.blit(menu_inicial_creditos.imagemFundo, (0, 0))
            elif estado == "menu_como_jogar":
                menu_como_jogar.tela.blit(menu_como_jogar.imagemFundo, (0, 0))
            elif estado == "menu_creditos":
                menu_creditos.tela.blit(menu_creditos.imagemFundo, (0, 0))
            elif estado == "menu_dificuldade_olodum":
                menu_dificuldade_olodum.tela.blit(menu_dificuldade_olodum.imagemFundo, (0, 0))
            elif estado == "menu_dificuldade_samba_normal":
                menu_dificuldade_samba_normal.tela.blit(menu_dificuldade_samba_normal.imagemFundo, (0, 0))
            elif estado == "menu_dificuldade_samba_frenetico":
                menu_dificuldade_samba_frenetico.tela.blit(menu_dificuldade_samba_frenetico.imagemFundo, (0, 0))
            elif estado == "menu_dificuldade_voltar":
                menu_dificuldade_voltar.tela.blit(menu_dificuldade_voltar.imagemFundo, (0, 0))

            relogio_jogo.relogio.tick(relogio_jogo.fps)
            pygame.display.update()

        if fechar_jogo:
            return "fechar_jogo"
        else:
            return estado



os.environ['SDL_VIDEO_CENTERED'] = '1' #abre a tela do jogo já centralizada

pygame.init()
pygame.font.init()

display_Width = 1115
display_Height = 713

#cores
yellow_carni = (254, 163, 0)
pink_carni = (222, 0, 148)
white = (255, 255, 255)
black = (0, 0, 0)

#variáveis de contagem
countacertos = 0
counterros = 0

gameExit = False
onLoad = False
onPause = False

menu = Menu()
estado = menu.game_menu()
if estado == "fechar_jogo":
    gameExit = True

buttonList = ([], [], [], [], [])  # lista dos tempos que cada nota deverá ser pressionada
indexButtonDraw = [0, 0, 0, 0, 0]  # diz qual é o index da última nota a ser desenhada,
                                   # para não ter que percorrer toda a buttonList
Time = 0.0  # variável de tempo
deltaTime = 4.0  # diferença de tempo onde começa a ver as notas, para poder pressioná-las
Frame = 0
numberOfButtons = 0

# configurações iniciais
FPS = 24
scene = 'main_menu'
gameName = "CarniceHero"
gameDisplay = pygame.display.set_mode((display_Width, display_Height))
clock = pygame.time.Clock()
background_surface = pygame.Surface((display_Width, display_Height))
background_surface.fill(black)
icon = pygame.image.load('images/urubu.png')
pygame.display.set_icon(icon)

#áudios importados
errorSound = pygame.mixer.Sound("sounds/note_erro.ogg")
musicaJogo = pygame.mixer.music
musicaJogo.load("sounds/samba_normal0.7.ogg")


def DrawDisplay(display_width, display_heigth, fps, Name):
    global clock, FPS
    pygame.display.set_caption(Name)
    clock = pygame.time.Clock()
    FPS = fps
    return pygame.display.set_mode((display_width, display_heigth))

def Event():
    return pygame.event.get()

def GameQuit():
    return pygame.QUIT

def Quit():
    pygame.quit()
    sys.exit()

class Image:
    def __init__(self, local):
        self.Local = local
        self.Image = Image.scaleImage(pygame.image.load(local), (2.0, 2.0)).convert_alpha()
        self.Rect = self.Image.get_rect()

    def scaleImage(image, scale=(1.0, 1.0)):
        ScaledImage = pygame.transform.smoothscale(image,(int(scale[0]*image.get_width()),int(scale[1]*image.get_height())))
        return ScaledImage

    def cutImage(image ,shown = (1.0,1.0)):
        CutImage = pygame.transform.chop(image, (0.0, 0.0, shown[0]*image.get_width(), shown[1]*image.get_height()))
        return CutImage

    def drawChangedImage(image , pos = (0.0,0.0)):
        rect = image.get_rect()
        global gameDisplay
        global atual_frame_rect
        atual_frame_rect.append(gameDisplay.blit(image, (int(pos[0] - rect.center[0]),int(pos[1] - rect.center[1]))))

class imageNotes: #lista de botões para instanciar as notas (definir comportamento), sem ter que armazenar as notas da tela
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
        self.i = i #número de imagens armazenadas na variável
        
    def isometricPositionDraw(self,index,time): #transforma a imagem dependendo da posição em que ela aparece,para se mostrar uma vista isometrica,para desenha-la
        global Time, deltaTime
        iniRatio = 0.20
        lastRatio = 0.95
        showNoteTime = 0.2

        r = (Time - time - deltaTime)
        if(r <= 0.0):
            return

        ratio = r*(lastRatio-iniRatio)/deltaTime + iniRatio
        image = Image.scaleImage(self.Images[index].Image,(ratio,ratio))

        #### altera-se em posY a distância do topo da tela e o início da nota
        posY = ratio*self.display_Height + 240
        #### altera-se em posX a distância horizontal entre as notas
        posX = self.display_Width/2 + 1.2*(index-2)*image.get_width()
        
        if(r < showNoteTime):
            dy = image.get_height()
            image = Image.cutImage(image,(0.0,r/showNoteTime))
            dy = dy - image.get_height()/2
            Image.drawChangedImage(image,(posX,posY + int(dy)))
            return
        Image.drawChangedImage(image,(posX,posY))

class playNote():
    def __init__(self, nomallocal, pressDir, rightDir):
        global display_Height
        global display_Width
        global Notes
        self.posY = 0.95*display_Height
        self.posX = []

        for i in range(0,5):
            self.posX.append(display_Width/2 + 1.5*(i-2)*Notes.Images[i].Image.get_width())
        self.Images = [] #imagem a ser desenhada
        self.NormalStateImage = [] #imagem a ser desenhada quando os botões para pressionar as notas não forem ativados
        self.pressedImages = [] #imagem a ser desenhada quando os botões forem ativados e errarem
        self.rightImages = [] #imagem a ser desenhada quando as notas forem pressionadas corretamente
        i = 0
        
        for loc in nomallocal:
            self.NormalStateImage.append(Image(loc))
            self.Images.append(Image(loc))
            i = i + 1

        for loc in pressDir:
            self.pressedImages.append(Image(loc))

        for loc in rightDir:
            self.rightImages.append(Image(loc))
        self.i = i #número de imagens armazenadas na variável

    def notePressed(self, i, time, impresTime):
        global buttonList
        global deltaTime
        global indexButtonDraw
        global counterros, countacertos
        if not buttonList[i]:
            self.Images[i] = self.pressedImages[i]
            return

        t = time - buttonList[i][0] - 2*deltaTime
        t = impresTime*2 #garante que entra no próximo loop
        n = indexButtonDraw[i]
        j = -1
        
        while t >= impresTime and  j < n:
            j = j + 1
            t = time - buttonList[i][j] - 2*deltaTime
        if onPause == False:
            if t < impresTime and t > -impresTime:
                self.Images[i] = self.rightImages[i] #troca a imagem a ser desenhada
                del buttonList[i][j]
                indexButtonDraw[i] = indexButtonDraw[i] - 1
                countacertos = countacertos + 1
                # print('acertos = ', countacertos) #adiciona os pontos por ter acertado a nota
            else:
                self.Images[i] = self.pressedImages[i]
                errorSound.play()
                counterros = counterros + 1
                # print('erros = ', counterros)
    def noteUnpress(self, i):
        self.Images[i] = self.NormalStateImage[i]

    def drawPlayNotes(self):
        i = 0
        while i < 5:
            pos = (self.posX[i],self.posY)
            Image.drawChangedImage(self.Images[i].Image,(self.posX[i]/2+280,self.posY))
            i = i + 1

    def events(self, evt):
        global Time
        imprecisionTime = 1 #intervalo de tempo em que o jogador pode ser impreciso
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
                self.notePressed(i, Time, imprecisionTime)
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
Notes.loadImages(("images/green_note.png","images/yellow_note.png","images/red_note.png","images/blue_note.png","images/orange_note.png"))
pressNotes = playNote(nomallocal = ("images/green_fixed.png","images/yellow_fixed.png","images/red_fixed.png","images/blue_fixed.png","images/orange_fixed.png")
    ,pressDir = ("images/green_pressed.png","images/yellow_pressed.png","images/red_pressed.png","images/blue_pressed.png","images/orange_pressed.png")
    ,rightDir = ("images/greenPressed.png","images/yellowPressed.png","images/redPressed.png","images/bluePressed.png","images/orangePressed.png"))
###### alterar as imagens dorightDir

def makesList():
    global buttonList
    lastTime = 0
    n = 0
    while n < 200:
        i = random.randint(0,4)
        if buttonList[i]:
            lastTime = buttonList[i][len(buttonList[i]) - 1]
        lastTime = lastTime + random.randint(0,40)/5
        buttonList[i].append(lastTime)
        n = n + 1

def makesListVirada():
    global buttonList
    lastTime = 0
    x=2
    buttonList = ([12.1, 17.8, 23.6, 25, 30.1, 31.5, 36.6, 38, 43.1, 44.5, 48.7, 52.2, 52.9, 57.8, 61.1, 64.6, 65.3, 70.2],
                  [10.7, 12.9, 16.6, 50.8, 53.6, 57.1, 63.2, 66, 69.5],
                  [11.6, 15.2, 17.2, 22.9, 24.3, 29.4, 30.8, 35.9, 37.3, 42.4, 43.8, 48, 49.4, 55.7, 60.4, 61.8, 68.1],
                  [19.2, 50.1, 54.3, 55.0, 58.5, 59.2, 62.5, 66.7, 67.4, 70.9, ],
                  [6.9, 7.4, 7.9, 10, 16.0, 22.2, 28.7, 35.2, 41.7, 47.3, 51.5, 56.4, 59.7, 63.9, 68.8])
BackGr  = pygame.image.load("images/backgr_ok.png")
def beginScene():
    global onPause
    global display_Width
    global display_Height
    global FPS
    global gameName
    global gameDisplay
    global musicaJogo
    global atual_frame_rect
    global BackGr
    atual_frame_rect.append(gameDisplay.blit(BackGr, (0, 0)))
    onPause = False
    global Time
    Time = 0.0
    gameDisplay.fill((0.0,0.0,0.0))
    gameDisplay = DrawDisplay(display_Width,display_Height,FPS,gameName)
    musicaJogo.play()
    
beginScene()

def ButtonsToDraw():
    global buttonList
    global indexButtonDraw
    global Time
    global deltaTime
    global Notes
    global display_Width
    global pressNotes
    global counterros
    i = Notes.i - 1
    while i >= 0:
        if buttonList[i]:
            if Time - buttonList[i][0] > 2*deltaTime:
                del buttonList[i][0]
                counterros += 1
                indexButtonDraw[i] = indexButtonDraw[i] - 1
        i = i - 1
    i = Notes.i - 1
    leftLine = display_Width/2 - 2*45
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
            Notes.isometricPositionDraw(i,buttonList[i][j])
        i = i-1

def drawScene():
    global gameDisplay
    global background_surface
    global display_Width, display_Height
    global counterros, countacertos,BackGr

    #gameDisplay.blit(background_surface,(0,0))
    gameDisplay.blit(BackGr, (0,0))
    """ImageMestreNormal = pygame.image.load('images/normal.png')
    ImageMestreSurprised = pygame.image.load('images/surpresa.png')
    ImageMestreSad = pygame.image.load('images/triste.png')
    ImageMestreDead = pygame.image.load('images/morta.png')
    ImageMestreWings = pygame.image.load('images/mortaAsas.png')
    
    gameDisplay.blit(ImageMestreNormal, (display_Width/2 - 125 ,45))"""

    """if counterros > 70 and counterros < 100:
        gameDisplay.blit(ImageMestreSad, (display_Width/2 - 125 ,45))
    elif counterros >= 100 and counterros < 110:
        gameDisplay.blit(ImageMestreDead, (display_Width/2 - 125 ,45))
    elif counterros >= 110: #gameover
        gameDisplay.blit(ImageMestreWings, (display_Width/2 - 125 ,45))

    if countacertos > 50:
        gameDisplay.blit(ImageSurprised, (display_Width/2 - 125 ,45))"""

    ButtonsToDraw()

ImageOne = pygame.image.load('images/cont1.png')
ImageTwo = pygame.image.load('images/cont2.png')
ImageThree = pygame.image.load('images/cont3.png')
ImageFour = pygame.image.load('images/cont4.png')
CarniChegou = pygame.image.load('images/carniceriachegou.png')

def contRegress():
    global ImageOne
    global ImageTwo
    global ImageThree
    global ImageFour
    global CarniChegou
    global atual_frame_rect

    timePause = 0
    
    if temporizador >=(3+timePause) and temporizador <(3.8+timePause):
        atual_frame_rect.append(gameDisplay.blit(ImageOne, (display_Width/2 - 250,100)))
    elif temporizador >=3.8 and temporizador <4.6:
        atual_frame_rect.append(gameDisplay.blit(ImageTwo, (display_Width/2 - 180,100)))
    elif temporizador >=4.6 and temporizador <5.4:
        atual_frame_rect.append(gameDisplay.blit(ImageThree, (display_Width/2 - 180,100)))
    elif temporizador >=5.4 and temporizador <6.2:
        atual_frame_rect.append(gameDisplay.blit(ImageFour, (display_Width/2 - 220,100)))
    elif temporizador >=25.5 and temporizador <27.7:
        atual_frame_rect.append(gameDisplay.blit(CarniChegou, (display_Width/2 - 370,280)))

def Update():
    global Time
    global onPause
    global Frame
    global gameExit
    global FPS
    global pressNotes
    global gameDisplay, display_Width, display_Height
    global musicaJogo
    global counterros, countacertos

    score = countacertos - counterros
    
    """ImagePause = pygame.image.load('images/pause.png')
    ImageScore = pygame.image.load('images/score.png')"""
    dt = clock.tick(FPS)/1000
    if onPause == False:
        Frame = Frame + 1
        Time = Time + dt

    ##painel de scores
    """text = pygame.font.Font("Symtext.ttf", 37)
    realScore = text.render(str(score), 1, white)"""

    drawScene()
    evt = Event()
    for event in evt:
        if event.type == GameQuit():
            gameExit = True
        elif event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_ESCAPE:
                counterros = counterros - 1

                if onPause:
                    onPause = False
                    musicaJogo.unpause()
                    print(onPause)
                    
                elif not onPause:
                    onPause = True
                    musicaJogo.pause()

                    print(onPause)
                    #fazer a imagem ficar enquanto o pause é vdd
                    #gameDisplay.blit(ImagePause, (150,300))
           
    """if onPause == False:
        gameDisplay.blit(ImageScore, (40,630))
        gameDisplay.blit(realScore, (240,619))
    """
    contRegress()
    global atual_frame_rect,last_frame_rect
    rects = atual_frame_rect + last_frame_rect
    pressNotes.events(evt)
    pygame.display.update(rects)
    last_frame_rect = atual_frame_rect
    atual_frame_rect = []

#makesList()
makesListVirada()

inicio = time.time()
tempozera1 = [0]
tempozera2 = [0]
i=0



frame = 0
while not gameExit:

    fim = time.time()
    temporizador = fim - inicio
    #fimPause = temporizador
    #inicioPause = fimPause
    if onPause == True:
        tempozera1.append(temporizador)
        i=i+1
        #inicioPause = temporizador
        #print('pausadoooooooooo', tempozera1[i]-tempozera1[1])
    if onPause == False:
        fimPause = temporizador
    
        
    #print('pausouuuuuuuuuuuuuuuuuuuuuuuuu?', tempozera1[i])
    if frame%30 == 0:
        print(temporizador)
    Update()
    frame += 1
Quit()
print("fim")
