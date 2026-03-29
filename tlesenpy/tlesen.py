import os
import warnings

# Silence Pygame and deprecation warnings
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
warnings.filterwarnings("ignore", category=DeprecationWarning)

import pygame

class Taibolesen:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        self.running = True

        # --- Set the Window Icon from inside the module folder ---
        try:
            # Finds the directory of THIS file (tlesen.py)
            module_dir = os.path.dirname(__file__)
            # Joins it with the icons folder
            icon_path = os.path.join(module_dir, "icons", "icon.png")
            
            if os.path.exists(icon_path):
                icon_surf = pygame.image.load(icon_path)
                pygame.display.set_icon(icon_surf)
            
            pygame.display.set_caption("Taibolesen Engine")
        except Exception as e:
            # We print this so you know if the path is still slightly off
            print(f"Warning: Could not load icon from {icon_path}. Error: {e}")

    def clear_layered(self):
        self.screen.fill((20, 20, 50)) 
        top_half = (0, 0, self.width, self.height // 2)
        self.screen.fill((80, 80, 90), top_half)

    def load_image(self, path):
        return pygame.image.load(path).convert_alpha()

    def draw_image(self, image, x, y):
        self.screen.blit(image, (x, y))

    def get_keys(self):
        return pygame.key.get_pressed()

    def run(self, hx_update):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.VIDEORESIZE:
                    self.width, self.height = event.size
                    self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
            
            hx_update()
            
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()