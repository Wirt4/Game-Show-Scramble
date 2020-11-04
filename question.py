class Question:
    score = -1

    def __init__(self, c, q, a):
        self.category = c
        self.question = q
        self.answer = a

    def set_score(self, n, is_double_score):
        multiplier = 200
        if is_double_score:
            multiplier *= 2
        self.score = multiplier * n