import pywhatkit as whatsapp
import datetime , dotenv , os


def  send_whatsapp_msg(contenue):
    dotenv.load_dotenv()
    num_tele = os.getenv("phone_number")
    now = datetime.datetime.now()
    whatsapp.sendwhatmsg(num_tele, contenue, 
                    now.hour, now.minute + 3)
