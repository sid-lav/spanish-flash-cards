from api_config import claude_query
from funcs import ask_question


# sample question
question = "What is the capital of France?"
answer = "Paris"
difficulty = ask_question(question, answer)
print(f"The question was rated as: {difficulty}")
