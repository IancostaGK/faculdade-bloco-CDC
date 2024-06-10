
def ind_filho_esq(ind):
  """Retorna o índice do filho esquerdo de ind"""
  return ind * 2 + 1

def ind_filho_dir(ind):
  """Retorna o índice do filho direito de ind"""
  return ind * 2 + 2

def ind_pai(ind):
  """Retorna o índice do pai de ind"""
  return (ind - 1) // 2

def identidade(item):
  """Retorna o próprio item (chave padrão)"""
  return item


class Heap(object):
  """Implementa um heap baseado em array"""

  def __init__(self, chave=identidade, max_heap=True):
    self.__dados = []
    self.__chave = chave
    self.__max_heap = max_heap

  def __repr(self, no=0, tipo="", indent=""):
    """Produz representação de subárvore como str"""
    s = ""
    if no < len(self.__dados):
      indent += "\t"
      s += self.__repr(ind_filho_dir(no), "┌→",
                       indent + "│" * (tipo == "└→"))
      s += f"{indent[1:]}{tipo} {self.__dados[no]}\n"
      s += self.__repr(ind_filho_esq(no), "└→",
                       indent + "│" * (tipo == "┌→"))
    return s

  def __str__(self):
    return self.__repr() + "\n" + str(self.__dados)

  def __maior(self, ind1, ind2):
    """Retorna True de ind1 > ind2 e False caso contrário"""
    chave1 = self.__chave(self.__dados[ind1])
    chave2 = self.__chave(self.__dados[ind2])
    if self.__max_heap:
      return chave1 > chave2
    return chave2 > chave1

  def __tem_filho_maior(self, ind):
    """Verifica se ind tem filho com valor maior"""
    esq = ind_filho_esq(ind)
    dir = ind_filho_dir(ind)
    return ((esq < len(self.__dados) and self.__maior(esq, ind)) 
            or 
            (dir < len(self.__dados) and self.__maior(dir, ind)))

  def __maior_filho(self, ind):
    """Retorna o índice do maior filho de ind"""
    esq = ind_filho_esq(ind)
    dir = ind_filho_dir(ind)
    if dir >= len(self.__dados):
      if esq < len(self.__dados):
        return esq
      return -1
    if self.__maior(dir, esq):
      return dir
    return esq

  def insere(self, item):
    """Insere item no heap"""
    self.__dados.append(item)
    novo = len(self.__dados) - 1
    pai = ind_pai(novo)
    while novo > 0 and self.__maior(novo, pai):
      self.__dados[novo], self.__dados[pai] = \
          self.__dados[pai], self.__dados[novo]
      novo = pai
      pai = ind_pai(novo)

  def remove(self):
    """Remove item do heap"""
    if not self.__dados:
      return None
    if len(self.__dados) == 1:
      return self.__dados.pop()
    item = self.max()
    self.__dados[0] = self.__dados.pop()
    no = 0
    while self.__tem_filho_maior(no):
      maior_filho = self.__maior_filho(no)
      self.__dados[no], self.__dados[maior_filho] = \
          self.__dados[maior_filho], self.__dados[no]
      no = maior_filho
    return item

  def max(self):
    """Retorna o valor máximo no heap"""
    if self.__dados:
      return self.__dados[0]

  def vazio(self):
    """Retorna True se o heap está vazio, False caso contrário"""
    return len(self.__dados) == 0
