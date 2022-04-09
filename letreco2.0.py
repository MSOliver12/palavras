while True:
    ###Aprender novas###
    arq=open('aprender.txt','a+',encoding='utf_8')
    arq.seek(0,0)
    ###existentes###
    arq2=open('palavras.txt','a+',encoding='utf_8')
    arq2.seek(0,0)
    p=arq2.readlines()
    p=[x.strip('\n') for x in p ]
    #print(f'p {p}')
    ###programa###
    from random import randint
    aprender=arq.readlines()
    aprender=[x.strip('\n') for x in aprender]
    #print(aprender)
    palavras=['ano','pano','plano','fulano','relogio','pescador']
    for i in p:
        palavras.append(i)
    #print(f'Palavras {palavras}')
    arq2.close()
    certo='\033[032m'
    errado='\033[031m'
    existe='\033[033m'
    fim='\033[m'
    escolha=palavras[randint(0,len(palavras)-1)].upper()
    palpites=0
    print('\033[034m{::^30}\033[m'.format('Letreco'))
    print(f'A palavra escolhida tem {len(escolha)} letras')
    while True:
        chute=input('Qual a palavra escolhida? ').upper().strip().rstrip()
        if chute=='0':
            while True:
                desi=input('Deseja desistir? [S/N]').upper()
                if desi=='S':
                    print(escolha)
                    break
                else:
                    break
        ver=chute.lower() in palavras
        if len(chute)==len(escolha) and ver==True:
            palpites=palpites+1
            if chute==escolha:
                break
            else:
                for l in range(0,len(escolha)):
                    if chute[l]==escolha[l]:
                        print(f'{certo}{chute[l]}{fim}',end='')
                    if chute[l]!=escolha[l]:
                        if chute[l] in escolha:
                            print(f'{existe}{chute[l]}{fim}',end='')
                        else:
                            print(f'{errado}{chute[l]}{fim}',end='')
                    if l==len(escolha)-1:
                        print('\n',end='')
        elif len(chute)==len(escolha) and ver==False:
            print(f'{errado}Palavra não aceita{fim}')
            #print(f'aprender{aprender}')
            teste=chute.lower() in aprender
            #print(f'teste{teste}')
            if teste==True:
                print(f'{existe}já estou aprendendo pra próxima{fim}')
            else:
                aprender.append(f'{chute.lower()}')
                print(f'{existe}vou aprender pra próxima{fim}')
                arq.write(f'{chute.lower()}\n')

        elif len(chute)!=len(escolha):
            print(f'{existe}A palavra escolhida tem {len(escolha)} letras{fim}')
    print(f'{certo}você acertou com {palpites} palpites{fim}')
    n=input('Deseja um novo jogo? ').upper()
    if n=='N':
        break
print('\033[034m{::^30}\033[m'.format('volte logo'))
arq.close()