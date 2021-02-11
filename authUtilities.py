# References:
# https://www.geeksforgeeks.org/getpass-and-getuser-in-python-password-without-echo/
# https://www.tutorialspoint.com/getpass-and-getuser-in-python-password-without-echo
# https://stackoverflow.com/questions/28579468/how-to-use-the-python-getpass-getpass-in-pycharm

from getpass import getpass, getuser
# from getpass4 import getpass

# Prompt for password and print user input
try:
    p = getpass()
    # p = getpass(prompt='Password: ')
except Exception as error:
    print('ERROR', error)
else:
    print('Password entered:', p)

# Prompt for answer to security question
pwd = getpass(prompt='What is your favorite colour? ')
if pwd == 'Blue' or pwd == 'blue':
    print('You are in!')
else:
    print('Try Again')

# Display username while prompting for password
username = getuser()  # checks the environment variables LOGNAME, USER, LNAME and USERNAME

while True:
    pwd = getpass("Username: %s" % username)
    if pwd == 'abcde':
        print('You are in!')
        break
    else:
        print('Wrong password')
