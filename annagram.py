prime = [2]

for i in range(3,200):
    modulus = []
    for j in range(2,i):
        modulus.append(i%j)
    if 0 not in modulus:
        prime.append(i)
    if len(prime)==37:
        break
#print(prime)
alpabets = "abcdefghijklmnopqrstuvwxyz 1234567890"

string1 = input("Enter string1 : ")
string2 = input("Enter string2 : ")

string1val =1
string2val =1

for items1 in string1:
    string1val = string1val*prime[alpabets.index(items1.lower())]

for items2 in string2:
    string2val = string2val*prime[alpabets.index(items2.lower())]

if string1val == string2val:
    print("given words are annagram")
else:
    print("given words are NOT annagram")
