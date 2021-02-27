import pieces
import time

# ==================================================================================================================== #


# Funções desenvolvidas para o processo

def open_app(path, win_title, timeout=10):

    # Abre o protheus
    pieces.os.startfile(path)

    timer = Timer(timeout)
    while timer.not_expired:
        screen_app_open = pieces.autoit.win_exists(win_title)
        pieces.lib.ultradebug("open_app() - Vai verificar se o aplicativo abriu")

        if screen_app_open:
            pieces.lib.ultradebug("open_app() - O Aplicativo está aberto")
            pieces.autoit.win_activate(win_title)
            return True
    
    # Caso o tempo tenha expirado
    if timer.expired:
        pieces.lib.ultradebug("abrir_login_smartclient(): [Timeout] O Aplicativo NAO ABRIU a tempo.")
        return False   

def imagesearch(path):

    # Função para encontrar imagem
    pos = pieces.imagesearch(path)
    if pos[0] != -1:
        return pos
    else:
        return False

# =================================================================================================================== #


# Funções auxiliares

class Timer:
    def __init__(self, duration=10):
        self.duration = float(duration)
        self.start = time.perf_counter()
        # print("The timer has started. Self.start: " + str(self.start))

    def reset(self):
        self.start = time.perf_counter()
        # print("The timer has been reset. Self.start: " + str(self.start))

    def explode(self):
        self.duration = 0
        # print("The timer has been force-expired.")

    def increment(self, increment=0):
        self.duration += increment
        # print("The timer has been incremented by " + str(increment) + " seconds")

    @property
    def not_expired(self):
        # duration == -1 means dev wants a infinite loop/Timer
        if self.duration == -1:
            return True
        return False if time.perf_counter() - self.start > self.duration else True

    @property
    def expired(self):
        return not self.not_expired

    @property
    def at(self):
        # print("The timer is running. Self.at: " + str(time.perf_counter() - self.start))
        return time.perf_counter() - self.start

def ultradebug(strlog,var_timeout=1):
    pieces.pymsgbox.alert(text=strlog, title='Robô Instagram', timeout=(var_timeout*1000))