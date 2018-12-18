alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
get_file_frequency = open ('warPeace.txt')
file_frequency = get_file_frequency.read()
def encoding_initial():	
	get_file = open('file.txt')
	text_of_file = get_file.read()
	text_to_be_put=[]
	for x in text_of_file :		
		x = x.lower()
		if x in alphabet:	    
			y=alphabet.index(x)
		else:
			text_to_be_put.append(x)
			continue
			
		if y > 23:
			x = alphabet[-24 + y]
			text_to_be_put.append(x)
		else:
			x = alphabet[y+2]
			text_to_be_put.append(x)
				
			
	open_encoded_text = open("file_encoded.txt", "w")
	encoded_text="".join(text_to_be_put)
	open_encoded_text.write(encoded_text) 
	return text_to_be_put

	
def decoding():
	frequency_of_original_text = []
	frequency_array_to_decode=[]
	array_to_decode =encoding_initial()
	string_to_decode = "".join(array_to_decode)
	decoded_string = ""
	for x in alphabet :
			try:
				y = array_to_decode.count (x)
				frequency = y/len(array_to_decode)
				frequency_array_to_decode.append([frequency,x])
			except:
				frequency_array_to_decode.append([0,x])
	
	
	for x in alphabet:
			try:
				y = file_frequency.count (x)
				frequency = y/len(file_frequency)
				frequency_of_original_text.append([frequency,x])
			except:
				frequency_of_original_text.append([0,x])
				
	
	
	sorted_frequency_array_to_decode = sorted(frequency_array_to_decode, key = lambda x: x[0] )
	sorted_frequency_of_original_text = sorted(frequency_of_original_text, key = lambda x: x[0] )
	print(sorted_frequency_array_to_decode)
	print(sorted_frequency_of_original_text)
	
	i = 0 
	while i<len(sorted_frequency_array_to_decode):
		string_to_decode = string_to_decode.replace(sorted_frequency_array_to_decode[i][1], sorted_frequency_of_original_text[i][1])
		i+=1
	save_decoded_string = open("file_decoded.txt", "w")
	save_decoded_string.write(string_to_decode) 
	
decoding()

	
