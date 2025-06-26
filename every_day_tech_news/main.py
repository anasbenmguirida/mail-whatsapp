from email.message import EmailMessage
import os , dotenv ,datetime
import smtplib
from prompte_GPT import prompt_LLM


def load_environment_variables():
    dotenv.load_dotenv()
    source= os.getenv("source")
    destinataire = os.getenv("destinataire")
    password = os.getenv("password")
    return source , destinataire , password

def construct_email():
    source , destinataire  , password = load_environment_variables()

    contenue = prompt_LLM()

    message = EmailMessage()
    message["From"] = source 
    message["To"] = destinataire 
    message["Subject"] = "News of the day  : "+str(datetime.date.today())
    message.set_content(contenue)
    return message

def send_email():
    source , destinataire  , password = load_environment_variables()
    message = construct_email()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(source, password)
            smtp.send_message(message)
        return "Mail sent successfully!"
    except Exception as e:
        return f" Something went wrong: {e}"


send_email()