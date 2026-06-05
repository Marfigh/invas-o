print('==================================')
print('=      Invasão a Instalação      =')
print('==================================')
vida=100
energia=50
chaves=1
maleta=0
kit=0
labo=1
depo=1
sala=1
ref=1
banhe=1
bilhe=0
nome=input('Digite seu nome espião(a)\n')
print('Muito prazer {}, meu nome é Ghost. Vou te orientar em sua nova missão.'. format(nome))
print('Sua primeira missão é invadir uma instalação do governo do Iraque. ')
print('Sua missão é simples {} ache a maleta com códigos de bombas e saia vivo.\n'. format(nome))
print('Na sua tela vai ter um menu com a seguintes opções:\n')

print('Abrir Porta: Lógicamente abre uma porta, mas necessita de uma chave.')
print('Ver status: Te mostra quanto dee vida, energia e chaves você tem.')
print('Descansar: Aumenta +10 de vida sua, mas você perde -10 de bateria.\n')
print('Vão ter guardas em algumas salas, se eles te perceberem você perde -20 de vida')
obs=input('Deseja observação? Se sim digite S se não quer ver digite N\n')
while obs != 'S' and obs != 'N':
    print('Escolha uma opção válida espião burro')
    obs=input('Escolha uma opção novamente\n')
if obs == 'S':
    print('Sua dica é se sua bateria acabar não tem como descansar\n')
print('Vamos a missão então, seja esperto espião e tome cuidado com os guardas!!!\n')
miss=input('Estamos embarcando você está pronto pra essa missão? S/N\n')
while miss !='S' and miss !='N':
    print('Escolha uma opção válida espião burro')
    miss=input('Escolha uma opção novamente\n')
if miss =='S':
    print('Então vamos a missão !!!!!!\n')
elif miss =='N':
    print('Parabéns por ser um bosta °_°')
    print('Mas você vai mesmo assim kkkkkkk\n')
while True:
    print('       ########## Menu de escolhas ##########\n')
    print('1 - Ver status')
    print('2 - Descansar')
    print('3 - Abrir Porta')
    menu=int(input('Digite a opção desejada\n'))
    while menu != 1 and menu != 2 and menu != 3:
        print('Escolha uma opção válida espião burro')
        menu=int(input('Escolha uma opção novamente\n'))
    if menu == 1:
        print('Vida = {}'. format(vida))
        print('Energia = {}'. format(energia))
        print('Chaves = {}'. format(chaves))
    elif menu == 2:
        if energia <= 9:
            print('Energia insuficiente')
        elif energia >= 10:
            vida=vida + 10
            energia=energia - 10
            print('Você se reculperou um pouco!!!!')
    elif menu == 3:
        print('Você chegou ao saguão principal, agora você tem que escolher pra qual porta entrar.\n')
        print('1 - Laboratório')
        print('2 - Depósito de armamento')
        print('3 - Sala de segurança')
        print('4 - Refeitório')
        print('5 - Banheiro')
        menu3=int(input('Escolha a onde você quer ir\n'))
        while menu3 != 1 and menu3 != 2 and menu3 != 3 and menu3 != 4 and menu3 != 5:
            print('Tá se superando na burrice soldado')
            menu3=input('Escolha uma opção novamente\n')
        if menu3 == 1:
            if labo <= 0:
                print('Você já entrou aqui')
            elif labo == 1:
                if chaves < 1:
                    print('Você está sem chave')
                    print('Porta bloqueada')
                elif chaves >= 1:
                    chaves=chaves - 1
                    labo=labo - 1
                    print('Você entrou no Laboratório e encontrou tudo bastante organizado e um armário bem chamativo')
                    abrir=input('Deseja abrir o armario? S/N\n')
                    while abrir !='S' and abrir !='N':
                        print('Não vou falar de novo inútil escolhe certo porra')
                        abrir=input('Escolha uma opção novamente\n')
                    if abrir == 'S':
                        print('Você encontou 3 itens:\n')
                        print('1 - kit médico que te da + 10 de vida')
                        print('2 - 2 Chaves desconhecidas ??')
                        print('3 - 5 de energia')
                        kit=kit + 2
                        chaves=chaves + 1
                        energia=energia + 5
                    elif abrir == 'N':
                        print('Você passou direto pelo armário')
        elif menu3 == 2:
            if depo <= 0:
                print('Você já estrou aqui')
            elif depo == 1:
                if chaves < 1:
                    print('Você está sem chave')
                    print('Porta bloqueada')
                elif chaves >= 1:
                    chaves=chaves - 1
                    depo=depo - 1
                    print('Você acaba de entrar no depósito de armamento')
                    print('Você vê diversas armas e bombas mas preucura pela maleta')
                    print('Você encontra um cofre com uma senha')
                    abrir2=input('Você deseja abrir o cofre? S/N\n')
                    while abrir2 !='S' and abrir2 !='N':
                        print('Não vou falar de novo inútil escolhe certo porra')
                        abrir2=input('Escolha uma opção novamente\n')
                    if abrir2 == 'N':
                        print('Você fez sua escolha')
                    elif abrir2 == 'S':
                        print('Você acha um papel com a dica do número do cofre que diz:\n')
                        print("Meu primeiro número é o dobro de 1.")
                        print('Meu segundo número é o dobro do primeiro.')
                        print('Meu terceiro número é a soma dos dois primeiros.')
                        print('Meu quarto número é a diferença entre o terceiro e o primeiro.')
                        senha=int(input('Digite a senha do cofre de 4 digitos'))
                        while senha != 2464:
                            print('Senha incorreta')
                            senha=int(input('Digite novamente'))
                        if senha == 2464:
                            print('Você acaba de abrir o cofre e encontra uma chave e um bilhete amaçado bem embaralhado:')
                            print('O segredo n3o #stá on*e se cria.')
                            print('!ão está on&e se pr8tege.')
                            print('Não es%á onde se a!imenta.....\n')
                            print('Está onde até @enerais e presidentes')
                            print('p$ecisam ir sozinhos.')
                            bilhe=bilhe + 1
                            chaves=chaves + 1
                        if bilhe > 1:
                            bilhe = 1
        elif menu3 == 3:
            if sala <=0:
                print('Você já entrou aqui')
            if sala == 1:
                if chaves < 1:
                    print('Você está sem chave')
                    print('Porta bloqueada')
                if chaves >= 1:
                    chaves=chaves - 1
                    sala=sala - 1
                    print('Você entra na sala de segurança do prédio')
                    print('Vê diversos paineis de controle. Mas sem queres esbarra em um botão de segurança e o alarme toca......')
                    print('Você tem pouco tempo pra se esconder escolha para onde vai:\n')
                    print('1 - Entrar no armario')
                    print('2 - Debaixo da mesa')
                    esconder=int(input('Escolha uma opção\n'))
                    while esconder != 1 and esconder != 2:
                        print('Escolha uma opção válida espião burro')
                        esconder=int(input('Escolha uma opção novamente\n'))
                    if esconder == 1:
                        print('Você fez uma bela escolha, o segurabça não encontrou nada e foi embora')
                        print('Ainda ganhou +5 de bateria e encontrou uma chave')
                        energia=energia + 5
                        chaves=chaves + 1
                    if esconder == 2:
                        print('Se fudeo você foi descoberto mais conseguiu sair')
                        print('Mas perdeu -25 de vida e encontrou uma chave')
                        vida=vida - 25
                        chaves=chaves + 1
        elif menu3 == 4:
            if ref <= 0:
                print('Você já entrou aqui')
            if ref >= 1:
                if chaves < 1:
                    print('Você está sem chave')
                    print('Porta bloqueada')
                if chaves >= 1:
                    chaves=chaves - 1
                    ref=ref -1
                    print('Você entra no refeitório e aparentemente não vê ninguém')
                    print('Você vê apenas 1 chave em cima da mesa')
                    chaves=chaves + 1
        elif menu3 == 5:
            if banhe <= 0:
                print('Você já entrou aqui')
            if banhe == 1:
                if chaves < 1:
                    print('Você está sem chave')
                    print('Porta bloqueada')
                if chaves >= 1:
                    chaves=chaves - 1
                    banhe=banhe - 1
                    print('Você entra no banheiro e vê 4 portas')
                    print('Você ouve três guardas conversando, mas não sabe ao certo em qual porta eles estão')
                    print('Vamos entrar em um consenso que ver um homem desse modo n é legal então escolha direito')
                    print('Se escolher errado você perde muita vida!!!!!')
                    porta=int(input('Escolha sua porta\n'))
                    while porta != 1 and porta != 2 and porta != 3 and porta != 4:
                        print('As vezes me canso dessas pessoas burras')
                        porta=int(input('Escolha uma opção novamente\n'))
                    while porta != 1:
                        print('Você escolheu uma porta com guarda e perdeu - 25 de vida ')
                        vida=vida - 25
                        porta=int(input('Escolha outra porta\n'))
                    if vida <= 0:
                        print('Você perdeu o jogo. Se fudeo kkkkk')
                    elif vida >= 1:
                        if porta == 1:
                            print('Você acha a porta sem guardas e eles não te percebem')
                            print('Você vê dois botões na parede e tem que escolher um certo')
                            print('Você pensa que se escolher errado vai tocar um alarme então pense bem\n')
                            print('Botão 1')
                            print('Botão 2')
                        escolha=int(input('Escolha a certa\n'))
                        while escolha != 1 and escolha != 2:
                            print('Puta que pariu .... ')
                            escolha=int(input('Escolha uma opção novamente\n'))
                        while escolha == 2:
                            print('Parabéns Você aparou o batão da descarga kkkkkkkkkkkk')
                            escolha=int(input('Escole o 1 que é melhor kkkkk\n'))
                        if escolha == 1:
                            print('Você aperta o botão na parede abre um compartimento com a maleta')
                            print('Você pega a maleta e pode ir embora são e salvo')
                            maleta=maleta + 1
                        if maleta == 1:
                            print('Parabén você concluiu o desafio!!!!')
        if maleta == 0:
            escolha2=input('Se deseja voltar ao menu digite S\nelse ')
            if escolha2 == 'S':
                print('Voltando ......')
        else:
            break
                


        


        

    
    
