import math
import time
global pontos
pontos = 0
n_questoes = 0
acertos = 0
erros = 0
jogador = []

def intro1():
    print('----------------------')
    print('GAME PYTHON DO MILHÃO')
    print('----------------------')
    print('Desenvolvedores: Ana Giulia,'
        ' Arthur Bernardo e Matheus Pfau.')
    time.sleep(2)
    nome = str()
    while True:
        nome = str(input("\nAntes de começarmos, insira o seu nome: "))
        jogador.append(nome)
        if nome.isalpha():
            break
        else:
            print ("Você digitou números ao invés de letras, no espaço nome.")
    for x in jogador:
        print ("\nSeja bem vindo", x, "ao jogo Python do Milhão!")
    time.sleep(2)

#-----------------------------------------------------------------------------

def pergunta1():
    print('\nQuestão 1 - Saúde Mental')
    print('A primeira questão será sobre distúrbios afetivos!')
    time.sleep(3)
    print('\nSão exemplos de distúrbios afetivos:')
    print('a)Depressão e distúrbio bipolar \nb)Fobia e distúrbios dissociativos\nc)Depressão e distúrbio de ansiedade\nd)Distúrbio bipolar e pânico\ne)Distúrbio bipolar e fobia')

    letraA = ("A")
    letraB = ("B")
    letraC = ("C")
    letraD = ("D")
    letraE = ("E")
    resp1 = str(input("Sua resposta: ")).upper()
    
    
    while resp1 != letraA and resp1 != letraB and resp1 != letraC and resp1 != letraD and resp1 != letraE :
        print ("\nPor favor insira uma letra correta.")
        time.sleep(2)
        print('\nQuestão 1 - Saúde Mental')
        print('\nSão exemplos de distúrbios afetivos:')
        print('a)Depressão e distúrbio bipolar \n'
              'b)Fobia e distúrbios dissociativos\n'
              'c)Depressão e distúrbio de ansiedade\n'
              'd)Distúrbio bipolar e pânico\n'
              'e)Distúrbio bipolar e fobia')
        resp1 = str(input("Sua resposta: ")).upper()
    else:
        return resp1

def correcao1(resp1):
    global acertos
    global erros
    global n_questoes
    global pontos
    if resp1 == "A" or resp1 == "a":
        print('\nParabéns você ganhou R$20.000,00 reais.')
        pontos+=20.000
        acertos = acertos + 1
        n_questoes = n_questoes + 1 
    else:
        pontos-=0
        erros = erros + 1
        n_questoes = n_questoes + 1        
    
        print('Que pena, você errou está questão, a alternativa correta era a letra A).')
        time.sleep(2)
        print('\nVeja agora a explicação do exercício:')
        print('\nA depressão é um distúrbio afetivo que acompanha a humanidade ao longo de'
              'sua história. No sentido patológico, há presença de tristeza, pessimismo,'
              'baixa auto-estima, que aparecem com frequência e podem combinar-se entre si.'
              'O Transtorno Afetivo Bipolar é uma doença que caracteriza-se por episódios '
              'repetidos, nos quais o humor e os níveis de atividade do paciente estão'
              'significativamente perturbados.')
        
#---------------------------------------------------------------------------------

def pergunta2():
    time.sleep(3)
    print('\nQuestão 2 - Saúde Mental')
    print('A segunda questão será sobre a definição de depressão!')
    time.sleep(3)
    print('\nA Depressão pode ser conceituada como:')
    print('a)Perturbação do pensamento\n'
          'b)Um estado mais intenso e persistente que a tristeza\n'
          'c)Um estado de crises decorrentes dos profundos conflitos mentais\n'
          'd)Distúrbios afetivos que podem interferir em pensamentos da realidade\n'
          'e)Um estado de perturbação, desordem mental e fobia')

    letraA = ("A")
    letraB = ("B")
    letraC = ("C")
    letraD = ("D")
    letraE = ("E")
    resp2 = str(input("Sua resposta: ")).upper()
    
    while resp2 != letraA and resp2 != letraB and resp2 != letraC and resp2 != letraD and resp2 != letraE :
        print ("\nPor favor insira uma letra correta.")
        time.sleep(2)
        print('--------------------------------------')
        print('\nQuestão 2 - Saúde Mental')
        print('\nA Depressão pode ser conceituada como:')
        print('a)Perturbação do pensamento\nb)Um estado mais intenso e persistente que a tristeza\nc)Um estado de crises decorrentes dos profundos conflitos mentais\n)d)Distúrbios afetivos que podem interferir em pensamentos da realidade\ne)Um estado de perturbação, desordem mental e fobia')

        resp2 = str(input("Sua resposta: ")).upper()
    else:
        return resp2


    
def correcao2(resp2):
    global acertos
    global erros
    global n_questoes
    global pontos
    
    
    if resp2 == "B" or resp2 == "b":
        print('\nParabéns você ganhou R$30.000,00 reais')
        pontos+=30.000
        acertos = acertos + 1
        n_questoes = n_questoes + 1 
    else:
        pontos-=0
        erros = erros + 1
        n_questoes = n_questoes + 1
        
        print('Que pena, você errou está questão, a alternativa correta era a letra B).')
        time.sleep(2)
        print('\nVeja agora a explicação do exercício:')
        print('\nA depressão é um estado mais intenso e persistente que a tristeza.'
              'É típico do deprimido sentir-se sem remédio e rejeitado.'
              'Podem ocorrer pensamentos de morte, até mesmo de suicídio.')

              
#-----------------------------------------------------------------------

def pergunta3():
    time.sleep(3)
    print('\nQuestão 3 - Saúde Mental')
    print('A terceira questão será sobre a relação do sistema prisional para com os pacientes mentalmente doentes!')
    time.sleep(4)
    print('\nNas últimas décadas, muitos pacientes mentalmente doentes nos Estados Unidos passaram a ser moradores de rua ou acabaram no sistema prisional. Qual das seguintes opções contribuiu para este problema?')
    print('a)Criminalização da doença mental\n'
          'b)Desintegração da família\n'
          'c)Desinstitucionalização\n'
          'd)Recessão econômica\n'
          'e)Distúrbio bipolar e fobia')

    letraA = ("A")
    letraB = ("B")
    letraC = ("C")
    letraD = ("D")
    letraE = ("E")
    resp3 = str(input("Sua resposta: ")).upper()
    
    while resp3 != letraA and resp3 != letraB and resp3 != letraC and resp3 != letraD and resp3 != letraE :
        print ("\nPor favor insira uma letra correta.")
        time.sleep(2)
        print('\nQuestão 3 - Saúde Mental')
        print('\nNas últimas décadas, muitos pacientes mentalmente doentes nos Estados Unidos passaram a ser moradores de rua ou acabaram no sistema prisional. Qual das seguintes opções contribuiu para este problema?')
        print('a)Criminalização da doença mental\nb)Desintegração da família\nc)Desinstitucionalização\nd)Recessão econômica\ne)Distúrbio bipolar e fobia')

        resp3 = str(input("Sua resposta: ")).upper()
    else:
        return resp3


    
def correcao3(resp3):
    global acertos
    global erros
    global n_questoes
    global pontos
    
    if resp3 == "C" or resp3 == "c":
        print('\nParabéns você ganhou R$50.000,00 reais.')
        pontos+=50.000
        acertos = acertos + 1
        n_questoes = n_questoes + 1 
    else:
        pontos-=0
        erros = erros + 1
        n_questoes = n_questoes + 1
        
        print('Que pena, você errou está questão, a alternativa correta era a letra C).')
        time.sleep(2)
        print('\nVeja agora a explicação do exercício:')
        print('\nHouve um movimento para trazer pessoas mentalmente doentes para fora das instituições'
              '(desinstitucionalização) e ampará-las de modo que elas possam viver em comunidade.'
              'Esse movimento tornou-se possível com o desenvolvimento de medicamentos eficazes em '
              'conjunto com algumas mudanças de atitude com relação aos doentes mentais.'
              'Entretanto, como as leis atualmente não permitem que pessoas com doenças mentais que'
              'não representam um perigo para si próprias ou para a sociedade sejam institucionalizadas'
              'ou tratadas contra a sua vontade, muitas delas tornam-se moradoras de rua ou acabam no sistema prisional.')


#--------------------------------------------------------------------

def pergunta4():
    time.sleep(3)
    print('\nQuestão 4 - Saúde Mental')
    print('A quarta questão será sobre a definição de algum tipo de transtorno psicológico!')
    time.sleep(4)
    print('\nTranstorno psicológico em que o indivíduo ao ver-se no espelho acha que tem mais peso do que realmente tem e sofre após a refeição.')
    print('a)Esquizofrenia\n'
          'b)Anorexia\n'
          'c)Bulimia\n'
          'd)Autismo\n'
          'e)Depressão Sistêmica')

    letraA = ("A")
    letraB = ("B")
    letraC = ("C")
    letraD = ("D")
    letraE = ("E")
    resp4 = str(input("Sua resposta: ")).upper()
    
    while resp4 != letraA and resp4 != letraB and resp4 != letraC and resp4 != letraD and resp4 != letraE :
        print ("\nPor favor insira uma letra correta.")
        time.sleep(2)
        print('\nQuestão 4 - Saúde Mental')
        print('\nTranstorno psicológico em que o indivíduo ao ver-se no espelho acha que tem mais peso do que realmente tem e sofre após a refeição.')
        print('a)Esquizofrenia\n'
              'b)Anorexia\n'
              'c)Bulimia\n'
              'd)Autismo\n'
              'e)Depressão Sistêmica')
        
        resp4 = str(input("Sua resposta: ")).upper()
    else:
        return resp4


    
def correcao4(resp4):
    global acertos
    global erros
    global n_questoes
    global pontos
    
    if resp4 == "B" or resp4 == "b":
        print('\nParabéns você ganhou R$70.00,00 reais.')
        pontos+=70.000
        acertos = acertos + 1
        n_questoes = n_questoes + 1 
    else:
        pontos-=0
        erros = erros + 1
        n_questoes = n_questoes + 1
        
        print('Que pena, você errou está questão, a alternativa correta era a letra B).')
        time.sleep(2)
        print('\nVeja agora a explicação do exercício:')
        print('\nA anorexia, também chamada de anorexia nervosa, é um transtorno alimentar '
              'capaz de afetar pessoas de ambos os sexos, causado por um desejo excessivo,'
              'ilimitado e sem controle de emagrecer e se manter em um determinado padrão de beleza.')

#-------------------------------------------------------------------

def pergunta5():
    time.sleep(3)
    print('\nQuestão 5 - Saúde Mental')
    print('A quinta questão será sobre os sintomas de uma crise de pânico!')
    time.sleep(4)
    print('\nQuais desses sintomas estão presentes durante uma crise do pânico?')
    print('a)Arritmia\n'
          'b)Dores / Desconforto\n'
          'c)Medo de morrer\n'
          'd)Sensação de engasgo\n'
          'e)Todas as alternativas acima')

    letraA = ("A")
    letraB = ("B")
    letraC = ("C")
    letraD = ("D")
    letraE = ("E")
    resp5 = str(input("Sua resposta: ")).upper()
    
    while resp5 != letraA and resp5 != letraB and resp5 != letraC and resp5 != letraD and resp5 != letraE :
        print ("\nPor favor insira uma letra correta.")
        time.sleep(2)
        print('\nQuestão 5 - Saúde Mental')
        print('\nQuais desses sintomas estão presentes durante uma crise do pânico?')
        print('a)Arritmia\n'
              'b)Dores / Desconforto\n'
              'c)Medo de morrer\n'
              'd)Sensação de engasgo\n'
              'e)Todas as alternativas acima')
        
        resp5 = str(input("Sua resposta: ")).upper()
    else:
        return resp5


    
def correcao5(resp5):
    global acertos
    global erros
    global n_questoes
    global pontos
    
    if resp5 == "E" or resp5 == "e":
        print('\nParabéns você ganhou R$100.00,00 reais.')
        pontos+=100.000
        acertos = acertos + 1
        n_questoes = n_questoes + 1 
    else:
        pontos-=0
        erros = erros + 1
        n_questoes = n_questoes + 1
        
        print('Que pena, você errou está questão, a alternativa correta era a letra E).')
        time.sleep(2)
        print('\nVeja agora a explicação do exercício:')
        print('Todas as alternativas se enquadrão em um momento de crise de pânico')        

#------------------------------------------------------------------

def pergunta6():
    time.sleep(3)
    print('\nQuestão 6 - Saúde Mental')
    print('A sexta questão será sobre os sintomas de uma crise de ansiedade!')
    time.sleep(4)
    print('\nQuais dos sintomas abaixo estão presentes durante uma crise de ansiedade?')
    print('a)Falta de ar\n'
          'b)Palpitação\n'
          'c)Tremores\n'
          'd)Formigamento\n'
          'e)Todas as alternativas acima')

    letraA = ("A")
    letraB = ("B")
    letraC = ("C")
    letraD = ("D")
    letraE = ("E")
    resp6 = str(input("Sua resposta: ")).upper()
    
    while resp6 != letraA and resp6 != letraB and resp6 != letraC and resp6 != letraD and resp6 != letraE :
        print ("\nPor favor insira uma letra correta.")
        time.sleep(2)
        print('\nQuestão 6 - Saúde Mental')
        print('\nQuais desses sintomas estão presentes durante uma crise do pânico?')
        print('a)Arritmia\n'
              'b)Dores / Desconforto\n'
              'c)Medo de morrer\n'
              'd)Sensação de engasgo\n'
              'e)Todas as alternativas acima')
        
        resp6 = str(input("Sua resposta: ")).upper()
    else:
        return resp6


    
def correcao6(resp6):
    global acertos
    global erros
    global n_questoes
    global pontos
    
    if resp6 == 'E' or resp6 == "e":
        print('\nParabéns você ganhou R$120.00,00 reais.')
        pontos+=120.000
        acertos = acertos + 1
        n_questoes = n_questoes + 1 
    else:
        pontos-=0
        erros = erros + 1
        n_questoes = n_questoes + 1
    
        print('Que pena, você errou está questão, a alternativa correta era a letra E).')
        time.sleep(2)
        print('\nVeja agora a explicação do exercício:')
        print('Nessa questão todas as alternativas se relacionam a uma crise de pânico!')


#---------------------------------------------------------------------------
def pergunta7():
    time.sleep(3)
    print('\nQuestão 7 - Saúde Mental')
    print('A sétima questão será sobre a definição de inteligência emocional!')
    time.sleep(4)
    print('\nO que é inteligência emocional ?')
    print('a)Capacidade de identificar e lidar com as emoções e sentimentos pessoais e de outros indivíduos\n'
        'b)Não dar importância aos sentimento das outras pessoas\n'
        'c)Não dar importância aos próprios sentimentos e emoções\n'
        'd)Capacidade de identificar e lidar com os próprios sentimentos e emoções\n'
        'e)Todas as alternativas acima.')

    letraA = ("A")
    letraB = ("B")
    letraC = ("C")
    letraD = ("D")
    letraE = ("E")
    resp7 = str(input("Sua resposta: ")).upper()
    
    while resp7 != letraA and resp7 != letraB and resp7 != letraC and resp7 != letraD and resp7 != letraE :
        print ("\nPor favor insira uma letra correta.")
        time.sleep(2)
        print('\nQuestão 7 - Saúde Mental')
        print('\nO que é inteligência emocional ?')
        print('a)Capacidade de identificar e lidar com as emoções e sentimentos pessoais e de outros indivíduos\n'
            'b)Não dar importância aos sentimento das outras pessoas\n'
            'c)Não dar importância aos próprios sentimentos e emoções\n'
            'd)Capacidade de identificar e lidar com os próprios sentimentos e emoções\n'
            'e)Todas as alternativas acima')
        
        resp7 = str(input("Sua resposta: ")).upper()
    else:
        return resp7


    
def correcao7(resp7):
    global acertos
    global erros
    global n_questoes
    global pontos
    
    if resp7 == 'A' or resp7 == "a":
        print('\nParabéns você ganhou R$130.00,00 reais.')
        pontos+=130.000
        acertos = acertos + 1
        n_questoes = n_questoes + 1 
    else:
        pontos-=0
        erros = erros + 1
        n_questoes = n_questoes + 1
        
        print('Que pena, você errou está questão, a alternativa correta era a letra A).')
        time.sleep(2)
        print('\nVeja agora a explicação do exercício:')
        print('De acordo com a psicologia, inteligência emocional é a capacidade de '
              'identificar e lidar com as emoções e sentimentos pessoais e de outros'
              'indivíduos. Um exemplo é a pessoa que consegue terminar suas tarefas e'
              'atingir suas metas, mesmo sentindo-se triste e ansiosa ao longo de um '
              'dia de trabalho')



#-------------------------------------------------------------------------

def pergunta8():
    time.sleep(3)
    print('\nQuestão 8 - Saúde Mental')
    print('A oitava questão está relacionada em descobrir a alternativa verdadeira!')
    time.sleep(3)
    print('\nQual é a alternativa correta?')
    print('a)O acolhimento é o mesmo que escuta\n'
        'b)O empoderamento é o mesmo que dependência do sujeito\n'
        'c)O acolhimento é uma escuta ampliada por qualquer pessoa\n'
        'd)O acolhimento é uma prática permitida apenas na área de Saúde\n'
        'e)O acolhimento só pode ser feito pelo psicólogo')

    letraA = ("A")
    letraB = ("B")
    letraC = ("C")
    letraD = ("D")
    letraE = ("E")
    resp8 = str(input("Sua resposta: ")).upper()
    
    while resp8 != letraA and resp8 != letraB and resp8 != letraC and resp8 != letraD and resp8 != letraE :
        print ("\nPor favor insira uma letra correta.")
        time.sleep(2)
        print('\nQuestão 8 - Saúde Mental')
        print('\nQual é a alternativa correta?')
        print('a)O acolhimento é o mesmo que escuta\n'
              'b)O empoderamento é o mesmo que dependência do sujeito\n'
              'c)O acolhimento é uma escuta ampliada por qualquer pessoa\n'
              'd)O acolhimento é uma prática permitida apenas na área de Saúde\n'
              'e)O acolhimento só pode ser feito pelo psicólogo')
        
        resp8 = str(input("Sua resposta: ")).upper()
    else:
        return resp8


    
def correcao8(resp8):
    global acertos
    global erros
    global n_questoes
    global pontos
    
    if resp8 == 'C' or resp8 == "c":
        print('\nParabéns você ganhou R$140.00,00 reais.')
        pontos+=140.000
        acertos = acertos + 1
        n_questoes = n_questoes + 1 
    else:
        pontos-=0
        erros = erros + 1
        n_questoes = n_questoes + 1
    
        print('Que pena, você errou está questão, a alternativa correta era a letra C).')
        time.sleep(2)
        print('\nVeja agora a explicação do exercício:')
        print('O acolhimento é visto como uma prática de altruísmo que nessa situação pode ajudar uma pessoa que necessita de ajuda, por meio de desabafos e troca de confidências a terceiros!')


#----------------------------------------------------------------------        


def pergunta9():
    time.sleep(3)
    print('\nQuestão 9 - Saúde Mental')
    print('A nova questão está relacionada ao número do Centro de Valorização da Vida!')
    time.sleep(4)
    print('\nO Centro de Valorização da Vida, central telefônica, funciona nacionalmente e 24 horas por dia para que pessoas possam desabafar e receber apoio especializado em momentos difíceis. Qual o número do CVV?')
    print('a)141\n'
        'b)191\n'
        'c)190\n'
        'd)181\n'
        'e)145')

    letraA = ("A")
    letraB = ("B")
    letraC = ("C")
    letraD = ("D")
    letraE = ("E")
    resp9 = str(input("Sua resposta: ")).upper()
    
    while resp9 != letraA and resp9 != letraB and resp9 != letraC and resp9 != letraD and resp9 != letraE :
        print ("\nPor favor insira uma letra correta.")
        time.sleep(2)
        print('\nQuestão 9 - Saúde Mental')
        print('\nO Centro de Valorização da Vida, central telefônica, funciona nacionalmente e 24 horas por dia para que pessoas possam desabafar e receber apoio especializado em momentos difíceis. Qual o número do CVV?')
        print('a)141\n'
            'b)191\n'
            'c)190\n'
            'd)181\n'
            'e)145')
        
        resp9 = str(input("Sua resposta: ")).upper()
    else:
        return resp9


    
def correcao9(resp9):
    global acertos
    global erros
    global n_questoes
    global pontos
    
    if resp9 == 'A' or resp9 == "a":
        print('\nParabéns você ganhou R$150.00,00 reais.')
        pontos+=150.000
        acertos = acertos + 1
        n_questoes = n_questoes + 1 
        
    else:
        pontos-=0
        erros = erros + 1
        n_questoes = n_questoes + 1
    
        print('Que pena, você errou está questão, a alternativa correta era a letra A).')
        time.sleep(2)
        print('\nVeja agora a explicação do exercício:')
        print('O CVV - Centro de Valorização da Vida (141) realiza apoio emocional e prevenção do suicídio,'
              'atendendo voluntária e gratuitamente todas as pessoas que querem e precisam '
              'conversar, sob total sigilo por telefone, email e chat 24 horas todos os dias.')


#------------------------------------------------------------------


def pergunta10():
    time.sleep(3)
    print('\nQuestão 10 - Saúde Mental')
    print('A décima questão será sobre o nome da alteração química presente nas pessoas com depressão!')
    time.sleep(4)
    print('\nO cérebro de uma pessoa com depressão mostra alterações químicas em relação a alguns neurotransmissores. Entre eles está:')
    print('a)Clomipramina\n'
        'b)Acetilcolina\n'
        'c)Adrenalina\n'
        'd)Serotonina\n'
        'e)Todas as alternativas estão corretas.')

    letraA = ("A")
    letraB = ("B")
    letraC = ("C")
    letraD = ("D")
    letraE = ("E")
    resp10 = str(input("Sua resposta: ")).upper()
    
    while resp10 != letraA and resp10 != letraB and resp10 != letraC and resp10 != letraD and resp10 != letraE :
        print ("\nPor favor insira uma letra correta.")
        time.sleep(2)
        print('\nQuestão 10 - Saúde Mental')
        print('\nO cérebro de uma pessoa com depressão mostra alterações químicas em relação a alguns neurotransmissores. Entre eles está:')
        print('a)Clomipramina\n'
            'b)Acetilcolina\n'
            'c)Adrenalina\n'
            'd)Serotonina\n'
            'e)Todas as alternativas estão corretas.')
        
        resp10 = str(input("Sua resposta: ")).upper()
    else:
        return resp10


    
def correcao10(resp10):
    global acertos
    global erros
    global n_questoes
    global pontos
    
    if resp10 == 'D' or resp10 == "d":
        print('\nParabéns você ganhou R$200.00,00 reais.')
        pontos+=200.000
        acertos = acertos + 1
        n_questoes = n_questoes + 1 
    else:
        pontos-=0
        erros = erros + 1
        n_questoes = n_questoes + 1
    
        print('Que pena, você errou está questão, a alternativa correta era a letra D).')
        time.sleep(2)
        print('\nVeja agora a explicação do exercício:')
        print('A Serotonina em baixa concentração, pode trazer'
              'algumas consequências para as pessoas e é relacionada,'
              'muitas vezes, com pacientes que sofrem com a depressão,'
              'por ser associada com o humor.')


#------------------------------------------------------------------
        
def main():
    nome = intro1()

    resp1 = pergunta1()
    correcao1(resp1)
    print('\nPontuação:',pontos)
    print('Respostas certas:', acertos)
    print('Respostas erradas:', erros) 
    print('Desempenho:', n_questoes, 'de 10' )

    resp2 = pergunta2()
    correcao2(resp2)
    print('\nPontuação:',pontos)
    print('Respostas certas:', acertos)
    print('Respostas erradas:', erros)
    print('Desempenho:', n_questoes, 'de 10' )

    resp3 = pergunta3()
    correcao3(resp3)
    print('\nPontuação:',pontos)
    print('Respostas certas:', acertos)
    print('Respostas erradas:', erros)
    print('Desempenho:', n_questoes, 'de 10' )


    resp4 = pergunta4()
    correcao4(resp4)
    print('\nPontuação:',pontos)
    print('Respostas certas:', acertos)
    print('Respostas erradas:', erros)
    print('Desempenho:', n_questoes, 'de 10' )


    resp5 = pergunta5()
    correcao5(resp5)
    print('\nPontuação:',pontos)
    print('Respostas certas:', acertos)
    print('Respostas erradas:', erros)
    print('Desempenho:', n_questoes, 'de 10' )


    resp6 = pergunta6()
    correcao6(resp6)
    print('\nPontuação:',pontos)
    print('Respostas certas:', acertos)
    print('Respostas erradas:', erros)
    print('Desempenho:', n_questoes, 'de 10' )


    resp7 = pergunta7()
    correcao7(resp7)
    print('\nPontuação:',pontos)
    print('Respostas certas:', acertos)
    print('Respostas erradas:', erros)
    print('Desempenho:', n_questoes, 'de 10' )


    resp8 = pergunta8()
    correcao8(resp8)
    print('\nPontuação:',pontos)
    print('Respostas certas:', acertos)
    print('Respostas erradas:', erros)
    print('Desempenho:', n_questoes, 'de 10' )


    resp9 = pergunta9()
    correcao9(resp9)
    print('\nPontuação:',pontos)
    print('Respostas certas:', acertos)
    print('Respostas erradas:', erros)
    print('Desempenho:', n_questoes, 'de 10' )
    
    resp10 = pergunta10()
    correcao10(resp10)
    print('\nPontuação:',pontos)
    print('Respostas certas:', acertos)
    print('Respostas erradas:', erros)
    print('Desempenho:', n_questoes, 'de 10' )
main()
