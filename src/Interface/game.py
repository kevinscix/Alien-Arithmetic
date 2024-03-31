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
    """
    Represents the game state for login and sign-in functionalities.

    This class inherits from the State class and provides functionality for game states.

    Attributes:
        ui (Group): A group to hold all the UI elements.
        settings (dict): Settings for the game.
        user (SaveState): Represents the user's state.
        level (int): The current level of the game.
        player (Player): Represents the player object.
        pause (bool): Represents the pause state of the game.
        btn_pause (ButtonTwoStates): Button to pause/resume the game.
        btn_level (ButtonPngIcon): Button to change the game level.
        shots (List[dict]): List of bullets shot by the player.
        exAsteroids (List[list]): List of exploded asteroids.
        rounds (int): Number of rounds in the game.
        player_pos (List[int]): Position of the player.
        asteroidMaster (Asteroid): Manages asteroids in the game.
        explosion_animation (List[pygame.Surface]): List of explosion animation frames.
        music (object): Represents game music.
        sfx (object): Represents sound effects.
        pause_surface (pygame.Surface): Surface for displaying "PAUSED" text.
        ended (bool): Represents whether the game has ended.

    Methods:
        change_state_level: Changes the game state to the level selection state.
        change_state_pause: Toggles the pause state of the game.
        create_shot: Creates a bullet shot by the player.
        move_shot: Moves the bullets on the screen.
        remove_shot: Removes bullets that have moved off the screen.
        get_rect: Returns the rectangle bounding the object.
        shot_collided: Checks if a bullet has collided with an asteroid.
        border_collided: Checks if an asteroid has collided with the border.
        updateHealthBar: Updates the health bar of the player.
        newRound: Starts a new round in the game.
        onGameEnd: Handles the game end event.
        onGameWin: Handles the game win event.
        on_draw: Draws the game elements on the screen.
        on_event: Handles the game events.
        handle_movement: Handles player movement in the game.
    """
    def __init__(self, engine, user, mode, level):
        """
        Initializes a GameState object.

        Args:
            engine: The game engine.
            user (SaveState): The user's state.
            mode: The game mode.
            level: The current level of the game.
        """
        super().__init__(engine)
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter
        WIDTH, HEIGHT = 800, 600

        self.settings = Settings().getbackground()

        self.user : SaveState = user
        self.level = level

        #make this into a utils function?
        currentPath = os.path.dirname(__file__)  # __file__ is the path to the current script
        parent_dir = os.path.dirname(currentPath)  # Moves up to 'interface'

        shotImagePath = os.path.join(current_dir, "..", "assets", "visuals", "projectiles", "red projectile icon.png")
        pauseButtonPath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "pauseButton.png")
        playButtonPath = os.path.join(currentPath, "..", "assets", "visuals", "buttons", "text buttons", "resume button pix.png")

        self.font_path = os.path.join(parent_dir, "assets", "visuals", "fonts", "PressStart2P-Regular.ttf")

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

        self.explosion_animation = []
        for i in range(7):
            explosion_frame_ath = os.path.join(parent_dir, "assets", "visuals", "explosion!!!!!", "explosion frames", "explosion{}.png".format(str(i + 1)))
            frame = pygame.image.load(explosion_frame_ath).convert_alpha()
            self.explosion_animation.append(pygame.transform.scale(frame, (60, 60)))

         #music
        from components.media import music, sfx
        self.music = music()
        self.music.game_music()
        self.sfx = sfx()

        self.pause_surface = pygame.font.Font(self.font_path, 50
                                              ).render("PAUSED", True, (255,0,0))



        self.ended : bool = False


    def change_state_level(self):
        """
        Changes the game state to the level selection state.

        This method changes the game state to the level selection state
        by setting the next state of the state machine to the OuterLevelState.

        Args:
            None

        Returns:
            None
        """
        from Interface.level import OuterLevelState
        self.sfx.button_sound()
        self.engine.machine.next_state = OuterLevelState(self.engine, self.user)

    #only button that exsit on the screen
    def change_state_pause(self):
        """
        Toggles the pause state of the game.

        This method toggles the pause state of the game by
        switching the value of the pause attribute.

        Args:
            None

        Returns:
            None
        """
        self.sfx.button_sound()
        self.pause = not self.pause
        pass

    #Game specific functions
    def create_shot(self, player_pos):
        """
        Creates a bullet shot by the player.

        This method creates a bullet shot by the player at the specified position.

        Args:
            player_pos (List[int]): The position of the player.

        Returns:
            dict: A dictionary containing the details of the created shot.
        """
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
        """
        Moves the bullets on the screen.

        This method moves the bullets on the screen upwards.

        Args:
            None

        Returns:
            None
        """
        for shot in self.shots:
            shot['position'][1] -= shot['speed']


    def remove_shot(self):
        """
        Removes bullets that have moved off the screen.

        This method removes bullets that have moved off the top of the screen.

        Args:
            None

        Returns:
            None
        """
        for shot in self.shots:
            if shot['position'][1] < 0:
                self.shots.remove(shot)

    def get_rect(self, obj):
        """
        Returns the rectangle bounding the object.

        This method returns the rectangle bounding the object.

        Args:
            obj (dict): The object for which the rectangle is to be calculated.

        Returns:
            pygame.Rect: The rectangle bounding the object.
        """
        return pygame.Rect(obj['position'][0],
                        obj['position'][1],
                        obj['surface'].get_width(),
                        obj['surface'].get_height())

    def shot_collided(self):
        """
        Checks if a shot collided with an asteroid.

        This method checks if the player's shot has collided with any asteroid.
        If a collision is detected, appropriate actions are taken, such as updating
        player's score and health, removing the shot and asteroid, and playing sound effects.

        Args:
            None

        Returns:
            bool: True if a collision occurred, False otherwise.
        """
        try:
            shot_rect = self.get_rect(self.shots[0])
            for asteroid in self.asteroidMaster.asteroid_arr:
                if shot_rect.colliderect(self.get_rect(asteroid)):
                    self.shots = []
                    self.user.addOneQuestion()
                    #write logic about point gain and lost for health if correct or not
                    if asteroid['correct']:
                        #gain health gain store
                        #how should we draw the health bar onto the screen
                        #remove asteroids and start new level
                        self.player.addPoints()
                        self.user.addOneCorrect()
                        self.newRound()
                    else:
                        if not asteroid['destroyed']:
                            self.player.damage()
                            #call destory func here...
                            self.exAsteroids.append([asteroid, 0])
                            self.asteroidMaster.asteroid_arr.remove(asteroid)
                            self.sfx.explosion_sound()
                            asteroid['destroyed'] = True
                    return True
            return False
        except:
            pass

    def border_collided(self):
        """
        Checks if an asteroid collided with the border.

        This method checks if any asteroid collided with the border of the game screen.

        Args:
            None

        Returns:
            bool: True if a collision occurred, False otherwise.
        """
        for asteroid in self.asteroidMaster.asteroid_arr:
            if self.border.colliderect(self.get_rect(asteroid)):
                return True
        return False

    def updateHealthBar(self):
        """
        Updates the health bar based on the player's health.

        This method updates the health bar width based on the player's health scale.
        If the player's health reaches zero, the game ends.

        Args:
            None

        Returns:
            None
        """
        self.healthbar.width = 800 * self.player.healthScale()
        if self.healthbar.width == 0:
            self.onGameEnd()

    def newRound(self):
        """
        Starts a new round of the game.

        This method starts a new round of the game by generating new asteroids
        and resetting round-related variables.

        Args:
            None

        Returns:
            None
        """
        #remove current asteroid and shots
        if self.rounds > 0:
            print(self.player.points)
            self.asteroidMaster.asteroid_arr = []
            self.asteroidMaster.generateAsteroids()
            self.rounds -= 1
        else:
            self.onGameWin()

    def onGameEnd(self):
        """
        Handles game ending.

        This method handles the end of the game by resetting variables, saving user data,
        and preparing for a return to the level selection screen.

        Args:
            None

        Returns:
            None
        """
        self.ended = True
        #empty all variables
        self.shots = []
        self.exAsteroids = []
        self.asteroidMaster.asteroid_arr = []
        self.gamePlay1Image = pygame.transform.scale(self.settings['over'], (800, 600))
        self.user.save_settings(self.user.model_dump_json(), self.user.name)
        
        #offset for the start
        self.user.correctAmt -= 1
        self.user.questionsCompleted -= 1
        self.user.score -= 10
        #return user to level

    def onGameWin(self):
        """
        Handles game win.

        This method handles the win condition of the game by updating user data,
        advancing the level, and preparing for a return to the level selection screen.

        Args:
            None

        Returns:
            None
        """
        self.ended = True
        #empty all variables
        self.shots = []
        self.exAsteroids = []
        self.asteroidMaster.asteroid_arr = []

        #increment the level by up
        self.gamePlay1Image = pygame.transform.scale(self.settings['level'], (800, 600))

        self.user.score += self.player.points

        #chekcs the level of the current level to increment accordingly
        if self.level == 3:
            if self.user.level[0] == 3:
                print("FINISHED LAST LEVEL")
            else:
                self.user.level[0] += 1
                self.user.level[1] = 1
        elif self.level < 3:
            self.user.level[1] += 1
        
        #offset for the start
        self.user.correctAmt -= 1
        self.user.questionsCompleted -= 1
        self.user.score -= 10
        self.user.save_settings(self.user.model_dump_json(), self.user.name)

    def on_draw(self, surface):
        """
        Draws the game elements on the screen.

        This method draws various game elements, including background, player, asteroids,
        health bar, and UI buttons, on the provided surface.

        Args:
            surface (pygame.Surface): The surface to draw the game elements on.

        Returns:
            None
        """
        surface.blit(self.gamePlay1Image, (0, 0))
        if self.ended == False:
            self.btn_pause.draw(surface, 0, 515)

        #stops incrementing the moving shots
        if not self.pause:
            self.move_shot()
            self.remove_shot()
            self.asteroidMaster.move_asteroids()
        else:
            surface.blit(self.pause_surface, [230,300])


        for shot in self.shots:
            surface.blit(shot['surface'], shot['position'])

        for asteroid in self.asteroidMaster.asteroid_arr:
            surface.blit(asteroid['surface'], asteroid['position'])
            surface.blit(asteroid['number_surface'], [asteroid['position'][0] + 15, asteroid['position'][1] + 15])

        #draws the dead asteroids animation
        for asteroid in self.exAsteroids:
            surface.blit(self.explosion_animation[int(asteroid[1])], asteroid[0]['position'])
            asteroid[1] += 0.2

            if asteroid[1] >= len(self.explosion_animation):
               # "animation cycle is finished remove from list should despawn here..."
                self.exAsteroids.remove(asteroid)


        #theres no keyboard condition or still need to be determined for menu
        self.shot_collided()

        #checks the shot_collided()
        if self.border_collided():
            self.player.removePoints()
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
        """
        Handles user events.

        This method handles user events such as key presses and button clicks.

        Args:
            event (pygame.event.Event): The event to handle.

        Returns:
            None
        """

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shot = self.create_shot(player_pos=self.player_pos)
                if shot:
                    self.shots.append(shot)
                    self.sfx.shoot_sound()
            if event.key == pygame.K_ESCAPE:
                print("Returning to menu screen")
                self.onGameEnd()
            if event.key == pygame.K_p:
                self.btn_pause._on_click()

        self.ui.handle_event(event)


    def handle_movement(self):
        """
        Handles player movement.

        This method handles player movement based on the keyboard input.

        Args:
            None

        Returns:
            None
        """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player_pos[0] > -40:
            self.player_pos[0] -= self.player_speed
        if keys[pygame.K_RIGHT] and self.player_pos[0] < 800 - 150:
            self.player_pos[0] += self.player_speed

