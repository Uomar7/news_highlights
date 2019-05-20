import unittest
from models import sources

Source = sources.Source


class SourcesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the source class 
    '''

    def setUp(self):
        '''
        set up method that will run before every test.
        '''

        self.new_source = Source('BBC', 'stanley', 'A great big world',
                                 'It has always been of difference with everybody estimating the universe size', '2019-05-18T13:05:00Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

    def test_init(self):
        '''
        test method to check each item is instanciated properly
        '''

        self.assertEqual(self.new_source.name, 'BBC')
        self.assertEqual(self.new_source.author, 'stanley')
        self.assertEqual(self.new_source.title, 'A great big world')
        self.assertEqual(self.new_source.description,
                         'It has always been of difference with everybody estimating the universe size')
        self.assertEqual(self.new_source.publishedAt, '2019-05-18T13:05:00Z')


if __name__ == "__main__":
    unittest.main()
