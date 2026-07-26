
import customtkinter as ctk
from storage.json_storage import load_students


class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # Colors (same theme as your app)
        BG_CARD = "#1e1a27"
        TEXT_PRIMARY = "#efe9f8"
        TEXT_MUTED = "#9b93aa"
        PURPLE = "#534ab7"

        self.configure(fg_color="#121016")

        # Title
        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Segoe UI", 30, "bold"),
            text_color=TEXT_PRIMARY
        )
        title.pack(anchor="w", padx=30, pady=(25, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Welcome back, Admin",
            font=("Segoe UI", 14),
            text_color=TEXT_MUTED
        )
        subtitle.pack(anchor="w", padx=30)

        # Statistics Cards Frame
        cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        cards_frame.pack(fill="x", padx=30, pady=30)

        students = load_students()

        total_students = len(students)


        avg_age = (
            round(
                sum(int(student["age"]) for student in students)
                / len(students),
                1
            )
            if students else 0
        )

        stats = [
            ("Students", total_students),
            ("Average Age", avg_age),
            ("New Added", total_students)
        ]

        for title_text, value in stats:

            card = ctk.CTkFrame(
                cards_frame,
                width=220,
                height=120,
                corner_radius=15,
                fg_color=BG_CARD
            )

            card.pack(
                side="left",
                expand=True,
                fill="both",
                padx=10
            )

            label = ctk.CTkLabel(
                card,
                text=title_text,
                font=("Segoe UI", 14),
                text_color=TEXT_MUTED
            )

            label.pack(
                anchor="w",
                padx=20,
                pady=(20, 5)
            )


            number = ctk.CTkLabel(
                card,
                text=str(value),
                font=("Segoe UI", 32, "bold"),
                text_color=PURPLE
            )

            number.pack(
                anchor="w",
                padx=20
            )


        # Bottom Section
        bottom_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        bottom_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )


        # Recent Students
        recent_frame = ctk.CTkFrame(
            bottom_frame,
            corner_radius=15,
            fg_color=BG_CARD
        )

        recent_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0,10)
        )


        ctk.CTkLabel(
            recent_frame,
            text="Recent Students",
            font=("Segoe UI",18,"bold"),
            text_color=TEXT_PRIMARY
        ).pack(
            anchor="w",
            padx=20,
            pady=15
        )


        for student in students[-5:]:

            ctk.CTkLabel(
                recent_frame,
                text=f'{student["name"]}     Class {student["class"]}',
                font=("Segoe UI",14),
                text_color=TEXT_MUTED
            ).pack(
                anchor="w",
                padx=20,
                pady=5
            )


        