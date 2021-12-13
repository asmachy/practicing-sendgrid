from datetime import datetime
from typing import List
from constants.constants import (
    CUSTOMER_EMAIL, CUSTOMER_LIST, CUSTOMER_NAME, EMAIL, SUBJECT, EMPLOYEE_NAME, FROM_EMAIL, NAME, NHST, NORWAY, OSLO,
    PRODUCT_LIST, PRODUCT_TEMPLATE_ID, SENDER_ADDRESS, SENDER_CITY, SENDER_NAME, SENDER_STATE, TABLE_DATA, TODAY)
from helpers.html_generator import HtmlGenerator
from sendgrid.helpers.mail import Mail, To


class SendGridHelper:
    def __init__(self, html_generator: HtmlGenerator) -> None:
        self.html_generator = html_generator

    def get_to_emails(self, customer_list, employee_name, subject) -> List:
        to_emails: List = []
        for customer in customer_list:
            email = customer[EMAIL]
            name = customer[NAME]
            product_list = customer[PRODUCT_LIST]
            product_list_html = self.html_generator.generate_table(product_list)
            today = datetime.now()
            today_str = today.strftime("%d %h, %Y")
            to_email = To(
                email=email,
                name=name,
                dynamic_template_data={
                    CUSTOMER_NAME: name,
                    CUSTOMER_EMAIL: email,
                    TABLE_DATA: product_list_html,
                    SUBJECT: subject,
                    TODAY: today_str,
                    EMPLOYEE_NAME: employee_name,
                    SENDER_NAME: NHST,
                    SENDER_ADDRESS: OSLO,
                    SENDER_CITY: OSLO,
                    SENDER_STATE: NORWAY
                }
            )
            to_emails.append(to_email)
        return to_emails

    def generate_mail(self, email_data):
        to_emails = self.get_to_emails(
            customer_list=email_data[CUSTOMER_LIST],
            employee_name=email_data[EMPLOYEE_NAME],
            subject=email_data[SUBJECT]
        )
        is_multiple = True if len(to_emails) > 1 else False

        message = Mail(
            from_email=(email_data[FROM_EMAIL], email_data[EMPLOYEE_NAME]),
            to_emails=to_emails,
            is_multiple=is_multiple
        )
        message.template_id = PRODUCT_TEMPLATE_ID
        return message
