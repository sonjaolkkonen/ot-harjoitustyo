import unittest
import os
from repositories.score_repository import ScoreRepository

dirname = os.path.dirname(__file__)
scores_file = os.path.join(dirname, "../..", "score.txt")

class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        self.score = 10

    def test_all_scores(self):

        with open(scores_file, "r") as scores:
            scores.truncate()

        ScoreRepository.add_new_score(self, self.score)
        scores = ScoreRepository.all_scores(self)

        self.assertEqual(len(scores), 1)
        self.assertEqual(scores[0], 10)

