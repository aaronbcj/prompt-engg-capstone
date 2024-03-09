import os
import streamlit as st
from gtts import gTTS
from playsound import playsound
from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import base64

class Translator:
  def __init__(self, from_text, lang):
    self.from_text = from_text
    self.lang = lang
    
  def translate(self):
    
    # Set up OpenAI API key
    os.environ["OPENAI_API_KEY"] = os.environ.get("AARON_OPENAI_KEY")

    # Initialize the ChatOpenAI model
    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature = 0.7, max_tokens=300)

    # Constructing the message format for the LLM
    to_text = [
        SystemMessage(content='Translate the following text to '+self.lang+':'),
        HumanMessage(content=self.from_text)
    ]

    # Generating the summary
    output = llm(to_text).content

    return output

class TextToSpeech:
  def __init__(self, text, lang):
    self.text = text
    langdict = {"Spanish": "es","Mandarin": "zh-CN","Tamil": "ta","Hindi": "hi"}
    self.lang = langdict[lang]
    print(self.lang)

  def text_to_speech(self):
    # Save the audio file
    tts = gTTS(self.text, lang=self.lang)
    filename = "output.mp3"

    tts.save(filename)

    # Play the audio file in windows
    # playsound(filename)

    # Play the audio file in streamlit cloud
    with open(filename, "rb") as f:
      data = f.read()
      b64 = base64.b64encode(data).decode()
      md = f"""
          <audio controls autoplay="true">
          <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
          </audio>
          """
      st.markdown(
          md,
          unsafe_allow_html=True,
      )

    # and remove to avoid permission error next time
    os.remove(filename)

def submittext():
  st.session_state['from_text'] = st.session_state['textinput']
  #st.session_state['textinput'] = ""
  

#def submitpdf():
#  st.session_state['from_text'] = st.session_state['pdfinput']

def main():
  # Streamlit UI
  st.title("Text Translator - 300 characters only")

  try:
  
    # default values
    lang = "Spanish"
    from_text = "hello my name is aaron. how are you doing today?"

    if 'from_text' not in st.session_state:
      st.session_state['from_text'] = ''

    # if testing, set to True
    testing = False

    if testing == False:
      # get info from user
      lang = st.selectbox('Which language do you want to translate into?',('Spanish', 'Mandarin', 'Tamil', 'Hindi'))
      
      if(st.toggle('Upload PDF?')):
        st.session_state['from_text']=''
        pdf = st.file_uploader("Choose to upload your pdf",key="pdfinput", type="pdf")
        if pdf is not None:
          pdf_reader = PdfReader(pdf)
          pdf_text = ""
          for page in pdf_reader.pages:
            pdf_text+= page.extract_text()
            if(len(pdf_text)>300):
              pdf_text = pdf_text[:300]
              st.session_state['from_text'] = pdf_text
              st.markdown(body=st.session_state['from_text'], unsafe_allow_html=False)
              break
      else:
        #st.session_state['from_text']=''
        textinput = st.empty()
        textinput.text_area("Paste your text for translation: ", key="textinput", value=st.session_state['from_text'], height=150, max_chars=300, on_change=submittext) 
        st.markdown(body=st.session_state['from_text'], unsafe_allow_html=False)
    
    
    if st.button("Translate") or testing:
      if st.session_state['from_text']:
        
        with st.spinner('Generating translation...'): 
          translator = Translator(st.session_state['from_text'], lang) 
          to_text = translator.translate()

          # Display the to_text
          st.write("Translation:")
          st.write(to_text)
        
        with st.spinner('Generating speech...'): 
          # Play the audio
          tts = TextToSpeech(to_text, lang)
          tts.text_to_speech()
          
      else:
          st.warning("Please input a text to translate.")
  except Exception as e:
    st.error("Error has occurred. Please try again.")
    print(e)

main()
