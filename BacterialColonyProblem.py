import numpy

class BacterialColonyProblem(object):

    def __init__(self, size, bacteriaPosition):
        if not size or size < 1 or type(size) is not int:
            raise ValueError('Incorrect size')

        if not bacteriaPosition or type(bacteriaPosition) is not list:
            raise ValueError('Incorrect positions')
        else:
            for item in bacteriaPosition:
                if type(item) is not tuple:
                    raise ValueError('Incorrect positions')

        self.size = size
        self.ecosystem = numpy.zeros( (size, size), dtype=int)

        for i, j in bacteriaPosition:
            if 0 <= i < size and 0 <= j < size:
                self.ecosystem[i][j] = True

    def run(self):
        ecosystem_copy = self.ecosystem.copy()
        ecosystem_old = []
        changes = numpy.zeros((1,1), dtype=bool)

        yield self.ecosystem
        while True:
            for i, row in enumerate(self.ecosystem):
                for j, bactery in enumerate(row):
                    ecosystem_copy[i][j] = self.__process(i, j, bactery)
            ecosystem_old = self.ecosystem.copy()
            changes = ecosystem_old == ecosystem_copy
            self.ecosystem = ecosystem_copy.copy()
            if changes.all():
                break
            yield ecosystem_copy

    def __process(self, i, j, bactery):
        if not bactery and self.__getNeighbors(i, j) == 3: # Born
            return True
        if bactery:
            if self.__getNeighbors(i, j) < 2: # Isolation
                return False
            if self.__getNeighbors(i, j) > 3: # Suffocation
                return False
            if self.__getNeighbors(i, j) in (2, 3): # Survival
                return True
        return bactery

    def __getNeighbors(self, i, j):
        n_i, n_j = i-1, j-1
        result = 0
        for row in range(3):
            for column in range(3):
                if (n_i, n_j) != (i, j) and 0 <= n_i < self.size and 0 <= n_j < self.size:
                    result += self.ecosystem[n_i][n_j]
                n_j += 1
            n_i += 1
            n_j = j-1
        return result
