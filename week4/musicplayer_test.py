import unittest
from Musicplayer.py import Song

class SongTest(unittest.TestCase):

    def setUP(self):
        self.set_song = Song("Gasne plamuk", "Raina", "Gasne plamuk", 4)

    def test_init(self):
        self.assertTrue(isinstance(self.set_song, Song))

    def test_str(self):
        self.assertEqual(str(self.set_song), "Raina - Gasne plamuk from Gasne plamuk - 4")

    def test_eq(self):
        new_song = Song("Gasne plamuk", "Raina", "Gasne plamuk", 4)
        self.assertTrue(new_song == self.set_song)

    def test_hash(self):
        self.assertIsNotNone(hash(self.set_song))
        self.assertTrue = Song(hash(self.set_song) == int(hash(self.set_song)))



