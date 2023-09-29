# python email client
from __future__ import print_function

import os.path
import base64
from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


def gmail_send_message():
    creds = None

    if os.path.exists('/Users/nickr/OneDrive/School/cs4390/Project 1/token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/Users/nickr/OneDrive/School/cs4390/Project 1/creds.json', SCOPES)
            creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open('/Users/nickr/OneDrive/School/cs4390/Project 1/token.json', 'w') as token:
        token.write(creds.to_json())

    try:
        service = build('gmail', 'v1', credentials=creds)

        emailMsg = 'Please work'

        # build email
        mimeMessage = MIMEMultipart()
        mimeMessage['to'] = 'nickrocks75@gmail.com'
        mimeMessage['subject'] = 'Success'
        mimeMessage.attach(MIMEText(emailMsg, 'plain'))

        # encode
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

        message = service.users().messages().send(
            userId='me', body={'raw': raw_string}).execute()
        print(message)

    except HttpError as error:
        print(F'ERROR: {error}')
        send_message = None

    return send_message


if __name__ == '__main__':
    gmail_send_message()
