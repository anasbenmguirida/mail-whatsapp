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
                "content": "donne moi tous des nouvelles sur le marché tech en france et au maroc , l'IA et tous ce qui est tech pendant la semaine actuelle",
            }
        ],

        # The language model which will generate the completion.
        model="llama-3.3-70b-versatile"
    )

    return chat_completion.choices[0].message.content

