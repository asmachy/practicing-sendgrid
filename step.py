import os
import json
from sendgrid import SendGridAPIClient
from constants.constants import EMAIL_DATA_FILE, FILES_PREFIX, STYLE_FILE

from helpers.html_generator import HtmlGenerator
from helpers.sendgrid_helper import SendGridHelper


with open(FILES_PREFIX+EMAIL_DATA_FILE, "r", encoding="utf-8") as email_data_file:
    email_data = json.load(email_data_file)

with open(FILES_PREFIX+STYLE_FILE) as style_file:
    style = json.load(style_file)

html_generator = HtmlGenerator(style)
sendgrid_helper = SendGridHelper(html_generator=html_generator)


if __name__ == '__main__':
    try:
        sendgrid_api_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        message = sendgrid_helper.generate_mail(email_data=email_data)
        response = sendgrid_api_client.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
