import random

RULE = 'What number is missing in the progression?'
LENGTH_MIN = 5
START_STEP_MIN = 1
LENGTH_START_STEP_MAX = 10


def generate_question_and_answer():
    length = random.randint(LENGTH_MIN, LENGTH_START_STEP_MAX)
    start = random.randint(START_STEP_MIN, LENGTH_START_STEP_MAX)
    step = random.randint(START_STEP_MIN, LENGTH_START_STEP_MAX)
    progression = [start + step * i for i in range(length)]
    missing_index = random.randint(0, length - 1)
    correct_answer = str(progression[missing_index])
    progression[missing_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
