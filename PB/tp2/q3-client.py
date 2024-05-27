import asyncio

async def tcp_client(message):
    reader, writer = await asyncio.open_connection('localhost', 8888)
    print(f'Enviando: {message}')
    writer.write(message.encode())
    await writer.drain()
    data = await reader.read(100)
    print(f'Recebido: {data.decode()}')
    writer.close()

asyncio.run(tcp_client('Olá, servidor!'))
