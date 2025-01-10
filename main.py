# Project: File Renamer
# Author: Martin Drus
# License: MIT

import os
import tkinter as tk
import magic

selected_directory = None

def rename_files_with_transition(directory):
    mime = magic.Magic(mime=True)
    file_listbox.delete(0, tk.END)  # Leere die Liste

    file_entries = []  # Sammle alle Einträge für die Listbox
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)

        # Ignoriere, wenn es sich um ein Verzeichnis handelt
        if not os.path.isfile(old_path):
            continue

        # Bestimme den MIME-Typ anhand des Datei-Inhalts
        mime_type = mime.from_file(old_path)

        if not mime_type:
            file_entries.append(f"{filename} - Unbekannter Dateityp, übersprungen.")
            continue

        # Umbenennung: Kleinbuchstaben, Umlaute und Leerzeichen ersetzen
        new_filename = (
            filename.lower()
            .replace("ä", "ae")
            .replace("ö", "oe")
            .replace("ü", "ue")
            .replace("ß", "ss")
            .replace(" ", "_")
        )

        # Prüfe die aktuelle Endung und den tatsächlichen Typ
        file_extension = os.path.splitext(new_filename)[1]
        if not file_extension:
            # Dynamische Endung basierend auf MIME-Typ
            mime_parts = mime_type.split("/")
            if len(mime_parts) == 2:
                main_type, sub_type = mime_parts
                # Ausnahme: text/plain -> .txt
                if mime_type == "text/plain":
                    new_filename = os.path.splitext(new_filename)[0] + ".txt"
                else:
                    new_filename = os.path.splitext(new_filename)[0] + f".{sub_type}"
            else:
                file_entries.append(f"{filename} - MIME-Typ nicht erkennbar, übersprungen.")
                continue

        new_path = os.path.join(directory, new_filename)
        if old_path != new_path:
            os.rename(old_path, new_path)
            file_entries.append(f"{filename} -> {new_filename}")
        else:
            file_entries.append(f"{filename} - Keine Änderungen erforderlich")

    # Zeige die Einträge mit Verzögerung an
    def show_entries(index=0):
        if index < len(file_entries):
            file_listbox.insert(tk.END, file_entries[index])
            file_listbox.see(tk.END)  # Scrollt automatisch zum neuesten Eintrag
            app.after(100, show_entries, index + 1)  # Nächster Eintrag nach 200ms

    show_entries()  # Starte den Effekt



def select_directory_with_preview():
    def update_preview(new_dir=None):
        current_dir = new_dir if new_dir else directory_var.get()
        if not os.path.isdir(current_dir):
            return
        directory_var.set(current_dir)
        directory_list.delete(0, tk.END)
        try:
            directory_list.insert(tk.END, ".. (Parent Directory)")
            for item in os.listdir(current_dir):
                directory_list.insert(tk.END, item)
        except PermissionError:
            directory_list.insert(tk.END, "Zugriff verweigert")

    def on_item_double_click(event):
        selection = directory_list.get(directory_list.curselection())
        if selection == ".. (Parent Directory)":
            new_path = os.path.dirname(directory_var.get())
        else:
            new_path = os.path.join(directory_var.get(), selection)

        if os.path.isdir(new_path):
            update_preview(new_path)

    def confirm_selection():
        global selected_directory
        selected_directory = directory_var.get()
        if os.path.isdir(selected_directory):
            label.config(text=f"Selected: {selected_directory}")
            update_file_list(selected_directory)
            preview_window.destroy()

    preview_window = tk.Toplevel(app)
    preview_window.title("Select Directory")
    preview_window.geometry("600x600")

    directory_var = tk.StringVar(value=os.path.join(os.path.expanduser("~"), "Desktop"))
    entry = tk.Entry(preview_window, textvariable=directory_var, width=60)
    entry.pack(pady=5)

    list_frame = tk.Frame(preview_window)
    list_frame.pack(padx=20, pady=10)

    directory_list = tk.Listbox(list_frame, width=80, height=20)
    directory_list.pack()

    directory_list.bind("<Double-1>", on_item_double_click)

    button_frame = tk.Frame(preview_window)
    button_frame.pack(pady=10)

    confirm_button = tk.Button(button_frame, text="Select", command=confirm_selection)
    confirm_button.pack(side=tk.LEFT, padx=5)

    update_preview()


def update_file_list(directory):
    file_listbox.pack(pady=10, padx=10)
    file_listbox.delete(0, tk.END)
    for item in os.listdir(directory):
        file_listbox.insert(tk.END, item)


def start_renaming():
    global selected_directory
    if not selected_directory:
        print("No directory selected!")
        return

    rename_files_with_transition(selected_directory)
    update_file_list(selected_directory)

app = tk.Tk()
app.title("File Renamer")

app.minsize(250, 150)
app.maxsize(800, 600)

label = tk.Label(app, padx=10, pady=10)
label.pack()

button_select = tk.Button(app, text="Select Directory", command=select_directory_with_preview)
button_select.pack(pady=5)

file_listbox = tk.Listbox(app, width=80, height=15)
file_listbox.pack_forget()

button_start = tk.Button(app, text="Start", command=lambda: rename_files_with_transition(selected_directory))
button_start.pack(pady=5)

app.mainloop()
