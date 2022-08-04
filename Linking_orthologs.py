import os
import re
import numpy as np
print("Enter the path to the folder")
path = input()
print("The name of the output file")
save_name = input()

def atoi(text):
	return int(text) if text.isdigit() else text
	
def natural_keys(text):
	return [atoi(c) for c in re.split(r"(\d+)", text)]

number = 0
lista = []
l = []
p = []
files = os.listdir(path)

for f in files:
	l.append(str(f))

l.sort(key=natural_keys)	
print("Files taken for analysis: " + str(l))	




for i in l:
	with open(path + "/" + i , 'r') as file:
		for line in file:
			line = file.read().replace("\n","").split(">")
		lista.append(line)



array1 = np.array(lista)
array1_transpose = array1.transpose()
lista1 = array1_transpose.tolist()

o=0
with open(save_name, 'a') as save:			
	for x in lista1:
		save.write('>' + str(o) + '\n')		
		for n in x:
			new_n = re.sub(r"(\d)-(\d)", "", str(n))
			new1_n = re.sub(r"[A-Z0-9:+=_!@#$%^&*()]","", str(new_n))
			save.write(new1_n)
		save.write("\n")
		o+=1

