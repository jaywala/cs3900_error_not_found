import smtplib

def host_email(host,property_name,dates,user):
    email = "Hi {},\n\n This is a confirmation email to notify your property, {} has been booked for the dates, {} by {}\n\nBest Regards\n NotAirBnB Team".format(host,property_name,dates,user)
    print(email)
    return email

def booker_email(user,property_name,dates):
    email = "Hi {},\n\n This is a email to confirm your booking of {} for the dates, {}\n\nBest Regards\n NotAirBnB Team".format(user,property_name,dates)
    print(email)
    return email

def send_email(to_addr, message, given_subject=''):

    gmail_user = 'comp3900.2018@gmail.com'
    gmail_password = '123Hello123'

    sent_from = gmail_user
    to = [to_addr]
    subject = given_subject
    body = message

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')

if __name__ == '__main__':
    host_email("_jeff_","_property_","_dates_","_user_")
    booker_email("_user_","_property_","_dates_")
    # send_email(to_addr='gladyschanmail@gmail.com', message='hello there', given_subject='test mail')
