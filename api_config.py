# api_config.py
# contains config and queying function for each API
# sid@lapentop .../[12.04]-thesis

import anthropic
import os
import time
from api import claude_key

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
You are a tool for language learning, your job is to make an A2 level Spanish sentence including the given word in the prompt.
Only provide the Spanish sentence! Do not write anything else in the prompt!
"""

    # sysmsg = "Use the word in the prompt in " 
    # prompt_format = """<nonword>{query_word}</nonword>?"""
    
    query = "The word is <word>{word}</word>".format(word = anki_word) 
    print(query)
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
    
    return response, response.content[0].text.lower()

claude_query("playa")
