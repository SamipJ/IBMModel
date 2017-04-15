import re						#for regular expressions
import math						#for square root			

def computeCosine(doc1,doc2):				#takes two documents as argument and prints the cosine similarity between them
    with open(doc1, 'r') as myfile:
        phrase=myfile.read().replace('\n',' ')
    list1 = re.findall('\w+', phrase)
    list1 = [element.lower() for element in list1]	#list1 contains all tokens from doc1 in lowercase form

    dict1= {}
    for word in list1:					#loop to build dictionary of tokens from list1 with term frequency as values
        if dict1.has_key(word):
            dict1[word] = dict1[word]+1
        else:
            dict1[word] = 1


    with open(doc2, 'r') as myfile:			
        phrase=myfile.read().replace('\n',' ')
    list2 = re.findall('\w+', phrase)
    list2 = [element.lower() for element in list2]	#list2 contains all tokens from doc2 in lowercase form


    dict2= {}

    for word in list2:					#loop to build dictionary of tokens from list2 with term frequency as values
        if dict2.has_key(word):
            dict2[word] = dict2[word]+1
        else:
            dict2[word] = 1

    prod = 0						#dot product of the two document vectors
    squaresum1 = 0					#sum of squares of dimensions of document vector of doc1
    squaresum2 = 0					#sum of squares of dimensions of document vector of doc2

    for key in dict1.keys():				#loop to calculate prod and squaresum1
        if dict2.has_key(key):
            prod += dict1[key]*dict2[key]
        squaresum1 += dict1[key]**2

    for key in dict2.keys():				#loop to calculate squaresum2
        squaresum2 += dict2[key]**2

    magnitude1 = math.sqrt(squaresum1)			#magnitude of document vector of doc1
    magnitude2 = math.sqrt(squaresum2)			#magnitude of document vector of doc2

    cosine = prod/(magnitude1 * magnitude2)		#cosine similarity of doc1 and doc2

    print cosine
def main():						#main function
    computeCosine("words1.txt","words2.txt")

if __name__ == '__main__':
  main()
