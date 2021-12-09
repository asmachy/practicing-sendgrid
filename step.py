import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail.content import Content

with open("users.html", "r", encoding="utf-8") as html_file:
    html_content = Content("text/html", html_file.read())
    message = Mail(
        from_email='asmachycu15@gmail.com',
        to_emails='towhidul@cefalo.com',
        subject='SendGrid Test Email',
        html_content=html_content
    )
    try:
        sendgrid_api_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sendgrid_api_client.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
