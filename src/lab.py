import pieces
import time


pieces.autoit.win_activate("BlueStacks")
pos = pieces.lib.imagesearch(pieces.gvars.path_img + "imgMeusJogos.png")
pieces.lib.ultradebug("POS: " + str(pos))