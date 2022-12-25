import unittest
import os
from repositories.score_repository import ScoreRepository

class TestScoreRepository(unittest.TestCase):
    def setUp(self):
        self.score = 10
        dirname = os.path.dirname(__file__)
        self.scores_file = os.path.join(dirname, "../..", "score.txt")

    def test_all_scores(self):

        with open(self.scores_file, "r") as scores:
            content = scores.read().splitlines()
            if content == []:
                content == []
            else:
                content == []

        ScoreRepository.add_new_score(self, self.score)
        scores = ScoreRepository.all_scores(self)

        self.assertEqual(len(scores), 1)
        self.assertEqual(scores[0], 10)

