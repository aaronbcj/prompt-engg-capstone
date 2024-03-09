This capstone project was created as part of Prompt Engineering course (Feb 2024 - March 2024) by edureka.co certification program.
This capstone project was created as part of Prompt Engineering course (Feb 2024 - March 2024) by edureka.co certification program.

# Overview

The goal of this capstone project is to create a web application using Streamlit thatenables users to translate text into different languages, convert the translated text tospeech, and download the audio file. The project leverages OpenAI's GPT-3.5-turbomodel for translation and Google Text-to-Speech (gTTS) for speech synthesis.

# Project Description

This project aims to develop a system that translates text into various languages andconverts the translated text into speech. The system is designed to be user-friendly andinteractive, allowing users to either enter text directly or upload a file in various formats(PDF, TXT, Excel, CSV). The text is then translated into a language selected by the userfrom a dropdown menu.

# Tasks for Learners:

1. Research Streamlit and Basics:Learn the fundamentals of Streamlit by referring to the official documentation and introductory tutorials.
2. Understand GPT-3.5-turbo for Translation:Research OpenAI's GPT-3.5-turbo for language translation. Understand input prompts and usage.
3. Explore gTTS for Text-to-Speech:Investigate the gTTS library for text-to-speech conversion. Learn about available options.
4. Design User Interface:Plan and design the user interface, considering input elements and layout
5. Implement Language Translation:Write code to take user input, select a language, and use GPT-3.5-turbo for translation.
6. Add Text-to-Speech:Implement text-to-speech functionality using gTTS and save the audio file.
7. Incorporate File Upload:Allow users to upload text or PDF files for translation. Implement text extraction.
8. Enhance User Experience:Implement error handling, user-friendly messages, and instructions.
9. Test and Debug:Thoroughly test the application, identifying and fixing any bugs.
10. Deploy Application:Explore deployment options (Heroku, Streamlit Sharing) and deploy the application.

# Submission Guidelines:

Submit the completed code and a documentation file.\
Documentation should explain how to use the app, considerations, and challenges.

# Instruction for usage:

1. Visit [https://prompt-engg-capstone.streamlit.app/]
2. Choose one of the four target languages (Spanish, Mandarin, Tamil, Hindi).
3. You can decide to paste the translation text in text area or toggle the mode for PDF upload instead.
4. A maximum of 300 characters only are extracted (either from text area or uploaded file) for translation.
5. After translation, audio is generated to read out the result.
6. Scope for future improvements: Options for input languages, option to accept user input via speech-to-text, search for specific topic within uploaded PDF and translate it.
7. Please send your feedback and ideas to further improve the scope of this project.

# Consideration & Challenges

1. streamlite state management was tricky, had to toggle upload and text area instead of having both of them together.
2. Audio lib/drivers in windows(local) wasn't working in streamlite cloud so had to find one that works in both.
3. Openai keys had expired so had to buy credits. In future, will explore free apis/models as well.
