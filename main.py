def add_time(start, duration, starting_day=None):
    # Split the start time into components
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Split the duration into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Convert start time to 24-hour format for easier calculation
    if period == 'PM':
        start_hour += 12
    if start_hour == 12 and period == 'AM':
        start_hour = 0
    
    # Calculate the new time
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + end_minute // 60
    end_minute %= 60
    end_day = end_hour // 24
    end_hour %= 24
    
    # Convert back to 12-hour format
    if end_hour == 0:
        end_hour_12 = 12
        end_period = 'AM'
    elif end_hour < 12:
        end_hour_12 = end_hour
        end_period = 'AM'
    elif end_hour == 12:
        end_hour_12 = 12
        end_period = 'PM'
    else:
        end_hour_12 = end_hour - 12
        end_period = 'PM'
    
    # Calculate the new day of the week if starting_day is provided
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        end_day_index = (starting_day_index + end_day) % 7
        new_day = days_of_week[end_day_index]
    else:
        new_day = None
    
    # Format the result
    new_time = f"{end_hour_12}:{end_minute:02d} {end_period}"
    if new_day:
        new_time += f", {new_day}"
    if end_day == 1:
        new_time += " (next day)"
    elif end_day > 1:
        new_time += f" ({end_day} days later)"
    
    return new_time

# Test cases
print(add_time('3:00 PM', '3:10'))  # Returns: 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # Returns: 2:02 PM, Monday
print(add_time('11:43 AM', '00:20'))  # Returns: 12:03 PM
print(add_time('10:10 PM', '3:30'))  # Returns: 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))  # Returns: 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))  # Returns: 7:42 AM (9 days later)