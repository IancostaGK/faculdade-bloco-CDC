class ListaDuplamenteEncadeada(object):
  """Implementa uma lista duplamente encadeada"""

  class No(object):
    """Implementa um nó de lista duplamente encadeada"""
    def __init__(self, valor, ant=None, prox=None):
      self.valor = valor
      self.anterior = ant
      self.proximo = prox

  def __init__(self):
    self.__primeiro_no = None
    self.__ultimo_no = None
    self.__comprimento = 0

  def __str__(self):
    no = self.__primeiro_no
    s = ""
    while no:
      s += f" ⇆ {no.valor}" if s else str(no.valor)
      no = no.proximo
    return s

  def __len__(self):
    return self.__comprimento

  def acessa(self, ind):
    """Retorna o item na posição ind da lista"""
    if ind < self.__comprimento // 2:
      no = self.__primeiro_no
      for _ in range(ind):
        no = no.proximo
      return no.valor
    if ind < self.__comprimento:
      no = self.__ultimo_no
      for _ in range(self.__comprimento - 1, ind, -1):
        no = no.anterior
      return no.valor

  def busca(self, item):
    """Retorna a posição do item (-1 se não encontra)"""
    no = self.__primeiro_no
    i = 0
    while no:
      if no.valor == item:
        return i
      no = no.proximo
      i += 1
    return -1

  def insere_fim(self, item):
    """Insere item no fim da lista"""
    novo_no = self.No(item, ant=self.__ultimo_no)
    if self.__ultimo_no:
      self.__ultimo_no.proximo = novo_no
    else:
      self.__primeiro_no = novo_no
    self.__ultimo_no = novo_no
    self.__comprimento += 1

  def insere(self, item, ind=0):
    """Insere item na posição ind (padrão 0)"""
    if ind >= self.__comprimento:
      return self.insere_fim(item)
    if ind == 0:
      novo_no = self.No(item, prox=self.__primeiro_no)
      self.__primeiro_no.anterior = novo_no
      self.__primeiro_no = novo_no
    else:
      if ind <= self.__comprimento // 2:
        no = self.__primeiro_no
        for _ in range(ind - 1):
          no = no.proximo
      else:
        no = self.__ultimo_no
        for _ in range(self.__comprimento, ind, -1):
          no = no.anterior
      novo_no = self.No(item, ant=no, prox=no.proximo)
      no.proximo.anterior = novo_no
      no.proximo = novo_no
    self.__comprimento += 1

  def remove_fim(self):
    """Remove/retorna item do fim da lista"""
    if self.__ultimo_no:
      item = self.__ultimo_no.valor
      self.__ultimo_no = self.__ultimo_no.anterior
      if self.__ultimo_no:
        self.__ultimo_no.proximo = None
      else:
        self.__primeiro_no = None
      self.__comprimento -= 1
      return item

  def remove(self, ind=0):
    """Remove/retorna item da posição ind (padrão 0)"""
    if ind >= self.__comprimento:
      return self.remove_fim()
    if ind == 0:
      item = self.__primeiro_no.valor
      self.__primeiro_no = self.__primeiro_no.proximo
      if self.__primeiro_no:
        self.__primeiro_no.anterior = None
      else:
        self.__ultimo_no = None
    else:
      if ind < self.__comprimento // 2:
        no = self.__primeiro_no
        for _ in range(ind):
          no = no.proximo
      else:
        no = self.__ultimo_no
        for _ in range(self.__comprimento - 1, ind, -1):
          no = no.anterior
      item = no.valor
      no.anterior.proximo = no.proximo
      no.proximo.anterior = no.anterior
    self.__comprimento -= 1
    return item


class Fila(object):
  """Implementa o tipo abstrato de dados 'fila'"""

  def __init__(self):
    self.__dados = ListaDuplamenteEncadeada()

  def __str__(self):
    return str(self.__dados)

  def enfileira(self, item):
    """Adiciona item no fim da fila."""
    self.__dados.insere_fim(item)

  def desenfileira(self):
    """Remove o 1º item da fila e o retorna."""
    if not self.vazia():
      return self.__dados.remove()

  def primeiro(self):
    """Retorna o 1º item da fila (sem removê-lo)."""
    if not self.vazia():
      return self.__dados.acessa(0)

  def vazia(self):
    """Verifica se a fila está vazia."""
    return len(self.__dados) == 0