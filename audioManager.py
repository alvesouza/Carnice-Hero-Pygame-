import pygame


class sound:
    def __init__(self,local,numChannel):
        if pygame.mixer.get_init() == None:
            pygame.mixer.init()
        print(str(pygame.mixer.get_num_channels()))
        self.Channel = pygame.mixer.Channel(numChannel)
        self.sound = pygame.mixer.Sound(local) #armazena no objeto o local do som
        self.volume = 100
    def play(self):#inicia o som
        self.Channel.play(self.sound)
        self.setVolume(self.volume)
    def pause(self):#Para o som
        self.Channel.pause()
    def unpause(self):
        self.Channel.unpause()
    def setVolume(self,vol = 100):#o volume é de 0-100
        self.volume = vol
        
        self.Channel.set_volume(vol/100.0)
    def volumeIs(self):#retorna o vlume de 0-100
        return 100*self.Channel.get_volume()
        
class music:
    def __init__(self,local):
        if pygame.mixer.get_init() == None:
            pygame.mixer.init()
        pygame.mixer.music.load(local)
        self.startedPlaying = False
        self.isPaused = False
        self.volume = 100

    def play(self):#inicia a musica
        if not self.startedPlaying:
            pygame.mixer.music.play()
            self.startedPlaying = True
        elif self.isPaused:
            pygame.mixer.music.unpause()
            self.isPaused = False
        self.setVolume(self.volume)
    def pause(self):#Para a musica
        pygame.mixer.music.pause()
        self.isPaused = True
    def setVolume(self,vol = 100):#o volume é de 0-100
        self.volume = vol
        pygame.mixer.music.set_volume(vol/100)
    def volumeIs(self):#retorna o vlume de 0-100
        return self.volume
    def setTime(self,time):
        pygame.mixer.music.set_pos(time)
    def getTime(self):
        return pygame.mixer.music.get_pos()
    def rewind(self):
        pygame.mixer.music.rewind()

def teste():
    display_Width = 600
    display_Height = 300
    FPS = 2
    gameExit = False
    Time = 0.0
    Frame = 0
    gameDisplay = pygame.display.set_mode((display_Width, display_Height))
    clock = pygame.time.Clock()
    background_surface = pygame.Surface((display_Width, display_Height))
    background_surface.fill((0, 0, 0))
    song = music("sound mp3\Olodum.mp3")
    #print('flag' + str(flag))
    print("Aperte 'a' para play")
    print("Aperte 's' para pause")
    print("Aperte 'd' para rewind")
    print("Aperte 'f' para reduzir o som pela metade")
    print("Aperte 'g' para dizer o volume da musica")
    while not gameExit:
        dt = clock.tick(FPS)/1000
        if True:
            Frame = Frame + 1
            Time = Time + dt
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameDisplay.blit(background_surface,(0,0))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        song.play()
                        print("Play")
                    elif event.key == pygame.K_s:
                        song.pause()
                        print("Pause")
                    elif event.key == pygame.K_d:
                        song.rewind()
                        print("Rewind")
                    elif event.key == pygame.K_f:
                        song.setVolume(song.volumeIs()/2)
                        print("reduziu o volume pela metade")
                    elif event.key == pygame.K_g:
                        print("o volume é "+ str(song.volumeIs()))
            pygame.display.flip()

    pygame.quit()

teste()
