import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_question_and_answer():
    number = random.randint(MIN_NUM, MAX_NUM)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
