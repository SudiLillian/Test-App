class Question(object):
    """This class models question objects."""

    def __init__(self, question_text, answer, choices):
        """
        Create a new Question object.
        The method accepts:
            question_text: The question itself
            answer: The answer to the question
            choices: A list containing the various choices
        """
        self.question_text = question_text
        self.answer = answer
        self.choices = choices

    def grade(self, user_answer):
        """Check whether answer provided is correct."""
        if self.answer.lower() == user_answer.lower():
            return True
        return False

    def to_string(self):
        """Return a string containing the question and its choices."""
        final_string = self.question_text + "\n"
        for key in sorted(self.choices.keys()):
            final_string += key + ". " + self.choices[key] + "\n"
        return final_string