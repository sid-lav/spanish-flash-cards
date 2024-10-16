import tkinter as tk

def tkinter(question, answer, tense, person):
    difficulty_result = [None]  # Using a list to store the result

    def show_answer():
        # Clear the Text widget
        answer_text.delete(1.0, tk.END)
        
        # Insert the labels in bold and variables in regular style
        answer_text.insert(tk.END, "Answer: ", "bold")
        answer_text.insert(tk.END, f"{answer}\n", "center")

        answer_text.insert(tk.END, "Tense: ", "bold")
        answer_text.insert(tk.END, f"{tense}\n", "center")

        answer_text.insert(tk.END, "Person: ", "bold")
        answer_text.insert(tk.END, f"{person}\n", "center")

        # Pack the rate frame after displaying the answer
        rate_frame.pack(pady=20)  # Add padding to move it further down

        # Hide the "Show Answer" button after it's clicked
        show_answer_button.pack_forget()

    def rate_difficulty(score):
        difficulty_result[0] = score - 1  # Store 0, 1, or 2
        difficulty_names = ["Easy", "Medium", "Hard"]

        # Update the label to show what the user rated without opening a new window
        rate_label.config(text=f"You rated this question as {difficulty_names[score - 1]}")
        
        # Hide the difficulty buttons after rating
        for widget in rate_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.pack_forget()

    root = tk.Tk()
    root.title("Question Asker")
    root.geometry("400x300")

    # Retrieve system default background color
    default_bg = root.cget("bg")

    question_label = tk.Label(root, text=question, wraplength=380, pady=10)
    question_label.pack()

    show_answer_button = tk.Button(root, text="Show Answer", command=show_answer)
    show_answer_button.pack(pady=10)

    # Change from Label to Text widget (no wraplength, use width instead) with background set to system default
    global answer_text  # Ensure it's accessible in show_answer
    answer_text = tk.Text(root, width=50, height=5, bg=default_bg, relief="flat", borderwidth=0)
    answer_text.pack(pady=20)  # Add padding to move it further down from the answer button

    # Create bold tag for the Text widget
    answer_text.tag_configure("bold", font=("Helvetica", 12, "bold"))

    # Create center-aligned tag for the variables
    answer_text.tag_configure("center", justify="center")

    rate_frame = tk.Frame(root, bg=default_bg)
    rate_label = tk.Label(rate_frame, text="Rate the difficulty:")
    rate_label.pack()

    for i, difficulty in enumerate(["Easy", "Medium", "Hard"], 1):
        btn = tk.Button(rate_frame, text=difficulty, command=lambda score=i: rate_difficulty(score))
        btn.pack(side=tk.LEFT, padx=5)

    root.mainloop()

    return difficulty_result[0]  # Return the numeric difficulty (0, 1, or 2)
