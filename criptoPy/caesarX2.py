import sys
""" AUTORE: PIZZI ANDREA """

""" ALGORITMO CESARE modificato """
#DIZIONARIO < VALORE - LETTERA >
alfabeto = {
			1 : 'a',
			2 : 'b',
			3 : 'c',
			4 : 'd',
			5 : 'e',
			6 : 'f',
			7 : 'g',
			8 : 'h',
			9 : 'i',
			10 : 'l',
			11 : 'm',
			12 : 'n',
			13 : 'o',
			14 : 'p',
			15 : 'q',
			16 : 'r',
			17 : 's',
			18 : 't',
			19 : 'u',
			20 : 'v',
			21 : 'z',
}

#DIZIONARIO < LETTERA - VALORE >
reverse_alfabeto = {
			 'a':1 ,
			 'b':2 ,
			 'c':3 ,
			 'd':4 ,
			 'e':5 ,
			 'f':6 ,
			 'g':7 ,
			 'h':8 ,
			 'i':9 ,
			 'l':10 ,
			 'm':11 ,
			 'n':12 ,
			 'o':13 ,
			 'p':14 ,
			 'q':15 ,
			 'r':16 ,
			 's':17 ,
			 't':18 ,
			 'u':19 ,
			 'v':20 ,
			 'z':21 
}
#CRIPTA UN MESSAGGIO DATA UNA CHIAVE#
def cerca_lettere(k, string_l):
 for letter in string_l:                        #PER OGNI LETTERA DEL MESSAGGIO
  code_l= (reverse_alfabeto[ letter ] * k)%21   #CALCOLA IL CORRIPONDENTE NUMERICO E AGGIUNGI LO SHIFT(MOD 20)
  sys.stdout.write( alfabeto[code_l] )          #TROVA LA NUOVA LETTERA CORRISPONDENTE
  

  
def format(string_l):
    string_l = string_l.lower()                 #elimina gli spazi a inizio stringa
    string_l = string_l.replace(" ", "")        #elimina tutti i caratteri speciali
    string_l = string_l.replace(",", "")
    string_l = string_l.replace(".", "")
    string_l = string_l.replace("?", "")
    string_l = string_l.replace("!", "")
    return string_l
    

   
#MAIN DEL PROGRAMMA#  
while "true":
	message = input("INSERIRE MESSAGGIO:\n")
	key = int( input("INSERIRE CHIAVE\n") )
	print (" MENU':\n(1):CODIFICA-DECODIFICA\n(2).EXIT\n");
	s = int (input("FAI LA TUA SCELTA => "))
	#ADEGUA LA STRINGA
	message = format(message) 
    
#SWITCH CASE#
	if s == 1:
	  cerca_lettere(key, message)
	elif s == 2:
          exit()           
	else:
          print("##ERROR##")

	print("\n")
#FINE PROGRAMMA
