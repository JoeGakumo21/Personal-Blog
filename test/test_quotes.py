import unittest
from app.models import Pitch

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch('Python Must Be Crazy','A thrilling new Python Series')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))