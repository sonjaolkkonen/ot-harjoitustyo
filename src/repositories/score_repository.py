
import bisect
import os

dirname = os.path.dirname(__file__)
scores_file = os.path.join(dirname, "../", "score.txt")

class ScoreRepository:
    """Pisteisiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, score):
        """Luokan konstruktori.
        Args:
            score: Pelaajan saamat pisteet.
        """

        self.score = score


    def all_scores(self):
        """lukee tiedoston score.txt sisällön
        Returns:
            str: kaikki pisteet
        """
        with open(scores_file, "r") as scores:
            content = scores.read().splitlines()
            if content == []:
                pass
            else:
                content = [int (i) for i in content]
        return content

    def add_new_score(self, score):
        """kirjoittaa tiedostoon score.txt uuden pistetuloksen
        oikeaan järjestykseen
        Returns: 
            str: top five -pisteet.
        """
        self.score= score
        all_scores = ScoreRepository.all_scores(self)
        bisect.insort(all_scores, self.score)
        
        with open(scores_file, "w") as scores:
            for score in all_scores:
                scores.write("%s\n" %score)

        
        top_five = [str(i) for i in all_scores]
        if len(top_five) >= 5:
            top_five = top_five[0:5]
        else:
            top_five = top_five[0:len(top_five)]
        
        return top_five

    def delete_all(self):
        with open(scores_file, "r") as scores:
            scores.truncate()


