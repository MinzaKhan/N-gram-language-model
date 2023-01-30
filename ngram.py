'''importing the library for regular expressions.'''
import re
'''importing the sys library to read the command line arguments'''
import sys
'''importing the library random so that the code randomly chooses from the list of unigrams bugrams and trigrams.'''
import random

'''storing whether the user wants a unigram, bigram, or trigram language model'''
model = int(sys.argv[1])
'''storing the number of sentences that need to be generated.'''
number_of_sentences = int(sys.argv[2])
'''The list List will store all the text from all the text files input by the user.'''
input_by_user =sys.argv[1]
for i in range(2, len(sys.argv)):
	input_by_user = input_by_user+" "+sys.argv[i]
print(input_by_user)

List=[]
for i in range(3, len(sys.argv)):
	'''Parsing through each text file and storing all the text in str_1'''
	str_1 =open(sys.argv[i], encoding="utf8").read()
	'''Appending the text to the list List'''
	List.append(str_1)

#List_1 contains all files added.
'''List_1 will contain all tprocessed text files.'''
List_1 =[]
for i in range(0, len(List)):
	str_new=  re.sub('\n', ' ', List[i])
	#removing any text that isn’t an alpha or a . , ? !	'
	str_new2=  re.sub('[^A-Za-z0-9\?,\.!\']', ' ', str_new)
	#separating . from alpha text
	str_new2 = re.sub('\.', ' . ', str_new2)
	#separating , from alpha text
	str_new2 = re.sub(',', ' , ', str_new2)
	#separating ? from alpha text
	str_new2 = re.sub('\?', ' ? ', str_new2)
	#separating ! from alpha text
	str_new2 = re.sub('!', ' ! ', str_new2)
	#converting all text to lower case
	str_new2=str_new2.lower()
	#adding processed text to List_1
	List_1.append(str_new2)


#The list all_sentences will contain lists of each sentence present in all documents
all_sentences=[]

for i in range(0, len(List_1)):
	'''This regular expression is being used to identify sentence boundaries.'''
	list1 = re.split("(.*?[\?!\.])", List_1[i])
	for l in list1:
		if(l!=None):
			'''Splitting each sentence to make sure that no empty lists get added to the list all_sentences.'''
			x=l.split()
			if(len(x)>0):
				all_sentences.append(x)

'''Calculating the number of tokens for unigram. This includes , . and ?'''
number_of_tokens =0
for i in range(0, len(List_1)):
	'''going through all processed text and splitting it, then counting all words present in the text.'''
	temp_str = List_1[i]
	num = temp_str.split()
	number_of_tokens = number_of_tokens + len(num)


'''The list starting_words_unigram is created to store all the first words of each sentence. These will later be used to generate sentences.'''
starting_words_unigram = []
for sentence in all_sentences:
	starting_words_unigram.append(sentence[0])


'''Calculating the number of types for unigram'''
temp_str2=""
for i in range(0, len(List_1)):
	'''All the text from all text files is stored in the string temp_str2'''
	temp_str2 = temp_str2 + " " +List_1[i]
'''We create a set after splitting the string. The set type_set stores all unique unigram types present in the document. 
The number of elements in type_set is the number of unigram types. '''
type_set = set(temp_str2.split())
'''The list all words contains a list of each word present in all text files.'''
all_words = temp_str2.split()

'''Calculate probability of each word.'''
'''The dictionary 'dictionary' stores all the unigram types and their probabilities.'''
dictionary = {}
'''The dictionary 'dictionary_count' stores all the unigram types and their counts.'''
dictionary_count = {}
for i in type_set:
	count = 0
	for j in range(0, len(all_words)):
		'''We check how many times each word is present in the text.'''
		if(i == all_words[j]):
			count = count+1
	dictionary_count[i] = count	
	'''Calculating the probability of each unigram type and storing it in 'dictionary'.'''
	dictionary[i] = count/len(all_words)

unigram_words=[]
unigram_probability =[]

for i, j in dictionary.items():
	unigram_words.append(i)
	unigram_probability.append(j/count)

'''If the user wants a unigram model, then the code will enter this loop and generate the number of sentences requested by the user based on the unigram language model.'''
if(model==1):
	print("UNIGRAM")
		
	print("SENTENCES:")
	'''This for loop will generate as many sentences as requested by the user.'''
	for i in range(0, number_of_sentences):
		sentence_unigram =""
		'''Randomly choosing a starting unigram from the list of unigrams. Each unigram token is present in the list as many times as it appears in the document,
		so the probability of getting any unigram type is based on how many times it appears in the text document.'''
		sentence_unigram = sentence_unigram + random.choice(starting_words_unigram)
		'''This while loop will keep generating unigram types randomly accoring to their probabilities and adding them to the sentence, until a terminating 
		punctuation mark occurs.'''
		while(sentence_unigram.find(".")==-1 and sentence_unigram.find("!")==-1 and sentence_unigram.find("?")==-1):
			z = random.choices(unigram_words, weights=unigram_probability)
			if(z[0] == "." or z[0] == "!" or z[0] == "?"):
				sentence_unigram = sentence_unigram+ z[0]
			else:
				sentence_unigram = sentence_unigram +" "+ z[0]

		'''Printing the sentence generated.'''
		print(i+1," : ",sentence_unigram)
	print ("The number of tokens is: ", number_of_tokens)


'''BIGRAMS'''

'''Calculating the number of bigram tokens by matching the string with the given regular expression. This includes , . and ?'''

List_of_bigrams = []
number_of_tokens_2 =0
counter = 0
bigram = []
bigram_dict = {}
starting_words_bigram = []
bigram_list = []
for sentence in all_sentences:
	'''add all starting bigram tokens to the list starting_words_bigram'''
	if(len(sentence)>=2):
		str_temp2 = sentence[0] + " "+ sentence[1]
		starting_words_bigram.append(str_temp2)
	for i in range(0, len(sentence)-1):
		'''Adding all unique bigram types and their counts to the dictionary bigram_dict'''
		str_temp = sentence[i] + " "+ sentence[i+1]
		if str_temp not in bigram_dict:
			bigram_dict[str_temp] = 1
		else:
			bigram_dict[str_temp] = bigram_dict[str_temp]+1
		'''The variable counter stores the number of bigram tokens.'''
		counter = counter+1


bigram_dict_count=bigram_dict
for i,j in bigram_dict.items():

	str_temp_bigram = i.split()
	'''The value of bigram_dict is the conditional probability of the bigram token, calculated by dividing the count of the bigram by the number of times that
	the first word of the bigram appears in the text document.'''
	bigram_dict[i] = j/dictionary_count[str_temp_bigram[0]]

'''Create dictionary containig all bigrams and their probabilities.'''

'''If the user wants a bigram model, then the code will enter this loop and generate the number of sentences requested by the user based on the bigram language model.'''
if(model==2):
	print("BIGRAM")
	
	print("SENTENCES:")
	for temp_num in range(0, number_of_sentences):
		sentence =""
		while(True):
			'''Choosing a random starting bigram token from the list starting_words_bigram whch contains all bigram tokens present in the beginning of each sentence.'''
			sentence = sentence + random.choice(starting_words_bigram)
			'''If the starting bigram token contains a terminating punctuation mark, then another bigram token is chosen.'''
			if(sentence.find(".")==-1 and sentence.find("?")==-1 and sentence.find("!")==-1):
				break
			else:
				sentence = ""
		x = sentence.split()
		temp = x[1]
		probability = 0.0
		new_text=""
		temp_list = []
		prob_list =[]
		'''This while loop keeps predicting bigram tokens until a bigram with a terminating punctuation mark is predicted.'''
		while(sentence.find(".")==-1 and sentence.find("?")==-1 and sentence.find("!")==-1 ):
			'''Looping through all bigram types.'''
			for i,j in bigram_dict.items():
				string = i
				x = string.split()
				'''Checking if the last word in the sentence generated till now matches the first word of the bigram type. If it does,
				the second word of the bigram type is added to the list temp_list, and its conditional probability is added to the list prob_list.'''
				if(x[0] == temp):
					prob_list.append(j)
					temp_list.append(x[1])
			'''A random word is chosen from the list of all possible words based on the bigram model, according to the conditional probability of each word.'''
			new_text = random.choices(temp_list, weights=prob_list)
			'''Adding the randomly chosen word to the sentence. If the word is a terminating punctuation mark, then the while loop ends and prints the generated sentence.'''
			if(new_text[0] == "." or new_text[0] == "!" or new_text[0] == "?"):
				sentence = sentence+new_text[0]
				break
			else:
				sentence = sentence+" "+new_text[0]
			temp = new_text[0]
			temp_list=[]
			prob_list=[]
		print(temp_num+1, " : ",sentence)
	print ("The number of tokens is: ", counter)


'''TRIGRAMS'''

List_of_trigrams = []
number_of_tokens_3 =0
counter = 0
trigram_dict = {}
starting_words_tri = []
trigram_list = []

for sentence in all_sentences:
	'''add all starting trigram tokens to the list starting_words_tri.'''
	if(len(sentence)>3):
		str_temp2 = sentence[0] + " "+ sentence[1]+ " "+sentence[2]
		starting_words_tri.append(str_temp2)
	'''Creating trigram types and saving them and their countin the dictionary trigram_dict'''
	for i in range(0, len(sentence)-2):
		str_temp = sentence[i] + " "+ sentence[i+1] +" "+ sentence[i+2]
		if str_temp not in trigram_dict:
			trigram_dict[str_temp] = 1
		else:
			trigram_dict[str_temp] = trigram_dict[str_temp]+1
		counter = counter+1		

'''Calculating the conditional probability of each trigram type, by dividing its count by the count of the first two words of the trigram type, and saving
it as a value in the dictionary trigram_dict.'''
for i,j in trigram_dict.items():
	str_temp_trigram = i.split()
	str_tri = str_temp_trigram[0]+" "+str_temp_trigram[1]
	trigram_dict[i] = j/bigram_dict_count[str_tri]


'''If the user wants a trigram model, then the code will enter this loop and generate the number of sentences requested by the user based on the trigram language model.'''
if(model==3):
	print("TRIGRAMS")
	print("SENTENCES:")
	'''This for loop generated the number of sentences requested by the user.'''
	for temp_num in range(0, number_of_sentences):
		sentence =""
		while(True):
			print("a")
			'''Choosing a random starting trigram token from the list starting_words_trigram whch contains all trigram tokens present in the beginning of each sentence.'''
			sentence = sentence + random.choice(starting_words_tri)
			'''If the starting trigram token contains a terminating punctuation mark, then another trigram token is chosen.'''
			if(sentence.find(".")==-1 and sentence.find("?")==-1 and sentence.find("!")==-1):
				break
			else:
				sentence = ""
		z = sentence.split()
		'''storing the second and third word of the generated trigram'''
		test = z[1]+" "+z[2]
		probability = 0.0
		new_text=""
		temp_list = []
		prob_list =[]
		test_2 =""
		'''This while loop keeps predicting trigram tokens until a trigram with a terminating punctuation mark is predicted.'''
		while(sentence.find(".")==-1 and sentence.find("?")==-1 and sentence.find("!")==-1 ):
			'''Looping through all trigram types.'''
			for i,j in trigram_dict.items():
				string = i
				x = string.split()
				x_test = x[0]+" "+x[1]
				'''Checking if the last two words in the sentence generated till now match the first two words of the trigram type. If it does,
				the third word of the trigram type is added to the list temp_list, and its conditional probability is added to the list prob_list.'''
				if(test == x_test):
					prob_list.append(j)
					temp_list.append(x[2])
			'''A random word is chosen from the list of all possible words based on the trigram model, according to the conditional probability of each word.'''
			new_text = random.choices(temp_list, weights=prob_list)
			'''Adding the randomly chosen word to the sentence. If the word is a terminating punctuation mark, then the while loop ends and prints the generated sentence.'''
			if(new_text[0] == "." or new_text[0] == "!" or new_text[0] == "?"):
				sentence = sentence+new_text[0]
				break
			else:
				sentence = sentence+" "+new_text[0]
			sentence_temp = sentence.split()
			test = sentence_temp[len(sentence_temp)-2]+" "+sentence_temp[len(sentence_temp)-1]			
			temp_list=[]
			prob_list=[]
		print(temp_num+1, " : ",sentence)
	print ("The number of tokens is: ", counter)
