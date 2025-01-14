import os
import tkinter as tk
import magic

def rename_files_with_transition(directory, file_listbox):
    mime = magic.Magic(mime=True)  # Initialize MIME type detector
    file_listbox.delete(0, tk.END)  # Clear the list

    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)

        # Skip if it's not a file
        if not os.path.isfile(old_path):
            file_listbox.insert(tk.END, f"Skipped: {filename} (not a file)")
            continue

        # Determine MIME type based on file content
        mime_type = mime.from_file(old_path)

        if not mime_type:
            file_listbox.insert(tk.END, f"Skipped: {filename} (unknown file type)")
            continue

        # Rename: lowercase, replace umlauts and spaces
        new_filename = (
            filename.lower()
            .replace("ä", "ae")
            .replace("ö", "oe")
            .replace("ü", "ue")
            .replace("ß", "ss")
            .replace(" ", "_")
        )

        # Check current extension and adjust based on MIME type
        file_extension = os.path.splitext(new_filename)[1]
        if not file_extension:
            # Dynamic extension based on MIME type
            mime_parts = mime_type.split("/")
            if len(mime_parts) == 2:
                main_type, sub_type = mime_parts
                # Special case: text/plain -> .txt
                if mime_type == "text/plain":
                    new_filename = os.path.splitext(new_filename)[0] + ".txt"
                else:
                    new_filename = os.path.splitext(new_filename)[0] + f".{sub_type}"
            else:
                file_listbox.insert(tk.END, f"Skipped: {filename} (unrecognized MIME type)")
                continue

        new_path = os.path.join(directory, new_filename)

        try:
            if old_path != new_path:
                os.rename(old_path, new_path)
                file_listbox.insert(tk.END, "-" * 80)
                file_listbox.insert(tk.END, f"Original Name: {filename}")
                file_listbox.insert(tk.END, f"     New Name:     {new_filename}")
            else:
                file_listbox.insert(tk.END, "-" * 80)
                file_listbox.insert(tk.END, f"Original Name: {filename}")
                file_listbox.insert(tk.END, "     New Name:     no change")
        except Exception as e:
            file_listbox.insert(tk.END, f"Error processing {filename}: {str(e)}")
