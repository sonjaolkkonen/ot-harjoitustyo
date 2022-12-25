import unittest
from repositories.score_repository import ScoreRepository

class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        self.score = 10

    def test_all_scores(self):
        ScoreRepository.add_new_score(self, self.score)
        scores = ScoreRepository.all_scores(self)

        self.assertEqual(len(scores), 1)
        self.assertEqual(scores[0], 10)

