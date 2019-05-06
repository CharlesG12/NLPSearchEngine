
class AnswerMachine:
    question = ""

    def __init__(self, _question):
        self.question = _question
        print(self.question)


if __name__ == "__main__":
    question = "Who supported Apple in creating a new computing platform?"
    QAMachine = AnswerMachine(question)
    print()


