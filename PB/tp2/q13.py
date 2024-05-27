class No:
    def __init__(self, linha):
        self.linha = linha
        self.anterior = None
        self.proximo = None

class EditorDeTexto:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.linha_corrente = None

    def inserir_linha(self, linha):
        novo_no = No(linha)
        if self.primeiro is None:
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            if self.linha_corrente is None:
                self.ultimo.proximo = novo_no
                novo_no.anterior = self.ultimo
                self.ultimo = novo_no
            else:
                proximo = self.linha_corrente.proximo
                self.linha_corrente.proximo = novo_no
                novo_no.anterior = self.linha_corrente
                novo_no.proximo = proximo
                if proximo:
                    proximo.anterior = novo_no
                else:
                    self.ultimo = novo_no
        self.linha_corrente = novo_no

    def excluir_linhas(self, inicio, fim):
        no_inicio = self.buscar_no(inicio)
        no_fim = self.buscar_no(fim)
        if no_inicio is None or no_fim is None:
            print("Linhas não encontradas.")
            return

        if no_inicio.anterior:
            no_inicio.anterior.proximo = no_fim.proximo
        else:
            self.primeiro = no_fim.proximo

        if no_fim.proximo:
            no_fim.proximo.anterior = no_inicio.anterior
        else:
            self.ultimo = no_inicio.anterior

    def duplicar_bloco(self, inicio, fim, posicao):
        no_inicio = self.buscar_no(inicio)
        no_fim = self.buscar_no(fim)
        no_posicao = self.buscar_no(posicao)
        if no_inicio is None or no_fim is None or no_posicao is None:
            print("Linhas não encontradas.")
            return

        novo_inicio = None
        novo_fim = None
        atual = no_inicio
        while atual:
            novo_no = No(atual.linha)
            if novo_inicio is None:
                novo_inicio = novo_no
                novo_fim = novo_no
            else:
                novo_fim.proximo = novo_no
                novo_no.anterior = novo_fim
                novo_fim = novo_no
            atual = atual.proximo

        proximo = no_posicao.proximo
        no_posicao.proximo = novo_inicio
        novo_inicio.anterior = no_posicao
        novo_fim.proximo = proximo
        if proximo:
            proximo.anterior = novo_fim
        else:
            self.ultimo = novo_fim

    def listar_blocos(self, inicio=None, fim=None):
            if inicio is None and fim is None:
                if self.primeiro is None or self.ultimo is None:
                    print("O texto está vazio.")
                    return

                inicio = self.primeiro
                fim = self.ultimo
            else:
                inicio = self.buscar_no(inicio)
                fim = self.buscar_no(fim)
                if inicio is None or fim is None:
                    print("Linhas não encontradas.")
                    return

            atual = inicio
            while atual != fim.proximo:
                print(atual.linha)
                atual = atual.proximo

    def carregar_arquivo(self, arquivo, posicao=None):
        try:
            with open(arquivo, "r") as f:
                linhas = f.readlines()
                for linha in linhas:
                    self.inserir_linha(linha.strip())
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    def salvar_arquivo(self, arquivo, inicio=None, fim=None):
        if inicio is None and fim is None:
            inicio = self.primeiro
            fim = self.ultimo
        else:
            inicio = self.buscar_no(inicio)
            fim = self.buscar_no(fim)
            if inicio is None or fim is None:
                print("Linhas não encontradas.")
                return

        try:
            with open(arquivo, "w") as f:
                atual = inicio
                while atual != fim.proximo:
                    f.write(atual.linha + "\n")
                    atual = atual.proximo
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    def alterar_linha(self, linha, novo_texto):
        no = self.buscar_no(linha)
        if no is None:
            print("Linha não encontrada.")
            return

        no.linha = novo_texto

    def buscar_no(self, linha):
        atual = self.primeiro
        while atual:
            if atual.linha == linha:
                return atual
            atual = atual.proximo
        return None

    def executar_comando(self, comando):
        comando = comando.split()
        if not comando:
            return

        if comando[0] == "I":
            if len(comando) > 1:
                posicao = comando[1]
                if posicao.isdigit():
                    posicao = int(posicao)
                    linha = input("Digite a linha a ser inserida: ")
                    self.inserir_linha(linha)
                else:
                    print("Posição inválida.")
            else:
                linha = input("Digite a linha a ser inserida: ")
                self.inserir_linha(linha)

        elif comando[0] == "E":
            if len(comando) > 2:
                inicio = comando[1]
                fim = comando[2]
                self.excluir_linhas(inicio, fim)
            else:
                if self.linha_corrente:
                    linha = self.linha_corrente.linha
                    self.excluir_linhas(linha, linha)
                else:
                    print("Nenhuma linha corrente definida.")

        elif comando[0] == "D":
            if len(comando) > 3:
                inicio = comando[1]
                fim = comando[2]
                posicao = comando[3]
                self.duplicar_bloco(inicio, fim, posicao)
            else:
                print("Comando incompleto.")

        elif comando[0] == "L":
            if len(comando) > 2:
                inicio = comando[1]
                fim = comando[2]
                self.listar_blocos(inicio, fim)
            else:
                self.listar_blocos()

        elif comando[0] == "C":
            if len(comando) > 2:
                arquivo = comando[1]
                posicao = comando[2]
                self.carregar_arquivo(arquivo, posicao)
            else:
                print("Comando incompleto.")

        elif comando[0] == "S":
            if len(comando) > 1:
                arquivo = comando[1]
                if len(comando) > 2:
                    inicio = comando[2]
                    if len(comando) > 3:
                        fim = comando[3]
                        self.salvar_arquivo(arquivo, inicio, fim)
                    else:
                        self.salvar_arquivo(arquivo, inicio, inicio)
                else:
                    self.salvar_arquivo(arquivo)
            else:
                print("Comando incompleto.")

        elif comando[0] == "A":
            if len(comando) > 1:
                linha = comando[1]
                novo_texto = input("Digite o novo texto para a linha {}: ".format(linha))
                self.alterar_linha(linha, novo_texto)
            else:
                print("Comando incompleto.")

        elif comando[0] == "F":
            print("Finalizando o editor.")
            return False

        else:
            print("Comando inválido.")

        return True

# Exemplo de uso:
editor = EditorDeTexto()
while True:
    comando = input("Digite um comando: ")
    continuar = editor.executar_comando(comando)
    if not continuar:
        break
