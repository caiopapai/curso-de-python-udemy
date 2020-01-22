trabalho_quinta = False
trabalho_terca = False

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print("TV50={} TV32={} Sorvete={} Saudavel={}".format(tv_50,tv_32,sorvete,mais_saudavel))