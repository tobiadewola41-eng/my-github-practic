# date and time
import datetime
#from http.cookiejar import datetime
import random
#date
current_date=datetime.datetime.now().strftime("%A-%d-%B-%Y")
print(current_date)


#time
time=datetime.datetime.now().time()
print(time)


#%Y:YEAR (FOUR DIGITS)
#%M: MINUTES
#%S:SECOND
#%P:AM/PM
#%A:FULL WEEKDAY
#%a:ABBREVIATED WEEKDAY(MON-SUN)
#%B:FULL MONTHS
#%b:abbreviated month(jan-dec)
#%m:month(01-12)
#%d:day(01-31)
#%H:HOUR (24-HOUR,00-24)
#%I:HOUR(12-HOUR,01-12)





# Function to generate a random strong password
def generate_password():
    """
    Generates a random 11-character strong password.
    """
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    password = ''.join(random.choice(characters) for _ in range(11))  # Pick 11 random characters
    return password

print(generate_password())
