import random
import tkinter as tk

answers = [
    'Yes - definitely',
    'It is decidedly so',
    'Without a doubt',
    'Reply hazy, try again',
    'Ask again later',
    'Better not tell you now',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful',
    'It is certain',
    'As I see it, yes',
    'Most likely',
    "Don't count on it",
    "Very doubtful",
    "My reply is no"
    "Cannot predict now",
    
]

def ask_question():
    question = question_entry.get()
    if question.strip() == '':
        answer_label.config(text='Please enter a question!', fg='red')
    else:
        answer = random.choice(answers)
        answer_label.config(text=answer, fg='white')
        question_entry.delete(0, tk.END)

# --- Window Setup ---
window = tk.Tk()
window.title('Magic 8 Ball')
window.geometry('400x300')
window.config(bg='black')

# --- Widgets ---
title_label = tk.Label(window, text='🎱 Magic 8 Ball', font=('Arial', 24, 'bold'), bg='black', fg='white')
title_label.pack(pady=20)

question_entry = tk.Entry(window, font=('Arial', 14), width=30)
question_entry.pack(pady=10)

ask_button = tk.Button(window, text='Ask', font=('Arial', 14), bg='purple', fg='white', command=ask_question)
ask_button.pack(pady=10)

answer_label = tk.Label(window, text='', font=('Arial', 14, 'italic'), bg='black', fg='white', wraplength=350)
answer_label.pack(pady=20)

# Allow pressing Enter to ask
window.bind('<Return>', lambda event: ask_question())

window.mainloop()