import os
import tkinter as tk
from tkinter import messagebox
from file_operations.renamer import rename_files_with_transition

selected_path = None  # Globale Variable für die Auswahl


def update_preview(directory_list, current_dir):
    directory_list.delete(0, tk.END)
    directory_list.insert(tk.END, "... Back")
    directory_list.insert(tk.END, "") 

    try:
        for item in os.listdir(current_dir):
            directory_list.insert(tk.END, item)
    except PermissionError:
        directory_list.insert(tk.END, "Permission denied")


def select_directory_with_navigation(app, file_listbox, button_start):
    def on_item_double_click(event):
        selection = directory_list.get(directory_list.curselection())
        if selection == "... Back":
            new_path = os.path.dirname(current_dir.get())
        else:
            new_path = os.path.join(current_dir.get(), selection)

        if os.path.isdir(new_path):
            current_dir.set(new_path)
            update_preview(directory_list, new_path)
        else:
            messagebox.showinfo("Invalid Selection", "Please select a directory.")

    def confirm_selection():
        global selected_path
        selected_path = current_dir.get()
        file_listbox.pack(pady=10, padx=20)
        button_start.pack(pady=(5, 20))  # Padding hier setzen, wenn der Button sichtbar wird
        file_listbox.delete(0, tk.END)
        file_listbox.insert(tk.END, f"Selected Directory: {selected_path}")
        try:
            for item in os.listdir(selected_path):
                full_path = os.path.join(selected_path, item)
                if os.path.isfile(full_path):
                    file_listbox.insert(tk.END, f" {item}")
                elif os.path.isdir(full_path):
                    file_listbox.insert(tk.END, f" {item}")
        except PermissionError:
            file_listbox.insert(tk.END, "Permission denied to access directory.")
        preview_window.destroy()

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    preview_window = tk.Toplevel(app)
    preview_window.title("Select Directory")
    preview_window.geometry("700x450")

    current_dir = tk.StringVar(value=desktop_path)

    entry = tk.Entry(preview_window, textvariable=current_dir, width=80)
    entry.pack(pady=5, padx=10)

    directory_list = tk.Listbox(preview_window, width=80, height=15, selectmode=tk.BROWSE)
    directory_list.pack(pady=10, padx=20)
    directory_list.bind("<Double-1>", on_item_double_click)

    update_preview(directory_list, desktop_path)

    confirm_button = tk.Button(preview_window, text="Select", command=confirm_selection, width=15)
    confirm_button.pack(pady=10)


def process_directory(file_listbox):
    if not selected_path or not os.path.isdir(selected_path):
        messagebox.showinfo("No Directory", "Please select a directory first.")
        return

    # Leere die Liste und füge einen Status hinzu
    file_listbox.delete(0, tk.END)
    file_listbox.insert(tk.END, f"Processing directory: {selected_path}")

    # Aufruf der Funktion aus renamer.py
    try:
        rename_files_with_transition(selected_path, file_listbox)
    except Exception as e:
        file_listbox.insert(tk.END, f"Error: {str(e)}")

def start_ui():
    global selected_path

    app = tk.Tk()
    app.title("File Renamer")
    app.minsize(300, 50)

    file_listbox = tk.Listbox(app, width=80, height=16)
    file_listbox.pack_forget()

    button_select = tk.Button(
        app, 
        text="Select Directory", 
        command=lambda: select_directory_with_navigation(app, file_listbox, button_start)
    )
    button_select.pack(pady=20)

    button_start = tk.Button(
        app, 
        text="Start", 
        command=lambda: process_directory(file_listbox)
    )
    button_start.pack_forget()

    app.mainloop()
