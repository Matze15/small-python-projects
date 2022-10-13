import ics

# this calendar is created to make it easy to create a plan for all day meetings which can
# then be exported as an ics. I personally wrote it to easy convert my training plan into
# something i can import in my google calendar.

#only right inputs, too lazy for else
def get_start_date():
    print('Start range date')
    start_day = input('Day (01-31): ')
    start_month = input('Month (01-12): ')
    start_year = int(input('Year: '))

    return {'day': start_day, 'month': start_month, 'year' : start_year, 'total': int(f'{start_year}{start_month}{start_day}'), 'format':f'{start_year}-{start_month}-{start_day}'}

def get_end_date():
    print('End range date')
    end_day = input('Day (01-31): ')
    end_month = input('Month (01-12): ')
    end_year = int(input('Year: '))

    return {'day': end_day, 'month': end_month, 'year': end_year, 'total': int(f'{end_year}{end_month}{end_day}'), 'format': f'{end_year}-{end_month}-{end_day}'}

months = [31,28,31,30,31,30,31,31,30,31,30,31]
#workaround
months_ct = ['00','01','02','03','04','05','06','07','08','09','10','11','12']
days_ct = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']


#ask user and set
start_date = get_start_date()
end_date = get_end_date()

# # test
# print(start_date)
# print(end_date)

latest_date = start_date

# ziel: [2022-10-17,2022-10-18.......2023-03-12]
date_list = [start_date['format']]

def calc_next_date(current_date):
    cd = current_date
    new_date = {'year' : None, 'month' : None, 'day': None, 'total': None, 'format': None}
    # current_date = {'year'....}
    # 2022-10-18
    # return: {'year'....} oder false
    if int(current_date['day']) == months[int(current_date['month'])-1]:
        if int(current_date['month']) == 12:
            new_date = {'year' : cd['year']+1, 'month' : '01', 'day': '01', 'total': int(f"{cd['year']+1}0101"), 'format': f"{cd['year']+1}-01-01"}
        else:
            new_date = {'year' : cd['year'], 'month' : months_ct[int(cd['month'])+1], 'day': '01', 'total': int(f"{cd['year']}{months_ct[int(cd['month'])+1]}01"), 'format': f"{cd['year']}-{months_ct[int(cd['month'])+1]}-01"}
    else:
        new_date = {'year':cd['year'], 'month': cd['month'], 'day': days_ct[int(cd['day'])+1], 'total': int(f"{cd['year']}{cd['month']}{days_ct[int(cd['day'])+1]}"), 'format': f"{cd['year']}-{cd['month']}-{days_ct[int(cd['day'])+1]}" }

    latest_date = new_date
    return new_date


# list mit allen daten erstellen
while latest_date['total'] < end_date['total']:
    latest_date = calc_next_date(latest_date)
    date_list.append(latest_date['format'])

event_list = []

for i in range(len(date_list)):
    apt_name = input(f"Ereignis am {date_list[i]}: ")
    if apt_name:
        event_list.append({'date':date_list[i],'name':apt_name})

# by now all data pairs are created/collected and need to go by the ics.py syntax to then be written to a file
#create new calendar
c = ics.Calendar()
# join all events to the calendar
for event in event_list:
    e = ics.Event(event)
    e.name = event['name']
    e.begin = event['date']
    c.events.add(e)

# write to file
with open('calendar.ics', 'w') as f:
    # .replace to make it an all day appt
    f.writelines(c.serialize().replace('DTSTART:','DTSTART;VALUE=DATE:').replace('T000000Z',''))



# test_calendar = ics.Calendar()
# test_event = ics.Event()
# test_event.name = 'Test event'
# test_event.begin = '2022-10-17'
# test_calendar.events.add(test_event)
# print(test_calendar.serialize())