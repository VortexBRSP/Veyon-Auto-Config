import os
import ctypes, sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    def gerarIp(ipBase, qtdIps):
        for i in range(0, qtdIps):
            print("{}.{} Adicionando IP.".format(ipBase, i))
            try:
                os.system('veyon-cli networkobjects add location Lab {}.{} "" ""'.format(ipBase, i))
            except:
                print("[ERRO] IP INVÁLIDO ERRO AO ADICIONAR!")

    print(".--.\n"
          "|__| .-------.\n"
          "|=.| |.-----.|\n"
          "|--| || VAS ||\n"
          "|  | |'-----'|\n"
          "|__|~')_____('\n"
          "VAS 2.0\n"
          "Author: @vortexbrsp")

    while True:
        try:
            ipBase = str(input("Digite as três primeiras seções do seu IP Local EX: 192.168.2\n"))
            qtdIps = int(input("Digite a quantidade de IPs para gerar( Recomendado: 200)\n"))
            gerarIp(ipBase, qtdIps)
            input("Ip's adicionado pressione qualquer tecla para encerrar...")
            break
        except:
            print("[ERRO] DADOS INVALIDOS TENTE NOVAMENTE\n")
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)




