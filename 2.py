time_in_seconds = int(input('Enter time in seconds: '))
hours = time_in_seconds // 3600
rest = time_in_seconds - hours * 3600
minutes = rest // 60
seconds = rest - minutes * 60
if len(str(hours)) == 1:
    hours_str = '0{}'.format(hours)
else:
    hours_str = str(hours)

if len(str(minutes)) == 1:
    minutes_str = '0{}'.format(minutes)
else:
    minutes_str = str(minutes)

if len(str(seconds)) == 1:
    seconds_str = '0{}'.format(seconds)
else:
    seconds_str = str(seconds)

print("Your time in hours, minutes and seconds: {}:{}:{}".format(hours_str, minutes_str, seconds_str))