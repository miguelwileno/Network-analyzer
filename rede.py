import os
import platform
import subprocess
import socket
import time
import random

# ================= CORES =================
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# ================= UTIL =================
def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def pause():
    input("\nPressione Enter para continuar...")

def center(text, width=80):
    return text.center(width)

def cmd(command):
    os.system(command)

# ================= ANIMAÇÕES =================
def type_text(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def loading_bar():
    print(CYAN + "\n[+] Inicializando módulos..." + RESET)
    for i in range(0, 101, 5):
        bar = "#" * (i // 5) + "-" * (20 - (i // 5))
        print(f"\r{YELLOW}[{bar}] {i}%{RESET}", end="")
        time.sleep(0.04)
    print("\n")

def fake_scan():
    print(CYAN + "\n[+] Escaneando rede local...\n" + RESET)
    for i in range(1, 15):
        ip = f"192.168.0.{i}"
        status = random.choice(["ATIVO", "OK", "RESPONDENDO"])
        print(GREEN + f"[✓] {ip} -> {status}" + RESET)
        time.sleep(0.03)

# ================= BANNER =================
def banner():
    clear()
    print(BLUE + "="*80 + RESET)

    # ASCII completo em uma cor
    ascii_logo = [
        "███████╗██████╗ ███████╗███████╗██████╗ ███╗   ██╗███████╗████████╗",
        "██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║██╔════╝╚══██╔══╝",
        "███████╗██████╔╝█████╗  █████╗  ██║  ██║██╔██╗ ██║█████╗     ██║   ",
        "╚════██║██╔═══╝ ██╔══╝  ██╔══╝  ██║  ██║██║╚██╗██║██╔══╝     ██║   ",
        "███████║██║     ███████╗███████╗██████╔╝██║ ╚████║███████╗   ██║   ",
        "╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝   "
    ]

    for line in ascii_logo:
        print(GREEN + center(line) + RESET)
        time.sleep(0.03)

    # Texto do criador
    type_text(YELLOW + center("Criado por MiguelWileno") + RESET, 0.01)
    print(BLUE + "="*80 + RESET)

    type_text(CYAN + "\n[+] Iniciando sistema MIIGBOT..." + RESET)
    loading_bar()
    fake_scan()
    type_text(GREEN + "\n[✓] Sistema pronto!" + RESET)
    time.sleep(0.5)

# ================= FUNÇÕES DE REDE =================
def show_ip():
    print(CYAN + "\n--- Informações de Rede ---\n" + RESET)
    cmd("ipconfig" if platform.system() == "Windows" else "ifconfig")
    pause()

def show_arp():
    print(CYAN + "\n--- Tabela ARP ---\n" + RESET)
    cmd("arp -a")
    pause()

def tracert_custom():
    print(CYAN + "\n--- Tracert ---\n" + RESET)
    site = input("Digite um IP ou Site: ")
    command = "tracert" if platform.system() == "Windows" else "traceroute"
    cmd(f"{command} {site}")
    pause()

def test_loop():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(CYAN + f"\n--- Loopback ({ip}) ---\n" + RESET)
    cmd(f"ping {ip}")
    pause()

# ================= MENU PING =================
def ping_target(target):
    print(YELLOW + f"\nPing para {target}:\n" + RESET)
    cmd(f"ping {target}")
    pause()

def ping_menu():
    targets = {
        "1": ("Google", "www.google.com"),
        "2": ("YouTube", "www.youtube.com"),
        "3": ("Facebook", "www.facebook.com"),
        "4": ("Globo", "www.globo.com")
    }

    while True:
        clear()
        print(CYAN + "\n--- Teste de Ping ---\n" + RESET)
        for key, (name, addr) in targets.items():
            print(f"{key} - {name} ({addr})")
        print("0 - Voltar")

        choice = input("\nEscolha: ")

        if choice in targets:
            ping_target(targets[choice][1])
        elif choice == "0":
            break
        else:
            print(RED + "Opção inválida!" + RESET)
            pause()

# ================= OPÇÃO 6: INSTRUÇÕES =================
def instructions_menu():
    while True:
        clear()
        print(CYAN + "\n--- INSTRUÇÕES TÉCNICAS ---\n" + RESET)
        print("⚠ Todos os testes devem ser efetuados com o computador cabeado (CABO GIGA)\n")
        print("💻 DNS recomendados:")
        print("  DNS 1: 200.39.146.250")
        print("  DNS 2: 200.39.146.251\n")
        print("🌐 Teste de velocidade recomendado nos sites:")
        print("  SpeedTest: speedtest.net")
        print("  Fast: fast.com\n")
        print("📌 Observações finais:")
        print("  - Após os testes, anexe prints e fotos no fechamento da O.S")
        print("  - Para mais dúvidas, contate o NOC responsável da sua região\n")
        print("0 - Voltar")

        choice = input("\nEscolha uma opção: ")
        if choice == "0":
            break
        else:
            print(YELLOW + "\nApenas leitura informativa nesta seção!" + RESET)
            pause()

# ================= MENU PRINCIPAL =================
def menu():
    while True:
        banner()
        print(GREEN + "+" + "-"*78 + "+" + RESET)
        print(GREEN + "| " + RESET + "1 - Dados da rede".ljust(76) + GREEN + " |" + RESET)
        print(GREEN + "| " + RESET + "2 - Lista de IP's".ljust(76) + GREEN + " |" + RESET)
        print(GREEN + "| " + RESET + "3 - Tracert".ljust(76) + GREEN + " |" + RESET)
        print(GREEN + "| " + RESET + "4 - Teste de Loopback".ljust(76) + GREEN + " |" + RESET)
        print(GREEN + "| " + RESET + "5 - Teste de Ping".ljust(76) + GREEN + " |" + RESET)
        print(GREEN + "| " + RESET + "6 - Instruções Técnicas".ljust(76) + GREEN + " |" + RESET)
        print(GREEN + "| " + RESET + "0 - Sair".ljust(76) + GREEN + " |" + RESET)
        print(GREEN + "+" + "-"*78 + "+" + RESET)

        choice = input("\nEscolha uma opção: ")

        if choice == "1":
            show_ip()
        elif choice == "2":
            show_arp()
        elif choice == "3":
            tracert_custom()
        elif choice == "4":
            test_loop()
        elif choice == "5":
            ping_menu()
        elif choice == "6":
            instructions_menu()
        elif choice == "0":
            print(RED + "\nSaindo..." + RESET)
            break
        else:
            print(RED + "Opção inválida!" + RESET)
            pause()

# ================= START =================
if __name__ == "__main__":
    menu()