import os
def gerarIp(ipBase, qtdIps):
    for i in range(0, qtdIps):
        print("{}.{}".format(ipBase, i))

gerarIp("192.168.0",200)