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

