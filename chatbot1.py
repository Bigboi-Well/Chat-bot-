import json
from difflib import get_close_matches
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

def chat_bot():
    knowledge_base = load_knowledge_base('knowledge_base.json')
    root = tk.Tk()
    root.title('Chatbot')
    root.geometry('400x500')

    def send_message():
        user_input = entry.get()
        entry.delete(0, 'end')

        if user_input.lower() == 'quit':
            root.quit()
            return

        best_match = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            messagebox.showinfo('Bot', answer)
        else:
            messagebox.showinfo('Bot', 'I don\'t know the answer. Can you teach me?')
            new_answer = messagebox.askokcancel('New Information', f'Type the answer or skip: {user_input}')

            if new_answer:
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                messagebox.showinfo('Bot', 'Thank you! I learned a new information!')

    frame = ttk.Frame(root)
    frame.pack(pady=10)

    entry = ttk.Entry(frame, width=50)
    entry.pack(pady=10)

    send_button = ttk.Button(frame, text='Send', command=send_message)
    send_button.pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    chat_bot()