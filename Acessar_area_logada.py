#### Passo 1: Entrar no site: https://login.sis.puc-campinas.edu.br/login?layoutEnvLabel=
#### Passo 2: Preencher nome, preencher e-mail 
#### Passo 3: Clicar no botão para enviar o formulário


from selenium import webdriver  # Automatiza ações em navegadores
from webdriver_manager.chrome import ChromeDriverManager  # Gerencia o download do ChromeDriver
from selenium.webdriver.chrome.service import Service  # Configura o serviço do ChromeDriver

# Configura o serviço do WebDriver
servico = Service(ChromeDriverManager().install())

# Inicializa o navegador
navegador = webdriver.Chrome(service=servico)

# Passo 1: Entrar no site
navegador.get("https://login.sis.puc-campinas.edu.br/login?layoutEnvLabel=")

# Passo 2: Acessar/preencher o login e senha
login = "digite_seu_login_aqui"  # Substitua pelo seu login
senha = "digite_sua_senha_aqui!"  # Substitua pela sua senha

navegador.find_element('xpath', '//*[@id="txtLogin"]').send_keys(login)  # Preenche o login
navegador.find_element('xpath', '//*[@id="txtSenha"]').send_keys(senha)  # Preenche a senha

# Passo 3: Clicar no botão de entrar
navegador.find_element('xpath', '//*[@id="login"]').click()


# Fechar o navegador ao final (opcional)
"""navegador.quit()"""
