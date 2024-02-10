import tkinter as tk
from tkinter import PhotoImage
import os
from itertools import cycle

prompts = ["Are you sure?", "Really really sure?", "100%?", "Positive?", "Alisaa Cmon!", "Babe Fr???"]
current_prompt_index = 0
# Function to update the displayed frame of the gif
def update_gif_frame():
    frame = next(gif_frames)
    gif_label.configure(image=frame)
    frame1 = next(gif_frames2)
    gif_label2.configure(image=frame1)
    window.after(150, update_gif_frame)  # No argument is passed here


def increase_yes_button_size():
    global current_prompt_index
    current_font = yes_button.cget("font")
    font_parts = current_font.split(' ')

    # Find the numeric part of the font specification (size) and increase it
    for i, part in enumerate(font_parts):
        if part.isdigit():  # Check if the part is a digit (font size)
            size = int(part)
            new_size = size + 15  # Increase the font size
            font_parts[i] = str(new_size)  # Update the font size in the font specification
            break

    # Apply the updated font specification
    yes_button.config(font=" ".join(font_parts))

    # Update the prompt text and cycle through prompts
    prompt_label.config(text=prompts[current_prompt_index])
    current_prompt_index = (current_prompt_index + 1) % len(prompts)


def show_second_screen():
    yes_button.pack_forget()
    no_button.pack_forget()
    prompt_label.place_forget()
    gif_label.place_forget()  # Hide the gif
    gif_label2.place_forget()
    second_screen_label = tk.Label(window, text="YIPEE!",font=("SignPainter", 150), bg="#FFAEB9")
    second_screen_label2 = tk.Label(window, text="see you on the 14th babe <3!",font=("SignPainter", 50), bg="#FFAEB9")
    second_screen_label.place(relx=0.5, rely=0.45, anchor='center')
    second_screen_label2.place(relx=0.5, rely=0.55, anchor='center')


# Initialize the main window
window = tk.Tk()
window.title("Valentine's Game")
window.state('zoomed')
window.configure(bg="#FFAEB9")

gif_file_path = '../valentines/image1.gif'
gif_file_path2 = '../valentines/uwu.gif'

if not os.path.exists(gif_file_path2):
    print(f"Current working directory: {os.getcwd()}")
    raise FileNotFoundError(f"The file {gif_file_path2} does not exist.")
if not os.path.exists(gif_file_path2):
    raise FileNotFoundError(f"The file {gif_file_path2} does not exist.")

gif_frames = cycle((tk.PhotoImage(file='../valentines/image1.gif', format=f'gif -index {i}') for i in range(8)))
gif_frames2 = cycle((tk.PhotoImage(file='../valentines/uwu.gif', format=f'gif -index {i}') for i in range(20)))

gif_label = tk.Label(window, image=next(gif_frames), bg="#FFAEB9")
gif_label2 = tk.Label(window, image=next(gif_frames2), bg="#FFAEB9")

gif_label.pack(side=tk.LEFT)
gif_label.pack()
gif_label2.pack(side=tk.RIGHT)
gif_label2.pack()

window.after(0, update_gif_frame, 0)
update_gif_frame()
# Create the frame that will contain the Yes/No buttons
button_frame = tk.Frame(window, bg="#FFAEB9")
button_frame.pack(expand=True)

# Updated part for nicer-looking buttons
yes_button = tk.Button(button_frame, text="Yes", font=("SignPainter", 25),
                       command=show_second_screen, bg="#FF69B4", fg="black",
                       highlightbackground="#FF69B4", highlightthickness=0, bd=0,
                       padx=20, pady=10, relief="ridge")
no_button = tk.Button(button_frame, text="No", font=("SignPainter", 25),
                      command=increase_yes_button_size, bg="#FF69B4", fg="black",
                      highlightbackground="#FF69B4", highlightthickness=0, bd=0,
                      padx=20, pady=10, relief="ridge")


prompt_label = tk.Label(window, text="Will you be my Valentine?", font=("SignPainter", 90), bg="#FFAEB9")
prompt_label.place(relx=0.5, rely=0.2, anchor="center")

yes_button.pack(pady=10)
no_button.pack(pady=10)
button_frame.place(relx=0.5, rely=0.5, anchor='center')
window.mainloop()
