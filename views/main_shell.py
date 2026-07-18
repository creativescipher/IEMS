import customtkinter as ctk

from services.session import Session
from services.auth_service import AuthService


class MainShell(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Income & Expenditure Management System")
        self.geometry("1100x700")
        self.minsize(1000, 650)

        # ---------- Header ----------

        header = ctk.CTkFrame(self, height=70)
        header.pack(fill="x")

        ctk.CTkLabel(
            header,
            text="Income & Expenditure Management System",
            font=("Segoe UI", 24, "bold")
        ).pack(side="left", padx=20, pady=15)

        ctk.CTkButton(
            header,
            text="Logout",
            width=120,
            command=self.logout
        ).pack(side="right", padx=20)

        # ---------- Main ----------

        body = ctk.CTkFrame(self)
        body.pack(fill="both", expand=True)

        # Sidebar

        sidebar = ctk.CTkFrame(body, width=220)
        sidebar.pack(side="left", fill="y")

        menu = [
            "Dashboard",
            "Income",
            "Expenditure",
            "Reports",
            "Users",
            "Settings"
        ]

        for item in menu:

            ctk.CTkButton(
                sidebar,
                text=item,
                width=180
            ).pack(pady=8, padx=15)

        # Content Area

        self.content = ctk.CTkFrame(body)
        self.content.pack(side="left", fill="both", expand=True)

        ctk.CTkLabel(
            self.content,
            text=f"Welcome, {Session.full_name()}",
            font=("Segoe UI", 28, "bold")
        ).pack(pady=(50, 10))

        ctk.CTkLabel(
            self.content,
            text=f"Username: {Session.username()}",
            font=("Segoe UI", 18)
        ).pack()

        ctk.CTkLabel(
            self.content,
            text=f"Role: {Session.role()}",
            font=("Segoe UI", 18)
        ).pack()

    def logout(self):

        AuthService.logout()

        self.destroy()

        from views.login_view import LoginView

        LoginView().mainloop()