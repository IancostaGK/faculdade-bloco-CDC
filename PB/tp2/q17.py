def imprimir_regua(ordem):
    if ordem == 0:
        return
    
    imprimir_regua(ordem - 1)
    print("-" * ordem)
    imprimir_regua(ordem - 1)

ordem_regua = 4
imprimir_regua(ordem_regua)
