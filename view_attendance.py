from tkinter import *
import customtkinter as ctk
import openpyxl
import numpy as np
import pandas as pd
from tkinter import ttk, filedialog, messagebox

def top_level():
    my_window = ctk.CTkToplevel()

    my_window.title('View Attendance')
    # my_window.iconbitmap('path of ico file')
    my_window.geometry("900x400")
    my_window.resizable(False, False)
    
    def close_window():
        my_window.destroy()

    def open_excel():
        # Open a file
        # my_file = filedialog.askopenfilename(title="Open File", filetype=(("Excel Files", "xlsx"), ("All Files", "*.*")))
        my_file = 'attendance.xlsx'
        # Grab the file
        try:
            df = pd.read_excel(my_file)
            # print(df.head(5))
        except Exception as e:
            messagebox.showerror("Woah!", f"There was a problem! {e}")
        
        # Clear the treeview
        my_tree.delete(*my_tree.get_children())
        
        # Get the Headers
        my_tree['column'] = list(df.columns)
        my_tree['show'] = 'headings'
        
        # Show the headers
        for col in my_tree['column']:
            my_tree.heading(col, text=col)
            
        # Show Data
        df_rows = df.to_numpy().tolist()
        for i, row in enumerate(df_rows):
            # Alternate row colors using tags
            tag = 'evenrow' if i % 2 == 0 else 'oddrow'
            my_tree.insert("", "end", values=row, tags=(tag,))
            
        # Set tag colors and foreground text color to white
        my_tree.tag_configure('evenrow', background='steel blue', foreground='white')
        my_tree.tag_configure('oddrow', background='navy', foreground='white')

    # Style the Treeview for hover and selection
    style = ttk.Style()
    style.theme_use("default")

    # Set the style for selected row
    style.map('Treeview', 
            background=[('selected', 'lightblue')],
            foreground=[('selected', 'black')])  # Black text when row is selected

    # Frame for the Treeview
    tree_frame = Frame(my_window)
    tree_frame.pack(pady=20)

    # Scrollbar
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
    my_tree.pack()

    # Configure scrollbar
    tree_scroll.config(command=my_tree.yview)

    # Button
    my_button = ctk.CTkButton(my_window, text="Close Window", command=close_window)
    my_button.pack(pady=20)
    
    open_excel()

#my_window.mainloop()
