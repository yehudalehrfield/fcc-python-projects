import re

HOURS_RE = '\d+(?=:)'
MINS_RE = '(?<=:)\d{2}'
TIME_RE = '\d{1,2}:\d{2}'
TIME_FORMAT_RE = '\d{1,2}:\d{2}\s?(AM|PM)'

daysOfTheWeek = [
  'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'
]


def add_time(start, duration, day=None):
  # get hours and minutes from start time
  startVals = getHoursMins(convertToArmy(start))
  # assign day zero to initial
  startVals.append(0)
  if day is not None: startVals.append(daysOfTheWeek.index(day.lower()))

  # get hours and minutes from duration time
  durationVals = getHoursMins(duration)

  # calculate total time and days/hours/minutes
  totalMin = startVals[1] + durationVals[1]
  totalHr = startVals[0] + durationVals[0]
  endMins = totalMin % 60
  endHours = (totalHr + (totalMin // 60)) % 24
  endDays = (totalHr + (totalMin // 60)) // 24
  endVals = [endHours, endMins, endDays]

  endDayOfWeek = '' if day is None else ', ' + daysOfTheWeek[
    (startVals[3] + endDays) % 7].capitalize()

  endTime = convertFromArmy(
    str(endVals[0]) + ':' +
    (str(endVals[1]) if endVals[1] >= 10 else ('0' + str(endVals[1]))))
  endDaysTranspired = '' if endDays == 0 else ' (next day)' if endDays == 1 else ' ({} days later)'.format(
    endDays)

  new_time = '{}{}{}'.format(endTime, endDayOfWeek, endDaysTranspired)

  return new_time


def convertToArmy(time):
  if not re.match(TIME_FORMAT_RE, time, re.I):
    return 'Error - Invalid Time Format'
  if int(re.findall(HOURS_RE, time)[0]) > 12:
    return 'Error: Invalid Time - Hour greater than 12'
  if int(re.findall(HOURS_RE, time)[0]) == 0:
    return 'Error: Invalid Time - Hour equal to "00"'

  if time[-2:].lower() == 'am':
    return ('00:' + re.findall(MINS_RE, time)[0]) if int(
      re.findall(HOURS_RE, time)[0]) == 12 else re.findall(TIME_RE, time)[0]
  elif time[-2:].lower() == 'pm':
    return (str((int(re.findall(HOURS_RE, time)[0]) + 12)) + ':' +
            re.findall(MINS_RE, time)[0]) if int(
              re.findall(HOURS_RE, time)[0]) != 12 else (re.findall(
                TIME_RE, time)[0])
  else:
    return 'Uncaught Error'


def convertFromArmy(time):
  if not re.findall(TIME_RE, time): return 'Error - Invalid Time Format'
  if int(re.findall(HOURS_RE, time)[0]) > 23:
    return 'Error: Invalid Time - Hour greater than 23'
  hours = int(re.findall(HOURS_RE, time)[0])
  mins = int(re.findall(MINS_RE, time)[0])
  res = ''
  if hours == 0:
    return '12' + ':' + re.findall(MINS_RE, time)[0] + ' AM'
  elif hours < 12:
    return re.findall(TIME_RE, time)[0] + ' AM'
  elif hours == 12:
    return re.findall(TIME_RE, time)[0] + ' PM'
  else:
    return str(hours % 12) + ':' + re.findall(MINS_RE, time)[0] + ' PM'


def getHoursMins(time):
  try:
    hours = int(re.findall(HOURS_RE, time)[0])
    mins = int(re.findall(MINS_RE, time)[0])
    return [hours, mins]
  except:
    return 'Unable to get time information.'
  return 'Error'


# TESTING AREA
# times = ['10:30', '14:30 PM','00:45 AM','10:30 AM','10:30PM', '1:30 AM', '1:30PM','12:30AM','12:45 PM','12:01 AM','11:59PM' ]

# for time in times:
# print(time, 'converts to', convertToArmy(time), 'with hours, mins:', getHoursMins(convertToArmy(time)))

# durations = ['00:01', '1:00', '1:30', '1:59', '24:00', '59:59', '360:00']

# for dur in durations:
#   print('Begin: 10:00 AM |', 'Duration:', dur, '\t| End:',
#         add_time('10:00 AM', dur, 'Tuesday'))

# armyTimes = ['0:30', '1:30', '12:30', '13:30', '20:30', '23:59' ]

# for time in armyTimes:
# print('Army:', time, 'converts to', convertFromArmy(time))
