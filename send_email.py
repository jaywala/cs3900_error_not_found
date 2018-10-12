import smtplib

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
    send_email(to_addr='gladyschanmail@gmail.com', message='hello there', given_subject='test mail')
