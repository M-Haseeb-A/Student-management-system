import customtkinter as ctk
from storage.json_storage import add_student,update_student
from CTkMessagebox import CTkMessagebox


class AddStudentPage(ctk.CTkFrame):
    def __init__(self, parent,controller):
        super().__init__(parent)
       
        self.controller = controller
        self.editing_student = None
        self.edit_mode = False
        self.current_student_id = None

        self.configure(fg_color="#191420")

        # Configure grid
        self.grid_columnconfigure(0, weight=1)

        # Page Title
        title = ctk.CTkLabel(
            self,
            text="Add Student",
            font=("Segoe UI", 28, "bold")
        )
        title.grid(row=0, column=0, pady=(20, 30))

        # Form Frame
        form_frame = ctk.CTkFrame(self,fg_color="#1e1a27")
        form_frame.grid(row=1, column=0, padx=20, pady=10)

        # Name
        name_label = ctk.CTkLabel(form_frame, text="Name")
        name_label.grid(row=0, column=0, sticky="w", padx=20, pady=(20, 5))

        self.name_entry = ctk.CTkEntry(form_frame, width=300)
        self.name_entry.grid(row=1, column=0, padx=20, pady=(0, 15))

        # ID
        id_label = ctk.CTkLabel(form_frame, text="Id")
        id_label.grid(row=2, column=0, sticky="w", padx=20, pady=(0, 5))

        self.id_entry = ctk.CTkEntry(form_frame, width=300)
        self.id_entry.grid(row=3, column=0, padx=20, pady=(0, 15))

        # Age
        age_label = ctk.CTkLabel(form_frame, text="Age")
        age_label.grid(row=4, column=0, sticky="w", padx=20, pady=(0, 5))

        self.age_entry = ctk.CTkEntry(form_frame, width=300)
        self.age_entry.grid(row=5, column=0, padx=20, pady=(0, 15))

        # Class
        class_label = ctk.CTkLabel(form_frame, text="Class")
        class_label.grid(row=6, column=0, sticky="w", padx=20, pady=(0, 5))

        self.class_entry = ctk.CTkEntry(form_frame, width=300)
        self.class_entry.grid(row=7, column=0, padx=20, pady=(0, 15))

        # Phone
        phone_label = ctk.CTkLabel(form_frame, text="Phone")
        phone_label.grid(row=8, column=0, sticky="w", padx=20, pady=(0, 5))

        self.phone_entry = ctk.CTkEntry(form_frame, width=300)
        self.phone_entry.grid(row=9, column=0, padx=20, pady=(0, 20))

        # Save Button
        self.save_button = ctk.CTkButton(
            form_frame,
            text="Save Student",
            width=300,
            command=self.save_student
            )

        self.save_button.grid(row=10, column=0, padx=20, pady=(0, 20))


    def save_student(self):
        name = self.name_entry.get()
        student_id = self.id_entry.get()
        age = self.age_entry.get()
        student_class = self.class_entry.get()
        phone = self.phone_entry.get()

        if not name or not student_id or not age or not student_class or not phone:
            CTkMessagebox(
                title='Error',
                message='Please fill in all fields.',
                icon='cancel'
            )
            return

        student = {
            'name': name,
            'id': student_id,
            'age': age,
            'class': student_class,
            'phone': phone
        }
          
        if self.edit_mode:

            if update_student(self.current_student_id, student):
                CTkMessagebox(
                    title="Success",
                    message="Student updated successfully!",
                    icon="check"
                )

                self.clear_form()

            else:
                CTkMessagebox(
                    title="Error",
                    message="Student could not be updated.",
                    icon="cancel"
                )

        else:

            if add_student(student):
                CTkMessagebox(
                    title="Success",
                    message="Student saved successfully!",
                    icon="check"
                )

                self.clear_form()

            else:
                CTkMessagebox(
                    title="Duplicate ID",
                    message="A student with this ID already exists!",
                    icon="warning"
                )


    def load_student(self, student):
        self.edit_mode = True
        self.current_student_id = student["id"]

        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, student["name"])

        self.id_entry.delete(0, "end")
        self.id_entry.insert(0, student["id"])

        self.age_entry.delete(0, "end")
        self.age_entry.insert(0, student["age"])

        self.class_entry.delete(0, "end")
        self.class_entry.insert(0, student["class"])

        self.phone_entry.delete(0, "end")
        self.phone_entry.insert(0, student["phone"])

        # Don't allow changing the ID while editing
        self.id_entry.configure(state="disabled")

        self.save_button.configure(text="Update Student")


    def clear_form(self):
        self.name_entry.delete(0, "end")
        self.id_entry.configure(state="normal")
        self.id_entry.delete(0, "end")
        self.age_entry.delete(0, "end")
        self.class_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")

        self.edit_mode = False
        self.current_student_id = None

        self.save_button.configure(text="Save Student")