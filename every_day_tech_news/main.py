import requests 


response = requests.get("https://theaxolotlapi.netlify.app/")

print(response.json())