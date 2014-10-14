import pygrid, pygame
from BacterialColonyProblem import *

def initPygame(size):
    pygame.init()
    grid = pygrid.Grid([size, size], [15, 15])
    screen = pygame.display.set_mode((grid.gridWidthInPixels, grid.gridHeightInPixels))

    return {'grid': grid, 'screen': screen}

def update(grid, screen, loop, ecosystem):
    array = pygrid.GrectArray(grid, False)
    new_positions = [(i, j) for i, row in enumerate(ecosystem) for j, item in enumerate(row) if True in row and item]
    for i, j in new_positions:
        array.add(pygrid.Grect(grid, j, i, grid.colors['GREEN'], False))

    # Draw your grects here.
    bg.draw(screen)
    array.draw(screen)
    pygame.display.set_caption("Colony: #%d loop" % loop)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(speed)


if __name__ == '__main__':
    size = 30
    colony = BacterialColonyProblem(size, [(0,1), (0,2), (1,1), (1,2), (2,2), (3,0), (3,2), (0+5,1+1), (0+5,2+1), (1+5,1+1), (1+5,2+1), (2+5,2+1), (3+5,0+1), (3+5,2+2), (0+10,1-1), (0+10,2-1), (1+10,1-1), (1+10,2-1), (2+10,2-1), (3+10,0-1), (3+10,2-1)])

    pygameObject = initPygame(size)
    bg = pygrid.Grect(pygameObject['grid'], 0, 0, (75,75,75), True)
    array = pygrid.GrectArray(pygameObject['grid'], False)
    clock = pygame.time.Clock()
    speed = 15


    generator = enumerate(colony.run())
    while True:
        keys = pygame.key.get_pressed()
        for e in pygame.event.get():
            if e.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                quit()

        try:
            i, colony = generator.next()
        except:
            continue

        update(pygameObject['grid'], pygameObject['screen'], i, colony)
