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

    def insere(self, string):
        """Insere string na trie"""
        no_atual = self.__raiz
        for c in string:
            if c not in no_atual.filhos:
                no_atual.filhos[c] = self.No()
            no_atual = no_atual.filhos[c]
        no_atual.filhos["*"] = None

from trie import Trie

t = Trie()
palavras = ["ace", "act", "bad", "bake", "bat", "batter", "cab", "cat", "catnap", "catnip"]

for palavra in palavras:
    t.insere(palavra)

print(t)
print('"cat" é um prefixo?', t.busca("cat"))
print('"cat" é uma palavra?', t.busca("cat", False))
print('"catn" é um prefixo?', t.busca("catn"))
print('"catn" é uma palavra?', t.busca("catn", False))
print('"cata" é um prefixo?', t.busca("cata"))
print('"cata" é uma palavra?', t.busca("cata", False))

print('\nInserindo "can":')
t.insere("can")
print(t)