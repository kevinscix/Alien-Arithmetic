import os
import sys

#change directory
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)  # Moves up to 'interface'
src_dir = os.path.dirname(parent_dir)  # Moves up to 'src'
sys.path.append(src_dir)

from Interface.state_machine import State
from Interface.modules.state import SaveState
from components.asteroid import Asteroid
from components.player import Player
from PygameUIKit import Group, button
import pygame

from settings import Settings
#this file is a quick scehem of how a state would look like for login and sign in state!

#this isn't importing properly???? ill figure it out or someone else can i give up

class GameState(State):
    def __init__(self, engine, user, mode, level):
        super().__init__(engine)
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter
        WIDTH, HEIGHT = 800, 600

        self.settings = Settings().getbackground()

        self.user : SaveState = user
        self.level = level

        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        shotImagePath = os.path.join(current_dir, "..", "assets", "visuals", "projectiles", "red projectile icon.png")
        pauseButtonPath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "pauseButton.png")
        playButtonPath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "resume button pix.png")

        self.font_path = os.path.join(currentPath, "..","assets", "visuals", "fonts", "PressStart2P-Regular.ttf")

        self.gamePlay1Image = pygame.transform.scale(self.settings['background'], (WIDTH, HEIGHT))
        self.playerImage = pygame.transform.scale(self.settings['ship'], (200, 200))

        #we need someone to load in the bullets
        self.shotImage = self.settings['shot']
        self.shotImage = pygame.transform.scale(self.shotImage, (50, 50))


        self.pauseButton = pygame.image.load(os.path.normpath(pauseButtonPath))
        self.pauseButton = pygame.transform.scale(self.pauseButton, (65, 85))
        self.playButton = pygame.image.load(os.path.normpath(playButtonPath))
        self.playButton = pygame.transform.scale(self.playButton, (65, 85))

        self.border = pygame.rect.Rect(0, 370, 800, 40)
        self.healthbar = pygame.rect.Rect(0, 0, 800, 10)
        self.player = Player()

        self.pause : bool = False
       # Start button
        self.btn_pause = button.ButtonTwoStates(
            self.playButton,
            self.pauseButton,
            self.change_state_pause,
            ui_group=self.ui
        )

        levelButtonPath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "levelSelectButton.png")
        self.levelButton = pygame.image.load(os.path.normpath(levelButtonPath))
        self.levelButton = pygame.transform.scale(self.levelButton, (200, 80))
        self.btn_level = button.ButtonPngIcon(
            self.levelButton,
            self.change_state_level,
            ui_group=self.ui
        )


        from components.media import sfx
        self.sfx = sfx()

        #game constants
        self.shots = []
        self.player_radius = 25
        self.player_speed = 5
        self.bullet_radius = 5
        self.exAsteroids = []

        self.rounds = 10

        #needs a better way to do the width and height
            # a big issue is how we pass the surface around this is causing problems
            # think of a work around
        self.player_pos = [WIDTH // 2, ((HEIGHT / 4) * 3 - 60)]

        self.asteroidMaster = Asteroid(mode, level)
        self.asteroidMaster.generateAsteroids()

        self.explosionAnimatation = []
        for i in range(7):
            explosionFramePath = os.path.join(parent_dir, "assets", "visuals", "explosion!!!!!", "explosion frames", "explosion{}.png".format(str(i + 1)))
            frame = pygame.image.load(explosionFramePath).convert_alpha()
            self.explosionAnimatation.append(pygame.transform.scale(frame, (60, 60)))

         #music
        from components.media import music, sfx
        self.music = music()
        self.music.game_music()
        self.sfx = sfx()

        self.pause_surface = pygame.font.Font(self.font_path, 50
                                              ).render("PAUSED", True, (255,0,0))



        self.ended : bool = False


    def change_state_level(self):
        from Interface.level import OuterLevelState
        self.sfx.button_sound()
        self.engine.machine.next_state = OuterLevelState(self.engine, self.user)

    #only button that exsit on the screen
    def change_state_pause(self):
        self.sfx.button_sound()
        self.pause = not self.pause
        pass

    #Game specific functions
    def create_shot(self, player_pos):
        #limits the number of bullets on screen to one
        if not (len(self.shots) > 0):
            bullet_pos = [player_pos[0] + 75, player_pos[1]]
            return {
                'surface' :  self.shotImage,
                'position' : bullet_pos,
                'speed' : 8,
                'radius' : self.bullet_radius,
            }

    def move_shot(self):
        for shot in self.shots:
            shot['position'][1] -= shot['speed']


    def remove_shot(self):
        for shot in self.shots:
            if shot['position'][1] < 0:
                self.shots.remove(shot)

    def get_rect(self, obj):
        return pygame.Rect(obj['position'][0],
                        obj['position'][1],
                        obj['surface'].get_width(),
                        obj['surface'].get_height())

    def shot_collided(self):
        try:
            shot_rect = self.get_rect(self.shots[0])
            for asteroid in self.asteroidMaster.asteroidArr:
                if shot_rect.colliderect(self.get_rect(asteroid)):
                    self.shots = []
                    #write logic about point gain and lost for health if correct or not
                    if asteroid['correct']:
                        #gain health gain store
                        #how should we draw the health bar onto the screen
                        #remove asteroids and start new level
                        self.player.addPoints(10)
                        self.newRound()
                    else:
                        if not asteroid['destroyed']:
                            self.player.damage()
                            #call destory func here...
                            self.exAsteroids.append([asteroid, 0])
                            self.asteroidMaster.asteroidArr.remove(asteroid)
                            self.sfx.explosion_sound()
                            asteroid['destroyed'] = True

                    return True
            return False
        except:
            pass

    def border_collided(self):
        for asteroid in self.asteroidMaster.asteroidArr:
            if self.border.colliderect(self.get_rect(asteroid)):
                return True
        return False

    def updateHealthBar(self):
        self.healthbar.width = 800 * self.player.healthScale()
        if self.healthbar.width == 0:
            self.onGameEnd()

    def newRound(self):
        #remove current asteroid and shots
        if self.rounds > 0:
            print(self.player.points)
            self.asteroidMaster.asteroidArr = []
            self.asteroidMaster.generateAsteroids()
            self.rounds -= 1
        else:
            self.onGameWin()

    def onGameEnd(self):
        self.ended = True
        #empty all variables
        self.shots = []
        self.exAsteroids = []
        self.asteroidMaster.asteroidArr = []
        self.gamePlay1Image = pygame.transform.scale(self.settings['over'], (800, 600))

        pass
        #return user to level

    def onGameWin(self):
        self.ended = True
        #empty all variables
        self.shots = []
        self.exAsteroids = []
        self.asteroidMaster.asteroidArr = []

        #increment the level by up
        self.gamePlay1Image = pygame.transform.scale(self.settings['level'], (800, 600))


        self.user.score += self.player.points

        if self.level == 3:
            if self.user.level[0] == 3:
                print("FINISHED LAST LEVEL")
            else:
                self.user.level[0] += 1
                self.user.level[1] = 1
        elif self.level < 3:
            self.user.level[1] += 1

        self.user.save_settings(self.user.model_dump_json(), self.user.name)
        print(self.user)

    def on_draw(self, surface):
        #pops the screen up
        #problem is the the surface is only passed on surface we can either hard code the width or heights to reduce calling this function
        #over and over again. for the sake of prototyping ill leave it here cause ill figure it out later
        surface.blit(self.gamePlay1Image, (0, 0))
        if self.ended == False:
            self.btn_pause.draw(surface, 0, 515)

        #stops incrementing the moving shots
        if not self.pause:
            #moves the bullets down the screen
            self.move_shot()
            self.remove_shot()
            self.asteroidMaster.move_asteroids()
        else:
            surface.blit(self.pause_surface, [230,300])


        for shot in self.shots:
            surface.blit(shot['surface'], shot['position'])

        for asteroid in self.asteroidMaster.asteroidArr:
            surface.blit(asteroid['surface'], asteroid['position'])
            surface.blit(asteroid['number_surface'], [asteroid['position'][0] + 15, asteroid['position'][1] + 15])



        #draws the dead asteroids animation
        for asteroid in self.exAsteroids:
            surface.blit(self.explosionAnimatation[int(asteroid[1])], asteroid[0]['position'])
            asteroid[1] += 0.2

            if asteroid[1] >= len(self.explosionAnimatation):
               # "animation cycle is finished remove from list should despawn here..."
                self.exAsteroids.remove(asteroid)


        self.shot_collided()
        if self.border_collided():
            self.player.addPoints(-10)
            self.player.damage()
            self.newRound()

        #when still not ended
        if not self.ended:
            self.updateHealthBar()
            pygame.draw.rect(surface, "gray31",  pygame.rect.Rect(310, 520, 165, 80))
            surface.blit(self.asteroidMaster.question_surface, [325, 550])
            surface.blit(self.playerImage, self.player_pos)
            pygame.draw.rect(surface, "green", self.healthbar)
        else:
            self.btn_level.draw(surface, 300, 500)

        pygame.display.flip()


    def on_event(self, event):
        #theres no keyboard condition or still need to be determined for menu
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shot = self.create_shot(player_pos=self.player_pos)
                if shot:
                    self.shots.append(shot)
                    self.sfx.shoot_sound()
            if event.key == pygame.K_ESCAPE:
                print("Returning to menu screen")
                self.change_state_level()
            if event.key == pygame.K_p:
                self.btn_pause._on_click()

        self.ui.handle_event(event)


    def handle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player_pos[0] > -40:
            self.player_pos[0] -= self.player_speed
        if keys[pygame.K_RIGHT] and self.player_pos[0] < 800 - 150:
            self.player_pos[0] += self.player_speed

