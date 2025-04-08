import tkinter as tk
from tkinter import filedialog
import pandas as pd
from pathlib import Path

class ExcelProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Processor")
        
        # Create GUI elements
        self.file_label = tk.Label(root, text="No file selected")
        self.file_label.pack(pady=10)
        
        self.select_button = tk.Button(
            root, 
            text="Select Excel File", 
            command=self.select_file
        )
        self.select_button.pack(pady=5)
        
        self.process_button = tk.Button(
            root, 
            text="Process Documents", 
            command=self.process_file,
            state=tk.DISABLED
        )
        self.process_button.pack(pady=5)
        
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=10)
        
        self.file_path = None
    
    def select_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx")]
        )
        if self.file_path:
            self.file_label.config(
                text=f"Selected: {Path(self.file_path).name}"
            )
            self.process_button.config(state=tk.NORMAL)
    
    def process_file(self):
        try:
            # Use your existing processing logic here
            df = pd.read_excel(self.file_path, usecols=[0, 2])
            df.columns = ['document_id', 'document_text']
            
            processed_df = df.groupby('document_id', as_index=False).agg({
                'document_text': lambda x: ' '.join(str(text).strip() for text in x)
            })
            
            # Write to new sheet
            with pd.ExcelWriter(
                self.file_path, 
                engine='openpyxl', 
                mode='a'
            ) as writer:
                processed_df.to_excel(
                    writer, 
                    sheet_name="Processed_Data", 
                    index=False
                )
            
            self.status_label.config(
                text="Processing complete! Check 'Processed_Data' sheet.",
                fg="green"
            )
        except Exception as e:
            self.status_label.config(
                text=f"Error: {str(e)}",
                fg="red"
            )

# Run the application
if __name__ == "__main__":
    root = tk.Tk() 
    app = ExcelProcessorApp(root)
    root.mainloop()