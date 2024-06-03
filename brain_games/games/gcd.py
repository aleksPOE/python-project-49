import random
import math

RULE = 'Find the greatest common divisor of given numbers.'
COUNT_FROM = 1
COUNT_BEFORE = 100

def generate_question_and_answer():
    number_1 = random.randint(COUNT_FROM, COUNT_BEFORE)
    number_2 = random.randint(COUNT_FROM, COUNT_BEFORE)
    question = f"{number_1} {number_2}"
    answer = str(math.gcd(number_1, number_2))
    return question, answer
