import os 
def main():
	print("[+] Mostrar todos? [N / s] ")
	mostrar = input()
	if mostrar == "N":
		print("[+] Running... ")
		os.system("netsh wlan show profile")
		rede1 = str(input("Escolha a rede "))
		os.system("netsh wlan show profile " + rede1 + " key=clear")
		print("[+] Nice")
	else:
		print("[+] Running...")
		os.system("netsh wlan show profile * key=clear")
		print("[+] Nice")
if __name__ == "__main__":
	main()