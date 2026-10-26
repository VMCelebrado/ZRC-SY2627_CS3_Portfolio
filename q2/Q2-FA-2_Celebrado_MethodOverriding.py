class Patient:
    def __init__(self, name: str, bill_amount: float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilhealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilhealthPatient("Pedro Reyes", 15000)

patients = [regular_patient, senior_patient, philhealth_patient]

print("V's Hospital Billing System")
print("============================")

for patient in patients:
    original_bill = patient.get_bill_amount()
    final_bill = patient.calculate_bill()

    print(f"\nPatient name: {patient.get_name()}")
    print(f"Original bill: ₱{original_bill:,.2f}")
    print(f"Final Bill: ₱{final_bill:,.2f}")
