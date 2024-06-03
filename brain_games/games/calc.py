import random
import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

RULE = 'What is the result of the expression?'
COUNT_FROM = 1
COUNT_BEFORE = 100
    

def generate_question_and_answer():
    num1 = random.randint(COUNT_FROM, COUNT_BEFORE)
    num2 = random.randint(COUNT_FROM, COUNT_BEFORE)
    operation = random.choice(list(OPERATIONS.keys()))

    question = f"{num1} {operation} {num2}"
    answer = str(OPERATIONS[operation](num1, num2))

    return question, answer
