class Trie(object):
  """Implementa uma trie"""

  class No(object):
    """Implementa um nó de trie"""
    def __init__(self):
      self.filhos = {}

  def __init__(self):
    self.__raiz = self.No()

  def __repr(self, no, chave="○", tipo="", indent="", 
             ord=-1):
    """Produz representação de subárvore como str"""
    s = ""
    indent += "\t"
    filhos = [(ch, filho) for ch, filho in 
              no.filhos.items() if ch != "*"]
    if ord or len(indent) == 2:
      s += indent[2:] + tipo + " " * (no != self.__raiz)
    else:
      s += " →\t"
    s += chave + '*' * ('*' in no.filhos)
    if no == self.__raiz or len(filhos) == 0:
      s += "\n"
    for i, (ch, filho) in enumerate(filhos):
      if i < len(filhos) - 1:
        s += self.__repr(filho, ch, "├→", 
           indent + "│" * (tipo == "├→"), i)
      else:
        s += self.__repr(filho, ch, "└→", 
           indent + "│" * (tipo == "├→"), i)
    return s

  def __str__(self):
    return self.__repr(self.__raiz)

  def __busca(self, string):
    """Retorna nó onde a string buscada é formada"""
    no_atual = self.__raiz
    for c in string:
      no_atual = no_atual.filhos.get(c)
      if not no_atual:
        return None
    return no_atual

  def busca(self, string, prefixo=True):
    """
    Verifica se a string está na trie.
    prefixo=True (padrão): busca por prefixo.
    prefixo=False: busca por palavra completa.
    Retorna bool.
    """
    no = self.__busca(string)
    return bool(no) and (prefixo or ("*" in no.filhos))

  def insere(self, item):
    """Insere string na trie"""
    no_atual = self.__raiz
    for c in item["palavra"]:
      if c not in no_atual.filhos:
        no_atual.filhos[c] = self.No()
      no_atual = no_atual.filhos[c]
    no_atual.filhos["*"] = item["freq"]

  def __recupera_palavras(self, no=None, prefixo="",
                          palavras=None):
    """Recupera todas as palavras a partir de um nó"""
    if not no:
      no = self.__raiz
    if palavras is None:
      palavras = []
    for chave, filho in no.filhos.items():
      if chave == "*":
        palavras.append({"palavra": prefixo, "freq": filho})
      else:
        self.__recupera_palavras(filho, 
                                 prefixo + chave,
                                 palavras)
    return palavras

  def autocompletar(self, prefixo, max=3):
    """Retorna lista de palavras por prefixo"""
    no = self.__busca(prefixo)
    if not no:
      return []
    palavras = self.__recupera_palavras(no, prefixo)
    if len(palavras) > max:
      quickselect(max, palavras, "freq")
      palavras = palavras[:max]
    return [p["palavra"] for p in palavras]
  
  def sugerir_palavras(self, texto, max=3):
        """Combina autocompletar e autocorreção"""
        if self.__busca(texto):
            return self.autocompletar(texto, max)
        else:
            prefixo = texto
            while prefixo:
                if self.__busca(prefixo):
                    return self.autocompletar(prefixo, max)
                else:
                    prefixo = prefixo[:-1]
            return []

def particiona(array, chave, inicio, fim):
  # Escolhe útimo elemento como pivô 
  ind_piv = fim
  pivo = array[ind_piv][chave]
  # Define ponteiros esq e dir
  esq = inicio
  dir = fim - 1
  while True:
    # Move esq para a direita e dir para a esquerda
    while array[esq][chave] > pivo:
      esq += 1
    while array[dir][chave] < pivo and dir > esq:
      dir -= 1
    # Se esq e dir se encontraram/cruzaram, sai do laço
    if esq >= dir:
      break
    # Caso contrário, troca os valores e move esq
    array[esq], array[dir] = array[dir], array[esq]
    esq += 1
  # Troca pivô com esq e retorna índice final do pivô
  array[esq], array[ind_piv] = array[ind_piv], array[esq]
  return esq


def quickselect(k, array, chave, inicio=0, fim=-1):
  if fim == -1:
    fim += len(array)
  # Se há mais que 1 elemento no array:
  if fim - inicio > 0:
    # Particiona os elementos e armazena o índice do pivô
    ind_piv = particiona(array, chave, inicio, fim)
    # Se for menor, seleciona no subarray à esquerda
    if k - 1 < ind_piv:
      quickselect(k, array, chave, inicio, 
                  ind_piv - 1)
    # Se for maior, seleciona no subarray à direita
    elif k - 1 > ind_piv:
      quickselect(k, array, chave, ind_piv + 1, fim)


t = Trie()

with open("Estruturas_de_Dados_e_Algoritmos_Avançados/at/palavras.txt") as palavras:
    for palavra in palavras:
        palavra = palavra.rstrip()
        if palavra and not palavra.startswith("#"):
            palavra = palavra.split()
            t.insere({"palavra": palavra[0], 
                      "freq": int(palavra[1])})

print(t)

prefixo = input("Texto: ")
while prefixo:
    print("Sugestões:", t.sugerir_palavras(prefixo))
    prefixo = input("\nTexto: ")