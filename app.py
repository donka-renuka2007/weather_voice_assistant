import streamlit as st
from dotenv import load_dotenv
import os
import requests
from gtts import gTTS
load_dotenv()
api_key=os.getenv("api_key")
st.title("Weather Voice Assistant")

location=st.text_input("Enter Location Here.....")

try:
  url=f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
  response=requests.get(url)
  data=response.json()
  text=f"""
      location:{location}
      weather description: {data['weather'][0]['description']}
      main view now: {data['weather'][0]['main']}
      temperature:{data['main']['temp']}
      temperature feels like:{data['main']['feels_like']}
      humidity:{data['main']['humidity']}
      """
  st.success("fetched successfully")
  gtts=gTTS(text=text,lang="en",slow=False)
  gtts.save("voice.mp3")
  audio=open("voice.mp3","rb")
  st.audio(audio,format="audio/mp3")
  st.write(f"""data fetched is
  {text}""")
except:
  st.error("something went wrong")


