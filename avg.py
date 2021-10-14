import os
import sys
import time

def clrscr():
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system("clear")
	else:
		pass

def main():
	clrscr()
	print("[ PROGRAM MENGHITUNG AVERAGE HARGA SAHAM & CRYPTO ]")
	print()
	print(""">> Credit :
	- IG : @syauqqii
	- TG : @syauqqii""")
	print()
	try:
		n = int(input("[>] Ada berapa kali pembelian? "))
		print()
	except:
		clrscr()
		print("[!] Error: Input harus berupa integer (Angka bilangan bulat!)")
		time.sleep(2)
		main()
	if n <= 1:
			clrscr()
			print("[!] Error: Input harus lebih besar dari 1!")
			time.sleep(2)
			main()
	clrscr()
	assets = 0
	jumlah = 0
	for i in range(0,n):
		try:
			beli = float(input("[>] Pembelian ke-%s harga     : " % (i+1)))
			asset = float(input("[>] Berapa banyak asset ke-%s : " % (i+1)))
			print()
		except:
			clrscr()
			print("[!] Error: Input harus angka!")
			time.sleep(2)
			main()
		assets += asset
		harganya = beli * asset
		jumlah += harganya

	hasil = jumlah / assets

	clrscr()
	print("\n[#] Average harga anda  : %0.5f" % hasil)
	print("[#] Dengan jumlah asset : %0.0f" % assets)

	print("\n[!] Program akan ditutup otomatis dalam 7 detik!")
	time.sleep(7)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		clrscr()
		sys.exit()
