# F2 - rename
# ctrl + \ - nowe okno edycji
# ctrl + f4 - zamknij okno edycji

q = "THE EYES"
print(q[:3], q[5], q[3], q[7], q[4], q[6], sep="")

q = "a gentleman"
print(q[3], q[6], q[7], q[2], q[0], q[4], q[5], q[1], q[8:], sep="")

line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[line.find(":") + 2 :]

tmp = line[line.find('"') + 1 :]
title = tmp[: tmp.find('"')]

title2 = line[line.find('"') + 1 : line.find('"', line.find('"') + 1)]
print(time, title2)

# python nie wywala błędów przy niepoprawnie wprowadzonym zakresie - jest inteligenty, np. line[5:9999] wyświetli od 5 do końca str a line[999:] wyświetli jako pustą liste