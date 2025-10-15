from datetime import date, datetime

def get_days_from_today(date):
    return (date.today() - date).days

while True:
    try:
        user_date = datetime.strptime(input("Enter a date (YYYY-MM-DD): "), "%Y-%m-%d").date()
        break
    except ValueError:
        print("Invalid date format. Please try again.")

days_from_today = get_days_from_today(user_date)
print(f"Days from today: {days_from_today}")