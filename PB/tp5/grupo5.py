import subprocess

# no Linux

# sudo apt-get update
# sudo apt-get install dnsrecon
# sudo apt-get install wfuzz
# sudo apt-get install sqlmap

def coletar_info_dns(dominio):
    try:
        # Executar o DNSRecon e coletar informações do DNS
        resultado = subprocess.run(["dnsrecon", "-d", dominio, "-t", "std"], capture_output=True, text=True)
        return resultado.stdout
    except Exception as e:
        return str(e)

def buscar_enderecos_vulneraveis(dominio):
    try:
        resultado = subprocess.run(["wfuzz", "-c", "-z", f"http://{dominio}/FUZZ"], capture_output=True, text=True)
        return resultado.stdout
    except Exception as e:
        return str(e)

def detectar_sql_injection(dominio):
    try:
        resultado = subprocess.run(["sqlmap", "-u", f"http://{dominio}/param", "--batch"], capture_output=True, text=True)
        return resultado.stdout
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    dominio = "google.com"
    print("Coletando informações de configuração de servidores DNS...")
    print(coletar_info_dns(dominio))
    
    print("\nBuscando endereços vulneráveis em servidores...")
    print(buscar_enderecos_vulneraveis(dominio))
    
    print("\nDetectando a ocorrência de ataques do tipo SQL injection...")
    print(detectar_sql_injection(dominio))
