from BacterialColonyProblem import BacterialColonyProblem
import unittest

class TestBacterialcolonyProblem(unittest.TestCase):
    """docstring for TestBacterialcolonyProblem"""

    def setup(self):
        # colony = BacterialColonyProblem()
        pass

    def test_iter1_problem1(self):
        bacteria = [(0,2), (1,1), (1,2), (2,2), (3,2)]
        expected = [[0,1,1,0], [0,1,1,1], [0,0,1,1], [0,0,0,0]]
        colony = BacterialColonyProblem(4, bacteria)
        result = self.getIter(1, colony)
        self.assertListEqual(expected, result)

    def test_iter2_problem1(self):
        bacteria = [(0,2), (1,1), (1,2), (2,2), (3,2)]
        expected = [[0,1,0,1], [0,0,0,0], [0,1,0,1], [0,0,0,0]]
        colony = BacterialColonyProblem(4, bacteria)
        result = self.getIter(2, colony)
        self.assertListEqual(expected, result)

    def test_iter1_problem2(self):
        bacteria = [(1,1)]
        expected = [[0,0,0], [0,0,0], [0,0,0]]
        colony = BacterialColonyProblem(3, bacteria)
        result = self.getIter(1, colony)
        self.assertListEqual(expected, result)

    def test_iter1_problem3(self):
        bacteria = [(1,1), (2,1), (2,2)]
        expected = [[0,0,0], [0,1,1], [0,1,1]]
        colony = BacterialColonyProblem(3, bacteria)
        result = self.getIter(1, colony)
        self.assertListEqual(expected, result)

    def test_iter16_problem3(self):
        bacteria = [(1,1), (2,1), (2,2)]
        expected = [[0,0,0], [0,1,1], [0,1,1]]
        colony = BacterialColonyProblem(3, bacteria)
        result = self.getIter(16, colony)
        self.assertListEqual(expected, result)

    def test_iter15_problem4(self):
        bacteria = [(1,1), (2,1), (2,2)]
        expected = [[0,0,0,0,0], [0,1,1,0,0], [0,1,1,0,0], [0,0,0,0,0], [0,0,0,0,0]]
        colony = BacterialColonyProblem(5, bacteria)
        result = self.getIter(15, colony)
        self.assertListEqual(expected, result)

    def testBacteriaIllegalData(self):
        self.assertRaises(ValueError, BacterialColonyProblem, -4, [(0,0)]);
        self.assertRaises(ValueError, BacterialColonyProblem, 0, [(0,0)]);
        self.assertRaises(ValueError, BacterialColonyProblem, 3, None);

    def getIter(self, iteractions, colony):
        loop = []
        for i, loop in enumerate(colony.run()):
            if i == iteractions: return loop.tolist()

        if loop is not []:
            return loop.tolist()
        return loop

if __name__ == '__main__':
    unittest.main()