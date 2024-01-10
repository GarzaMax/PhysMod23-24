import pygame


class CollideSquare():
    def __init__(self, mass, velocity, surface, pos):
        self.mass = mass
        self.velocity = velocity
        self.surface = surface
        self.pos = pos


pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)

mass1 = 1000000
time_step = 1000
fps = 1000

clock = pygame.time.Clock()

# Font settings
pygame.font.init()
textfont = pygame.font.SysFont("Segoe UI", 30)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Window settings
pygame.display.set_caption("ITMO Physics Modelling Pi Collisions")
screen.fill((40, 40, 40))

# Big square body
s = pygame.Surface((150, 150))
s.fill((50, 50, 50))

# Little square body
s1 = pygame.Surface((60, 60))
s1.fill((255, 255, 255))

# Squares Specs
m1 = CollideSquare(mass1, -50, s, 300)
m2 = CollideSquare(1, 0, s1, 200)

# Render base geometry
wall = pygame.Rect(35, 500, 5, 300)
pygame.draw.line(screen, WHITE, (40, 500), (40, 0), 5)  # zid vert
pygame.draw.line(screen, WHITE, (800, 450), (0, 450), 15)

collisionCounter = 0

while True:
    clock.tick(fps)

    dt1, dt2 = clock.tick(fps) / 1000, clock.tick(time_step) / 1000
    dt = dt1 * dt2

    r1 = pygame.Rect(m1.pos, 450, 60, 60)
    r2 = pygame.Rect(m2.pos, 450, 60, 60)

    for i in range(time_step):

        m1.pos += m1.velocity * dt
        m2.pos += m2.velocity * dt

        if m1.pos <= m2.pos + 60:
            collisionCounter += 1
            prevVelocityBigSquare, prevVelocityLittleSquare = m1.velocity, m2.velocity
            m1.velocity = (m1.mass - m2.mass) / (m1.mass + m2.mass) * prevVelocityBigSquare + (2 * m2.mass) / (
                    m1.mass + m2.mass) * m2.velocity
            m2.velocity = (2 * m1.mass) / (m1.mass + m2.mass) * prevVelocityBigSquare + (m2.mass - m1.mass) / (
                    m1.mass + m2.mass) * prevVelocityLittleSquare

        elif m2.pos <= 40 and m2.velocity < 0:
            m2.velocity *= -1
            collisionCounter += 1

    pygame.Surface.fill(screen, (20, 20, 20))

    # Floor + Wall
    pygame.draw.line(screen, (150, 150, 150), (40, 450), (40, 0), 5)
    pygame.draw.line(screen, (150, 150, 150), (800, 452), (38, 452), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(m1.surface, (m1.pos, 300))
    screen.blit(m2.surface, (m2.pos, 390))
    textTBD = textfont.render("Collision counter: " + str(collisionCounter), True, (255, 255, 255))
    screen.blit(textTBD, (50, 500))
    pygame.display.flip()
