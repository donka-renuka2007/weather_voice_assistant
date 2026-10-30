import streamlit as st
from dotenv import load_dotenv
import os
import json
import requests
from gtts import gTTS
from streamlit_lottie import st_lottie
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
  def load_lottie(url):
    r=requests.get(url)
    if r.status_code == 200:
      return r.json()
    return None
  url="https://assets10.lottiefiles.com/packages/lf20_1pxqjqps.json"
  lottie_json=load_lottie(url)
  col1,col2=st.columns(2)
  with col1:
    st_lottie(lottie_json,height=300)
  with col2:
    onetext = f"""
📍 **Location:** {location}  
🌤️ **Weather:** {data['weather'][0]['description']}  
👀 **Main View:** {data['weather'][0]['main']}  
🌡️ **Temp:** {data['main']['temp']}°C  
🤔 **Feels Like:** {data['main']['feels_like']}°C  
💧 **Humidity:** {data['main']['humidity']}%
"""
    st.info(onetext)
except:
  st.error("something went wrong")


