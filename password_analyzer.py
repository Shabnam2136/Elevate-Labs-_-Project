import tkinter as tk
from tkinter import ttk, messagebox, filedialog, font
import zxcvbn
import itertools
import json
from datetime import datetime
import os
from tkinter import Tk, Frame, Label, Button, Entry, Text, Checkbutton, BooleanVar, StringVar, IntVar

class PasswordAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Analyzer & Wordlist Generator")
        self.root.geometry("900x700")
        self.root.configure(bg='#f5f5f5')
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure fonts
        self.title_font = ('Segoe UI', 16, 'bold')
        self.header_font = ('Segoe UI', 11, 'bold')
        self.text_font = ('Segoe UI', 10)
        self.button_font = ('Segoe UI', 10, 'bold')
        
        # Configure colors
        self.bg_color = '#f5f5f5'
        self.card_bg = '#ffffff'
        self.accent_color = '#4a90e2'
        self.success_color = '#2ecc71'
        self.warning_color = '#e74c3c'
        
        # Configure styles
        style.configure('TFrame', background=self.bg_color)
        style.configure('Card.TFrame', background=self.card_bg, relief='solid', borderwidth=0)
        style.configure('TLabel', background=self.bg_color, font=self.text_font)
        style.configure('Header.TLabel', font=self.header_font, foreground='#333333')
        style.configure('TButton', font=self.button_font, padding=6)
        style.configure('Accent.TButton', background=self.accent_color, foreground='white')
        style.configure('TCheckbutton', background=self.card_bg, font=self.text_font)
        style.configure('TEntry', font=self.text_font, padding=5)
        style.map('Accent.TButton',
                 background=[('active', '#357abd'), ('pressed', '#2a5d90')],
                 foreground=[('pressed', 'white'), ('active', 'white')])
        
        # Create main container with padding
        self.main_container = ttk.Frame(root, padding=20)
        self.main_container.pack(fill='both', expand=True)
        
        # Title
        title_frame = ttk.Frame(self.main_container)
        title_frame.pack(fill='x', pady=(0, 20))
        ttk.Label(title_frame, text="Password Strength Analyzer", font=self.title_font, 
                 foreground='#2c3e50').pack(side='left')
        
        # Create notebook for tabs with custom style
        style.configure('TNotebook', background=self.bg_color)
        style.configure('TNotebook.Tab', padding=[15, 5], font=self.button_font)
        
        self.notebook = ttk.Notebook(self.main_container)
        self.notebook.pack(expand=True, fill='both')
        
        # Create tabs
        self.tab_analyzer = ttk.Frame(self.notebook)
        self.tab_wordlist = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_analyzer, text='Password Analyzer')
        self.notebook.add(self.tab_wordlist, text='Wordlist Generator')
        
        self.setup_analyzer_tab()
        self.setup_wordlist_tab()
    
    def setup_analyzer_tab(self):
        # Main container for the tab
        container = ttk.Frame(self.tab_analyzer)
        container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Input card
        input_card = ttk.Frame(container, style='Card.TFrame')
        input_card.pack(fill='x', pady=(0, 20), ipadx=15, ipady=15)
        
        # Password Entry
        ttk.Label(input_card, text="Enter Password to Analyze:", style='Header.TLabel').pack(anchor='w', pady=(0, 5))
        
        entry_frame = ttk.Frame(input_card)
        entry_frame.pack(fill='x')
        
        self.password_entry = ttk.Entry(entry_frame, show="*", font=self.text_font)
        self.password_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        # Analyze Button with custom style
        analyze_btn = ttk.Button(entry_frame, text="Analyze Password", 
                               command=self.analyze_password, style='Accent.TButton')
        analyze_btn.pack(side='right')
        
        # Results Card
        results_card = ttk.Frame(container, style='Card.TFrame')
        results_card.pack(fill='both', expand=True, ipadx=15, ipady=15)
        
        # Results Header
        ttk.Label(results_card, text="Analysis Results", style='Header.TLabel').pack(anchor='w', pady=(0, 10))
        
        # Results Text with scrollbar
        text_frame = ttk.Frame(results_card)
        text_frame.pack(fill='both', expand=True)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side='right', fill='y')
        
        self.results_text = tk.Text(text_frame, wrap=tk.WORD, font=self.text_font,
                                  yscrollcommand=scrollbar.set, padx=10, pady=10,
                                  highlightthickness=0, borderwidth=0)
        self.results_text.pack(fill='both', expand=True)
        scrollbar.config(command=self.results_text.yview)
        
        # Configure tag for better text formatting
        self.results_text.tag_configure('success', foreground='#27ae60')
        self.results_text.tag_configure('warning', foreground='#e74c3c')
        self.results_text.tag_configure('info', foreground='#3498db')
        self.results_text.config(state='disabled')
    
    def setup_wordlist_tab(self):
        # Main container with padding
        container = ttk.Frame(self.tab_wordlist)
        container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Left side - Inputs and options
        left_frame = ttk.Frame(container)
        left_frame.pack(side='left', fill='both', padx=(0, 10), expand=False)
        
        # Personal Info Card
        info_card = ttk.Frame(left_frame, style='Card.TFrame')
        info_card.pack(fill='x', pady=(0, 20), ipadx=15, ipady=15)
        
        ttk.Label(info_card, text="Personal Information", style='Header.TLabel').grid(row=0, column=0, columnspan=2, sticky='w', pady=(0, 10))
        
        # Name
        ttk.Label(info_card, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.name_entry = ttk.Entry(info_card, font=self.text_font)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
        
        # Pet Name
        ttk.Label(info_card, text="Pet Name:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.pet_entry = ttk.Entry(info_card, font=self.text_font)
        self.pet_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
        
        # Birth Year
        ttk.Label(info_card, text="Birth Year:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.year_entry = ttk.Entry(info_card, font=self.text_font, width=10)
        self.year_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        
        # Options Card
        options_card = ttk.Frame(left_frame, style='Card.TFrame')
        options_card.pack(fill='x', pady=(0, 20), ipadx=15, ipady=15)
        
        ttk.Label(options_card, text="Wordlist Options", style='Header.TLabel').pack(anchor='w', pady=(0, 10))
        
        # Checkboxes for word variations
        self.leet_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_card, text="Include Leet Speak", variable=self.leet_var).pack(anchor='w', padx=5, pady=5)
        
        self.year_combos_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_card, text="Include Year Combinations", variable=self.year_combos_var).pack(anchor='w', padx=5, pady=5)
        
        self.special_chars_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_card, text="Add Special Characters", variable=self.special_chars_var).pack(anchor='w', padx=5, pady=5)
        
        # Action Buttons
        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill='x')
        
        ttk.Button(btn_frame, text="Generate Wordlist", command=self.generate_wordlist, 
                  style='Accent.TButton').pack(side='left', padx=(0, 10))
        
        ttk.Button(btn_frame, text="Save Wordlist to File", command=self.save_wordlist).pack(side='left')
        
        # Right side - Preview
        right_frame = ttk.Frame(container)
        right_frame.pack(side='right', fill='both', expand=True)
        
        preview_card = ttk.Frame(right_frame, style='Card.TFrame')
        preview_card.pack(fill='both', expand=True, ipadx=15, ipady=15)
        
        ttk.Label(preview_card, text="Wordlist Preview", style='Header.TLabel').pack(anchor='w', pady=(0, 10))
        
        # Preview text with scrollbar
        text_frame = ttk.Frame(preview_card)
        text_frame.pack(fill='both', expand=True)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side='right', fill='y')
        
        self.preview_text = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set,
                                  font=('Consolas', 9), padx=10, pady=10,
                                  highlightthickness=0, borderwidth=0)
        self.preview_text.pack(fill='both', expand=True)
        scrollbar.config(command=self.preview_text.yview)
        self.preview_text.config(state='disabled')
    
    def analyze_password(self):
        password = self.password_entry.get()
        if not password:
            messagebox.showwarning("Warning", "Please enter a password to analyze.")
            return
        
        results = zxcvbn.zxcvbn(password)
        
        self.results_text.config(state='normal')
        self.results_text.delete(1.0, tk.END)
        
        # Basic info with styling
        self.results_text.insert(tk.END, f"Password: ", 'info')
        self.results_text.insert(tk.END, f"{password}\n\n")
        
        # Strength score with color coding
        score = results['score']
        score_text = f"Strength Score: {score}/4"
        if score >= 3:
            self.results_text.insert(tk.END, score_text, 'success')
        else:
            self.results_text.insert(tk.END, score_text, 'warning')
        self.results_text.insert(tk.END, "\n\n")
        
        # Feedback with better formatting
        if 'feedback' in results and results['feedback']:
            feedback = results['feedback']
            if feedback['warning']:
                self.results_text.insert(tk.END, "⚠️ ", 'warning')
                self.results_text.insert(tk.END, f"{feedback['warning']}\n\n", 'warning')
                
            if feedback['suggestions']:
                self.results_text.insert(tk.END, "🔍 Suggestions:\n", 'info')
                for suggestion in feedback['suggestions']:
                    self.results_text.insert(tk.END, f"• {suggestion}\n")
                self.results_text.insert(tk.END, "\n")
        
        # Crack time with emoji
        crack_time = results['crack_times_display']['offline_slow_hashing_1e4_per_second']
        self.results_text.insert(tk.END, "⏱️ ", 'info')
        self.results_text.insert(tk.END, f"Estimated Time to Crack: {crack_time}")
        
        # Add some spacing at the bottom
        self.results_text.insert(tk.END, "\n\n")
        
        # Auto-scroll to top
        self.results_text.see('1.0')
        self.results_text.config(state='disabled')
    
    def generate_wordlist(self):
        name = self.name_entry.get().strip()
        pet = self.pet_entry.get().strip()
        year = self.year_entry.get().strip()
        
        if not any([name, pet, year]):
            messagebox.showwarning("Warning", "Please enter at least one piece of information.")
            return
        
        # Show loading state
        self.preview_text.config(state='normal')
        self.preview_text.delete(1.0, tk.END)
        self.preview_text.insert(tk.END, "Generating wordlist...")
        self.preview_text.config(state='disabled')
        self.root.update()
        
        try:
            words = []
            if name:
                words.append(name.lower())
                words.append(name.capitalize())
            if pet:
                words.append(pet.lower())
                words.append(pet.capitalize())
            
            # Generate combinations
            wordlist = set()
            
            # Add individual words
            for word in words:
                wordlist.add(word)
            
            # Add combinations
            if len(words) > 1:
                for r in range(2, min(4, len(words) + 1)):  # Combinations of 2-3 words
                    for combo in itertools.permutations(words, r):
                        wordlist.add(''.join(combo))
                        wordlist.add('.'.join(combo))
                        wordlist.add('_'.join(combo))
                        wordlist.add('-'.join(combo))
            
            # Apply leet speak if selected
            if self.leet_var.get():
                leet_words = set()
                leet_map = {
                    'a': ['@', '4'],
                    'e': ['3'],
                    'i': ['1', '!'],
                    'o': ['0'],
                    's': ['5', '$'],
                    't': ['7', '+']
                }
                
                for word in wordlist.copy():
                    for i, char in enumerate(word.lower()):
                        if char in leet_map:
                            for leet_char in leet_map[char]:
                                new_word = word[:i] + leet_char + word[i+1:]
                                leet_words.add(new_word)
                wordlist.update(leet_words)
            
            # Add year combinations if selected and year is provided
            if self.year_combos_var.get() and year:
                year_combos = set()
                for word in wordlist.copy():
                    year_combos.add(f"{word}{year}")
                    year_combos.add(f"{year}{word}")
                    if len(year) == 4:
                        short_year = year[2:]
                        year_combos.add(f"{word}{short_year}")
                        year_combos.add(f"{short_year}{word}")
                wordlist.update(year_combos)
            
            # Add special characters if selected
            if self.special_chars_var.get():
                special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
                special_combos = set()
                for word in wordlist.copy():
                    for char in special_chars:
                        special_combos.add(f"{word}{char}")
                        special_combos.add(f"{char}{word}")
                        special_combos.add(f"{word}{char}{char}")
                wordlist.update(special_combos)
            
            # Store the wordlist for saving
            self.current_wordlist = sorted(list(wordlist))
            
            # Update preview with better formatting
            self.preview_text.config(state='normal')
            self.preview_text.delete(1.0, tk.END)
            
            # Show first 20 items with numbering
            preview_items = self.current_wordlist[:20]
            for i, item in enumerate(preview_items, 1):
                self.preview_text.insert(tk.END, f"{i:2d}. {item}\n")
                
            if len(self.current_wordlist) > 20:
                self.preview_text.insert(tk.END, f"\n... and {len(self.current_wordlist) - 20} more variations")
            
            # Add summary at the bottom
            self.preview_text.insert(tk.END, f"\n\nTotal variations generated: {len(self.current_wordlist):,}")
            
            # Auto-scroll to top
            self.preview_text.see('1.0')
            self.preview_text.config(state='disabled')
            
            # Show success message with count
            messagebox.showinfo("Success", f"Generated {len(self.current_wordlist):,} password variations!")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.preview_text.config(state='normal')
            self.preview_text.delete(1.0, tk.END)
            self.preview_text.insert(tk.END, f"Error: {str(e)}")
            self.preview_text.config(state='disabled')
    
    def save_wordlist(self):
        if not hasattr(self, 'current_wordlist') or not self.current_wordlist:
            messagebox.showwarning("Warning", "No wordlist generated to save.")
            return
        
        # Suggest a filename with timestamp
        default_filename = f"wordlist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        # Show save dialog with file type options
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("Wordlist files", "*.txt;*.lst;*.dic"),
                ("All files", "*.*")
            ],
            initialfile=default_filename,
            title="Save Wordlist As"
        )
        
        if filename:
            try:
                # Show progress in the preview area
                self.preview_text.config(state='normal')
                self.preview_text.delete(1.0, tk.END)
                self.preview_text.insert(tk.END, f"Saving wordlist to:\n{filename}\n\n")
                self.preview_text.insert(tk.END, "This may take a moment for large wordlists...")
                self.preview_text.see('1.0')
                self.preview_text.update()
                
                # Write the file
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(self.current_wordlist))
                
                # Update status
                self.preview_text.delete(1.0, tk.END)
                self.preview_text.insert(tk.END, "✅ Wordlist saved successfully!\n\n")
                self.preview_text.insert(tk.END, f"Location: {filename}\n")
                self.preview_text.insert(tk.END, f"Entries: {len(self.current_wordlist):,}")
                self.preview_text.see('1.0')
                
                # Show success message
                messagebox.showinfo(
                    "Success",
                    f"Successfully saved {len(self.current_wordlist):,} entries to:\n{filename}",
                    parent=self.root
                )
                
            except Exception as e:
                error_msg = f"Failed to save file: {str(e)}"
                self.preview_text.delete(1.0, tk.END)
                self.preview_text.insert(tk.END, f"❌ Error saving file:\n{error_msg}")
                messagebox.showerror("Error", error_msg, parent=self.root)
            finally:
                self.preview_text.config(state='disabled')

def main():
    root = tk.Tk()
    app = PasswordAnalyzer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
