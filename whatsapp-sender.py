import pywhatkit #install pywhatkit installation method is given in README.md

phone_number = input('Please enter the phone nummber in which you want me to send the message\n>')
message_of_user = input('Hello My name is bot, what message do you want me to send\n>')
time_hour = int(input('At what hour do you want me to send the message (Please enter in 24 hour format)\n>'))
time_minutes = int(input('At what minutes do you want me to send the message\n>'))
pywhatkit.sendwhatmsg(phone_number, message_of_user, time_hour, time_minutes)
