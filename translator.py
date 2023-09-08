import tkinter as tk
from tkinter import *
from google.cloud import translate_v2 as translate

# Initialize the Google Cloud Translation client
client = translate.Client.from_service_account_json('json file Path')

# Function to perform translation
def translate_text():
    text_to_translate = entry_text.get("1.0", END)
    selected_language = target_language_var.get()

    # Translate the text
    result = client.translate(text_to_translate, target_language = selected_language)

    # Display the translated text
    entry_translation.delete("1.0", END)
    entry_translation.insert("1.0", result['translatedText'])

# Create the main application window
window = Tk()

# Create a title
window.title("Translator")

## Create and configure GUI elements
# Center 
app_width = 850
app_height = 300

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

# Left: "Type in English" Label and Text Entry
lbl1 = Label(window, text='Type in English:', font='Helvetica 16 bold')
lbl1.place(x=50, y=50)
entry_text = Text(window, width=30, height=5)  # Adjust height as needed
entry_text.place(x=50, y=80)


# Middle: Language Selection and Translate Button
lbl2 = Label(window, text='Select Target Language:', font='Helvetica 12 bold')
lbl2.place(x=325, y=50)

target_language_var = StringVar(window) # helps to store target language
target_language_listbox = OptionMenu(window, target_language_var, 'zh-HK', 'fr', 'es', 'de', 'it', 'ko', 'pt')
target_language_listbox.place(x=395, y=80)

btn = Button(window, text='Translate', command = translate_text, font='Helvetica 10 bold')
btn.place(x=382, y=120)

# Right: "Translation" Label and Text Entry
lbl3 = Label(window, text='Translation:', font='Helvetica 16 bold')
lbl3.place(x=550, y=50)
entry_translation = Text(window, width=30, height=5)  
entry_translation.place(x=550, y=80)

# Start the Tkinter main loop
window.mainloop()
