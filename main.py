from datetime import datetime, timedelta, date
import calendar

def get_birthdays_per_week(users):
    today = date.today()
    weekdays = {day: [] for day in calendar.day_name}
    
    for user in users:
        birth_date_this_year = user['birthday'].replace(year=today.year)
        birth_date_next_year = user['birthday'].replace(year=today.year + 1)
        
        upcoming_birthdays = []
        
        if today <= birth_date_this_year <= today + timedelta(days=6):
            upcoming_birthdays.append(birth_date_this_year)
            
        if today <= birth_date_next_year <= today + timedelta(days=6):
            upcoming_birthdays.append(birth_date_next_year)
        
        for upcoming_birthday in upcoming_birthdays:
            weekday = calendar.day_name[upcoming_birthday.weekday()]
            if weekday in ['Saturday', 'Sunday']:
                weekday = 'Monday'
            weekdays[weekday].append(user['name'])
    
    return {k: v for k, v in weekdays.items() if v}


if __name__ == "__main__":
    users = [
        {"name": "Bill", "birthday": datetime(1990, 10, 5).date()},
        {"name": "Marry", "birthday": datetime(2000, 11, 12).date()},
        {"name": "Arry", "birthday": date(2000, 1, 2)},
        {"name": "Bill Gates", "birthday": date(1955, 10, 28)},
        {"name": "Liza", "birthday": date(1955, 10, 28)},
    ]

   
    result = get_birthdays_per_week(users)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")