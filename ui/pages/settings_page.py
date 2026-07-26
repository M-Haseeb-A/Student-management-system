import customtkinter as ctk
import os
import shutil
from CTkMessagebox import CTkMessagebox


class SettingsPage(ctk.CTkFrame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # Theme colors
        BG_CARD = "#1e1a27"
        TEXT_PRIMARY = "#efe9f8"
        TEXT_MUTED = "#9b93aa"
        PURPLE = "#534ab7"


        self.configure(
            fg_color="#121016"
        )


        # Title
        title = ctk.CTkLabel(
            self,
            text="Settings",
            font=("Segoe UI",30,"bold"),
            text_color=TEXT_PRIMARY
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=(25,20)
        )


        # =========================
        # Data Management
        # =========================

        data_title = ctk.CTkLabel(
            self,
            text="Data Management",
            font=("Segoe UI",20,"bold"),
            text_color=TEXT_PRIMARY
        )

        data_title.pack(
            anchor="w",
            padx=30
        )


        data_frame = ctk.CTkFrame(
            self,
            fg_color=BG_CARD,
            corner_radius=15
        )

        data_frame.pack(
            fill="x",
            padx=30,
            pady=15
        )


        self.create_setting_row(
            data_frame,
            "Backup Data",
            "Create Backup",
            self.backup_data
        )


        self.create_setting_row(
            data_frame,
            "Restore Data",
            "Restore",
            self.restore_data
        )


        self.create_setting_row(
            data_frame,
            "Clear Database",
            "Delete All Data",
            self.clear_database
        )



        # =========================
        # Application Info
        # =========================


        app_title = ctk.CTkLabel(
            self,
            text="Application",
            font=("Segoe UI",20,"bold"),
            text_color=TEXT_PRIMARY
        )

        app_title.pack(
            anchor="w",
            padx=30,
            pady=(25,0)
        )


        app_frame = ctk.CTkFrame(
            self,
            fg_color=BG_CARD,
            corner_radius=15
        )

        app_frame.pack(
            fill="x",
            padx=30,
            pady=15
        )


        info = [
            ("Application Name", "EDU.O"),
            ("Version", "1.0.0"),
            ("Developer", "M HASEEB"),
            ("Technology", "Python + CustomTkinter")
        ]


        for label,value in info:

            row = ctk.CTkFrame(
                app_frame,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=20,
                pady=8
            )


            ctk.CTkLabel(
                row,
                text=label,
                font=("Segoe UI",14),
                text_color=TEXT_MUTED
            ).pack(
                side="left"
            )


            ctk.CTkLabel(
                row,
                text=value,
                font=("Segoe UI",14,"bold"),
                text_color=TEXT_PRIMARY
            ).pack(
                side="right"
            )



    def create_setting_row(
            self,
            parent,
            text,
            button_text,
            command
        ):

        row = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        row.pack(
            fill="x",
            padx=20,
            pady=12
        )


        ctk.CTkLabel(
            row,
            text=text,
            font=("Segoe UI",15)
        ).pack(
            side="left"
        )


        ctk.CTkButton(
            row,
            text=button_text,
            width=140,
            command=command
        ).pack(
            side="right"
        )



    # =========================
    # Functions
    # =========================


    def backup_data(self):

        os.makedirs(
            "backup",
            exist_ok=True
        )

        shutil.copy(
            "data/students.json",
            "backup/students_backup.json"
        )


        CTkMessagebox(
            title="Backup Complete",
            message="Student data backed up successfully!",
            icon="check"
        )



    def restore_data(self):

        backup_file = "backup/students_backup.json"

        if not os.path.exists(backup_file):

            CTkMessagebox(
                title="Error",
                message="No backup file found!",
                icon="cancel"
            )

            return


        shutil.copy(
            backup_file,
            "data/students.json"
        )


        CTkMessagebox(
            title="Restore Complete",
            message="Student data restored successfully!",
            icon="check"
        )



    def clear_database(self):

        msg = CTkMessagebox(
            title="Delete Database",
            message="Are you sure you want to delete all students?",
            icon="warning",
            option_1="Cancel",
            option_2="Delete"
        )


        if msg.get() == "Delete":

            with open(
                "data/students.json",
                "w"
            ) as file:

                file.write("[]")


            CTkMessagebox(
                title="Deleted",
                message="All student data removed!",
                icon="check"
            )