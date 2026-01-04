import streamlit as st
import google.generativeai as genai

# Configuração da página e Título
st.set_page_config(page_title="Beta Kofrinho", page_icon="💰")
st.title("💰 Beta Kofrinho")

# 1. Configuração da API
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Erro: API Key não encontrada nos Secrets.")

# 2. Tentar carregar o modelo (usando o nome mais recente)
try:
    # Este é o nome padrão atual para o modelo gratuito
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception:
    # Caso falhe, tenta o nome alternativo
    model = genai.GenerativeModel('gemini-pro')

st.write("Digite sua pergunta abaixo:")
user_input = st.text_input("Sua mensagem:", placeholder="Como economizar dinheiro?")

if st.button("Enviar"):
    if user_input:
        with st.spinner('A IA está escrevendo...'):
            try:
                # O comando generate_content é o padrão para o Gemini
                response = model.generate_content(user_input)
                st.success("Resposta:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro ao gerar resposta: {e}")
    else:
        st.warning("Escreva algo antes de clicar em enviar.")
