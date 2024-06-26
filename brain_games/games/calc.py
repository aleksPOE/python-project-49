import random
import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

RULE = 'What is the result of the expression?'
MIN_NUM = 1
MAX_NUM = 100


def generate_question_and_answer():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    operation = random.choice(list(OPERATIONS.keys()))

    question = f'{num1} {operation} {num2}'
    answer = str(OPERATIONS[operation](num1, num2))

    return question, answer
