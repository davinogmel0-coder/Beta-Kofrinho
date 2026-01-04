import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="Beta Kofrinho", page_icon="💰")
st.title("💰 Beta Kofrinho")

# 1. Configuração da API
if "GOOGLE_API_KEY" in st.secrets:
    # Esta linha garante que você use a versão estável da API
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Erro: API Key não encontrada nos Secrets.")

# 2. Definição do Modelo (usando o nome mais padrão possível)
model = genai.GenerativeModel('gemini-1.5-flash')

st.write("Digite sua pergunta abaixo:")
user_input = st.text_input("Sua mensagem:", placeholder="Como economizar dinheiro?")

if st.button("Enviar"):
    if user_input:
        with st.spinner('A IA está escrevendo...'):
            try:
                # Gerar conteúdo
                response = model.generate_content(user_input)
                st.success("Resposta:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Erro detalhado: {e}")
    else:
        st.warning("Escreva algo antes de clicar em enviar.")
