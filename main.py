import passalgs


import tkinter as tk
from tkinter import ttk



options = ["Passgen v1 by SpoonStory", "Passgen v2.1 by SpoonStory"]

pass_alg = options[0]




def update_text():
    if pass_alg == options[0]:
        new_text = passalgs.gen_pass_w2n3s1v1()
    elif pass_alg == options[1]:
        new_text = passalgs.gen_pass_simple_w2n3s1v2()
    else:
        new_text = 'Error. Unsupported algorythm or just my creator being dumb.'
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, new_text)

def copy_text():
    text_to_copy = text_widget.get(1.0, tk.END).strip()  
    root.clipboard_clear()
    root.clipboard_append(text_to_copy)
    # print(text_to_copy, PASS_ALG)
    root.update()
    
def on_combobox_select(event):
    global pass_alg
    # global options
    pass_alg = combo.get()
    
    
root = tk.Tk()
root.title('PassGen by SpoonStory v0.0.3')

# Combobox



combo = ttk.Combobox(root, values=options, state="readonly")
combo.set(options[0])  # Значение по умолчанию
combo.pack(pady=10, fill=tk.X)
combo.bind("<<ComboboxSelected>>", on_combobox_select)

text_widget = tk.Text(root, wrap=tk.WORD, width=40, height=10, font=("Arial", 14))
text_widget.pack(pady=20)


button = tk.Button(root, text='Генерировать', command=update_text)
button.pack(pady=10, padx=10)

button2 = tk.Button(root, text='Копировать', command=copy_text)
button2.pack(pady=10, padx=10)



root.mainloop()
