import tkinter as tk
from tkinter import font

def on_font_select(event):
    selected_font = font_listbox.get(font_listbox.curselection())
    label.config(font=(selected_font, 12))

root = tk.Tk()
root.title("Font List with Scrollbar")

# Create a Listbox to display fonts
font_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
font_listbox.pack(side=tk.LEFT, fill=tk.Y)

# Create a Scrollbar and associate it with the Listbox
scrollbar = tk.Scrollbar(root, command=font_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
font_listbox.config(yscrollcommand=scrollbar.set)

# Populate the Listbox with font names
available_fonts = sorted(font.families())
for font_name in available_fonts:
    font_listbox.insert(tk.END, font_name)

# Bind the font selection event
font_listbox.bind('<<ListboxSelect>>', on_font_select)

# Create a Label to display selected font
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 12))
label.pack(pady=10)

root.geometry("1080x540")




root.mainloop()
