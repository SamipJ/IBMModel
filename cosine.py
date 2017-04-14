import re
import math

def computeCosine(doc1,doc2):
    with open(doc1, 'r') as myfile:
        phrase=myfile.read().replace('\n',' ')
    list1 = re.findall('\w+', phrase)
    list1 = [element.lower() for element in list1]

    dict1= {}
    for word in list1:
        if dict1.has_key(word):
            dict1[word] = dict1[word]+1
        else:
            dict1[word] = 1


    with open(doc2, 'r') as myfile:
        phrase=myfile.read().replace('\n',' ')

    list2 = re.findall('\w+', phrase)

    list2 = [element.lower() for element in list2]


    dict2= {}

    for word in list2:
        if dict2.has_key(word):
            dict2[word] = dict2[word]+1
        else:
            dict2[word] = 1

    prod = 0
    squaresum1 = 0
    squaresum2 = 0

    for key in dict1.keys():
        if dict2.has_key(key):
            prod += dict1[key]*dict2[key]
        squaresum1 += dict1[key]**2

    for key in dict2.keys():
        squaresum2 += dict2[key]**2

    magnitude1 = math.sqrt(squaresum1)
    magnitude2 = math.sqrt(squaresum2)

    cosine = prod/(magnitude1 * magnitude2)

    print cosine
def main():
    computeCosine("words1.txt","words2.txt")

if __name__ == '__main__':
  main()
