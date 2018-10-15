
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
