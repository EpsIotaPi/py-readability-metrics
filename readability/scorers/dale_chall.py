from readability.scorers.base_scorer import ReadabilityScorer


class DaleChall(ReadabilityScorer):
    def __init__(self, stats, min_words=100):
        super().__init__(stats, min_words)
        self.scorer_name = "Dale-Chall"

    def _raw_score(self):
        stats = self._stats
        words_per_sent = stats.num_words / stats.num_sentences
        percent_difficult_words = \
            stats.num_dale_chall_complex / stats.num_words * 100
        raw_score = 0.1579 * percent_difficult_words + 0.0496 * words_per_sent
        adjusted_score = raw_score + 3.6365 \
            if percent_difficult_words > 5 \
            else raw_score
        return adjusted_score

    def _grade_level(self):
        score = self._raw_score()
        if score <= 4.9:
            return ['1', '2', '3', '4']
        elif score >= 5 and score < 6:
            return ['5', '6']
        elif score >= 6 and score < 7:
            return ['7', '8']
        elif score >= 7 and score < 8:
            return ['9', '10']
        elif score >= 8 and score < 9:
            return ['11', '12']
        elif score >= 9 and score < 10:
            return ['college']
        else:
            return ['college_graduate']
