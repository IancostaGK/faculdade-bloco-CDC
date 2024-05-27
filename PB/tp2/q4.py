import asyncio
import numpy as np

async def produto_escalar_async(vetor1, vetor2):
    resultado = 0
    for i in range(len(vetor1)):
        resultado += vetor1[i] * vetor2[i]
    return resultado

async def main():
    vetor1 = np.random.rand(1000)
    vetor2 = np.random.rand(1000)

    resultado = await produto_escalar_async(vetor1, vetor2)
    print("Produto escalar assíncrono:", resultado)

asyncio.run(main())
