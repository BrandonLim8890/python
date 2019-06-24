#! python3
# command-line-emailer.py - Takes an email address and string
# and uses Selenium to log into your email account

from selenium import webdriver
import time, re


def emailLogin(user, password, mail_service):

    if not validEmail(user):
        print('User not valid')

    else:
        browser = webdriver.Firefox()
        time.sleep(5)


        if mail_service == 'gmail.com':
            browser.get('http://' + mail_service)

            # Gets user name and inputs
            user_elem = browser.find_element_by_id('identifierId')
            user_elem.send_keys(user)

            # Clicks next to get to password screen
            link_elem = browser.find_element_by_id('identifierNext')
            link_elem.click()
            time.sleep(5)

            # Gets password field and inputs
            pass_elem = browser.find_element_by_name('password')
            pass_elem.send_keys(password)

            # Clicks next to sign in
            link_pass_elem = browser.find_element_by_id('passwordNext')
            link_pass_elem.click()


        elif mail_service == 'yahoomail.com':
            browser.get('http://yahoomail.com')

            # Get user field and input
            user_elem = browser.find_element_by_id('login-username')
            user_elem.send_keys(user)

            # Click next
            link_elem = browser.find_element_by_id('login-signin')
            link_elem.click()

            time.sleep(5)

            # Get password field and input
            pass_elem = browser.find_element_by_id('login-passwd')
            pass_elem.send_keys(password)

            # CLick next to login
            link_pass_elem = browser.find_element_by_id('login-signin')
            link_pass_elem.click()

# Determins if the email inputted is valid
def validEmail(email):
    email_re = re.compile(r'''(
        [a-zA-Z0-9._+%-]+       # usernmae
        @                       # @ symbol
        [a-zA-Z0-9._+%-]+      # domain name
        (\.[a-zA-z]+)        # dot-something
        )''', re.VERBOSE)
    return email_re.match(email)


print('Enter your username:')
email = input()
print('Enter your password:')
passwd = input()
print('Enter your email provider:')
email_provider = input()

emailLogin(email, passwd, email_provider)