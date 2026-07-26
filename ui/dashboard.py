from ui.pages.dashboard_page import DashboardPage
from ui.pages.add_student_page import AddStudentPage
from ui.pages.view_students_page import ViewStudentsPage
from ui.pages.settings_page import SettingsPage
import customtkinter as ctk

ctk.set_appearance_mode("dark")

PURPLE = "#534ab7"
PURPLE_LIGHT = "#7f77dd"
BG_MAIN = "#121016"
BG_SIDEBAR = "#1a1620"
BG_CARD = "#1e1a27"
BG_CONTENT = "#191420"
TEXT_PRIMARY = "#efe9f8"
TEXT_MUTED = "#9b93aa"
TEXT_NAV = "#a39cae"
TEXT_LOGOUT = "#e0999a"


class SchoolDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("School Management System")
        self.geometry("1200x600")
        self.configure(fg_color=BG_MAIN)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self._build_sidebar()
        self._build_main()
        self.show_page(DashboardPage)
        

    def _build_sidebar(self):
        sidebar = ctk.CTkFrame(
            self, fg_color=BG_SIDEBAR, 
            width=180, 
            corner_radius=0
            )
        sidebar.grid(
            row=0, 
            column=0,
            sticky="nsw"
            )
        sidebar.grid_propagate(False)

        ctk.CTkLabel(
            sidebar, text="\U0001F3EB  EDU.O", text_color=TEXT_PRIMARY,
            font=("Segoe UI", 16, "bold")
        ).pack(anchor="w", padx=14, pady=(20, 28))

        nav = ctk.CTkFrame(sidebar, fg_color="transparent")
        nav.pack(fill="x", padx=10)

        pages = {
            "Dashboard": DashboardPage,
            "Add Student": AddStudentPage,
            "View Students": ViewStudentsPage,
            "Settings": SettingsPage,
        }

        nav_items = [
            ("🏠", "Dashboard"),
            ("➕", "Add Student"),
            ("👥", "View Students"),
            ("⚙", "Settings")
            ]


        for icon, label in nav_items:

            button = ctk.CTkButton(
                nav,
                text=f"{icon}  {label}",
                fg_color="transparent",
                hover_color=PURPLE_LIGHT,
                text_color=TEXT_NAV,
                anchor="w",
                command=lambda p=pages[label]: self.show_page(p)
        )

            button.pack(fill="x", pady=2)


        logout = ctk.CTkFrame(sidebar, fg_color="transparent")
        logout.pack(
            side="bottom", 
            fill="x", 
            padx=10, 
            pady=14
            )
        ctk.CTkFrame(logout, fg_color="#2c2634", height=1).pack(fill="x", pady=(0, 10))
        ctk.CTkLabel(
            logout, text="\u2192  Logout", 
            text_color=TEXT_LOGOUT,
            font=("Segoe UI", 13), anchor="w").pack(fill="x")

        
    def _stat_card(self, parent, label, value):
        card = ctk.CTkFrame(
            parent, fg_color=BG_CARD, corner_radius=10,
            border_width=0, border_color=PURPLE_LIGHT
        )
        left_bar = ctk.CTkFrame(card, fg_color=PURPLE_LIGHT, width=3, corner_radius=0)
        left_bar.pack(side="left", fill="y")
        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(side="left", fill="both", expand=True, padx=13, pady=14)
        ctk.CTkLabel(
            body, text=label, text_color=TEXT_MUTED, font=("Segoe UI", 12), anchor="w"
        ).pack(anchor="w")
        ctk.CTkLabel(
            body, text=str(value), text_color=TEXT_PRIMARY,
            font=("Segoe UI", 24, "bold"), anchor="w"
        ).pack(anchor="w", pady=(6, 0))
        return card

    def _build_main(self):
        main = ctk.CTkFrame(self, fg_color=BG_MAIN, corner_radius=0)
        main.grid(row=0, column=1, sticky="nsew", padx=28, pady=24)

        self.content_frame = ctk.CTkFrame(
        main,
        fg_color="transparent"
        )

        self.content_frame.pack(
        fill="both",
        expand=True
        )
        self.pages = {}

        self.pages[DashboardPage] = DashboardPage(self.content_frame, self)
        self.pages[AddStudentPage] = AddStudentPage(self.content_frame, self)
        self.pages[ViewStudentsPage] = ViewStudentsPage(self.content_frame, self)
        self.pages[SettingsPage] = SettingsPage(self.content_frame, self)

        for page in self.pages.values():
            page.place(relx=0, rely=0, relwidth=1, relheight=1)
        
    def show_page(self, page_class):
        self.pages[page_class].tkraise()

    

if __name__ == "__main__":
    app = SchoolDashboard()
    app.mainloop()