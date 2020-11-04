from question import Question
import csv
import random
class Game:
    def __init__(self, filepath, is_double_score):
        self.questions = self._read_questions(filepath, is_double_score)
    categories = dict()

    def _read_questions(self, filepath, is_double_jepoardy):
        with open(filepath) as f:
            reader = csv.reader(f)
            questions =[]
            for row in reader:
                #design a constructor that takes category, question, answer
                q = Question(row[0].upper(), row[1], row[2])
                if q.category in self.categories.keys():
                    self.categories[q.category] += 1
                else:
                    self.categories[q.category] = 1
                q.set_score(self.categories[q.category], is_double_jepoardy)
                questions.append(q)
            return questions

    def make_file(self, filename):
        if not filename.endswith(".txt"):
            filename += ".txt"
        random.shuffle(self.questions)
        divider = "=================================\n"
        d_space = "\n\n"
        with open(filename, 'w') as out_file:
            out_file.write(divider)
            for q in self.questions:
                out_file.write(q.category + " : $" +str(q.score) + d_space)
                out_file.write(q.question + d_space)
                out_file.write(q.answer + "\n")
                out_file.write(divider)
