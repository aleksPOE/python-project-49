import random
import math

RULE = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f"{number_1} {number_2}"
    answer = str(math.gcd(number_1, number_2))
    return question, answer