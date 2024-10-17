from modules.api_config import claude_query
from modules.gui import tkinter
from modules.data import *
import ast
import json

print(type(verbs))

for i in range(3):
    result = claude_query(verbs_keylist[i])
    result = ast.literal_eval(result)
    question, answer, tense, person = result[0], result[1], result[2], result[3]
    result = tkinter(question, answer, tense, person)
    

"""
# sample question
question = "What is the capital of France?"
answer = "Paris"
difficulty = tkinter(question, answer)
print(f"The question was rated as: {difficulty}")
"""
