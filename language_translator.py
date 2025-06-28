from googletrans import Translator, LANGUAGES
import streamlit as st

translator = Translator()
langs = list(LANGUAGES.values())
lang_dict = dict(map(reversed, LANGUAGES.items()))

st.title("🌐 Language Translation Tool")
st.markdown("Built by **Kiran Langoti** – CodeAlpha AI Internship")

input_text = st.text_area("Enter text to translate")

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language", langs, index=langs.index("english"))
with col2:
    target_lang = st.selectbox("Target Language", langs, index=langs.index("hindi"))

if st.button("Translate"):
    src = lang_dict[source_lang]
    tgt = lang_dict[target_lang]
    result = translator.translate(input_text, src=src, dest=tgt)
    st.success("Here’s your translation:")
    st.text_area("Translated Text", result.text, height=150)
