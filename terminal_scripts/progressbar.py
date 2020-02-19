#Importa o pacote de time
import time

#Define as variàveis controladoras
load = True
progrss = 0
string = "#"

#Enquanto estiver carregando ele vai fazer um ciclo pegando oque ja tem na variavel string e adicionando + uma #
#e quando Chegar em 100% ele para e exibe uma mensagem "Progrsso Concluìdo!"
while load == True:
    if progrss < 100:
        # Code executed here
        time.sleep(0.1)
        progrss = progrss + 1
        string = string + "#"
        print("{}".format(string))
    else:
        load = False
print("Progresso Concluìdo!")
