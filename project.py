######################################################
#                                                    #
#   UNIDADE CURRICULAR: Fundamentos da Programacao   #
#                                                    #
#   TEMA: Jogo do Galo                               #
#                                                    #
#                                                    #
#   NOME: Goncalo Nunes                              #
#   NUMERO: 99074                                    #
#                                                    #
######################################################


# Esta funcao verifica se o argumento inserido corresponde a um tabuleiro
# eh_tabuleiro: universal -> booleano
def eh_tabuleiro(valor):
    """
    Verifica se um determinado valor e um tabuleiro valido.

    Parametros:
        valor (any): Possivel tabuleiro.

    Retorna:
        (bool): True se for tabuleiro e False se nao for.
   """

    tamanho = 3    
    num_validos = (1, 0, -1)

    if type(valor) != tuple or len(valor) != tamanho:
        return False

    for el in valor:
        if type(el) != tuple or len(el) != tamanho:
            return False
        for num in el:
            if type(num) != int or num not in num_validos:
                return False

    return True


# Esta funcao verifica se o argumento inserido corresponde a uma posicao valida
# eh_posicao: universal -> booleano
def eh_posicao(pos):
    """
    Verifica se um determinado valor e uma posicao valida

    Parametros:
        pos (universal): Possivel posicao.

    Retorna:
        (bool): True se for numero valido e False se nao for.
   """
    return False if type(pos) != int or pos < 1 or pos > 9 else True


# Esta funcao obtem os valores das posicoes da coluna inserida
# obter_coluna: tabuleiro x inteiro -> vetor
def obter_coluna(tab, num):
    """
    Obtem os valores das posicoes de uma determinada coluna

    Parametros:
        tab (tuplo): tabuleiro a verificar
        num (int): toluna a obter.

    Retorna:
        coluna (tuplo): tuplo com os valores da coluna fornecida.
   """
    if not eh_tabuleiro(tab) or type(num) != int or num < 1 or num > 3:
        raise ValueError("obter_coluna: algum dos argumentos e invalido")
    
    coluna = ()
    for linha in tab:
        coluna += (linha[num-1],)

    return coluna


# Esta funcao obtem os valores das posicoes da linha inserida
# obter_linha: tabuleiro x inteiro -> vetor 
def obter_linha(tab, num):
    """
    Obtem os valores das posicoes de uma determinada linha

    Parametros:
        tab (tuplo): Tabuleiro a verificar
        num (int): Linha a obter.

    Retorna:
        linha (tuplo): tuplo com os valores da linha fornecida
   """
    if not eh_tabuleiro(tab) or type(num) != int or num < 1 or num > 3:
        raise ValueError("obter_linha: algum dos argumentos e invalido")
    
    linha = ()
    for el in tab[num-1]:
        linha += (el,)

    return linha


# Esta funcao obtem os valores das posicoes da diagonal inserida
# obter_diagonal: tabuleiro x inteiro -> vetor
def obter_diagonal(tab, num):
    """
    Obtem os valores de uma determinada diagonal

    Parametros:
        tab (tuplo): Tabuleiro a verificar
        num (int): (1 -> diagonal descendente da esquerda para a direita \
             2 -> diagonal ascendente da esquerda para a direita)

    Retorna:
        diagonal (tuplo): valores da diagonal.
   """
    if not eh_tabuleiro(tab) or type(num) != int or num < 1 or num > 2:
        raise ValueError("obter_diagonal: algum dos argumentos e invalido")

    diagonal = ()
    for i in range(len(tab)): 
        coluna = obter_coluna(tab, i+1)
        if num == 1:
            diagonal += (coluna[i],)
        else: 
            diagonal += (coluna[-(i+1)],)

    return diagonal


# Esta funcao auxiliar converte uma determinada posicao para a linha, coluna 
# e diagonal/diagonais que a contem
# posicao_para_coordenadas: inteiro -> tuplo
def posicao_para_coordenadas(pos):
    """
    Obtem as coordenadas de uma dada posicao

    Parametros:
        pos (int): posicao a obter coordenadas
    
    Retorna:
        (tuplo): tuplo de 3 elementos em que o primeiro corresponde a linha,\
             o segundo a coluna e o terceiro a diagonal da posicao fornecida
    """
    if not eh_posicao(pos):
        raise ValueError("posicao_para_coordenadas: argumento invalido")
    
    coordenadas = {
        1: (1, 1, 1),
        2: (1, 2, None),
        3: (1, 3, 2),
        4: (2, 1, None),
        5: (2, 2, (1,2)),
        6: (2, 3, None),
        7: (3, 1, 2),
        8: (3, 2, None),
        9: (3, 3, 1)
    }

    return coordenadas[pos]


# Funcao auxiliar que retorna a linha, coluna e diagonal de uma coordenada
# converter_coordenadas: tuplo -> inteiro, inteiro, inteiro ou tuplo ou None
def converter_coordenadas(coordenadas):
    """
    Retorna a linha, coluna e diagonal de uma coordenada

    Parametros:
        coordenadas (tuplo)
    
    Retorna: 
        linha (int): linha correspondente a coordenada
        coluna (int): coluna correspondente a coordenada
        diagonal (int, tuplo ou None): diagonal correspondente a coordenada, 
        tuplo de diagonais no caso da posicao central
         ou None caso a posicao nao seja abrangida por uma diagonal
    """
    return coordenadas[0], coordenadas[1], coordenadas[2]


# Funcao auxiliar que vai converter o tabuleiro e as respetivas linhas para listas
# tabuleiro_lst: tabuleiro -> lista
def tabuleiro_lst(tab):
    """
    Converte o tabuleiro de tuplos para listas

    Parametros:
        tab (tuplo): Tabuleiro a converter
        
    Retorna:
        tabuleiro (lista): Tabuleiro do tipo lista.
   """
    if not eh_tabuleiro(tab):
        raise ValueError("tabuleiro_lst: o argumento e invalido")

    tabuleiro = list(tab)
    for i in range(len(tab)):
        tabuleiro[i] = list(tab[i])
    return tabuleiro


# Funcao auxiliar que vai converter o tabuleiro de listas em tuplos
# tabuleiro_tpl: lista -> tabuleiro
def tabuleiro_tpl(tab):
    """
    Converte o tabuleiro de tuplos para listas

    Parametros:
        tab (lista): Tabuleiro a converter
        
    Retorna:
        tabuleiro (tuplo): Tabuleiro do tipo tuplo
   """

    for i in range(len(tab)):
        tab[i] = tuple(tab[i])

    tabuleiro = tuple(tab)

    return tabuleiro


# Esta funcao obtem a representacao grafica do tabuleiro 
# para que esta possa ser mostrada ao utilizador posteriormente
# tabuleiro_str: tabuleiro -> string
def tabuleiro_str(tab):
    """
    Obtem a representacao grafica do tabuleiro

    Parametros:
        tab (tuplo): Tabuleiro a desenhar
        
    Retorna:
        tabuleiro_string (string): Tabuleiro em formato string.
   """

    if not eh_tabuleiro(tab):
        raise ValueError("tabuleiro_str: o argumento e invalido")
    
    tabuleiro_string = ""
    tabuleiro = tabuleiro_lst(tab)
    for j, linha in enumerate(tabuleiro):
        for i in range((len(linha))):
            linha[i] = " X " if linha[i] == 1 else " O " if linha[i] == -1 else "   "

            tabuleiro_string +=  linha[i] + ("|" if i < len(linha)-1 \
                else "\n-----------\n" if j < len(tabuleiro)-1 else "")

    return tabuleiro_string
    

# Funcao auxiliar que obtem o valor de uma determinada posicao no tabuleiro
# obter_posicao: tabuleiro x posicao -> jogador ou 0
def obter_posicao(tab, pos):
    """
    Obtem o valor de uma dada posicao, esta pode estar livre 
    ou ocupada por qualquer um dos jogadores

    Parametros: 
        tab (tabuleiro): tabuleiro a analisar
        pos (posicao): posicao a analisar
    
    Retorna:
        valor (jogador ou 0): jogador que ocupa a posicao 
        ou 0 se a posicao estiver livre
    """
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError("obter_posicao: algum dos argumentos e invalido")

    coordenadas = posicao_para_coordenadas(pos)
    linha, coluna, _ = converter_coordenadas(coordenadas)

    valor = obter_linha(tab, linha)[coluna-1]

    return valor


# Esta funcao verifica se a posicao do tabuleiro fornecido esta livre 
# eh_posicao_livre: tabuleiro x posicao -> booleano
def eh_posicao_livre(tab, pos):
    """
    Verifica se uma determinada posicao do tabuleiro esta livre.

    Parametros:
        tab (tabuleiro): tabuleiro de jogo.

    Retorna:
        (bool): True se a posicao estiver livre e False se nao estiver.
   """
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")
    
    return True if obter_posicao(tab, pos) == 0 else False

 
# Esta funcao obtem todas as posicoes livres do tabuleiro inserido
# obter_posicoes_livres: tabuleiro -> vetor
def obter_posicoes_livres(tab):
    """
    Obtem todas as posicoes livres ordenadas do tabuleiro

    Parametros:
        tab (tabuleiro): tabuleiro de jogo.

    Retorna:
        livres (vetor): posicoes livres ordenadas
    """
    if not eh_tabuleiro(tab):
        raise ValueError("obter_posicoes_livres: o argumento e invalido")
    
    posicoes = [x+1 for x in range(9)]
    
    livres = ()
    for pos in posicoes:
        if eh_posicao_livre(tab, pos):
            livres += (pos,)

    return livres


# Esta funcao determina se algum dos jogadores ganhou a partida
#  e em caso afirmativo, qual deles e o vencedor
# jogador_ganhador: tabuleiro -> jogador
def jogador_ganhador(tab):
    """
    Determina se algum dos jogadores ganhou a partida e se sim qual

    Parametros:
        tab (tabuleiro): tabuleiro de jogo.
    
    Retorna:
        (jogador): jogador que venceu a partida ou 0 caso ninguem tenha ganho
    """

    if not eh_tabuleiro(tab):
        raise ValueError("jogador_ganhador: o argumento e invalido")
    
    vitoria_x = (1, 1, 1)
    vitoria_o = (-1, -1, -1)

    i = 1
    while i <= 3:
        linha = obter_linha(tab, i)
        coluna = obter_coluna(tab, i)
        diagonal = obter_diagonal(tab, i) if i <= 2 else None
        conjunto = [linha] + [coluna] + [diagonal]
        
        if vitoria_x in conjunto:
            return 1
        elif vitoria_o in conjunto:
            return -1
        i += 1
    return 0
            

# Funcao auxiliar para verificar se um dado numero corresponde a um jogador
# eh_jogador: inteiro -> booleano
def eh_jogador(jogador):
    """
    Verifca se um determinado numero corresponde a um jogador

    Parametros:
        jogador (int): inteiro a verificar se e jogador
    
    Retorna:
        (bool): True se for um jogador valido e False se nao for
    """
    return type(jogador) == int and (jogador == 1 or jogador == -1)


# Esta funcao marca no tabuleiro uma determinada posicao livre
# com a marca do jogador inserido
# marcar_posicao: tabuleiro x jogador x posicao -> inteiro
def marcar_posicao(tab, jogador, pos):
    """
    Marca uma determinada posicao livre com a marca do jogador

    Parametros:
        tab (tabuleiro): tabuleiro de jogo.
        jogador (jogador): jogador que vai marcar a posicao.
        pos (posicao): posicao a ser marcada.
        
    Retorna:
        tabuleiro (tabuleiro): tabuleiro com a posicao marcada
    """

    if not eh_tabuleiro(tab) or not eh_jogador(jogador) \
        or not eh_posicao(pos) or not eh_posicao_livre(tab, pos):
        raise ValueError("marcar_posicao: algum dos argumentos e invalido")
    
    coordenadas = posicao_para_coordenadas(pos)
    linha, coluna, _ = converter_coordenadas(coordenadas)

    tabuleiro = tabuleiro_lst(tab)
    tabuleiro[linha-1][coluna-1] = jogador
    tabuleiro = tabuleiro_tpl(tabuleiro)

    return tabuleiro


# Esta funcao pede ao utilizador para escolher uma posicao livre do tabuleiro
# escolher_posicao_manual: tabuleiro -> posicao
def escolher_posicao_manual(tab):
    """
    Pede ao utilizador para escolher uma posicao livre do tabuleiro

    Parametros:
        tab (tabuleiro): tabuleiro de jogo.
        
    Retorna:
        pos (posicao): posicao escolhida
    """
    if not eh_tabuleiro(tab):
        raise ValueError("escolher_posicao_manual: o argumento e invalido")

    pos = int(input("Turno do jogador. Escolha uma posicao livre: "))

    if not eh_posicao(pos) or not eh_posicao_livre(tab, pos):
        raise ValueError("escolher_posicao_manual: a posicao introduzida e invalida")

    return pos


# Funcao auxiliar que verifica se a estrategia fornecida e ou nao uma estrategia valida
# eh_estrategia: string -> booleano
def eh_estrategia(strat):
    """
    Verificar se uma determinada string e uma estrategia valida

    Parametros:
        start (string): possivel estrategia

    Retorna: 
        (bool): True caso a estrategia seja valida e False caso contrario
    """
    strats = ("basico", "normal", "perfeito")
    return strat in strats


# Funcao auxiliar que obtem todas as posicoes ocupadas por um determinado jogador
# obter_posicoes_ocupadas: tabuleiro x jogador -> tuplo
def obter_posicoes_ocupadas(tab, jogador):
    """
    Obtem todas as posicoes ocupadas pelo jogador

    Parametros:
        tab (tabuleiro): tabuleiro a analisar
        jogador (jogador): jogador a verificar as posicoes ocupadas
    
    Retorna:
        pos_jogador (tuplo): tuplo com todas as posicoes ocupadas pelo jogador
    """
    pos_jogador = ()
    posicoes = [x+1 for x in range(9)]
    for pos in posicoes:
        if obter_posicao(tab, pos) == jogador:
            pos_jogador += (pos,)
    return pos_jogador


# Funcao auxiliar que obtem todas as colunas do tabuleiro
# obter_colunas: tabuleiro -> tuplo
def obter_colunas(tab):
    """
    Obtem todas as colunas do tabuleiro

    Parametros: 
        tab (tabuleiro): tabuleiro a analisar
    
    Retorna:
        colunas (tuplo): tuplo com 3 elementos do tipo tuplo com os 
        valores de cada coluna do tabuleiro
    """
    colunas = (obter_coluna(tab, 1), obter_coluna(tab, 2), obter_coluna(tab, 3))
    return colunas


# Funcao auxiliar que obtem todas as diagonais do tabuleiro
# obter_diagonais: tabuleiro -> tuplo
def obter_diagonais(tab):
    """
    Obtem todas as diagonais do tabuleiro

    Parametros: 
        tab (tabuleiro): tabuleiro a analisar
    
    Retorna:
        diagonais (tuplo): tuplo com 2 elementos do tipo tuplo
        com os valores de cada diagonal do tabuleiro
    """
    diagonais = (obter_diagonal(tab,1), obter_diagonal(tab, 2))
    return diagonais


# Funcao auxiliar que remove os elementos repetidos num tuplo
# remover_repetidos: tuplo -> tuplo
def remover_repetidos(tpl):
    """
    Remove os elementos repetidos de um tuplo

    Parametros:
        tpl (tuplo): tuplo a remover os elementos repetidos
    
    Retorna:
        res (tpl): tuplo sem elementos repetidos
    """
    res = ()
    for el in tpl:
        if el not in res:
            res += (el,)
    return res


# Funcao auxiliar que obtem os elementos repetidos de um tuplo
# obter_repetidos: tuplo -> tuplo
def obter_repetidos(tpl):
    """
    obtem os elementos repetidos de um tuplo

    Parametros: 
        tpl (tuplo): tuplo a obter os elemetos repetidos

    Retorna:
        res (tuplo): tuplo que contem os elementos repetidos do tuplo inserido
    """
    res = ()
    for el in tpl:
        if tpl.count(el) > 1:
            res += (el,)

    return remover_repetidos(res)
    
    
# Funcao auxiliar que remove as posicoes ocupadas de um tuplo de posicoes
# remover_posicoes_ocupadas: tabuleiro x tuplo -> tuplo
def remover_posicoes_ocupadas(tab, tpl):
    """
    Remove de um tuplo as posicoes no tabuleiro que estao ocupadas

    Parametros:
        tab (tabuleiro): tabuleiro a verificar se as posicoes estao ocupadas
        tpl (tuplo): tuplo a remover as posicoes ocupadas
    
    Retorna:
        livres (tuplo): tuplo em que todos os elementos sao posicoes livres do tabuleiro
    """
    livres = ()
    for el in tpl:
        if eh_posicao_livre(tab, el):
            livres += (el,)
    return livres




# Esta funcao obtem as posicoes de bifurcacao de um determinado jogador
# obter_bifurcacoes: tabuleiro x jogador -> tuplo
def obter_bifurcacoes(tab, jogador):
    """
    Obtem todas as posicoes possiveis de bifurcacao

    Parametros:
        tab (tabuleiro): tabuleiro a obter as bifurcacoes
        jogador (jogador): jogador a que se vai verificar as bifurcacoes
    
    Retorna:
        posicoes (tuplo): posicoes de bifurcacao ordenadas por ordem crescente
    """
    # Atribuir a cada linha, coluna e diagonal o conjunto 
    # de posicoes que estas abrangem
    linhas_pos = {1: (1,2,3), 2: (4,5,6), 3: (7,8,9)}
    colunas_pos = {1: (1,4,7), 2: (2,5,8), 3: (3,6,9)}
    diagonais_pos = {1: (1,5,9), 2: (7,5,3)}

    # Obter as linhas, colunas e diagonais que estao ocupadas pelo jogador 
    # e nao pelo adversario ou estao livres e converte-las em posicoes
    posicoes = ()
    for i, linha in enumerate(tab):
        if linha.count(jogador) >= 1 and linha.count(jogador*-1) == 0:
            posicoes += linhas_pos[i+1]
    
    colunas = obter_colunas(tab)
    for i, coluna in enumerate(colunas):
        if coluna.count(jogador) >= 1 and coluna.count(jogador*-1) == 0:
            posicoes += colunas_pos[i+1]
    
    diagonais = obter_diagonais(tab)
    for i, diagonal in enumerate(diagonais):
        if diagonal.count(jogador) >= 1 and diagonal.count(jogador*-1) == 0:
            posicoes += diagonais_pos[i+1]
    
    # Remover as posicoes repetidas e ocupadas
    # obtendo assim as posicoes de bifurcacao
    posicoes = obter_repetidos(posicoes)
    posicoes = remover_posicoes_ocupadas(tab, posicoes)

    return sorted(posicoes)


# Esta funcao obtem, se existir, a posicao livre 
# necessaria de se marcar para ganhar o jogo
# vitoria: tabuleiro x jogador -> posicao ou None
def vitoria(tab, jogador):
    """
    Obtem se existir a primeira posicao livre em que caso seja marcada pelo jogador
     leva a sua vitoria

    Parametros:
        tab (tabuleiro): tabuleiro a analisar
        jogador (jogador): jogador a analisar
     
    Retorna:
        livre (posicao): posicao livre que caso estivesse marcada 
        conduziria a vitoria do jogador
        (None): caso nao haja nenhuma posicao livre que 
        verifique as condicoes necessarias
    """
    livres = obter_posicoes_livres(tab)
    for livre in livres:
        if jogador_ganhador(marcar_posicao(tab, jogador, livre)):
            return livre
        


# Esta funcao obtem, se existir, a posicao livre necessaria de se marcar
# para impedir o adversario de ganhar o jogo
# bloqueio: tabuleiro x jogador -> posicao ou None
def bloqueio(tab, jogador):
    """
    Obtem se existir a posicao livre necessaria de se marcar para evitar
     a vitoria do adversario na proxima jogada

    Parametros:
        tab (tabuleiro): tabuleiro a analisar
        jogador (jogador): jogador a analisar
    
    Retorna:
        (posicao): posicao livre que caso estivesse marcada 
        conduziria a vitoria do jogador adversario
        (None): caso nao haja nenhuma posicao livre que verifique 
        as condicoes necessarias
    """
    return vitoria(tab, jogador*-1)


# Esta funcao obtem, se existir, a primeira posicao de bifurcacao do jogador
# bifurcacao: tabuleiro x jogador -> posicao ou None
def bifurcacao(tab, jogador):
    """
    Obtem se existir a primeira posicao onde o jogador pode criar uma bifurcacao

    Parametros:
        tab (tabuleiro): tabuleiro a analisar
        jogador (jogador): jogador a analisar

    Retorna:
        (posicao): posicao livre que caso ocupada leva a uma bifurcacao
        (None): caso nao haja nenhuma posicao livre que verifique as condicoes necessarias
    """
    bifurcacoes = obter_bifurcacoes(tab, jogador)

    # Retornar a primeira posicao livre de bifurcacao que encontramos
    for pos in bifurcacoes:
        if eh_posicao_livre(tab, pos):
            return pos


# Esta funcao obtem, se existir, a posicao livre necessaria de se marcar 
# de forma a impedir o adversario de formar uma bifurcacao
# bloqueio_bifurcacao: tabuleiro x jogador -> posicao ou None
def bloqueio_bifurcacao(tab, jogador):
    """
    Obtem uma posicao livre que caso seja marcada pelo
    jogador impede o adversario de formar uma bifurcacao

    Parametros:
        tab (tabuleiro): tabuleiro a analisar
        jogador (jogador): jogador a analisar

    Retorna:
        (posicao): posicao livre que caso ocupada leva impede a formacao 
    de uma bifurcacao do adversario
        (None): caso nao haja nenhuma posicao livre
         que verifique as condicoes necessarias
    """
    adversario = jogador *-1
    bifurcacoes = obter_bifurcacoes(tab, adversario)
    if len(bifurcacoes) == 1:
        return bifurcacoes[0]
    elif len(bifurcacoes) > 1:
        for pos in obter_posicoes_livres(tab):
            tabuleiro = tuple(tab)
            # analisar o que aconteria se jogassemos numa determinda posicao livre
            tabuleiro = marcar_posicao(tabuleiro, jogador, pos)
            pos_bloqueio = bloqueio(tabuleiro, adversario)
            if pos_bloqueio != None:
                    tabuleiro = marcar_posicao(tabuleiro, adversario, pos_bloqueio)
            pos_bloqueio = bloqueio(tabuleiro, jogador)
            if pos_bloqueio != None:
                    tabuleiro = marcar_posicao(tabuleiro, jogador, pos_bloqueio)
            # se jogar nessa posicao nao leva a formacao de bifurcacoes nem a vitoria por parte
            #  do adversario nas proximas jogadas entao retornamos essa posicao
            if bifurcacao(tabuleiro, adversario) == None and vitoria(tabuleiro, adversario) == None:
                    return pos


# Esta funcao retorna a posicao central do tabuleiro, caso esta esteja livre
# centro: tabuleiro x jogador -> posicao ou None
def centro(tab, jogador):
    """
    Retorna a posicao central do tabuleiro caso esta esteja livre

    Parametros:
        tab (tabuleiro): tabuleiro a analisar
        jogador (jogador): jogador a analisar
    
    Retorna:
        centro (posicao): posicao central do tabuleiro se esta estiver livre
        (None): caso a posicao central ja esteja ocupada
    """
    centro = 5
    if eh_posicao_livre(tab, centro):
        return centro 
    

# Esta funcao obtem, se existir, o canto oposto ao jogado pelo adversario
# canto_oposto: tabuleiro x jogador -> posicao ou None
def canto_oposto(tab, jogador):
    """
    Obtem se existir o canto oposto do marcado pelo adversario

    Parametros:
        tab (tabuleiro): tabuleiro a analisar
        jogador (jogador): jogador a analisar

    Retorna:
        value (posicao): canto oposto ao do adversario
        (None): caso nao haja nenhum canto que verifique as condicoes

    """
    jogador *= -1
    cantos_combinacoes = {
        1:9,
        9:1,
        3:7,
        7:3
    }
    for key, value in cantos_combinacoes.items():
        if obter_posicao(tab, key) == jogador and eh_posicao_livre(tab, value):
            return value


# Esta funcao obtem, se existir, o primeiro canto livre
# canto_vazio: tabuleiro x jogador -> posicao ou None
def canto_vazio(tab, jogador):
    """
    Obtem o primeiro canto vazio

    Parametros:
        tab (tabuleiro): tabuleiro a analisar
        jogador (jogador): jogador a analisar
    
    Retorna:
        canto (posicao): primeiro canto livre
        (None): caso nao hajam cantos livres
    """
    cantos = (1, 3, 7, 9)
    for canto in cantos:
        if eh_posicao_livre(tab, canto):
            return canto


# Esta funcao obtem a primeira posicao lateral livre
# lateral_vazio: tabuleiro x jogador -> posicao ou None
def lateral_vazio(tab, jogador):
    """
    Obtem a primeira posicao lateral livre

    Parametros:
        tab (tabuleiro): tabuleiro a analisar
        jogador (jogador): jogador a analisar
    
    Retorna:
        lateral (posicao): primeira posicao lateral livre
        (None): caso nao hajam posicoes laterais livres
    """
    laterais = (2, 4, 6, 8)
    for lateral in laterais:
        if eh_posicao_livre(tab, lateral):
            return lateral


# Esta funcao retorna a melhor posicao possivel de acordo 
# com a dificuldade/estrategia definida
# escolher_posicao_auto: tabuleiro x jogador x estrategia -> posicao
def escolher_posicao_auto(tab, jogador, strat):
    """
    Devolve uma posicao de acordo com o tabuleiro e a dificuldade escolhida

    Parametros:
        tab (tabuleiro): tabuleiro de jogo.
        jogador (int): jogador
        strat (string): estrategia a adotar (basico, normal, perfeito)

    Retorna:
        pos (posicao): posicao escolhida pelo algoritmo selecionado
    """
    
    if not eh_tabuleiro(tab) or not eh_jogador(jogador) or not eh_estrategia(strat):
        raise ValueError("escolher_posicao_auto: algum dos argumentos e invalido")

    # Atribuir funcoes a cada estrategia
    if strat == "basico":
        criterios = (centro, canto_vazio, lateral_vazio)
    elif strat == "normal":
        criterios = (vitoria, bloqueio, centro, canto_oposto, canto_vazio, lateral_vazio)
    elif strat == "perfeito":
        criterios = (vitoria, bloqueio, bifurcacao, bloqueio_bifurcacao, \
            centro, canto_oposto, canto_vazio, lateral_vazio)

    # Iterar por cada funcao ate encontrar a melhor posicao
    # de acordo com a estrategia definida
    for criterio in criterios:
        pos = criterio(tab, jogador)
        if eh_posicao(pos):
            return pos


# Esta funcao e responsavel pelo funcionamento do jogo do galo
# que permite ao utilizador jogar contra o computador
# jogo_do_galo: string x estrategia -> string
def jogo_do_galo(simbolo, strat):
    """
    Funcao responsavel pelo funcionamento do jogo do galo

    Parametros:
        simbolo (string): simbolo escolhido pelo utilizador (X ou O)
        strat (string): estrategia / dificuldade do computador
    
    Retorna:
        resultado (string): simbolo do jogador vencedor ou 'EMPATE' em caso de empate
    """

    if type(simbolo) != str or (simbolo != "X" and simbolo != "O") or not eh_estrategia(strat):
        raise ValueError("jogo_do_galo: algum dos argumentos e invalido")

    print("Bem-vindo ao JOGO DO GALO.")
    print("O jogador joga com '{}'.".format(simbolo))
    
    jogador = 1 if simbolo == "X" else -1
    computador = jogador * -1
    tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    fim_jogo = False
    turno = 1
    resultado = "EMPATE"
    while not fim_jogo:
        if jogador == turno:
            pos = escolher_posicao_manual(tab)
        else:
            print("Turno do computador ({}):".format(strat))
            pos = escolher_posicao_auto(tab, computador, strat)
            
        tab = marcar_posicao(tab, turno, pos)
        print(tabuleiro_str(tab))

        ganhador = jogador_ganhador(tab)
        if ganhador != 0:
            resultado = "O" if ganhador == -1 else "X"
            fim_jogo = True
        elif not obter_posicoes_livres(tab):
            fim_jogo = True
        turno *= -1

    return resultado

