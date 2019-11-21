import unittest
from box import make_boxplot
import numpy as np
import os


class TestCounts(unittest.TestCase):
    # Test to see if file exists after boxplot is created
    def test_boxplot_exist(self):
        self.tissues = ["Tissue " + chr(i) for i in range(100, 105)]
        self.genes = ["Gene " + chr(i) for i in range(110, 115)]
        self.counts = {}
        for i in range(100, 105):
            self.counts.update({"Tissue " + chr(i):
                                np.random.randint(0, 100, size=100)})

        self.output_file = "test_exist.png"
        make_boxplot(self.tissues, self.genes, self.counts,
                     self.output_file)
        self.assertEqual(True, os.path.exists(self.output_file))


if __name__ == '__main__':
    unittest.main()
