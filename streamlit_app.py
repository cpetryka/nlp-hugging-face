import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os

# import streamlit as st
# from transformers import pipeline

# option = st.selectbox(
#     "Opcje",
#     [
#         "Wydźwięk emocjonalny tekstu (eng)",
#         "???",
#     ],
# )

# if option == "Wydźwięk emocjonalny tekstu (eng)":
#     text = st.text_area(label="Wpisz tekst")
#     if text:
#         classifier = pipeline("sentiment-analysis")
#         answer = classifier(text)
#         st.write(answer)

# st.subheader('Zadanie do wykonania')
# st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/docs/transformers/index')
# st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
# st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
# st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
# st.write('🐞 Na końcu umieść swój numer indeksu')
# st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
# st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')

import streamlit as st
import pandas as pd
import time
import os
from transformers import pipeline

st.set_page_config(page_title="Aplikacja NLP z Hugging Face", page_icon="🤖")
st.title("Aplikacja NLP z Hugging Face 🤖")
st.image("https://huggingface.co/front/assets/huggingface_logo.svg", width=150)
st.write("""
### Instrukcja:
Ta aplikacja pozwala:
- **Analizować wydźwięk emocjonalny tekstu (sentiment analysis)** w języku angielskim.
- **Tłumaczyć tekst z języka angielskiego na język niemiecki**.

Wybierz odpowiednią opcję z listy poniżej, wpisz tekst i zobacz wynik.
""")

option = st.selectbox(
    "Wybierz opcję:",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumaczenie EN → DE",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst w języku angielskim:")
    if text:
        with st.spinner("Analizuję wydźwięk..."):
            try:
                classifier = pipeline("sentiment-analysis")
                answer = classifier(text)
                st.success("Analiza zakończona!")
                st.write("**Wynik:**", answer)
            except Exception as e:
                st.error(f"Wystąpił błąd: {e}")

elif option == "Tłumaczenie EN → DE":
    text = st.text_area(label="Wpisz tekst w języku angielskim do tłumaczenia:")
    if text:
        with st.spinner("Tłumaczę tekst..."):
            try:
                translator = pipeline("translation_en_to_de")
                answer = translator(text)
                st.success("Tłumaczenie zakończone!")
                st.write("**Tekst przetłumaczony:**", answer[0]['translation_text'])
            except Exception as e:
                st.error(f"Wystąpił błąd: {e}")

st.write("---")
st.write("Numer indeksu: **s27984**")

st.info("Aplikacja wykorzystuje modele z biblioteki Hugging Face")
st.balloons()