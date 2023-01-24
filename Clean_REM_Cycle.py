print("REM is approximately 90 minutes\nHow much REM you can get with your sleep schedule in a 24 hr span\n")

user_bedtime_hr = 0
user_bedtime_min = 0
while not int(user_bedtime_hr) in range(1, 13) or not int(user_bedtime_min) in range(0, 60):
    user_bedtime_hr, user_bedtime_min = input("Enter when your going to bed with two numbers:").split()
    # User enters bedtime. Repeats if hr is not (1-12) & min is not (0-59).

user_bedtime_ampm = ''
while user_bedtime_ampm.lower() not in {'am', 'pm'}:
    user_bedtime_ampm = input(f"{user_bedtime_hr} AM or PM:").lower()
    # User enters am or pm. Repeats if it's not am or pm.

user_wakeup_hr = 0
user_wakeup_min = 0
while not int(user_wakeup_hr) in range(1, 13) or not int(user_wakeup_min) in range(0, 60):
    user_wakeup_hr, user_wakeup_min = input("Enter when you would like to wakeup with two numbers:").split()
    # User enters alarm. Repeats if hr is not (1-12) & min is not (0-59).

user_wakeup_ampm = ''
while user_wakeup_ampm.lower() not in {'am', 'pm'}:
    user_wakeup_ampm = input(f"{user_wakeup_hr} AM or PM:").lower()
    # User enters am or pm. Repeats if it's not am or pm.


def pm(bedtime, wakeup):
    if (bedtime == 'pm' and wakeup == 'pm' and int(user_bedtime_hr) < int(user_wakeup_hr) or
            bedtime == 'am' and wakeup == 'am' and int(user_bedtime_hr) < int(user_wakeup_hr)):
        total_wakeup_min = (int(user_wakeup_hr) * 60) + int(user_wakeup_min)  # Converting hours to minutes and combining it with the extra wakeup minutes.
        total_bedtime_min = (int(user_bedtime_hr) * 60) + int(user_bedtime_min)  # Converting hours to minutes and combining it with the extra bedtime minutes.
        total_slept_min = int(total_wakeup_min) - int(total_bedtime_min)  # Subtracting the difference between bedtime minutes and wakeup minutes.
        rem = total_slept_min // 90  # Dividing the difference found by 90 to figure out rem cycle.
        print(f"This gives you approximately {rem} full cycles.")

    elif (bedtime == 'pm' and wakeup == 'pm' and int(user_bedtime_hr) >= int(user_wakeup_hr) or
            bedtime == 'am' and wakeup == 'am' and int(user_bedtime_hr) >= int(user_wakeup_hr)):
        if int(user_bedtime_hr) == 12:
            total_wakeup_min = (int(user_wakeup_hr) * 60) + int(user_wakeup_min)  # Converting hours to minutes and combining it with the extra wakeup minutes.
            total_bedtime_min = (0 * 60) + int(user_bedtime_min)  # Converting hours to minutes and combining it with the extra bedtime minutes.
            total_slept_min = int(total_wakeup_min) - int(total_bedtime_min)  # Subtracting the difference between bedtime minutes and wakeup minutes.
            rem = total_slept_min // 90  # Dividing the difference found by 90 to figure out rem cycle.
            print(f"This gives you approximately {rem} full cycles.")
        else:
            total_bedtime_min = (int(user_bedtime_hr) * 60) + int(user_bedtime_min)
            bedtime_plus_720 = (720 - total_bedtime_min) + 720  # Figuring out how many hours from pm to am, and adding 720 minutes because it went through entire am.
            total_wakeup_min = (int(user_wakeup_hr) * 60) + int(user_wakeup_min)  # Converting hours to minutes and combining it with the extra wakeup minutes.
            total_slept_min = int(bedtime_plus_720) + int(total_wakeup_min)  # Subtracting the difference between bedtime minutes and wakeup minutes.
            rem = total_slept_min // 90 # Dividing the difference found by 90 to figure out rem cycle.
            print(f"This gives you approximately {rem} full cycles.")

    elif (bedtime == 'pm' and wakeup == 'am' or
            bedtime == 'am' and wakeup == 'pm'):
        total_wakeup_min = (int(user_wakeup_hr) * 60) + int(user_wakeup_min)
        total_bedtime_min = (int(user_bedtime_hr) * 60) + int(user_bedtime_min)
        bedtime_minus_720 = 720 - int(total_bedtime_min)
        total_slept_min = bedtime_minus_720 + total_wakeup_min
        rem = total_slept_min // 90  # Dividing the difference found by 90 to figure out rem cycle.
        print(f"This gives you approximately {rem} full cycles.")


pm(user_bedtime_ampm, user_wakeup_ampm)
