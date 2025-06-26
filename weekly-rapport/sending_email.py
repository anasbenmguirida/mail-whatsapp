from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
import os , dotenv
from time import sleep
from sending_prompt import prompt_LLM
import datetime
from whatsapp_reminder import send_whatsapp_msg




def load_environment_variables():
    dotenv.load_dotenv()
    source= os.getenv("source")
    destinataire = os.getenv("destinataire")
    password = os.getenv("password")
    return source , destinataire , password

def construct_mail():
    source , destinataire , password = load_environment_variables()
    
    contenue = prompt_LLM()
    
    msg = MIMEMultipart()
    msg['Subject'] = "UAE/ENSAT : Rapport du sprint de semaine "
    msg['From'] = source
    msg['To'] = destinataire
    msg.attach(MIMEText(contenue, "plain"))

    filename = "Equipe 4 - compte rendu.pdf"  

    
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    
    msg.attach(part)
    return msg 


def send_mail_with_file():
    
    send_whatsapp_msg("le mail va être envoyer dans environ 1 minute ")

    msg = construct_mail()
    
    source , destinataire , password = load_environment_variables()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(source, password)
            smtp.send_message(msg)
        return "Mail sent successfully!"
    except Exception as e:
        return f" Something went wrong: {e}"



print(send_mail_with_file())