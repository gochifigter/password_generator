"""
Simple GUI Interface for Password Generator
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pyperclip  # For clipboard functionality
from password_generator import PasswordGenerator

class PasswordGeneratorGUI:
    """Graphical user interface for password generator"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Password Generator")
        self.root.geometry("500x600")
        self.root.resizable(True, True)
        
        self.generator = PasswordGenerator()
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Password length
        ttk.Label(main_frame, text="Password Length:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.length_var = tk.IntVar(value=16)
        length_spinbox = ttk.Spinbox(main_frame, from_=8, to=128, textvariable=self.length_var, width=10)
        length_spinbox.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Character sets
        ttk.Label(main_frame, text="Character Sets:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        char_frame = ttk.Frame(main_frame)
        char_frame.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.lower_var = tk.BooleanVar(value=True)
        self.upper_var = tk.BooleanVar(value=True)
        self.digit_var = tk.BooleanVar(value=True)
        self.symbol_var = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(char_frame, text="Lowercase (a-z)", variable=self.lower_var).grid(row=0, column=0, sticky=tk.W)
        ttk.Checkbutton(char_frame, text="Uppercase (A-Z)", variable=self.upper_var).grid(row=0, column=1, sticky=tk.W)
        ttk.Checkbutton(char_frame, text="Digits (0-9)", variable=self.digit_var).grid(row=1, column=0, sticky=tk.W)
        ttk.Checkbutton(char_frame, text="Symbols (!@#...)", variable=self.symbol_var).grid(row=1, column=1, sticky=tk.W)
        
        # Custom character set
        ttk.Label(main_frame, text="Custom Characters:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.custom_var = tk.StringVar()
        custom_entry = ttk.Entry(main_frame, textvariable=self.custom_var, width=30)
        custom_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Number of passwords
        ttk.Label(main_frame, text="Number to generate:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.count_var = tk.IntVar(value=1)
        count_spinbox = ttk.Spinbox(main_frame, from_=1, to=20, textvariable=self.count_var, width=10)
        count_spinbox.grid(row=3, column=1, sticky=tk.W, pady=5)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Generate Password", command=self.generate_password).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_output).pack(side=tk.LEFT, padx=5)
        
        # Output area
        ttk.Label(main_frame, text="Generated Passwords:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.output_text = scrolledtext.ScrolledText(main_frame, width=50, height=15, wrap=tk.WORD)
        self.output_text.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Strength analysis
        self.strength_text = tk.Text(main_frame, width=50, height=6, wrap=tk.WORD)
        self.strength_text.grid(row=7, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        self.strength_text.config(state=tk.DISABLED)
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
    
    def get_character_types(self):
        """Get selected character types"""
        char_types = []
        if self.lower_var.get():
            char_types.append('lowercase')
        if self.upper_var.get():
            char_types.append('uppercase')
        if self.digit_var.get():
            char_types.append('digits')
        if self.symbol_var.get():
            char_types.append('symbols')
        return char_types
    
    def generate_password(self):
        """Generate password based on current settings"""
        try:
            self.generator = PasswordGenerator()
            
            custom_chars = self.custom_var.get().strip()
            if custom_chars:
                self.generator.set_custom_character_set(custom_chars)
            else:
                char_types = self.get_character_types()
                if not char_types:
                    messagebox.showerror("Error", "Please select at least one character set")
                    return
                self.generator.set_character_set(char_types)
            
            length = self.length_var.get()
            count = self.count_var.get()
            
            if count == 1:
                password = self.generator.generate_password(length)
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, password)
                
                # Show strength analysis
                self.show_strength_analysis(password)
            else:
                passwords = self.generator.generate_multiple_passwords(length, count)
                output = "\n".join([f"{i+1}. {pwd}" for i, pwd in enumerate(passwords)])
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, output)
                self.clear_strength_analysis()
        
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    
    def show_strength_analysis(self, password):
        """Show password strength analysis"""
        strength = self.generator.get_password_strength(password)
        
        analysis = f"Password Strength Analysis:\n\n"
        analysis += f"Length: {len(password)} characters\n"
        analysis += f"Contains lowercase: {'✓ Yes' if strength['has_lowercase'] else '✗ No'}\n"
        analysis += f"Contains uppercase: {'✓ Yes' if strength['has_uppercase'] else '✗ No'}\n"
        analysis += f"Contains digits: {'✓ Yes' if strength['has_digits'] else '✗ No'}\n"
        analysis += f"Contains symbols: {'✓ Yes' if strength['has_symbols'] else '✗ No'}\n\n"
        analysis += f"Overall strength: {'STRONG ✓' if strength['is_strong'] else 'WEAK ✗'}"
        
        self.strength_text.config(state=tk.NORMAL)
        self.strength_text.delete(1.0, tk.END)
        self.strength_text.insert(tk.END, analysis)
        self.strength_text.config(state=tk.DISABLED)
    
    def clear_strength_analysis(self):
        """Clear strength analysis display"""
        self.strength_text.config(state=tk.NORMAL)
        self.strength_text.delete(1.0, tk.END)
        self.strength_text.config(state=tk.DISABLED)
    
    def copy_to_clipboard(self):
        """Copy generated password to clipboard"""
        password = self.output_text.get(1.0, tk.END).strip()
        if password:
            try:
                pyperclip.copy(password)
                messagebox.showinfo("Success", "Password copied to clipboard!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not copy to clipboard: {e}")
        else:
            messagebox.showwarning("Warning", "No password to copy")
    
    def clear_output(self):
        """Clear output text area"""
        self.output_text.delete(1.0, tk.END)
        self.clear_strength_analysis()

def main():
    """Launch the GUI application"""
    try:
        root = tk.Tk()
        app = PasswordGeneratorGUI(root)
        root.mainloop()
    except ImportError as e:
        print("GUI requires tkinter to be available")
        print("On some systems, you may need to install python3-tk")
        raise e

if __name__ == "__main__":
    main()