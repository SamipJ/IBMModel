import re
def computeJaccard(doc1,doc2):

    f1 = open(doc1,'r')								#opening files in read-only mode
    f2 = open(doc2,'r')

    d1 = []									#creating lists to store unique words in a document
    d2 = []

    intersect = []								#list containing the words common in both the documents

    for line in f1:								#parsing through each word in each line in doc1
        for word in re.compile('\w+').findall(line):
            word=word.lower()
            if word not in d1:							#adding the word to d1, if it is not already present
                d1.append(word)

    for line in f2:								#parsing through each word in each line in doc2
        for word in re.compile('\w+').findall(line):
            word=word.lower()
            if word not in d2:							#adding the word to d2, if it is not already present
                d2.append(word)

                if word in d1:							#adding this word to intersect, if it is present in d1
                    intersect.append(word)

    score = float(len(intersect))/float((len(d1)+len(d2)-len(intersect)))	#calculating score=(no. of words in intersection(doc1,doc2))/(no. of words in union(doc1,doc2))
    return score

def main():
    computeJaccard("doc1.txt","doc2.txt")

if __name__ == '__main__':
  main()
