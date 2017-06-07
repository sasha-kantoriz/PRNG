#!usr/bin/python
import os
import unittest
from alfg import (
    fish, fish_to_file,
    mush, mush_to_file
)


class BaseGeneratorTest(unittest.TestCase):
    test_output = 'test'
    size = 256

    @classmethod
    def tearDownClass(self):
        super(BaseGeneratorTest, self).tearDownClass()
        if os.path.exists(self.test_output):
            os.remove(self.test_output)


class TestFishGenerator(BaseGeneratorTest):
    def test_get_sequence(self):
        result = fish(self.size)
        self.assertEqual(len(result), self.size)
        self.assertEqual(result, filter(lambda i: i in ['0', '1'], result))

    def test_output_to_file(self):
        fish_to_file(self.test_output, self.size)
        self.assertTrue(os.path.exists(self.test_output))
        self.assertEqual(os.stat(self.test_output).st_size, self.size)


class TestMushGenerator(BaseGeneratorTest):
    def test_get_sequence(self):
        result = mush(self.size)
        self.assertEqual(len(result), self.size)
        self.assertEqual(result, filter(lambda i: i in ['0', '1'], result))

    def test_output_to_file(self):
        mush_to_file(self.test_output, self.size)
        self.assertTrue(os.path.exists(self.test_output))
        self.assertEqual(os.stat(self.test_output).st_size, self.size)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFishGenerator))
    suite.addTest(unittest.makeSuite(TestMushGenerator))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
