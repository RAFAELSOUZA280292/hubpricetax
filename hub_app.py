import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="HUB Price Tax",
    layout="centered", # 'wide' para tela cheia, 'centered' para centralizar conteúdo
    initial_sidebar_state="collapsed" # Esconde a sidebar por padrão
)

# --- Senha e Autenticação ---
# ATENÇÃO: Para produção, o ideal é usar st.secrets para armazenar senhas,
# e não diretamente no código. Ex: st.secrets["password"]
PASSWORD = "Ivana_2025"

# Usar st.session_state para manter o estado de login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Se não estiver logado, pede a senha
if not st.session_state.logged_in:
    st.header("Acesso Restrito ao HUB Price Tax")
    st.info("Por favor, digite a senha para acessar as ferramentas.")

    password_input = st.text_input("Senha:", type="password") # type="password" esconde o texto

    if st.button("Entrar", key="login_button"):
        if password_input == PASSWORD:
            st.session_state.logged_in = True
            st.success("Acesso concedido! Redirecionando...")
            st.experimental_rerun() # Recarrega a página para mostrar o conteúdo do HUB
        else:
            st.error("Senha incorreta. Tente novamente.")
            st.session_state.logged_in = False # Garante que não está logado

# Conteúdo do HUB após o login
if st.session_state.logged_in:
    # --- Estilo "Amarelo Riqueza" ---
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f2f6; /* Cor de fundo padrão do Streamlit ou ajuste */
        }
        h1 {
            color: #FFD700; /* Amarelo Riqueza para o título */
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2); /* Sutil sombra para destacar */
            font-size: 3em; /* Tamanho do título */
            text-align: center;
        }
        .description-text {
            font-size: 1.1em;
            color: #555;
            text-align: center;
            margin-bottom: 30px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("HUB Price Tax")
    st.markdown('<p class="description-text">Bem-vindo(a) ao seu centro de ferramentas! Clique nos botões abaixo para acessar as aplicações.</p>', unsafe_allow_html=True)

    st.write("---") # Linha divisória

    # IMPORTANT: URLs REAIS DOS SEUS APLICATIVOS STREAMLIT DEPLOYADOS
    app_urls = {
        "Consulta CNPJ (Preço/Taxa)": "https://cnpjpricetax.streamlit.app/",
        "Consulta CNPJ em Lote": "https://cnpjpricetaxlote.streamlit.app/",
        "Consulta CNPJ (Geral)": "URL_DO_SEU_APP_CONSULTA_CNPJ_GERAL_AQUI" # Por favor, forneça este link se ele existir
    }

    st.subheader("Ferramentas Disponíveis:")

    # Criar botões que abrem os links em uma nova aba com estilo personalizado
    for app_name, app_url in app_urls.items():
        st.markdown(
            f"""
            <a href="{app_url}"  style="text-decoration: none;">
                <button style="
                    background-color: #FFD700;
                    color: black;
                    font-weight: bold;
                    border-radius: 10px;
                    padding: 12px 24px;
                    border: 2px solid #CCA300;
                    cursor: pointer;
                    font-size: 1.1em;
                    width: 100%;
                    margin-bottom: 15px;
                    box-shadow: 3px 3px 6px rgba(0,0,0,0.2);
                    transition: all 0.2s ease-in-out;
                "
                onmouseover="this.style.backgroundColor='#e6c200'; this.style.borderColor='#B38F00'; this.style.transform='translateY(-2px)';"
                onmouseout="this.style.backgroundColor='#FFD700'; this.style.borderColor='#CCA300'; this.style.transform='translateY(0)';">
                    Acessar {app_name}
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )

    st.write("---")

    # Botão para sair (limpa o estado de login)
    if st.button("Sair do HUB", key="logout_button"):
        st.session_state.logged_in = False
        st.experimental_rerun() # Recarrega a página para voltar para a tela de login