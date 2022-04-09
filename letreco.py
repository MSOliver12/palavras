from random import randint
print('\033[35m{::^38}\033[m'.format('letroca'))
ten=1
palavras=['massa','mamao','mamae','rural','moral','parto','pedra','terno','lixar','morar','mucho','muito','grita','mudar','mesas','festa','nesta','achar','estar','ligar','potes','amora','limpo','limao','pilao','litro','limpa','girar','tirar','tiram','vasco','luxar','mirar','puxar','corar','casar','carro','arroz','anjos','lutar','grana','grama','famas','fones','fonte','puxar','lugar','pixar','pista','pinho','prato','prata','praia','motor','rodar','rodas','vasos','pasto','banho','trono','teste','besta','mesma','lesma','livro','livre','luvas','chuva','vazio','ficha']
palavra=palavras[randint(0,len(palavras)-1)]
print('A palavra escolhida tem 5 letras')
esc=input('Qual a palavra? ').lower().strip()
if palavra == esc:
    print('\033[032mA PALAVRA É {}\033[m'.format(esc.upper()))
    print('VOCÊ USOU {} TENTATIVAS'.format(ten))
    print('\033[035m{::^38}\033[m'.format('Fim'))
while len(esc)!=5:
        print('A palavra {} não tem 5 letras'.format(esc))
        esc=input('Qual a palavra? ').strip().lower()
while len(esc)==5:
    while palavra!=esc:
        t1 = esc[0] in palavra
        t2 = esc[1] in palavra
        t3 = esc[2] in palavra
        t4 = esc[3] in palavra
        t5 = esc[4] in palavra
        if t1==True:
            if esc[0]==palavra[0]:
                l1='\033[032m{}\033[m'.format(esc[0].upper())
            else:
                l1='\033[033m{}\033[m'.format(esc[0].upper())
        else:
            l1='\033[031m{}\033[m'.format(esc[0].upper())
        if t2==True:
            if esc[1]==palavra[1]:
                l2='\033[032m{}\033[m'.format(esc[1].upper())
            else:
                l2='\033[033m{}\033[m'.format(esc[1].upper())
        else:
            l2='\033[031m{}\033[m'.format((esc[1]).upper())
        if t3==True:
            if esc[2]==palavra[2]:
                l3='\033[032m{}\033[m'.format(esc[2].upper())
            else:
                l3='\033[033m{}\033[m'.format(esc[2].upper())
        else:
            l3='\033[031m{}\033[m'.format(esc[2].upper())
        if t4==True:
            if esc[3]==palavra[3]:
                l4='\033[032m{}\033[m'.format(esc[3].upper())
            else:
                l4='\033[033m{}\033[m'.format(esc[3].upper())
        else:
            l4='\033[031m{}\033[m'.format(esc[3].upper())
        if t5==True:
            if esc[4]==palavra[4]:
                l5='\033[032m{}\033[m'.format(esc[4].upper())
            else:
                l5='\033[033m{}\033[m'.format(esc[4].upper())
        else:
            l5='\033[031m{}\033[m'.format(esc[4].upper())
        print(l1, l2, l3, l4,l5)
        ten=ten+1
        esc=input('Qual a palavra? ').lower().strip()
        while len(esc) != 5:
            print('A palavra {} não tem 5 letras'.format(esc))
            esc = input('Qual a palavra? ').strip().lower()
        if palavra == esc:
            print('\033[032mA PALAVRA É {}\033[m'.format(esc.upper()))
            print('VOCÊ USOU {} TENTATIVAS'.format(ten))
            print('\033[035m{::^38}\033[m'.format('Fim'))


