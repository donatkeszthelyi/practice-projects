def add_time(start, duration, dayName=''):
    if 'PM' in start:
        startHour = int(start[:-6]) + 12
    else:
        startHour = int(start[:-6])
    startMinute = int(start[-5:-3])

    durationHour = int(duration[:-3])
    durationMinute = int(duration[-2:])

    days = 0

    endHour = startHour + durationHour
    if endHour > 23:
        days = endHour//24
        endHour = endHour%24

    endMinute = startMinute + durationMinute
    if endMinute > 59:
        endHour += endMinute//60
        endMinute = endMinute%60

    if endMinute < 10:
        endMinute = '0' + str(endMinute)
    else:
        endMinute = str(endMinute)

    if endHour >= 12 and endHour != 24:
        AMPM = 'PM'
        if endHour > 12:
            endHour -= 12
    elif endHour == 24:
        days += 1
        AMPM = 'AM'
        endHour -= 12
    else:
        AMPM = 'AM'
        if endHour == 0:
            endHour = 12

    endHour = str(endHour)
    
    dayNames = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    if dayName:
        dayName = dayName.lower()
        dayName = ', ' + dayNames[(dayNames.index(dayName)+days)%7].title()
    else:
        dayName = ''
    
    if days == 1:
        m = ' (next day)'
    elif days:
        m = f' ({days} days later)'
    else:
        m = ''

    new_time = endHour + ':' + endMinute + ' ' + AMPM + dayName + m
    
    return new_time
    
a = True
while a == True:
    try:
        time = input('Enter a time (HH:MM AM/PM):')
        duration = input('Enter a time to spend (HH:MM):')
        day = input('Enter the day (optional):')

        print(add_time(time, duration, day))
        a = False
    except:
        print('\nWrong input, try again!\n')
        continue

