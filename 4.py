roznica = ord('a')-ord('A')
litera = input("Wprowadz litere: ")

if 'a' <= litera <= 'z' :
    print(chr(ord(litera)-roznica))
elif 'A' <= litera <= 'Z':
    print(chr(ord(litera)+roznica))
else :
    print("to nie jest litera")

