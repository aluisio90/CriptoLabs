import sys
""" AUTORE: PIZZI ANDREA """

""" ALGORITMO CESARE """
#DIZIONARIO < VALORE - LETTERA >
alfabeto = {
			0 : 'a',
			1 : 'b',
			2 : 'c',
			3 : 'd',
			4 : 'e',
			5 : 'f',
			6 : 'g',
			7 : 'h',
			8 : 'i',
			9 : 'l',
			10 : 'm',
			11 : 'n',
			12 : 'o',
			13 : 'p',
			14 : 'q',
			15 : 'r',
			16 : 's',
			17 : 't',
			18 : 'u',
			19 : 'v',
			20 : 'z',
}

#DIZIONARIO < LETTERA - VALORE >
reverse_alfabeto = {
			 'a':0 ,
			 'b':1 ,
			 'c':2 ,
			 'd':3 ,
			 'e':4 ,
			 'f':5 ,
			 'g':6 ,
			 'h':7 ,
			 'i':8 ,
			 'l':9 ,
			 'm':10 ,
			 'n':11 ,
			 'o':12 ,
			 'p':13 ,
			 'q':14 ,
			 'r':15 ,
			 's':16 ,
			 't':17 ,
			 'u':18 ,
			 'v':19 ,
			 'z':20 ,
}
#CRIPTA UN MESSAGGIO DATA UNA CHIAVE#
def cripta(k, string_l):
 for letter in string_l:                        #PER OGNI LETTERA DEL MESSAGGIO
  code_l= (reverse_alfabeto[ letter ] + k)%21   #CALCOLA IL CORRIPONDENTE NUMERICO E AGGIUNGI LO SHIFT(MOD 20)
  sys.stdout.write( alfabeto[code_l] )          #TROVA LA NUOVA LETTERA CORRISPONDENTE
  
#DECRIPTA UN MESSAGGIO DATA UNA CHIAVE#
def decripta(k, string_l):
 for letter in string_l:
  code_l= (reverse_alfabeto[ letter ] - k)%21   #COME SOPRA MA QUI LO SHIFT E' NEGATIVO
  sys.stdout.write( alfabeto[code_l] )

#FORMATTAZIONE STRINGA#
def format(string_l):
    string_l = string_l.lower()         #elimina gli spazi a inizio stringa
    string_l = string_l.replace(" ", "")#elimina tutti i caratteri speciali
    string_l = string_l.replace(",", "")
    string_l = string_l.replace(".", "")
    string_l = string_l.replace("?", "")
    string_l = string_l.replace("!", "")
    return string_l
#MAIN DEL PROGRAMMA#  
while "true":
	message = input("INSERIRE MESSAGGIO:\n")
	key = int( input("INSERIRE CHIAVE\n") )
	print (" MENU':\n(1):CRIPTA\n(2)DECRIPTA\n");
	s = int (input("FAI LA TUA SCELTA => "))
	#ADEGUA LA STRINGA
	message = format(message) 
    
#SWITCH CASE#
	if s == 1:
		cripta(key, message)
	elif s == 2:
		decripta(key, message)
	elif s == 0:
		exit()
	else:
		print("##ERROR##")

	print("\n")
#FINE PROGRAMMA
