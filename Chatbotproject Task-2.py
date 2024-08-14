import tkinter as tk
from tkinter import scrolledtext

def send_message():
    user_input = entry_box.get("1.0", "end-1c").strip()
    entry_box.delete("1.0", "end")

    if user_input.lower() == "quit":
        display_text.insert(tk.END, "You: " + user_input + '\n')
        display_text.insert(tk.END, "Chatbot: Bye! Take care.\n")
        root.quit()
    else:
        display_text.insert(tk.END, "You: " + user_input + '\n')
        response = chatbot_response(user_input)
        display_text.insert(tk.END, "Chatbot: " + response + '\n')

# Create the main window
root = tk.Tk()
root.title("Simple Chatbot")

# Create a text widget to display the conversation
display_text = scrolledtext.ScrolledText(root, wrap=tk.WORD)
display_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create an entry box for user input
entry_box = tk.Text(root, height=3, wrap=tk.WORD)
entry_box.grid(row=1, column=0, padx=10, pady=10)

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
