# Author: Israel Colman
# 11/12/2026

current_hour = int(input('Enter current hour 0-23: '))

#if current_hour in range(5,10):
    #print(f'Good Morning!')
#elif current_hour in range(10, 18):
    #print(f'Good day!')
#elif current_hour > 17:
    #print(f'Good evening!')
#elif current_hour < 0 or current_hour > 23:
    #print(f'Invalid hour')


# rewriten version to account for "what are you doing up so late??"
if current_hour in range(0, 5):
    print("What are you doing up so late??")
elif current_hour in range(5, 10):
    print("Good Morning!")
elif current_hour in range(10, 17):
    print("Good day!")
elif current_hour in range(17, 23):
    print("Good evening!")
elif current_hour in range(23, 24):
    print("What are you doing up so late??")
elif current_hour < 0 or current_hour > 23:
    print("Invalid hour")
