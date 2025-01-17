from typing import List, Optional
from datetime import datetime, timedelta

# ============================================
#               CLASS DEFINITIONS
# ============================================

class Appointment:
    """
    An appointment has:
      - A patient
      - A doctor
      - A start datetime
      - An optional duration (in minutes)
      - Notes & prescriptions
    """
    def __init__(
        self,
        patient: "Patient",
        doctor: "Doctor",
        start_time: datetime,
        duration_minutes: int = 30,
        notes: str = ""
    ) -> None:
        self.patient = patient
        self.doctor = doctor
        self.start_time = start_time
        self.duration_minutes = duration_minutes
        self.end_time = start_time + timedelta(minutes=duration_minutes)
        self.notes = notes
        self.prescriptions: List[str] = []

    def __str__(self) -> str:
        return (f"Appointment:\n"
                f"  Doctor: {self.doctor.name} ({self.doctor.specialty})\n"
                f"  Patient: {self.patient.name}, Age: {self.patient.age}\n"
                f"  Start: {self.start_time.strftime('%Y-%m-%d %H:%M')}\n"
                f"  End:   {self.end_time.strftime('%Y-%m-%d %H:%M')}\n"
                f"  Notes: {self.notes}\n"
                f"  Prescriptions: {', '.join(self.prescriptions) if self.prescriptions else 'None'}")

    def __repr__(self) -> str:
        return self.__str__()

    def overlaps_with(self, other: "Appointment") -> bool:
        """
        Checks if this appointment’s time overlaps with another appointment.
        Overlap occurs if any part of this appointment is within another’s start-end range.
        """
        return not (self.end_time <= other.start_time or self.start_time >= other.end_time)

    def set_notes(self, new_notes: str) -> None:
        self.notes = new_notes

    def add_prescription(self, prescription: str) -> None:
        self.prescriptions.append(prescription)

    def remove_prescription(self, prescription: str) -> bool:
        if prescription in self.prescriptions:
            self.prescriptions.remove(prescription)
            return True
        return False


class Doctor:
    """
    A doctor has:
      - A name
      - A specialty
      - A list of appointments
    """
    def __init__(self, name: str, specialty: str) -> None:
        self.name = name
        self.specialty = specialty
        self.appointments: List[Appointment] = []

    def __str__(self) -> str:
        return f"Doctor: {self.name}, Specialty: {self.specialty}"

    def __repr__(self) -> str:
        return self.__str__()

    def schedule_appointment(self, appointment: Appointment) -> bool:
        """
        Schedules a new appointment if it does not overlap with existing ones.
        Returns True if successful, False otherwise.
        """
        for existing in self.appointments:
            if existing.overlaps_with(appointment):
                return False  # Overlap detected
        self.appointments.append(appointment)
        return True

    def cancel_appointment(self, appointment: Appointment) -> bool:
        """Cancels a specific appointment for the doctor."""
        if appointment in self.appointments:
            self.appointments.remove(appointment)
            return True
        return False

    def find_appointment(self, appointment: Appointment) -> bool:
        return appointment in self.appointments

    def get_appointments(self) -> List[Appointment]:
        return self.appointments


class MedicalRecord:
    """
    Represents a single medical record entry for a patient.
    Example of usage:
      - record_date
      - diagnosis
      - treatment
    """
    def __init__(self, record_date: datetime, diagnosis: str, treatment: str):
        self.record_date = record_date
        self.diagnosis = diagnosis
        self.treatment = treatment

    def __str__(self) -> str:
        return (f"Medical Record:\n"
                f"  Date: {self.record_date.strftime('%Y-%m-%d')}\n"
                f"  Diagnosis: {self.diagnosis}\n"
                f"  Treatment: {self.treatment}")


class Patient:
    """
    A patient has:
      - A name
      - An age
      - A list of appointments
      - A list of MedicalRecord entries
    """
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.appointments: List[Appointment] = []
        self.records: List[MedicalRecord] = []

    def __str__(self) -> str:
        return f"Patient: {self.name}, Age: {self.age}"

    def __repr__(self) -> str:
        return self.__str__()

    def add_record(self, record: MedicalRecord) -> None:
        self.records.append(record)

    def get_records(self) -> List[MedicalRecord]:
        return self.records


class AppointmentManager:
    """
    Provides static methods for searching/filtering appointments from a list.
    """
    @staticmethod
    def find_by_date(appointments: List[Appointment], date_str: str) -> List[Appointment]:
        """
        Finds all appointments on a specific date (YYYY-MM-DD).
        """
        results = []
        for appt in appointments:
            if appt.start_time.strftime('%Y-%m-%d') == date_str:
                results.append(appt)
        return results

    @staticmethod
    def find_by_date_range(
        appointments: List[Appointment],
        start_date: datetime,
        end_date: datetime
    ) -> List[Appointment]:
        """
        Finds all appointments within a date range, inclusive.
        """
        results = []
        for appt in appointments:
            if start_date <= appt.start_time <= end_date:
                results.append(appt)
        return results

    @staticmethod
    def find_by_patient_name(appointments: List[Appointment], patient_name: str) -> List[Appointment]:
        """
        Returns all appointments for a given patient name (case-insensitive).
        """
        return [
            appt for appt in appointments
            if appt.patient.name.lower() == patient_name.lower()
        ]

    @staticmethod
    def find_by_doctor_name(appointments: List[Appointment], doctor_name: str) -> List[Appointment]:
        """
        Returns all appointments for a given doctor name (case-insensitive).
        """
        return [
            appt for appt in appointments
            if appt.doctor.name.lower() == doctor_name.lower()
        ]

# ============================================
#        HELPER FUNCTIONS
# ============================================

def parse_datetime(date_str: str, time_str: str) -> datetime:
    """
    Given date_str in 'YYYY-MM-DD' and time_str in 'HH:MM' or 'HH:MM AM/PM',
    returns a datetime object or raises ValueError if invalid.
    """
    # Try different formats
    dt_str_24 = date_str + " " + time_str
    # Common attempts:
    fmts = [
        "%Y-%m-%d %H:%M",    # 24-hour format
        "%Y-%m-%d %I:%M %p"  # 12-hour format with AM/PM
    ]
    for f in fmts:
        try:
            return datetime.strptime(dt_str_24, f)
        except ValueError:
            pass
    raise ValueError("Invalid date/time format. Please use 'YYYY-MM-DD HH:MM' or 'YYYY-MM-DD HH:MM AM/PM'.")


def gather_all_appointments(doctors: List[Doctor]) -> List[Appointment]:
    """Returns a flat list of all appointments across all doctors."""
    all_appts = []
    for doc in doctors:
        all_appts.extend(doc.get_appointments())
    return all_appts


# ============================================
#        MAIN PROGRAM WITH MENU
# ============================================

def main():
    doctors = {}   # key: doctor name (case-sensitive?), value: Doctor object
    patients = {}  # key: patient name,                  value: Patient object

    while True:
        print("\n====== Hospital Management System ======")
        print("1. Register a Doctor")
        print("2. Register a Patient")
        print("3. Add Medical Record to a Patient")
        print("4. Schedule an Appointment (with collision check)")
        print("5. Edit an Existing Appointment")
        print("6. Cancel an Appointment")
        print("7. Add/Remove Prescriptions or Notes in an Appointment")
        print("8. Search Appointments by Date or Range or Names")
        print("9. View Patient’s Medical Records")
        print("10. View a Doctor’s Appointments")
        print("11. View a Patient’s Appointments")
        print("12. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Register a Doctor
            doc_name = input("Enter Doctor's Name: ").strip()
            specialty = input("Enter Doctor's Specialty: ").strip()
            if doc_name in doctors:
                print("A doctor with this name already exists.")
            else:
                doctors[doc_name] = Doctor(doc_name, specialty)
                print(f"Doctor '{doc_name}' (Specialty: {specialty}) registered.")

        elif choice == "2":
            # Register a Patient
            pat_name = input("Enter Patient's Name: ").strip()
            age_str = input("Enter Patient's Age: ").strip()
            try:
                age = int(age_str)
            except ValueError:
                print("Invalid age. Defaulting to 0.")
                age = 0
            if pat_name in patients:
                print("A patient with this name already exists.")
            else:
                patients[pat_name] = Patient(pat_name, age)
                print(f"Patient '{pat_name}' (Age: {age}) registered.")

        elif choice == "3":
            # Add Medical Record
            pat_name = input("Enter Patient's Name: ").strip()
            patient_obj = patients.get(pat_name)
            if not patient_obj:
                print(f"No patient found with name '{pat_name}'.")
                continue
            diagnosis = input("Enter Diagnosis: ").strip()
            treatment = input("Enter Treatment: ").strip()
            record_date_str = input("Enter Record Date (YYYY-MM-DD) [Leave blank for today]: ").strip()
            if not record_date_str:
                record_date = datetime.now()
            else:
                try:
                    record_date = datetime.strptime(record_date_str, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Using today's date.")
                    record_date = datetime.now()
            new_record = MedicalRecord(record_date, diagnosis, treatment)
            patient_obj.add_record(new_record)
            print(f"Medical record added for {pat_name}.")

        elif choice == "4":
            # Schedule an Appointment
            doc_name = input("Enter Doctor's Name: ").strip()
            doctor_obj = doctors.get(doc_name)
            if not doctor_obj:
                print(f"No doctor found with name '{doc_name}'.")
                continue

            pat_name = input("Enter Patient's Name: ").strip()
            patient_obj = patients.get(pat_name)
            if not patient_obj:
                print(f"No patient found with name '{pat_name}'.")
                continue

            date_str = input("Enter Appointment Date (YYYY-MM-DD): ").strip()
            time_str = input("Enter Appointment Time (HH:MM or HH:MM AM/PM): ").strip()
            dur_str = input("Enter Duration (minutes) [Default: 30]: ").strip()
            if not dur_str:
                duration = 30
            else:
                try:
                    duration = int(dur_str)
                except ValueError:
                    print("Invalid duration. Using 30 minutes by default.")
                    duration = 30

            # Parse date/time
            try:
                start_dt = parse_datetime(date_str, time_str)
            except ValueError as ve:
                print("Error parsing date/time:", ve)
                continue

            # Create and schedule the appointment
            new_appt = Appointment(
                patient=patient_obj,
                doctor=doctor_obj,
                start_time=start_dt,
                duration_minutes=duration
            )
            success = doctor_obj.schedule_appointment(new_appt)
            if success:
                patient_obj.appointments.append(new_appt)
                print("Appointment scheduled successfully!")
                print(new_appt)
            else:
                print("Failed to schedule appointment: time conflict with existing appointment.")

        elif choice == "5":
            # Edit an Existing Appointment (change date/time)
            doc_name = input("Enter Doctor's Name for the Appointment: ").strip()
            doctor_obj = doctors.get(doc_name)
            if not doctor_obj:
                print(f"No doctor found with name '{doc_name}'.")
                continue

            # List doctor's appointments
            doc_appts = doctor_obj.get_appointments()
            if not doc_appts:
                print("No appointments to edit for this doctor.")
                continue
            for i, appt in enumerate(doc_appts, start=1):
                print(f"{i}. {appt}")

            idx_str = input("Select the appointment number to edit: ").strip()
            try:
                idx = int(idx_str)
                if not (1 <= idx <= len(doc_appts)):
                    print("Invalid selection.")
                    continue
                appt_to_edit = doc_appts[idx - 1]
            except ValueError:
                print("Invalid input.")
                continue

            # Prompt for new date/time/duration
            date_str = input("Enter new Date (YYYY-MM-DD) [leave blank to keep current]: ").strip()
            time_str = input("Enter new Time (HH:MM or HH:MM AM/PM) [leave blank to keep current]: ").strip()
            dur_str = input("Enter new Duration (minutes) [leave blank to keep current]: ").strip()

            new_date = appt_to_edit.start_time.strftime("%Y-%m-%d")
            new_time = appt_to_edit.start_time.strftime("%H:%M")  # 24h fallback
            new_duration = appt_to_edit.duration_minutes

            if date_str:
                new_date = date_str
            if time_str:
                new_time = time_str
            if dur_str:
                try:
                    new_duration = int(dur_str)
                except ValueError:
                    print("Invalid duration. Keeping old duration.")

            # Create a temporary new appointment object to test collisions
            try:
                edited_start = parse_datetime(new_date, new_time)
            except ValueError as ve:
                print("Error parsing new date/time:", ve)
                continue

            # Temporarily remove the old appointment from the doc’s list
            doctor_obj.appointments.remove(appt_to_edit)

            test_appointment = Appointment(
                patient=appt_to_edit.patient,
                doctor=appt_to_edit.doctor,
                start_time=edited_start,
                duration_minutes=new_duration,
                notes=appt_to_edit.notes
            )
            test_appointment.prescriptions = appt_to_edit.prescriptions[:]  # copy prescriptions

            # Attempt to reschedule
            if doctor_obj.schedule_appointment(test_appointment):
                # Also update patient’s appointment list
                # Remove old from patient
                appt_to_edit.patient.appointments.remove(appt_to_edit)
                appt_to_edit.patient.appointments.append(test_appointment)
                print("Appointment updated successfully!")
            else:
                # Restore old appointment (collision)
                doctor_obj.appointments.append(appt_to_edit)
                print("Failed to update: time conflict with existing appointment.")

        elif choice == "6":
            # Cancel an Appointment
            doc_name = input("Enter Doctor's Name: ").strip()
            doctor_obj = doctors.get(doc_name)
            if not doctor_obj:
                print(f"No doctor found with name '{doc_name}'.")
                continue

            doc_appts = doctor_obj.get_appointments()
            if not doc_appts:
                print("No appointments to cancel for this doctor.")
                continue

            for i, appt in enumerate(doc_appts, start=1):
                print(f"{i}. {appt}")

            idx_str = input("Select the appointment number to cancel: ").strip()
            try:
                idx = int(idx_str)
                if not (1 <= idx <= len(doc_appts)):
                    print("Invalid selection.")
                    continue
                appt_to_cancel = doc_appts[idx - 1]
            except ValueError:
                print("Invalid input.")
                continue

            cancelled = doctor_obj.cancel_appointment(appt_to_cancel)
            if cancelled:
                # Also remove from patient's list
                appt_to_cancel.patient.appointments.remove(appt_to_cancel)
                print("Appointment canceled successfully.")
            else:
                print("Failed to cancel the appointment.")

        elif choice == "7":
            # Add/Remove Prescriptions or Update Notes
            doc_name = input("Enter Doctor's Name: ").strip()
            doctor_obj = doctors.get(doc_name)
            if not doctor_obj:
                print(f"No doctor found with name '{doc_name}'.")
                continue

            doc_appts = doctor_obj.get_appointments()
            if not doc_appts:
                print("No appointments for this doctor.")
                continue

            for i, appt in enumerate(doc_appts, start=1):
                print(f"{i}. {appt}")

            idx_str = input("Select an appointment number: ").strip()
            try:
                idx = int(idx_str)
                if not (1 <= idx <= len(doc_appts)):
                    print("Invalid selection.")
                    continue
                chosen_appt = doc_appts[idx - 1]
            except ValueError:
                print("Invalid input.")
                continue

            print("\n1. Add a prescription")
            print("2. Remove a prescription")
            print("3. Update notes")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                prescription = input("Enter prescription details: ")
                chosen_appt.add_prescription(prescription)
                print("Prescription added.")
            elif sub_choice == "2":
                if not chosen_appt.prescriptions:
                    print("No prescriptions to remove.")
                else:
                    print("Current Prescriptions:")
                    for i, p in enumerate(chosen_appt.prescriptions, start=1):
                        print(f"{i}. {p}")
                    idx_p_str = input("Select a prescription to remove: ").strip()
                    try:
                        idx_p = int(idx_p_str)
                        if not (1 <= idx_p <= len(chosen_appt.prescriptions)):
                            print("Invalid selection.")
                            continue
                        remove_item = chosen_appt.prescriptions[idx_p - 1]
                        chosen_appt.remove_prescription(remove_item)
                        print("Prescription removed.")
                    except ValueError:
                        print("Invalid input.")
            elif sub_choice == "3":
                new_notes = input("Enter new notes: ")
                chosen_appt.set_notes(new_notes)
                print("Notes updated.")
            else:
                print("Invalid choice.")

        elif choice == "8":
            # Search Appointments
            print("\n--- Search Menu ---")
            print("1. By Exact Date (YYYY-MM-DD)")
            print("2. By Date Range (start YYYY-MM-DD, end YYYY-MM-DD)")
            print("3. By Patient Name")
            print("4. By Doctor Name")

            sub_choice = input("Enter your choice: ").strip()
            # Gather all appointments
            all_appts = gather_all_appointments(list(doctors.values()))

            if sub_choice == "1":
                date_str = input("Enter date (YYYY-MM-DD): ").strip()
                results = AppointmentManager.find_by_date(all_appts, date_str)
                if results:
                    print(f"Appointments on {date_str}:")
                    for ap in results:
                        print(" -", ap)
                else:
                    print("No appointments found on that date.")

            elif sub_choice == "2":
                start_str = input("Enter start date (YYYY-MM-DD): ").strip()
                end_str = input("Enter end date (YYYY-MM-DD): ").strip()
                try:
                    start_dt = datetime.strptime(start_str, "%Y-%m-%d")
                    end_dt = datetime.strptime(end_str, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format.")
                    continue
                if end_dt < start_dt:
                    print("End date cannot be before start date.")
                    continue
                results = AppointmentManager.find_by_date_range(all_appts, start_dt, end_dt + timedelta(days=1) - timedelta(seconds=1))
                if results:
                    print(f"Appointments between {start_str} and {end_str}:")
                    for ap in results:
                        print(" -", ap)
                else:
                    print("No appointments found in that date range.")

            elif sub_choice == "3":
                pat_name = input("Enter Patient Name: ").strip()
                results = AppointmentManager.find_by_patient_name(all_appts, pat_name)
                if results:
                    print(f"Appointments for {pat_name}:")
                    for ap in results:
                        print(" -", ap)
                else:
                    print(f"No appointments found for patient '{pat_name}'.")

            elif sub_choice == "4":
                doc_name2 = input("Enter Doctor Name: ").strip()
                results = AppointmentManager.find_by_doctor_name(all_appts, doc_name2)
                if results:
                    print(f"Appointments for Dr. {doc_name2}:")
                    for ap in results:
                        print(" -", ap)
                else:
                    print(f"No appointments found for doctor '{doc_name2}'.")
            else:
                print("Invalid choice.")

        elif choice == "9":
            # View Patient's Medical Records
            pat_name = input("Enter Patient's Name: ").strip()
            patient_obj = patients.get(pat_name)
            if not patient_obj:
                print(f"No patient found with name '{pat_name}'.")
                continue

            records = patient_obj.get_records()
            if not records:
                print("No medical records found for this patient.")
            else:
                print(f"Medical Records for {pat_name}:")
                for r in records:
                    print(" -", r)

        elif choice == "10":
            # View Doctor's Appointments
            doc_name = input("Enter Doctor's Name: ").strip()
            doctor_obj = doctors.get(doc_name)
            if not doctor_obj:
                print(f"No doctor found with name '{doc_name}'.")
                continue
            doc_appts = doctor_obj.get_appointments()
            if not doc_appts:
                print("No appointments found for this doctor.")
            else:
                print(f"Appointments for Dr. {doc_name}:")
                for ap in doc_appts:
                    print(" -", ap)

        elif choice == "11":
            # View a Patient’s Appointments
            pat_name = input("Enter Patient's Name: ").strip()
            patient_obj = patients.get(pat_name)
            if not patient_obj:
                print(f"No patient found with name '{pat_name}'.")
                continue
            pat_appts = patient_obj.appointments
            if not pat_appts:
                print("No appointments found for this patient.")
            else:
                print(f"Appointments for {pat_name}:")
                for ap in pat_appts:
                    print(" -", ap)

        elif choice == "12":
            print("Exiting the Advanced Hospital Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()