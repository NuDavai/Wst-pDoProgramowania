sample_dict = {"name": "Kelly","surname": "Jones","age": 25,"salary": 8000,"city": "New york"}
print(sample_dict)
for k, v in sample_dict.items():
    print(k, "=" , v)

klucz=["name", "second_name", "height", "age", "weight", "country", "city"]
D_2={}
"""for i in range(len(klucz)):
    if klucz[i] in sample_dict.keys():        ZLE
        D_2[klucz[i]]=sample_dict[i]
print(D_2)"""
for i in klucz:
    for x in sample_dict.keys():
        if(i == x):
            D_2[i] = sample_dict[x]
print(D_2)

for k in klucz:
    if k in sample_dict.keys():
        sample_dict.pop(k)
print(D_2)

# for i in sample_dict:
#     if i=="Jones":
#         print("Jones wystepuje")      1 wersja
#         break
# else:
#     print("Nie wystepuje")

if "Jones" in sample_dict.values():
    print("Jones wystepuje")
else:
    print("Nie wystepuje")

