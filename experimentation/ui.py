import pygame
from PygameUIKit import Group, button, slider

W = 800
H = 600


class MyGame:
    def __init__(self):
        # You class code here
        self.window = pygame.display.set_mode((W, H), pygame.RESIZABLE)
        # Ui
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter
        self.btn_start = button.ButtonText("Start",
                                           self.on_test,
                                           rect_color=(85, 145, 92),
                                           fixed_width=200,
                                           border_radius=10,
                                           text_align="center",
                                           ui_group=self.ui)

        self.btn_quit = button.ButtonText("Quit", self.quit,
                                          rect_color=(181, 71, 71),
                                          fixed_width=180,
                                          border_radius=10,
                                          text_align="center",
                                          ui_group=self.ui)


    def on_test(self):
        print("Testing....")


    def run(self):
        while True:  # Game loop
            # Your game code here

            # Ui
            # Handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                self.ui.handle_event(event)  # Handle the events for all the ui elements

            # Draw
            self.window.fill((0, 0, 0))
            self.btn_start.draw(self.window, *self.btn_start.surface.get_rect(center=(W // 2, H // 2 - 50)).topleft)
            self.btn_quit.draw(self.window, *self.btn_quit.surface.get_rect(center=(W // 2, H // 2 + 50)).topleft)
            pygame.display.flip()

    def start(self):
        print("Starting")

    def quit(self):
        print("Quitting")
        pygame.quit()


if __name__ == "__main__":
    pygame.init()
    MyGame().run()