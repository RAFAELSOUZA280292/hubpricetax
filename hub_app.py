import streamlit as st
import base64
from pathlib import Path

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

# --- Função para Carregar Imagem e Codificar em Base64 ---
# Assumimos que 'IMAGE.png' está no mesmo diretório do script 'hub_app.py'
# Se a imagem estiver em uma pasta 'images' no mesmo nível do 'hub_app.py', o caminho seria:
# image_path = Path(__file__).parent.parent / "images" / "IMAGE.png"
image_path = Path(__file__).parent / "IMAGE.png" # Caminho para a imagem no mesmo diretório

def get_img_as_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        st.error(f"Erro: A imagem de fundo '{file_path.name}' não foi encontrada. Certifique-se de que ela está no diretório correto.")
        return None # Retorna None se o arquivo não for encontrado

img_base64 = get_img_as_base64(image_path)

# Se não estiver logado, pede a senha
if not st.session_state.logged_in:
    st.header("Acesso Restrito ao HUB Price Tax")
    st.info("Por favor, digite a senha para acessar as ferramentas.")

    password_input = st.text_input("Senha:", type="password") # type="password" esconde o texto

    if st.button("Entrar", key="login_button"):
        if password_input == PASSWORD:
            st.session_state.logged_in = True
            st.success("Acesso concedido! Redirecionando...")
            st.rerun()
        else:
            st.error("Senha incorreta. Tente novamente.")
            st.session_state.logged_in = False

# Conteúdo do HUB após o login
if st.session_state.logged_in:
    # --- Estilo Personalizado ---
    # Somente injeta o CSS se a imagem Base64 foi carregada com sucesso
    if img_base64:
        st.markdown(
            f"""
            <style>
            /* === Configuração da Imagem de Fundo (via Base64) === */
            .stApp {{
                background-image: url("data:image/png;base64,{img_base64}"); /* <--- IMAGEM EMBUTIDA EM BASE64 */
                background-size: cover; /* Faz a imagem cobrir toda a área, cortando se necessário */
                background-position: center; /* Centraliza a imagem */
                background-repeat: no-repeat; /* Evita que a imagem se repita */
                background-attachment: fixed; /* Mantém a imagem de fundo fixa enquanto a página rola */
                background-color: #111111; /* Cor de fallback caso a imagem não carregue ou para espaços vazios */
                color: #f0f2f6; /* Cor do texto padrão para contraste com o fundo escuro */
            }}
            /* === Fim da Configuração da Imagem de Fundo === */

            h1, h2, h3, h4, h5, h6 {{
                color: #FFD700; /* Amarelo Riqueza para os títulos */
                text-shadow: 2px 2px 4px rgba(0,0,0,0.4); /* Sutil sombra para destacar */
            }}
            .description-text {{
                font-size: 1.1em;
                color: #CCCCCC; /* Cinza mais claro para descrição */
                text-align: center;
                margin-bottom: 30px;
            }}
            /* Estilo para os botões do HUB (mantido do seu código anterior) */
            .stButton > button {{
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
            }}
            .stButton > button:hover {{
                background-color: #e6c200;
                border-color: #B38F00;
                transform: translateY(-2px);
            }}
            /* Estilo para st.info, st.warning, st.error para se adequar ao fundo escuro */
            .stAlert {{
                background-color: #282828; /* Fundo mais escuro para alertas */
                color: #DDDDDD; /* Texto mais claro para alertas */
                border-left: 5px solid #FFD700; /* Borda amarela */
                border-radius: 5px;
            }}
            .stAlert > div > div > div > div > span {{
                color: #DDDDDD !important; /* Garante que o texto dentro do alerta seja claro */
            }}
            .stAlert > div > div > div > div > svg {{
                color: #FFD700 !important; /* Garante que o ícone do alerta seja amarelo */
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        # Estilo padrão caso a imagem não carregue (apenas cor de fundo)
        st.markdown(
            """
            <style>
            .stApp {
                background-color: #111111; /* Cor de fundo escura */
                color: #f0f2f6; /* Cor do texto padrão para contraste com o fundo escuro */
            }
            h1, h2, h3, h4, h5, h6 {
                color: #FFD700; /* Amarelo Riqueza para os títulos */
                text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
            }
            .description-text {
                font-size: 1.1em;
                color: #CCCCCC;
                text-align: center;
                margin-bottom: 30px;
            }
            .stButton > button {
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
            }
            .stButton > button:hover {
                background-color: #e6c200;
                border-color: #B38F00;
                transform: translateY(-2px);
            }
            .stAlert {
                background-color: #282828;
                color: #DDDDDD;
                border-left: 5px solid #FFD700;
                border-radius: 5px;
            }
            .stAlert > div > div > div > div > span {
                color: #DDDDDD !important;
            }
            .stAlert > div > div > div > div > svg {
                color: #FFD700 !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

    st.title("HUB Price Tax")
    st.markdown('<p class="description-text">Bem-vindo(a) ao seu centro de ferramentas! Clique nos botões abaixo para acessar as aplicações.</p>', unsafe_allow_html=True)

    st.write("---") # Linha divisória

    # IMPORTANT: URLs REAIS DOS SEUS APLICATIVOS STREAMLIT DEPLOYADOS.
    # Se você não tiver um link para "Consulta CNPJ (Geral)", pode remover essa linha.
    app_urls = {
        "Consulta CNPJ Unitário": "https://cnpjpricetax.streamlit.app/",
        "Consulta CNPJ em Lote": "https://cnpjpricetaxlote.streamlit.app/",
        "Extrator Dados Chave de Acesso - 55": "https://dadosnf55.streamlit.app/"
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
        st.rerun()
