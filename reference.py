# MIDEAST 341
# Matthew Axner (maxner)
# Interdisciplinary Project 2
# Ancient Egyptian Mathematical Sourcebook

# reference document for sourcebook.py

def print_2N_table():
	print("Ancient Egyptian 2 / N Table\n")

	print("N\t2/N\n___________________")
	print("3\t2/3\n5\t1/3 1/15\n7\t1/4 1/28\n9\t1/6 1/18\n11\t1/6 1/66\n13\t1/8 1/52 1/104\n15\t1/10 1/30\n17\t1/12 1/51 1/68")
	print("19\t1/12 1/76 1/114\n21\t1/14 1/42\n23\t1/12 1/276\n25\t1/15 1/75")
	print("27\t1/18 1/54\n29\t1/24 1/58 1/174 1/232\n31\t1/20 1/124\n33\t1/22 1/66\n35\t1/30 1/42")
	print("37\t1/24 1/111 1/296\n39\t1/26 1/78\n41\t1/24 1/246 1/328\n43\t1/42 1/86 1/129 1/301\n45\t1/30 1/90\n47\t1/30 1/141 1/470\n49\t1/28 1/196")
	print("51\t1/34 1/102\n53\t1/30 1/318 1/795\n55\t1/30 1/330\n57\t1/38 1/114\n59\t1/36 1/236 1/531\n61\t1/40 1/244 1/488 1/610\n63\t1/42 1/126")
	print("65\t1/39 1/195\n67\t1/40 1/335 1/536\n69\t1/46 1/138\n71\t1/40 1/568 1/710\n73\t1/60 1/219 1/292 1/365\n75\t1/50 1/150")
	print("77\t1/44 1/308\n79\t1/60 1/237 1/316 1/790\n81\t1/54 1/162\n83\t1/60 1/332 1/415 1/498\n85\t1/51 1/255\n87\t1/58 1/174\n89\t1/60 1/356 1/1/534 1/890")
	print("91\t1/70 1/130\n93\t1/62 1/186\n95\t1/60 1/380 1/570\n97\t1/56 1/679 1/776\n99\t1/66 1/198\n101\t1/101 1/202 1/303 1/606")

def cont():
	prompt = ''
	while (prompt != 'Y' and prompt != 'N' and prompt != 'y' and prompt != 'n'):
		prompt = raw_input("Keep practicing? (Y/N) ")
		if (prompt != 'Y' and prompt != 'N' and prompt != 'y' and prompt != 'n'):
			print("ERROR: Invalid input.")

	if (prompt == 'Y' or prompt == 'y'):
		return True
	else:
		return False

def prime(x):
	for i in range(2, x):
		if ((x / float(i)) % 1 == 0):
			return False
	return True

def floor(n):
	return int(n)