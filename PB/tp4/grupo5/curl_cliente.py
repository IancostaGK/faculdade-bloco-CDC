import asyncio

async def handle_client(reader, writer):
    print("Cliente conectado")
    message = "Bem-vindo ao servidor Telnet de teste\n"
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    message = data.decode()
    print(f"Recebido do cliente: {message}")

    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 23)
    addr = server.sockets[0].getsockname()
    print(f'Servidor de teste ouvindo em {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
