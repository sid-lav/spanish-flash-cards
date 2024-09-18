import tkinter as tk
from tkinter import messagebox

def ask_question(question, answer):
    difficulty_result = [None]  # Using a list to store the result

    def show_answer():
        answer_label.config(text=f"Answer: {answer}")
        rate_frame.pack()

    def rate_difficulty(score):
        difficulty_result[0] = score - 1  # Store 0, 1, or 2
        difficulty_names = ["Easy", "Medium", "Hard"]
        messagebox.showinfo("Difficulty Rated", f"You rated this question as {difficulty_names[score - 1]}")
        root.quit()

    root = tk.Tk()
    root.title("Question Asker")
    root.geometry("400x300")

    question_label = tk.Label(root, text=question, wraplength=380, pady=10)
    question_label.pack()

    show_answer_button = tk.Button(root, text="Show Answer", command=show_answer)
    show_answer_button.pack(pady=10)

    answer_label = tk.Label(root, text="", wraplength=380)
    answer_label.pack()

    rate_frame = tk.Frame(root)
    rate_label = tk.Label(rate_frame, text="Rate the difficulty:")
    rate_label.pack()

    for i, difficulty in enumerate(["Easy", "Medium", "Hard"], 1):
        btn = tk.Button(rate_frame, text=difficulty, command=lambda score=i: rate_difficulty(score))
        btn.pack(side=tk.LEFT, padx=5)

    root.mainloop()

    return difficulty_result[0]  # Return the numeric difficulty (0, 1, or 2)

# Example usage
"""
question = "What is the capital of France?"
answer = "Paris"
difficulty = ask_question(question, answer)
print(f"The question was rated as: {difficulty}")
"""

