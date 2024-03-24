import pygame
from PygameUIKit import Group, button

W = 800
H = 600

class State():
    def __init__(self, engine):
        self.engine = engine
    def on_draw(self, surface): pass
    def on_event(self, event): pass
    def on_update(self, delta): pass

class Machine:
    def __init__(self):
        self.current = None
        self.next_state = None

    def update(self):
        if self.next_state:
            self.current = self.next_state
            self.next_state = None

class DisplayEngine:
    def __init__(self, caption, fps, width, height, flags=0):
        pygame.display.set_caption(caption)
        self.surface = pygame.display.set_mode((width, height), flags)
        self.rect = self.surface.get_rect()
        self.clock = pygame.time.Clock()
        self.running = True
        self.delta = 0
        self.fps = fps

        self.machine = Machine()

    def loop(self):
        while self.running:
            self.machine.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.machine.current.on_event(event)

            self.machine.current.on_draw(self.surface)
            self.machine.current.on_update(self.delta)

            pygame.display.flip()
            self.delta = self.clock.tick(self.fps)

    def run(self, state):
        self.machine.current = state
        self.loop()

class YourStateA(State):
    def __init__(self, engine):
        super().__init__(engine)
        self.background = 'dodgerblue'

    def on_draw(self, surface):
        surface.fill(self.background)

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.engine.machine.next_state = UISTATEB(self.engine)

class YourStateB(State):
    def __init__(self, engine):
        super().__init__(engine)
        self.background = 'firebrick'

    def on_draw(self, surface):
        surface.fill(self.background)

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.engine.machine.next_state = YourStateA(self.engine)

class UISTATEB(State):
    def __init__(self, engine):
        super().__init__(engine)
        self.background = 'white'
        #UI
        self.ui = Group()  # Create a group to hold all the ui elements. This is filled with the ui elements below thanks to the ui_group parameter
        self.btn_start = button.ButtonText("Start",
                                           self.change_state_a,
                                           rect_color=(85, 145, 92),
                                           fixed_width=200,
                                           border_radius=10,
                                           text_align="center",
                                           ui_group=self.ui)

        self.btn_quit = button.ButtonText("Quit",
                                          self.change_state_b,
                                          rect_color=(181, 71, 71),
                                          fixed_width=180,
                                          border_radius=10,
                                          text_align="center",
                                          ui_group=self.ui)
    def change_state_a(self):
        self.engine.machine.next_state = YourStateA(self.engine)

    def change_state_b(self):
        self.engine.machine.next_state = YourStateB(self.engine)

    def on_draw(self, surface):
        surface.fill(self.background)
        self.btn_start.draw(surface, *self.btn_start.surface.get_rect(center=(W // 2, H // 2 - 50)).topleft)
        self.btn_quit.draw(surface, *self.btn_quit.surface.get_rect(center=(W // 2, H // 2 + 50)).topleft)
        pygame.display.flip()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.engine.machine.next_state = YourStateB(self.engine)
        self.ui.handle_event(event)

