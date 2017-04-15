import re
def computeJaccard(doc1,doc2):
	#opening files in read-only mode
    f1 = open(doc1,'r')
    f2 = open(doc2,'r')
	#creating lists to store unique words in a document
    d1 = []
    d2 = []
	#list containing the words common in both the documents
    intersect = []
	#parsing through each word in each line in doc1
    for line in f1:
        for word in re.compile('\w+').findall(line):
			#adding the word to d1, if it is not already present
            if word not in d1:
                d1.append(word)
	#parsing through each word in each line in doc2
    for line in f2:
        for word in re.compile('\w+').findall(line):
			#adding the word to d2, if it is not already present
            if word not in d2:
                d2.append(word)
				#adding this word to intersect, if it is present in d1
                if word in d1:
                    intersect.append(word)
	#calculating score=(no. of elements in intersection(doc1,doc2))/(no. of words in union(doc1,doc2))
    score = float(len(intersect))/float((len(d1)+len(d2)-len(intersect)))
    print score

def main():
    computeJaccard("doc1.txt","doc2.txt")

if __name__ == '__main__':
  main()
