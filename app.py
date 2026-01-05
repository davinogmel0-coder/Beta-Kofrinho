import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Beta Kofrinho", page_icon="💰")
st.title("💰 Beta Kofrinho - Modo Diagnóstico")

# 1. Configuração da API
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Chave API não encontrada nos Secrets!")
    st.stop()

# 2. Diagnóstico: Listar modelos disponíveis
try:
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    st.write(f"Modelos que sua chave alcança: {available_models}")
    
    # Tenta usar o primeiro da lista automaticamente ou o flash
    model_name = 'models/gemini-1.5-flash' if 'models/gemini-1.5-flash' in available_models else available_models[0]
    model = genai.GenerativeModel(model_name)
    st.success(f"Conectado com sucesso ao modelo: {model_name}")
except Exception as e:
    st.error(f"Erro de Conexão/Permissão: {e}")
    st.stop()

# 3. Chat
user_input = st.text_input("Faça sua pergunta:")
if st.button("Enviar"):
    if user_input:
        with st.spinner('IA respondendo...'):
            try:
                response = model.generate_content(user_input)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Erro ao gerar conteúdo: {e}")
