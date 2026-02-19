import pygame
import math

pygame.init()

GREEN, MATTE_WHITE, BLACK, WHITE = (81, 184, 86), (225, 230, 226), (0, 0, 0), (255, 255, 255)
GRID_SIZE = 150
SIZE = 4

class lattice_bacteria():
    def __init__(self):
        self.width = GRID_SIZE*(SIZE+1)
        self.height = GRID_SIZE*(SIZE+1)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.circles = [(GRID_SIZE*i, GRID_SIZE*n) for i in range(1, SIZE+1) for n in range(1, SIZE+1)]
        self.bacteria = [(GRID_SIZE, SIZE*GRID_SIZE)]
        self.font = pygame.font.SysFont("Arial", 18, bold=True)
        self.moves = 0

        pygame.display.set_caption("Lattice bacteria")
    def update(self):
        self.screen.fill(BLACK)

        for i in range(1, SIZE+1):
            pygame.draw.line(self.screen, WHITE, (GRID_SIZE, GRID_SIZE*i), (GRID_SIZE*SIZE, GRID_SIZE*i))
            pygame.draw.line(self.screen, WHITE, (GRID_SIZE*i, GRID_SIZE), (GRID_SIZE*i, GRID_SIZE*SIZE))
        for i in range(len(self.circles)):
            pygame.draw.circle(self.screen, MATTE_WHITE, self.circles[i], 20)
        
        for i in range(len(self.bacteria)):
            pygame.draw.circle(self.screen, GREEN, self.bacteria[i], 25)
        
        text_surface = self.font.render("Moves: " + str(self.moves), True, WHITE)
        self.screen.blit(text_surface, (25, 10))




if __name__ == "__main__":
    running = True
    app = lattice_bacteria()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = event.pos

                for x, y in app.bacteria:
                    dist = math.hypot(mousePos[0]-x, mousePos[1]-y)
                    if dist <= 25:
                        grid_x, grid_y = x, y
                        break

                if grid_y <= GRID_SIZE*SIZE and grid_x <= GRID_SIZE*SIZE:
                    if (grid_x, grid_y) in app.bacteria and (grid_x+GRID_SIZE, grid_y) not in app.bacteria and (grid_x, grid_y-GRID_SIZE) not in app.bacteria:
                        app.moves += 1
                        app.bacteria.remove((grid_x, grid_y))
                        
                        if grid_x < GRID_SIZE*SIZE:
                            app.bacteria.append((grid_x+GRID_SIZE, grid_y))
                        if grid_y > GRID_SIZE:
                            app.bacteria.append((grid_x, grid_y-GRID_SIZE))

        app.update()
        pygame.display.flip()

pygame.quit()