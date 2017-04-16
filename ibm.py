import re
import collections
import copy

def buildCorpus(englishFile,frenchFile):
	freTest = open("writetest.txt","w+")
	engFile = open(englishFile,"r")
	freFile = open(frenchFile,"r")
	corpus=[]
	for line in engFile:
		fline=freFile.readline()
		line1=""
		fline1=""
		if (line[-1]=='\n'):
			if(line[-2]=='.' or line[-2]==',') :
				# engCorpus.append(line[:-2])
				line=line[:-2]
				fline=fline[:-2]
			else:
				# engCorpus.append(line[:-1])
				line=line[:-1]
				fline=fline[:-1]
		else:
			if(line[-1]=='.' or line [-1]==','):
				# engCorpus.append(line[:-1])
				line=line[:-1]
				fline=fline[:-1]
		for letter in line:
			if(letter.isalnum() or letter.isspace() or letter=="'"):		#edit if you want single quotes to be
				line1+=letter
		for fletter in fline:
			if(fletter!='"'  and fletter!="," and fletter!="."):	#and fletter!="'"
				fline1+=fletter
		fline1+=' '

		line1 = line1.lower()
		fline1 = fline1.lower()
		freTest.write(fline1)
		corpus.append((line1,fline1))
	print corpus
	return corpus
	engFile.close()
	freFile.close()
	freTest.close()

def const(value):
    return lambda: value

def train(corpus, max_iter=10000):
    f_words = set()
    for (es, fs) in corpus:
        for f in fs:
            f_words.add(f)
    t = collections.defaultdict(const(1.0/len(f_words)))
    t_old = None
    i = 0
    while i < max_iter and t_old != t:
        t_old = copy.copy(t)
        count = collections.defaultdict(float)
        total = collections.defaultdict(float)
        s_total = collections.defaultdict(float)
        for (es, fs) in corpus:
            for e in es:
                s_total[e] = float()
                for f in fs:
                    s_total[e] += t[(e, f)]
            for e in es:
                for f in fs:
                    count[(e, f)] += t[(e, f)] / s_total[e]
                    total[f] += t[(e, f)] / s_total[e]
        for (e, f) in count.keys():
            t[(e, f)] = count[(e, f)] / total[f]
            if t[(e, f)] < 0.00001:
                t[(e, f)] = 0
        i += 1
        # print i
    for (e, f), val in t.items():
		print("{}\t{}\t{}".format(e, f, val))
    return t

def fre_to_eng(sentences, max_iter=10000):
    tokenized_corpus = [(es.split(), fs.split()) for (es, fs) in sentences]
    t = train(tokenized_corpus, max_iter)
    mp = tmap(t)
    return mp
def eng_to_fre(sentences, max_iter=10000):
    tokenized_corpus = [(fs.split(), es.split()) for (es, fs) in sentences]
    t = train(tokenized_corpus, max_iter)
    mp = tmap(t)
    return mp
def tmap(t):
    mx = collections.defaultdict(float)
    mp = {}
    for (e,f), val in t.items():
        if(val > mx[f]):
            mp[f], mx[f] = e, val
        elif(val == mx[f] and val > 0):
            mp[f] += " "
            mp[f] += e
        # mp[f], mx[f] = (e, val) if val >= mx[f] else (mp[f], mx[f])
    return mp

def translate(qs, mp):
    rs = [mp[q] if q in mp.keys() else q for q in qs]
    str = " ".join(rs)
    return str

# def test(sent_pairs):
#     sent_pairs = [("the house", "Haus das"),
#                   ("the new  book", "das Buch"),
#                   ("a new shiny book", "ein Buch"),]
#     query = ["Buch","Haus"]
#     t = fre_to_eng(sent_pairs)
#     for (e, f), val in t.items():
#         print("{}\t{}\t{}".format(e, f, val))
#     mp = tmap(t)
#     #print mp
#     return mp
#     #print translate(query,mp)

def main():
	# sent_pairs = [("the house", "Haus das"),
 #                  ("the new  book", "das Buch"),
 #                  ("a new shiny book", "ein Buch")]
	# query = ["buch","haus"]
	sent_pairs = buildCorpus('parallel_corpus_IR2/eng.txt','parallel_corpus_IR2/fre.txt')	#change filenames
	# sent_pairs = buildCorpus('e1.txt','f1.txt')
	f_to_e = fre_to_eng(sent_pairs)
	# e_to_f = eng_to_fre(sent_pairs)
	#query
	query=["reprise","bonnes","dernier"]
	print f_to_e
	print translate(query,f_to_e)		#give choices for language translation


if __name__ == '__main__':
	main()
