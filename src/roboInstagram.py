import pieces

# Realiza login e verifica se a tela principal carregou
retorno_realiza_login = pieces.lib_processo.realiza_login(title=pieces.gvars.title_app, timeout=60)

# Clica em "Meus Jogos" e verifica se o app Instagram carregou
retorno_aguarda_app_instagram = pieces.lib_processo.aguarda_app_instagram(title=pieces.gvars.title_app, param_realiza_login=retorno_realiza_login)

# Clica app Instagram e verifica a imagem "Seu Story" carregou na página principal do Instagram
retorno_clica_app_instagram = pieces.lib_processo.clica_app_instagram (title=pieces.gvars.title_app, param_realiza_login=retorno_aguarda_app_instagram)

