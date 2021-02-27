import pieces
import time

def realiza_login(title, timeout):
    # Mata Processo no início para assegurar realização do login
    pieces.os.system('taskkill /f /im BlueStacks.exe')

    # Executa a rotina para abrir o aplicativo 
    status_open_app = pieces.lib.open_app(path=pieces.gvars.path_app, win_title=title, timeout=30)

    # Caso o aplicativo esteja aberto
    if status_open_app == True:
        pieces.lib.ultradebug("realiza_login() - O aplicativo foi aberto com sucesso")
        
        # Maximiza Tela
        bluestacks_window = pieces.gw.getWindowsWithTitle(title)[0]
        bluestacks_window.maximize()

        # Laço de repetição para aguardar o carregamento da tela principal
        timer = pieces.lib.Timer(timeout)
        while timer.not_expired:
            pieces.autoit.win_activate(title)
            pos = pieces.lib.imagesearch(pieces.gvars.path_img + "imgMeusJogos.png")
            if pos != False:
                pieces.lib.ultradebug("realiza_login() - Carregou tela principal")
                return True, pos
            pieces.lib.ultradebug("realiza_login() - Aguardando Tela Principal Carregar")

    # Caso tenha ocorrido um erro ao abrir o aplicativo
    if status_open_app == False:
        pieces.lib.ultradebug("realiza_login() - Erro ao abrir Aplicativo")
        return False

    # Caso tenha ocorrido o timeout ao aguardar o carregamento da tela principal
    if timer.expired:
        pieces.lib.ultradebug("realiza_login() - [TIMEOUT] Ao aguardar tela principal carregar")
        return False

def aguarda_app_instagram(title, param_realiza_login):
    # Variaveis de retorno para validação e referência
    valida_execucao_def = param_realiza_login[0]
    posimg_execucao_def = param_realiza_login[1]

    # Caso o login tenha sido realizado com sucesso e a página principal esteja disponível
    # clica na imagem referência "Meus Jogos"

    if valida_execucao_def == True:

        # clica na opção "Meus Jogos" enquanto o ícone Instagram não aparecer
        pieces.lib.ultradebug("aguarda_app_instagram() - Vai aguardar app Instagram aparecer após o click")
        timer = pieces.lib.Timer(10)

        # Laço de repetição para aguardar app do Instagram carregar
        while timer.not_expired:
            # clica na opção "Meus Jogos"
            pieces.pyautogui.click((posimg_execucao_def[0] + 15), (posimg_execucao_def[1] + 15))
            pieces.autoit.win_activate(title)
            pos = pieces.lib.imagesearch(pieces.gvars.path_img + "imgAppInstagram.png")
            if pos != False:
                pieces.lib.ultradebug("aguarda_app_instagram() - Carregou app do Instagram")
                return True, pos
            pieces.lib.ultradebug("aguarda_app_instagram() - Aguardando app do Instagram carregar")

    # Caso tenha ocorrido um erro ao abrir o aplicativo
    if valida_execucao_def == False:
        pieces.lib.ultradebug("aguarda_app_instagram() - O Login e a pagina principal não foi executada com sucesso")
        return False

    # Caso tenha ocorrido o timeout ao aguardar app do Instagram carregar
    if timer.expired:
        pieces.lib.ultradebug("aguarda_app_instagram() - [TIMEOUT] Ao aguardar app do Instagram carregar")
        return False

def clica_app_instagram(title, param_realiza_login):
    # Variaveis de retorno para validação e referência
    valida_execucao_def = param_realiza_login[0]
    posimg_execucao_def = param_realiza_login[1]

    # Clica no app Instagram enquanto não abrir a página inicial
    if valida_execucao_def == True:

        # clica no app Instagram enquanto a imagem "Seu Story" não aparecer
        pieces.lib.ultradebug("clica_app_instagram() - Vai aguardar app Instagram carregar tela principal após o click")
        timer = pieces.lib.Timer(10)

        # Laço de repetição para aguardar tela principal do Instagram carregar
        while timer.not_expired:
            # clica na opção app Instagram
            pieces.pyautogui.click((posimg_execucao_def[0] + 15), (posimg_execucao_def[1] + 15))
            pieces.autoit.win_activate(title)
            pos = pieces.lib.imagesearch(pieces.gvars.path_img + "imgSeuStory.png")
            if pos != False:
                pieces.lib.ultradebug("clica_app_instagram() - Carregou tela principal do Instagram")
                return True
            pieces.lib.ultradebug("clica_app_instagram() - Aguardando tela principal do Instagram carregar")

    # Caso tenha ocorrido um erro ao abrir o aplicativo
    if valida_execucao_def == False:
        pieces.lib.ultradebug("clica_app_instagram() - O app Instagram não apareceu na tela")
        return False

    # Caso tenha ocorrido o timeout ao aguardar app do Instagram carregar
    if timer.expired:
        pieces.lib.ultradebug("clica_app_instagram() - [TIMEOUT] Ao aguardar tela principal do Instagram carregar")
        return False
    
