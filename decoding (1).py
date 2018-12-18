import string,numpy

def open_text(txt):
	s = ''.join([line.rstrip() for line in open(txt)])  
	b = "".join([f.lower() for f in s if f not in string.digits])
	return b

def get_list(txt):
	occurences = {}
	i=0
	while True:
		if i+2>len(txt):
			break
		occurences[txt[i:i+2]] = occurences.get(txt[i:i+2],0) + 1
		i+=1
	length = len(txt)-1
	list = []
	for k, v in occurences.items():
		list.append([k,v/length])
	sorted_list = sorted(list, key = lambda x : x[1])
	print(sorted_list)
	return sorted_list


list_frequency_original = get_list(open_text('file.txt'))
list_frequency_encoded = get_list(open_text('file_encoded.txt'))
#длинны массивов соответственны
if (len(list_frequency_original) > len(list_frequency_encoded)):
	del list_frequency_original[0: len(list_frequency_original) -  len(list_frequency_encoded)]
elif (len(list_frequency_original) < len(list_frequency_encoded)):
	del list_frequency_original[0: len(list_frequency_encoded) -  len(list_frequency_original)]

	
encoded_text_to_decode = open_text('file_encoded.txt')
encoded_text_to_decode_array = list(encoded_text_to_decode)
#x = [x for x in list_frequency_encoded if 'qp'  in x][0]
#print(list_frequency_encoded.index(x))

z = 0
while True:
	if z+2>len(encoded_text_to_decode):
		break
	#добавляем 
	encoded_text_to_decode_array.insert(z+2, encoded_text_to_decode[z+1])
	#меняем
	x = [x for x in list_frequency_encoded if encoded_text_to_decode[z:z+2]  in x][0] #получаем нужный массив 
	y = list_frequency_encoded.index(x) #получаем индекс нужного массива 
	p = list_frequency_original[y][0] # получаем стринг на который надо заменить 
	print(p)
	encoded_text_to_decode_array[z] = p[0]
	encoded_text_to_decode_array[z+1] = p[1]
	#удаляем
	encoded_text_to_decode_array.pop(z+1)
	z+=1
print("".join([f for f in encoded_text_to_decode_array]))








