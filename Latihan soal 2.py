#soal 1: Perbedaan data Structure
#List: tipe data yang terbentuk dari beberapa objek baik itu integer, float dll.
#tuple: tipe data ordered yang mana tidak dapat diubah objectnya.
#Dictionary: pasangan key-value dan ditandai dengan {} kurung kurawal.

#soal 2: Akses list
a = ['1', '13b', 'aa1', 1.32, 22.1, 2.34]
print (a [1:5])

#soal 3: Akses nested list
a = [
    [5, 9, 8],
    [0, 0, 6]
    ]
print (a [1] [1:3])

#soal 4: List manipulation
a = [
    [5, 9, 8],
    [0, 0, 6],
    [5, 9, 10],
    [11, 0, 6]
    ]
print (a [2:4])

#soal 5: Delete element list
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
del areas [8:10]
print (areas)

#saol 6: List comprehension
S = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

T = [x for x in S if x %2 == 0]
print (T)

#soal 8: Menambahkan key-value baru ke Dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

europe ["italy"] = "roma"

print (europe)

#soal 9: Boolean Comparison
print ((10>11)) and ((15<17))
print ((10==10)) or ((12==11))
print (not (20>31))

#soal 10: If-Else Statement
A = 26000
if A > 100000 :
    print ("high")
elif A > 50000 :
    print ("medium")
elif A <= 50000 :
    print ("low")



