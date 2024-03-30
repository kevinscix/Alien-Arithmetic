import pygame
from PygameUIKit import Group, button

class State():
    def __init__(self, engine):
        self.engine = engine
    def on_draw(self, surface): pass
    def on_event(self, event): pass
    def on_update(self, delta): pass

    def handle_movement(self): pass

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
            try:
                self.machine.current.handle_movement()
            except:
                continue
            pygame.display.flip()
            self.delta = self.clock.tick(self.fps)

    def run(self, state):
        self.machine.current = state
        self.loop()

