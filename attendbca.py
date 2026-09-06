import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import sqlite3
from datetime import datetime
import os

# Database Setup
def init_db():
    conn = sqlite3.connect('bca_attendance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        roll_no TEXT UNIQUE
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        date TEXT,
        status TEXT,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )''')
    conn.commit()
    conn.close()

# Colors
BG_COLOR = "#12121c"
PANEL_COLOR = "#1c1c28"
BLUE = "#5b6cf9"
PINK = "#d946ef"
WHITE = "#ffffff"
GREY = "#888899"
INPUT_BG = "#2a2a3a"

class AttendanceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BCA Attendance System")
        self.geometry("900x600")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)
        init_db()
        
        # Load Background Image (Pillow)
        self.bg_image = self.create_gradient_bg(900, 600, "#12121c", "#1e1e2e")
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Main Container
        self.main_frame = tk.Frame(self, bg=BG_COLOR)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.show_signup()

    def create_gradient_bg(self, width, height, color1, color2):
        """Create a simple gradient background using Pillow"""
        img = Image.new("RGB", (width, height))
        pixels = img.load()
        r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
        r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
        for y in range(height):
            r = int(r1 + (r2 - r1) * (y / height))
            g = int(g1 + (g2 - g1) * (y / height))
            b = int(b1 + (b2 - b1) * (y / height))
            for x in range(width):
                pixels[x, y] = (r, g, b)
        return ImageTk.PhotoImage(img)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.main_frame.destroy()
        self.main_frame = tk.Frame(self, bg=BG_COLOR)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

    def create_rounded_button(self, parent, text, color, command):
        """Create a styled flat button (simulating rounded look)"""
        btn = tk.Button(parent, text=text, bg=color, fg=WHITE, font=("Arial", 12, "bold"),
                        bd=0, padx=20, pady=10, command=command, activebackground=color, activeforeground=WHITE)
        return btn

    def show_signup(self):
        self.clear_frame()
        
        # Card Frame
        card = tk.Frame(self.main_frame, bg=BG_COLOR, padx=40, pady=40)
        card.pack(fill="both", expand=True)

        # Title
        tk.Label(card, text="Sign Up", bg=BG_COLOR, fg=WHITE, font=("Arial", 28, "bold")).pack(anchor="w", pady=(0, 5))
        tk.Label(card, text="BCA Attendance System - Register Student", bg=BG_COLOR, fg=GREY, font=("Arial", 10)).pack(anchor="w", pady=(0, 20))

        # Name
        tk.Label(card, text="Full Name", bg=BG_COLOR, fg=WHITE, font=("Arial", 10, "bold")).pack(anchor="w")
        self.name_entry = tk.Entry(card, bg=INPUT_BG, fg=WHITE, insertbackground=WHITE, font=("Arial", 12), bd=0, width=40)
        self.name_entry.pack(pady=(5, 15), ipady=8)

        # Roll No and Email
        row_frame = tk.Frame(card, bg=BG_COLOR)
        row_frame.pack(fill="x", pady=(0, 15))
        
        tk.Label(row_frame, text="Roll No", bg=BG_COLOR, fg=WHITE, font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w")
        self.roll_entry = tk.Entry(row_frame, bg=INPUT_BG, fg=WHITE, insertbackground=WHITE, font=("Arial", 12), bd=0, width=18)
        self.roll_entry.grid(row=1, column=0, padx=(0, 10), ipady=8)

        tk.Label(row_frame, text="Email ID", bg=BG_COLOR, fg=WHITE, font=("Arial", 10, "bold")).grid(row=0, column=1, sticky="w")
        self.email_entry = tk.Entry(row_frame, bg=INPUT_BG, fg=WHITE, insertbackground=WHITE, font=("Arial", 12), bd=0, width=18)
        self.email_entry.grid(row=1, column=1, ipady=8)

        # Password
        tk.Label(card, text="Password", bg=BG_COLOR, fg=WHITE, font=("Arial", 10, "bold")).pack(anchor="w")
        self.pass_entry = tk.Entry(card, bg=INPUT_BG, fg=WHITE, insertbackground=WHITE, font=("Arial", 12), show="•", bd=0, width=40)
        self.pass_entry.pack(pady=(5, 20), ipady=8)

        # Signup Button
        self.create_rounded_button(card, "Sign Up", BLUE, self.register_student).pack(fill="x", pady=(0, 15))

        # Divider
        tk.Label(card, text="──────────  Or  ──────────", bg=BG_COLOR, fg=GREY, font=("Arial", 10)).pack(pady=(0, 15))

        # Social Buttons (Mock)
        social_frame = tk.Frame(card, bg=BG_COLOR)
        social_frame.pack(fill="x", pady=(0, 15))
        self.create_rounded_button(social_frame, "Google", "#db4437", lambda: messagebox.showinfo("Info", "Google Login Mocked")).pack(side="left", expand=True, fill="x", padx=(0, 5))
        self.create_rounded_button(social_frame, "Facebook", "#4267B2", lambda: messagebox.showinfo("Info", "Facebook Login Mocked")).pack(side="right", expand=True, fill="x", padx=(5, 0))

        # Login Link
        tk.Label(card, text="Already have an account? Login", bg=BG_COLOR, fg=BLUE, font=("Arial", 10, "underline"), cursor="hand2").pack()
        # Bind click to login page (we will skip full login implementation for brevity, but you can add it here)

    def register_student(self):
        name = self.name_entry.get()
        roll = self.roll_entry.get()
        email = self.email_entry.get()
        pwd = self.pass_entry.get()

        if not name or not roll or not email or not pwd:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = sqlite3.connect('bca_attendance.db')
            c = conn.cursor()
            c.execute("INSERT INTO students (name, email, password, roll_no) VALUES (?, ?, ?, ?)",
                      (name, email, pwd, roll))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Student Registered Successfully!")
            self.clear_fields()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email or Roll No already exists!")
            return

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.roll_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.pass_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = AttendanceApp()
    app.mainloop()
