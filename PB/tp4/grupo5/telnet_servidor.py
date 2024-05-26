import asyncio
import telnetlib3

async def shell(reader, writer):
    writer.write("Olá, cliente!\n")
    data = await reader.read(1024)
    print(f"Recebido: {data.strip()}")
    writer.write("Adeus!\n")
    await writer.drain()
    writer.close()

def main():
    loop = asyncio.get_event_loop()
    coro = telnetlib3.create_server(port=23, shell=shell)
    server = loop.run_until_complete(coro)
    print(f"Servidor Telnet ouvindo na porta 23")
    
    try:
        loop.run_until_complete(server.wait_closed())
    except KeyboardInterrupt:
        print("Servidor interrompido pelo usuário")
    finally:
        server.close()
        loop.run_until_complete(server.wait_closed())

if __name__ == "__main__":
    main()
