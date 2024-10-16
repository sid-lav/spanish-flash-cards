from modules.api_config import claude_query
from modules.gui import tkinter
from modules.data import adjectives, verbs, adverbs, nouns
import ast
import json

for i in range(3):
    result = claude_query(verbs[i])
    result = ast.literal_eval(result)
    question, answer, tense, person = result[0], result[1], result[2], result[3]
    result = tkinter(question, answer, tense, person)
    

"NA MAIKA TI PUTKATATAAAAAAAAAAAAAA"


"""
# sample question
question = "What is the capital of France?"
answer = "Paris"
difficulty = tkinter(question, answer)
print(f"The question was rated as: {difficulty}")
"""
