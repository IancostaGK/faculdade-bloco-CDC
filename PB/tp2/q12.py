class No:
    def __init__(self, linha):
        self.linha = linha
        self.anterior = None
        self.proximo = None

class EditorDeTexto:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def inserir_linha(self, linha):
        novo_no = No(linha)
        if self.primeiro is None:
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            novo_no.anterior = self.ultimo
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no

    def imprimir_texto(self):
        atual = self.primeiro
        while atual:
            print(atual.linha)
            atual = atual.proximo

    def mover_linha(self, linha_origem, linha_destino):
        if linha_origem == linha_destino:
            return
        
        no_origem = self.buscar_no(linha_origem)
        if no_origem is None:
            print("Linha de origem não encontrada.")
            return

        no_destino = self.buscar_no(linha_destino)
        if no_destino is None:
            print("Linha de destino não encontrada.")
            return

        linha = no_origem.linha
        self.remover_linha(linha_origem)

        if no_destino.proximo:
            no_destino.proximo.anterior = No(linha)
            no_destino.proximo.anterior.proximo = no_destino.proximo
        else:
            self.ultimo.proximo = No(linha)
            self.ultimo.proximo.anterior = self.ultimo
            self.ultimo = self.ultimo.proximo

        no_destino.proximo = self.buscar_no(linha)

    def copiar_linha(self, linha_origem, linha_destino):
        no_origem = self.buscar_no(linha_origem)
        if no_origem is None:
            print("Linha de origem não encontrada.")
            return

        linha = no_origem.linha
        if linha_destino == 0:
            self.inserir_linha(linha)
        else:
            no_destino = self.buscar_no(linha_destino)
            if no_destino is None:
                print("Linha de destino não encontrada.")
                return

            if no_destino.proximo:
                no_destino.proximo.anterior = No(linha)
                no_destino.proximo.anterior.proximo = no_destino.proximo
            else:
                self.ultimo.proximo = No(linha)
                self.ultimo.proximo.anterior = self.ultimo
                self.ultimo = self.ultimo.proximo

            no_destino.proximo = self.buscar_no(linha)

    def remover_linha(self, linha):
        no = self.buscar_no(linha)
        if no is None:
            print("Linha não encontrada.")
            return

        if no.anterior:
            no.anterior.proximo = no.proximo
        else:
            self.primeiro = no.proximo

        if no.proximo:
            no.proximo.anterior = no.anterior
        else:
            self.ultimo = no.anterior

    def buscar_no(self, linha):
        atual = self.primeiro
        while atual:
            if atual.linha == linha:
                return atual
            atual = atual.proximo
        return None

# Exemplo de uso:
editor = EditorDeTexto()
editor.inserir_linha("A natureza,")
editor.inserir_linha("dizem-nos,")
editor.inserir_linha("é apenas o hábito...")
editor.inserir_linha("(Rousseau)")

editor.imprimir_texto()
print("")

editor.mover_linha("A natureza,", "(Rousseau)")
editor.imprimir_texto()
print("")

editor.copiar_linha("dizem-nos,", 2)
editor.imprimir_texto()
print("")

editor.remover_linha("(Rousseau)")
editor.imprimir_texto()
