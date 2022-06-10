import os

def gerarIp(ipBase, qtdIps):
    for i in range(0, qtdIps):
        print("{}.{} Adicionando IP.".format(ipBase, i))
        try:
            os.system('veyon-cli networkobjects add location Lab {}.{} "" ""'.format(ipBase, i))
        except:
            print("[ERRO] IP INVÁLIDO ERRO AO ADICIONAR!")

ipBase = input("Digite as três primeiras seções do seu IP Local EX: 192.168.2\n")
qtdIps = input("Digite a quantidade de IPs para gerar( Recomendado: 200)\n")
