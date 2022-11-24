date = '2020-01-01'
end_date = '2020-12-31'
max_days = 31
end_max_days = 31
date = date.split('-')
end_date = end_date.split('-')
date_year = date[0]
end_date_year = end_date[0]
date_month = date[1]
end_date_month = end_date[1]
date_day = date[2]
end_date_day = end_date[2]
date_length = len((str(date_year+date_month+date_day)))
end_date_length = len((str(end_date_year+end_date_month+end_date_day)))

if date_length < 8 or date_length > 8:
    print('Please enter using the date format yyyy-mm-dd')
    exit()

if end_date_length <8 or end_date_length > 8:
    print('Please enter using the date format yyyy-mm-dd')
    exit()

date_int = int(date_year+date_month+date_day)
end_date_int = int(end_date_year+end_date_month+end_date_day)

if date_month == '02':
    if (int(date_year) % 4 == 0):
        max_days = 29
        if int(date_day) > max_days:
            print('This is a leap year! Please enter a valid date!')
            exit()
    else:
        max_days = 28
        if int(date_day) > max_days:
            print('This is not a leap year! Please enter a valid date!')
            exit()
if date_month == '04' or date_month == '06' or date_month == '09' or date_month == '11':
    max_days = 30
    if int(date_day) > max_days:
        print('Only 30 days this month! Please enter a valid date!')
        exit()
if int(date_day) > 31:
    print('Only 31 days this month! Please enter a valid date!')
    exit()

if end_date_month == '02':
    if (int(end_date_year) % 4 == 0):
        end_max_days = 29
        if int(end_date_day) > end_max_days:
            print('This is a leap year! Please enter a valid end date!')
            exit()
    else:
        end_max_days = 28
        if int(end_date_day) > end_max_days:
            print('This is not a leap year! Please enter a valid end date!')
            exit()
if end_date_month == '04' or end_date_month == '06' or end_date_month == '09' or end_date_month == '11':
    end_max_days = 30
    if int(end_date_day) > end_max_days:
        print('Only 30 days in your end month! Please enter a valid date!')
        exit()
if int(end_date_day) > 31:
    print('Only 31 days in your end month! Please enter a valid date!')
    exit()

date_day_int = int(date_day)
date_month_int = int(date_month)
end_date_month_int = int(end_date_month)
for date in range(date_int,end_date_int+1):
    if date_day_int <= max_days:
        print(date)
        date_day_int += 1

while date_month_int < end_date_month_int:
    date_day = '01'
    date_day_int = int(date_day)
    date_month = str(date_month_int+1).zfill(2)
    date_int = int(date_year+date_month+date_day)
    if int(date_month) == 1:
        max_days = 31
    if int(date_month) == 2 and (int(date_year) % 4 == 0):
        max_days = 29
    if int(date_month) == 2:
        max_days = 28    
    if int(date_month) == 3:
        max_days = 31
    if int(date_month) == 4:
        max_days = 30
    if int(date_month) == 5:
        max_days = 31
    if int(date_month) == 6:
        max_days = 30
    if int(date_month) == 7:
        max_days = 31
    if int(date_month) == 8:
        max_days = 31
    if int(date_month) == 9:
        max_days = 30
    if int(date_month) == 10:
        max_days = 31
    if int(date_month) == 11:
        max_days = 30
    if int(date_month) == 12:
        max_days = 31    
    for date in range(date_int,end_date_int+1):
        if date_day_int <= max_days:
            print(date)
            date_day_int += 1
    date_month_int += 1
else:
    exit()