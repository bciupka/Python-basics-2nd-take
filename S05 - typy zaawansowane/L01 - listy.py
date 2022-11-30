hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
hitsTitles.extend(['CHILD IN TIME', 'AGAIN'])
hitsTitles.insert(2, 'HOTEL CALIFORNIA')
hitsTitles.insert(0, 'THE SOUND OF SILENCE')
print(hitsTitles.index("HOTEL CALIFORNIA"))

# ctrl +k, +ctrl +i - help --- najechanie myszką + przytrzymaniectrl - long help --- prawy/lewy przycisk - definicja
# ctrl +k, +s - zapisz wszystko

'''
listy w przeciwieństwie np do int odnoszą się do jednego regionu pamięci - tworząc listaKopia = listaOryginal nie tworzymy kopii tylko "pointer" do oryginału.
Metody listy modyfikujące jej skład (np. append, insert, remove, clear itp.) modyfikują oryginał, nie tak jak w str gdzie trzeba przepisać działanie metody na nową zmienną


append vs extend

append appends object at the end.

>>> x = [1, 2, 3]
>>> x.append([4, 5])
>>> print(x)
[1, 2, 3, [4, 5]]

extend extends list by appending elements from the iterable.

>>> x = [1, 2, 3]
>>> x.extend([4, 5])
>>> print(x)
[1, 2, 3, 4, 5]
'''

hitsTitles.remove("HOTEL CALIFORNIA")
hitsTitles[0] = "ENJOY THE SILENCE"
hitsToRead = hitsTitles.copy()
hitsToRead.reverse()
hitsToRead.sort()
hitsToRead.pop(0)
hitsToRead.pop(0)
additionalSongs = ['NOTHING COMPARES 2 U', 'WISH YOU WERE HERE']
hitsToRead.extend(additionalSongs)
print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))
print(hitsToRead)
hitsToRead.clear()
print(hitsToRead)