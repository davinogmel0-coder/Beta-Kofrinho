import streamlit as st
import google.generativeai as genai

# 1. Configuração do Gemini (puxando dos Secrets)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Configure a GOOGLE_API_KEY nos Secrets do Streamlit.")

model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Interface do Usuário
st.set_page_config(page_title="Beta Kofrinho", page_icon="💰")
st.title("💰 Beta Kofrinho")
st.write("Bem-vindo ao teste! Digite sua pergunta para a IA abaixo:")

user_input = st.text_input("Sua mensagem:", placeholder="Ex: Como economizar dinheiro?")

if st.button("Enviar"):
    if user_input:
        with st.spinner('Processando...'):
            try:
                response = model.generate_content(user_input)
                st.success("Resposta da IA:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro ao gerar resposta: {e}")
    else:
        st.warning("Por favor, digite algo antes de clicar em enviar.")
