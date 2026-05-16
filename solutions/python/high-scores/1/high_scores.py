class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        largest_scores = sorted(self.scores, reverse=True)[:3]
        return largest_scores

        # I only later realised that sorted() is a thing, so before I did this:
        """
        def personal_top_three(scores):
    largest = max(scores)
    largest_index = scores.index(largest)
    highest_scores = [largest]
    new_scores = []

    for i in range(len(scores)):
        new_scores.append(scores[i])

    while len(highest_scores) < 3:
        new_scores.pop(largest_index)
        largest = max(new_scores)
        largest_index = scores.index(largest)
        highest_scores.append(largest)

    return highest_scores 
"""

    def latest(self):
        return self.scores[-1]
