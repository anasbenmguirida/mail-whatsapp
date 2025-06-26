from groq import Groq
import os , dotenv

def prompt_LLM():
    dotenv.load_dotenv()
    key = os.getenv("api_key")
    

    client = Groq(api_key=key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "donne moi juste le mail , pas de ok je vais le faire ,ni objet , directement just le contenue !!!!! ou je veux envoyer a mon prof (qui est un homme) , le rapport de sprint de cette semaine (2 phrases) et la signature tu fait equipe 4 ",
            }
        ],

        # The language model which will generate the completion.
        model="llama-3.3-70b-versatile"
    )

    return chat_completion.choices[0].message.content