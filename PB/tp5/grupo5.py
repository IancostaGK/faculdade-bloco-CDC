import subprocess

# no Linux

# sudo apt-get update
# sudo apt-get install dnsrecon
# sudo apt-get install wfuzz
# sudo apt-get install sqlmap

# Função para coletar informações de configuração de servidores DNS usando DNSRecon
def coletar_info_dns(dominio):
    try:
        # Executar o DNSRecon e coletar informações do DNS
        resultado = subprocess.run(["dnsrecon", "-d", dominio, "-t", "std"], capture_output=True, text=True)
        return resultado.stdout
    except Exception as e:
        return str(e)

# Função para buscar endereços vulneráveis em servidores usando um fuzzer
def buscar_enderecos_vulneraveis(dominio):
    try:
        # Executar um fuzzer para buscar vulnerabilidades
        resultado = subprocess.run(["wfuzz", "-c", "-z", "file,big.txt", f"--hc=404,403", f"http://{dominio}/FUZZ"], capture_output=True, text=True)
        return resultado.stdout
    except Exception as e:
        return str(e)

# Função para detectar a ocorrência de ataques do tipo SQL injection usando FuzzDB
def detectar_sql_injection(dominio):
    try:
        # Executar um scanner de vulnerabilidades SQL injection
        resultado = subprocess.run(["sqlmap", "-u", f"http://{dominio}/param", "--batch"], capture_output=True, text=True)
        return resultado.stdout
    except Exception as e:
        return str(e)

# Exemplo de uso das funções
if __name__ == "__main__":
    dominio = "example.com"
    print("Coletando informações de configuração de servidores DNS...")
    print(coletar_info_dns(dominio))
    
    print("\nBuscando endereços vulneráveis em servidores...")
    print(buscar_enderecos_vulneraveis(dominio))
    
    print("\nDetectando a ocorrência de ataques do tipo SQL injection...")
    print(detectar_sql_injection(dominio))
