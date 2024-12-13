import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os
def play_text():
    text = text_entry.get()
    if text.strip():
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        os.system("start output.mp3" if os.name == "nt" else "afplay output.mp3")
    else:
        messagebox.showwarning()
def reset_text():
    text_entry.delete(0, tk.END)
def exit_program():
    root.destroy()
    
root = tk.Tk()
root.title("Text to Speech")
root.geometry("600x400")
root.configure(bg="#101010")  
 
header = tk.Label(
    root, 
    text="Text to Speech", 
    font=("Helvetica", 28, "bold"), 
    bg="#101010", 
    fg="#FFD700"  
)
header.pack(pady=10)

sub_header = tk.Label(
    root, 
    text="Enter your text below:", 
    font=("Helvetica", 14), 
    bg="#101010", 
    fg="#AAAAAA"   
)
sub_header.pack(pady=5)

text_entry = tk.Entry(
    root, 
    width=40, 
    font=("Helvetica", 14), 
    bg="#1A1A1A",  
    fg="#00FF7F",  
    insertbackground="#FFD700",  
    bd=2,
    relief="flat"
)
text_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#101010")
button_frame.pack(pady=20)

play_button = tk.Button(
    button_frame, 
    text="Play", 
    font=("Helvetica", 12, "bold"), 
    bg="#00509E",  
    fg="#FFFFFF", 
    activebackground="#0066CC", 
    activeforeground="#FFD700", 
    width=12,
    height=1,
    bd=0,
    command=play_text
)
play_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(
    button_frame, 
    text="Reset", 
    font=("Helvetica", 12, "bold"), 
    bg="#008450",  
    fg="#FFFFFF", 
    activebackground="#00A65E", 
    activeforeground="#FFD700", 
    width=12,
    height=1,
    bd=0,
    command=reset_text
)
reset_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(
    button_frame, 
    text="Exit", 
    font=("Helvetica", 12, "bold"), 
    bg="#8B0000",   
    fg="#FFFFFF", 
    activebackground="#B22222", 
    activeforeground="#FFD700", 
    width=12,
    height=1,
    bd=0,
    command=exit_program
)
exit_button.grid(row=0, column=2, padx=10)

footer = tk.Label(
    root, 
    text="Developed by: Mohamed Elsayed Eleshmawi", 
    font=("Helvetica", 10, "italic"), 
    bg="#101010", 
    fg="#F5F5F5"  # لون النص أوف وايت (off-white)
)
footer.pack(side="bottom", pady=10)
root.mainloop()