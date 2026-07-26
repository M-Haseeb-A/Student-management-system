import customtkinter as ctk
from storage.json_storage import load_students, delete_student
from ui.pages.add_student_page import AddStudentPage
from CTkMessagebox import CTkMessagebox


class ViewStudentsPage(ctk.CTkFrame):
    def __init__(self, parent,controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(fg_color="#191420")

        title = ctk.CTkLabel(
            self,
            text="View Students",
            font=("Segoe UI", 24, "bold")
        )
        title.pack(pady=20)

        refresh_btn = ctk.CTkButton(
            self,
            text="Refresh",
            command=self.display_students
        )
        refresh_btn.pack(pady=10)

        search_frame = ctk.CTkFrame(self)
        search_frame.pack(pady=10)

        self.search_entry = ctk.CTkEntry(
            search_frame,
            width=250,
            placeholder_text="Search by ID or Name"
        )
        self.search_entry.pack(side="left", padx=5)

        search_btn = ctk.CTkButton(
            search_frame,
            text="Search",
            command=self.search_students
        )
        search_btn.pack(side="left", padx=5)

        clear_btn = ctk.CTkButton(
            search_frame,
            text="Clear",
            command=self.clear_search
        )
        clear_btn.pack(side="left", padx=5)

        # Scrollable table
        
        self.table = ctk.CTkScrollableFrame(self,fg_color="#1e1a27")
        self.table.pack(fill="both", expand=True, padx=20, pady=10)

        self.display_students()

    def display_students(self, students=None):
        # Remove old widgets
        for widget in self.table.winfo_children():
            widget.destroy()

        headers = ["ID", "Name", "Age", "Class", "Phone", "Edit", "Delete"]

        for col, header in enumerate(headers):
            ctk.CTkLabel(
                self.table,
                text=header,
                font=("Segoe UI", 14, "bold"),
                width=120
            ).grid(row=0, column=col, padx=5, pady=8)

        if students is None:
            students = load_students()

        for row, student in enumerate(students, start=1):

            ctk.CTkLabel(self.table, text=student["id"], width=120).grid(row=row, column=0)
            ctk.CTkLabel(self.table, text=student["name"], width=120).grid(row=row, column=1)
            ctk.CTkLabel(self.table, text=student["age"], width=120).grid(row=row, column=2)
            ctk.CTkLabel(self.table, text=student["class"], width=120).grid(row=row, column=3)
            ctk.CTkLabel(self.table, text=student["phone"], width=120).grid(row=row, column=4)

            edit_btn = ctk.CTkButton(
                self.table,
                text="Edit",
                width=80,
                command=lambda s=student: self.edit_student(s)
            )

            edit_btn.grid(row=row, column=5, padx=5, pady=5)


            delete_btn = ctk.CTkButton(
                self.table,
                text="Delete",
                width=80,
                fg_color="red",
                command=lambda sid=student["id"]: self.delete_student(sid)
            )

            delete_btn.grid(row=row, column=6, padx=5, pady=5)


    def delete_student(self, student_id):

        msg = CTkMessagebox(
            title="Delete Student",
            message="Are you sure you want to delete this student?",
            icon="warning",
            option_1="No",
            option_2="Yes"
        )

        response = msg.get()

        if response == "Yes":
            delete_student(student_id)
            self.display_students()

            CTkMessagebox(
                title="Success",
                message="Student deleted successfully!",
                icon="check"
            )

    def edit_student(self, student):

        add_page = self.controller.pages[AddStudentPage]
        add_page.load_student(student)
        self.controller.show_page(AddStudentPage)


    def search_students(self):

        search_text = self.search_entry.get().strip().lower()

        students = load_students()

        filtered_students = []

        for student in students:

            name = str(student.get("name", "")).lower()
            student_id = str(student.get("id", "")).lower()

            if search_text in name or search_text in student_id:
                filtered_students.append(student)

        self.display_students(filtered_students)

    def clear_search(self):

        self.search_entry.delete(0, "end")

        self.display_students()