import re
def computeJaccard(doc1,doc2):
    f1 = open(doc1,'r')
    f2 = open(doc2,'r')
    d1 = []
    d2 = []
    intersect = []
    for line in f1:
        for word in re.compile('\w+').findall(line):
            if word not in d1:
                d1.append(word)
    for line in f2:
        for word in re.compile('\w+').findall(line):
            if word not in d2:
                d2.append(word)
                if word in d1:
                    intersect.append(word)
    score = float(len(intersect))/float((len(d1)+len(d2)-len(intersect)))
    print score

def main():
    computeJaccard("words1.txt","words2.txt")

if __name__ == '__main__':
  main()
