#1 10/04 importar lib os(operationas system)
import os

#2 declarando a função finalizar_app
def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')



def chamar_nome_do_app():
 print('Restaurante Expresso\n')


def escolher_opcoes():
 print ('1-Cadastrar um restaurantes')
 print ('2-Listar restaurantes')
 print ('3-Ativar um restaurante')
 print ('4-Sair do programa\n')


opcao_digitada=int(input('Escolha uma opção: '))
print('Você selecionou a opção:', opcao_digitada,'\n')

if(opcao_digitada==1):
    print('Você escolheu cadastrar um restaurante \n')
elif(opcao_digitada==2):
    print('Você escolheu listar os restaurante do app \n')
elif(opcao_digitada==3):
    print('Você escolheu ativar um restaurante \n')
else:
    print('Você escolheu sair do programa\n')
    #3 chamada a função finalizar_app
    finalizar_app()

    #5 escrever a função main
    def main():
       #6 chamar o nome do app
    

    #4 criando a entrega através da variável main
    if __name__=='__Main__': # type: ignore
     main()