from datetime import datetime

def calculate_interest(value, due_date_str):
    today = datetime.today().date()
    due_date = datetime.strptime(due_date_str,"%d-%m-%Y").date()
    days_late= (today - due_date).days
    if days_late<= 0:
        return 0.0

    daily_rate= 0.025
    interest_value= value*daily_rate*days_late
    return interest_value

amount = 1000.00
due_date="20-11-2025"

interest=calculate_interest(amount, due_date)
print(f"Juros:R${interest:.2f}")
