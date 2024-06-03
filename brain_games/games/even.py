import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
COUNT_FROM = 1
COUNT_BEFORE = 100


def is_even(num):
    return num % 2 == 0


def generate_question_and_answer():
    number = random.randint(COUNT_FROM, COUNT_BEFORE)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
