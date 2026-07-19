import customtkinter as ctk

from config import theme
from services.report_service import ReportService


class ReportsPage(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=theme.BACKGROUND
        )

        self.build_ui()
        self.load_report()

    # ==================================================

    def build_ui(self):

        ctk.CTkLabel(
            self,
            text="Financial Report",
            font=theme.TITLE_FONT
        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 20)
        )

        self.report_frame = ctk.CTkFrame(self)

        self.report_frame.pack(
            padx=30,
            pady=10,
            fill="x"
        )

        self.income_label = ctk.CTkLabel(
            self.report_frame,
            text="",
            font=("Segoe UI", 15)
        )
        self.income_label.pack(anchor="w", pady=8)

        self.expenditure_label = ctk.CTkLabel(
            self.report_frame,
            text="",
            font=("Segoe UI", 15)
        )
        self.expenditure_label.pack(anchor="w", pady=8)

        self.balance_label = ctk.CTkLabel(
            self.report_frame,
            text="",
            font=("Segoe UI", 15, "bold")
        )
        self.balance_label.pack(anchor="w", pady=8)

        self.income_count_label = ctk.CTkLabel(
            self.report_frame,
            text="",
            font=("Segoe UI", 15)
        )
        self.income_count_label.pack(anchor="w", pady=8)

        self.expenditure_count_label = ctk.CTkLabel(
            self.report_frame,
            text="",
            font=("Segoe UI", 15)
        )
        self.expenditure_count_label.pack(anchor="w", pady=8)

        ctk.CTkButton(
            self,
            text="Refresh Report",
            width=180,
            command=self.load_report
        ).pack(
            pady=25
        )

    # ==================================================

    def load_report(self):

        report = ReportService.get_summary()

        self.income_label.configure(
            text=f"Total Income: ₦{report['total_income']:,.2f}"
        )

        self.expenditure_label.configure(
            text=f"Total Expenditure: ₦{report['total_expenditure']:,.2f}"
        )

        self.balance_label.configure(
            text=f"Net Balance: ₦{report['balance']:,.2f}"
        )

        self.income_count_label.configure(
            text=f"Income Records: {report['income_count']}"
        )

        self.expenditure_count_label.configure(
            text=f"Expenditure Records: {report['expenditure_count']}"
        )