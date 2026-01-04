import streamlit as st
import google.generativeai as genai

# Configuração da página
st.title("🤖 Meu App Beta com Gemini")
st.write("Bem-vindo à fase de testes! Digite algo abaixo.")

# Pegando a chave de API dos 'Segredos' (veremos isso no passo 4)
api_key = st.secrets["GOOGLE_API_KEY"]

# Configurando o Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash') # Ou o modelo que você usou

# Interface do Chat
user_input = st.text_input("Sua mensagem:", placeholder="Digite aqui...")

if st.button("Enviar"):
    if user_input:
        with st.spinner('A IA está pensando...'):
            try:
                # Aqui entra a lógica do seu prompt se tiver instruções de sistema
                response = model.generate_content(user_input)
                st.success("Resposta:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Ocorreu um erro: {e}")
    else:
        st.warning("Por favor, digite algo antes de enviar.")
      streamlit
google-generativeai
