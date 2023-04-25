import os
import smtplib
import requests
from dotenv import load_dotenv

load_dotenv()

api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
api_key = f"{os.getenv('API_KEY')}"
header_dic = {'Authorization': 'Bearer ' + api_key}

# Get LinkedIn profile URL from user input
url = input("Enter the LinkedIn profile URL: ")

# API request parameters
params = {
    'url': url,
    'fallback_to_cache': 'on-error',
    'use_cache': 'if-present',
    'skills': 'include',
    'inferred_salary': 'include',
    'personal_email': 'include',
    'personal_contact_number': 'include',
    'twitter_profile_id': 'include',
    'facebook_profile_id': 'include',
    'github_profile_id': 'include',
    'extra': 'include',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

data = response.json()
full_name = data['full_name']
personal_emails = data['personal_emails']
summary = data['summary']
occupation = data['occupation']

# Email message
subject = "Предложение сотрудничества от HappyAI"
body = f"""
Здравствуйте, {full_name}!

Мы команда HappyAI, которая специализируется на внедрении искусственного интеллекта в бизнес-процессы для увеличения прибыли.

Мы заметили, что вы профессионал в вашей области, и хотели бы предложить вам сотрудничество в рамках наших проектов.

Если вы заинтересованы, пожалуйста, ответьте на это письмо, чтобы мы могли обсудить детали.

С уважением,
Команда HappyAI
"""

# Send email

sender_email = f"{os.getenv('YOUR_EMAIL')}"  # Replace with your email address
password = f"{os.getenv('YOUR_PASSWORD')}"  # Replace with your email password
receiver_email = personal_emails

# Create SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Login to email account
server.login(sender_email, password)

# Send email
message = f'Subject: {subject}\n\n{body}'
server.sendmail(sender_email, receiver_email, message)

# Quit the SMTP session
server.quit()

print(f"Email sent to {full_name} at {personal_emails}")
