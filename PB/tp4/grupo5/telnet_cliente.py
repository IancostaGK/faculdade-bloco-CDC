import asyncio
import telnetlib3

async def telnet_client(host, port):
    try:
        reader, writer = await telnetlib3.open_connection(host, port)
        print(f"Conectado ao servidor Telnet {host} na porta {port}")

        writer.write("Olá, servidor!\n")
        await writer.drain()

        response = await reader.read(1024)
        print(f"Resposta do servidor: {response}")

        writer.close()
        await writer.wait_closed()
    except Exception as e:
        print(f"Erro ao conectar ao servidor Telnet: {e}")

if __name__ == "__main__":
    host = "127.0.0.1"  
    port = 23  
    asyncio.run(telnet_client(host, port))
