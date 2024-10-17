# api_config.py
# contains config and queying function for each API
# sid@lapentop .../[12.04]-thesis

import anthropic
import os
import time
from __pycache__.api import claude_key

##########################################################################################################################################################################################
# 1. globals
##########################################################################################################################################################################################

def message(word, prompt_format):
    prompt = prompt_format.format(non_word = word)
    return prompt

##########################################################################################################################################################################################
#### QUERY FUNC
##########################################################################################################################################################################################

def claude_query(anki_word):
    client = anthropic.Anthropic(api_key=claude_key)

    # system message
    sysmsg = """
You are a tool for language learning, you will be given a Spanish verb, your job is to conjugate the verb randomly in European/Castillian Spanish.
Output in a python list format like this [conjugated verb, english translation, tense, person)]
Do not include any other text in your output than the given list
"""

    # sysmsg = "Use the word in the prompt in " 
    # prompt_format = """<nonword>{query_word}</nonword>?"""
    
    query = "The word is <word>{word}</word>".format(word = anki_word) 
    message = [
        {
            "role": "user",
            "content": query,
        },
    ]

    response = client.messages.create(
        model = "claude-3-5-sonnet-20240620",
        max_tokens = 40,
        messages = message,
        system = sysmsg
    )
    print(response.content[0].text.lower())
    
    return response.content[0].text.lower()

