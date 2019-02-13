from pygame.locals import *
import pygame
import speech_recognition as sr
import pyaudio
from Player import Player
from Maze import Maze

"""

class Game contains information about: 
    1) how everything is drawn using pygame;
    2) the speech recognition part of the game

"""


class Game:
    windowWidth = 800
    windowHeight = 600

    def __init__(self):
        self._running = True
        self._display_surf = None
        self.player_image = None  # png image of player block
        self.block_image = None   # png image obstacle block
        self.player = Player()
        self.maze = Maze()

    def on_init(self):
        pygame.init()

        # set the window size and don't add the frame/header
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.NOFRAME)

        # set title
        pygame.display.set_caption('Speak To Me')
        self._running = True

        # load images
        self.player_image = pygame.image.load("player.png").convert()
        self.block_image = pygame.image.load("block.png").convert()

    # quit game function
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass

    # adapted from the pygame library documentation/tutorial at https://pythonspot.com/maze-in-pygame/
    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self.player_image, (self.player.x_coordinate, self.player.y_coordinate))
        self.maze.draw(self._display_surf, self.block_image)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            self.on_loop()
            self.on_render()

            """

            Speech recognition section
            - listens for 3 seconds
            - tries to recognize input
            - stores recognized input in a variable

            """

            recognizer = sr.Recognizer()
            mic = sr.Microphone()

            user_input = "x"

            try:

                with mic as source:
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source, 3)

                user_input = str(recognizer.recognize_google(audio))
                print(user_input)

            except sr.RequestError:
                print("unreachable")
            except sr.UnknownValueError:
                print("unknown")
            except sr.WaitTimeoutError:
                print("timeout")

            """
            End of Speech recognition section
            """

            # keyboard input listener
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            """
            Check where the player should move against the input if any
            
            Commands are:
            - "right"
            - "left"
            - "up" (recognizer not very good at "hearing" this)
            - "down"
            - "stop" OR HOLD esc key to stop game
            
            Needs automating - can be made into 1 function
            """

            if user_input == "right":
                # check for obstacle in the maze
                if self.maze.layout[self.player.startingPosition + 1] == 0:
                    self.player.move_right()
                    user_input = "x"

            if user_input == "left":
                # check for obstacle in the maze
                if self.maze.layout[self.player.startingPosition - 1] == 0:
                    self.player.move_left()
                    user_input = "x"

            if user_input == "up":
                # check for obstacle in the maze
                if self.maze.layout[self.player.startingPosition - 13] == 0:
                    self.player.move_up()
                    user_input = "x"

            if user_input == "down":
                # check for obstacle in the maze
                if self.maze.layout[self.player.startingPosition + 13] == 0:
                    self.player.move_down()
                    user_input = "x"

            if keys[K_ESCAPE] or user_input == "stop":
                self._running = False

            self.on_loop()
            self.on_render()
        self.on_cleanup()
