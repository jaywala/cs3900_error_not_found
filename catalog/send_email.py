
import smtplib
import subprocess
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def cancel_host_email(host,property_name,dates,user):
    message = """\
    <html>
      <head></head>
      <body style="border:3px; border-style:solid; border-color:#3081EA; padding: 1em;">
        <p ><font face="Trebuchet MS" color="#474B50">
           Hi {host}<br>
           <br>
           &nbsp; &nbsp; &nbsp; &nbsp; This is a confirmation email to notify your property, <strong>{property_name}</strong><br>
           &nbsp; &nbsp; &nbsp; &nbsp; has been CANCELED for the dates, <strong>{dates}</strong> by <strong>{user}</strong>.<br>
           &nbsp; &nbsp; &nbsp; &nbsp; <br>
           &nbsp; &nbsp; &nbsp; &nbsp; Click <strong><a href="http://localhost:8080/manage/">here</a></strong> to manage your bookings.<br>
           &nbsp; &nbsp; &nbsp; &nbsp; <br>

           Best Regards,<br>
           <font color="#3081EA">NotAirBnB Team</font>
           </font>
        </p>
      </body>
    </html>
    """.format(host=host, property_name=property_name, dates=dates, user=user)

    return message


def host_email(host,property_name,dates,user):
    message = """\
    <html>
      <head></head>
      <body style="border:3px; border-style:solid; border-color:#3081EA; padding: 1em;">
        <p ><font face="Trebuchet MS" color="#474B50">
           Hi {host}<br>
           <br>
           &nbsp; &nbsp; &nbsp; &nbsp; This is a confirmation email to notify your property, <strong>{property_name}</strong><br>
           &nbsp; &nbsp; &nbsp; &nbsp; has been booked for the dates, <strong>{dates}</strong> by <strong>{user}</strong>.<br>
           &nbsp; &nbsp; &nbsp; &nbsp; <br>
           &nbsp; &nbsp; &nbsp; &nbsp; Click <strong><a href="http://localhost:8080/manage/">here</a></strong> to manage your bookings.<br>
           &nbsp; &nbsp; &nbsp; &nbsp; <br>

           Best Regards,<br>
           <font color="#3081EA">NotAirBnB Team</font>
           </font>
        </p>
      </body>
    </html>
    """.format(host=host, property_name=property_name, dates=dates, user=user)

    return message


def cancel_booker_email(user,property_name,dates): #TODO change the link when ready
    message = """\
    <html>
      <head></head>
      <body style="border:3px; border-style:solid; border-color:#3081EA; padding: 1em;">
        <p ><font face="Trebuchet MS" color="#474B50">
           Hi {user}<br>
           <br>
           &nbsp; &nbsp; &nbsp; &nbsp; This is an email to confirm your booking of, <strong>{property_name}</strong><br>
           &nbsp; &nbsp; &nbsp; &nbsp; for the dates <strong>{dates}</strong> has been CANCELED.<br>
           &nbsp; &nbsp; &nbsp; &nbsp; <br>
           &nbsp; &nbsp; &nbsp; &nbsp; Click <strong><a href="http://localhost:8080/trips/">here</a></strong> to manage your bookings.<br>
           &nbsp; &nbsp; &nbsp; &nbsp; <br>

           Best Regards,<br>
           <font color="#3081EA">NotAirBnB Team</font>
           </font>
        </p>
      </body>
    </html>
    """.format(user=user, property_name=property_name, dates=dates)

    return message


def booker_email(user,property_name,dates): #TODO change the link when ready
    message = """\
    <html>
      <head></head>
      <body style="border:3px; border-style:solid; border-color:#3081EA; padding: 1em;">
        <p ><font face="Trebuchet MS" color="#474B50">
           Hi {user}<br>
           <br>
           &nbsp; &nbsp; &nbsp; &nbsp; This is an email to confirm your booking of, <strong>{property_name}</strong><br>
           &nbsp; &nbsp; &nbsp; &nbsp; for the dates <strong>{dates}</strong>.<br>
           &nbsp; &nbsp; &nbsp; &nbsp; <br>
           &nbsp; &nbsp; &nbsp; &nbsp; Click <strong><a href="http://localhost:8080/trips/">here</a></strong> to manage your bookings.<br>
           &nbsp; &nbsp; &nbsp; &nbsp; <br>

           Best Regards,<br>
           <font color="#3081EA">NotAirBnB Team</font>
           </font>
        </p>
      </body>
    </html>
    """.format(user=user, property_name=property_name, dates=dates)

    return message


def send_email(to_addr, message, subject):
    # me == my email address
    # you == recipient's email address
    me = "comp3900.2018@gmail.com"
    you = to_addr

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    #text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = message

    # Record the MIME types of both parts - text/plain and text/html.
    #part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    #msg.attach(part1)
    msg.attach(part2)

    try:
        # Send the message via local SMTP server.
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(me, '123Hello123')
        mail.sendmail(me, you, msg.as_string())
        mail.quit()

        print('Email sent!')
    except:
        print('Something went wrong...')

if __name__ == '__main__':

    # Booker args
    #['send_email.py', 'booker', 'booker_name', 'property_name',
    # 'booked_period', 'booker', 'subject']

    # Host args
    #['send_email.py', 'host', 'poster_name', 'property_name',
    # 'booked_period', 'booker_name', 'ad_owner', 'subject']

    # tells me if I'm emailing the host or booker
    if sys.argv[1] == 'booker':

        booker_name = sys.argv[2]
        property_name = sys.argv[3]
        booked_period = sys.argv[4]
        booker = sys.argv[5]
        subject = sys.argv[6]

        b_email = booker_email(booker_name, property_name, booked_period)
        send_email(booker, b_email, subject)

    elif sys.argv[1] == 'host':

        poster_name = sys.argv[2]
        property_name = sys.argv[3]
        booked_period = sys.argv[4]
        booker_name = sys.argv[5]
        ad_owner = sys.argv[6]
        subject = sys.argv[7]

        h_email = host_email(poster_name, property_name, booked_period, booker_name)
        send_email(ad_owner, h_email, subject)
