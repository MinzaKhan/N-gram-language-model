This is a command line program that develops an ngram language model from any number of plain text files
specified in the command line. The program will generate any number of sentences specified in the command line, based on the ngram model.
The user will input whether they want a unigram, bigram, or trigram model by entering the input 1, 2, or 3 in the command line.

EXAMPLES:
INPUT: PA2.py 2 3 alittleprincess.txt prideandprejudice.txt
In this input, PA2.py is the name of the program. The forst argument after that is to specify whether the user wants a unigram, bigram,
or trigram language model. Since the value of the argument is 2, the program will generate a bigram language model. The next argument is the 
number of sentences that the user wants the program to generate. Since this number is 3, the program will print 3 sentences as output. 
the rest of the arguments are the names of the text files based on which the language model will be generated. The user can input as many 
text files as they want. For this input, the text files that the program will read are alittleprincess.txt and prideandprejudice.txt

OUTPUT: 
2 10 alittleprincess.txt prideandprejudice.txt
BIGRAM
SENTENCES:
1 : yes , and it was certain sixpence and elizabeth was spared her.
2 : in a great spirits she should have removed into insignificance.
3 : she looked at all his tenants , and others think we were aware of his speech?
The number of tokens is: 210598


USAGE INSTRUCTIONS: First give the argument 1 in command line for unigram language model, 2 for bigram language model, and 3 for trigram
language model. Then enter the number of sentences that the program should print based on the ngram model. After that, write the names of the 
text files based on which the program will create the ngram language model. The program can take any number of text files and generate an ngram
model based on that.

ALGORITHM:

The program first stores the input. The text files are opened and read by the program and then the entire text from each file
is stored in a list called List. Then the text is processed. All characters that are not alpha characters, numbers, or . , ! ? ' are 
substitued by '' using the regular expression: [^A-Za-z0-9\?,\.!\' ]. After this, all the text is changed to lowercase.
To identify sentence boundaries, all the text is split whenever a . ? or ! is found, using the regular expression (.*?[\?!\.]) to match the
text. All the sentences are stored separately in a list named all_sentences.

For unigrams, first the number of tokens is calculated, by splitting the words in each sentence using str.split() and calculating the number
of words. This count includes all ? . and , . Then the number of types and the count of each type is calculated. This is done by creating
a dictionary called dictionary, that stores each word as the key, and its count as the value. The program goes through he entire text 
and every time a word is encountered, it checks whether the word is present in the dictionary or not. If the word is not present, it is added 
to the dictionary and the count is set to 1 for the word. If the word encountered is already present in the dictionary, 
then the count of the word is incremented by 1. A list starting_words_unigram has been created which stores all the words that have been used
in the beginning of any sentence present in the text files given as input by the user. 
To generate the sentence, the program first chooses a random unigram from the list starting_words_unigram. It then randomly chooses the next
word based on the probability of the unigram types. This probability is calculated by dividing the count of the word by the total number
of tokens. The program keeps adding words to the sentence until it naturally predicts a terminating punctuation mark - . ! or ?. 

For bigram, the number of tokens is calculated by going through each sentence and then going through a loop that checks each word in the
sentence and creates sets of two words until it reaches the end of the sentence. The words are stored in a dictionary called bigram_dict, which also stores the count
of each bigram type. If a bigram token is not present in bigram_dict, then it is added to bigram_dict, and a count of 1 is assigned to it.
If a bigram token is already present in bigram_dict, then its count is incremented by 1. A list of starting bigrams is stored in a 
list called starting_words_bigram, which stores all the bigram tokens that have been used in the beginning of any sentence 
present in the text files given as input by the user. The probability of each bigram type is then calculated by dividing 
the count of bigram type by the number of times the first word of the bigram is present in the entire text.
To generate the sentence, the program first chooses a random bigram from the list starting_words_bigram. It then predicts the next word
by going through the entire dictionary that includes all bugram types and their probability. It checks which bigram tokens have the same
first word as the second word of the previously chosen bigram. A list of all such bigram types and their probabilities is created.
Then a bigram type is chosen randomly based on the probabilities of the bigram types. Then the second word of the randomly chosen bigram is
added to the sentence. This goes on until the program randomly generates a bigram that has a terminating punctuation mark - . ! or ?.

For trigram, the number of tokens is calculated by going through each sentence and then going through a loop that checks each word in the
sentence and creates sets of three words until it reaches the end of the sentence. The words are stored in a dictionary called trigram_dict, 
which also stores the count of each trigram type. If a trigram token is not present in trigram_dict, then it is added to trigram_dict, and a count of 1 is assigned to it.
If a trigram token is already present in trigram_dict, then its count is incremented by 1. A list of starting trigrams is stored in a 
list called starting_words_trigram, which stores all the trigram tokens that have been used in the beginning of any sentence 
present in the text files given as input by the user. The probability of each trigram type is then calculated by dividing 
the count of the trigram type by the number of times the first 2 words of the trigram is present in the entire text.
To generate the sentence, the program first chooses a random trigram from the list starting_words_trigram. It then predicts the next word
by going through the entire dictionary that includes all trigram types and their probability. It checks which trigram tokens have the same
first and second word as the second and third word of the previously chosen bigram. A list of all such trigram types and their probabilities is created.
Then a trigram type is chosen randomly based on the probabilities of the trigram types. Then the third word of the randomly chosen trigram is
added to the sentence. This goes on until the program randomly generates a trigram that has a terminating punctuation mark - . ! or ?.
