import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def is_even(num):
    return num % 2 == 0


def generate_question_and_answer():
    number = random.randint(MIN_NUM, MAX_NUM)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
