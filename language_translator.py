from deep_translator import GoogleTranslator
import streamlit as st

langs = GoogleTranslator.get_supported_languages(as_dict=True)
lang_names = list(langs.keys())

st.title("🌐 Language Translation Tool")
st.markdown("Built by **Kiran Langoti** – CodeAlpha AI Internship")

text = st.text_area("Enter text to translate")

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Select source language", lang_names, index=lang_names.index("english"))
with col2:
    target_lang = st.selectbox("Select target language", lang_names, index=lang_names.index("hindi"))

if st.button("Translate"):
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        st.success("Translation:")
        st.text_area("Translated Text", translated, height=150)
    except Exception as e:
        st.error(f"Error: {e}")

