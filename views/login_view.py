import customtkinter as ctk
from tkinter import messagebox

from services.auth_service import AuthService


class LoginView(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Income & Expenditure Management System")
        self.geometry("500x420")
        self.resizable(False, False)

        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")

        title = ctk.CTkLabel(
            self,
            text="Income & Expenditure\nManagement System",
            font=("Segoe UI", 24, "bold")
        )
        title.pack(pady=(40, 20))

        self.username = ctk.CTkEntry(
            self,
            width=280,
            placeholder_text="Username"
        )
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(
            self,
            width=280,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=10)

        self.status = ctk.CTkLabel(
            self,
            text="",
            text_color="red"
        )
        self.status.pack()

        login_button = ctk.CTkButton(
            self,
            text="Login",
            width=200,
            command=self.login
        )

        login_button.pack(pady=20)

        self.bind("<Return>", lambda event: self.login())

    def login(self):

        username = self.username.get().strip()
        password = self.password.get()

        if not username or not password:
            self.status.configure(text="Please enter username and password.")
            return

        if AuthService.login(username, password):

            messagebox.showinfo(
                "Success",
                f"Welcome {username}!"
            )

            self.destroy()

            from views.main_shell import MainShell

            app = MainShell()
            app.mainloop()

        else:

            self.status.configure(
                text="Invalid username or password."
            )