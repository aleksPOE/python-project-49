import random
import math

RULE = 'Find the greatest common divisor of given numbers.'
MIN_NUM = 1
MAX_NUM = 100


def generate_question_and_answer():
    number_1 = random.randint(MIN_NUM, MAX_NUM)
    number_2 = random.randint(MIN_NUM, MAX_NUM)
    question = f'{number_1} {number_2}'
    answer = str(math.gcd(number_1, number_2))
    return question, answer
