ListGPA = [2.1,2.5,4,3]
for b in range (4):
    print(ListGPA[b])

def bonus(a):
    bonus = a*500000
    return bonus

for a in ListGPA:
    if a > 2.5:
        print("Selamat anda mendapatkan bonus sebesar: ",bonus(a))
    else:
        print("Maaf anda tidak mendapatkan bonus")

