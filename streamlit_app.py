import streamlit as st
import process

st.title("Simple Decoder by Lev0nid")
st.write("Simple decoding app by Lev0nid. Made for fun. Can decode lower case Russian letters.")

form = st.form('input_text_form')
text = form.text_area('Input text to get your text decoded')

submitted = form.form_submit_button('Submit')

decoder = process.Decoder()

output_text = 'Input is empty'

if submitted:
    if text != '':
        output_text = decoder.decode(text)
    st.write(output_text)