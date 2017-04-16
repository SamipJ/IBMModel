import re
import collections
import copy
import json
import io
import sys
import time
reload(sys)
sys.setdefaultencoding('latin-1')

#buildCorpus takes the English and French files as input, and outputs the corresponding corpus - as a list of tuples of corresponding English and French sentence pairs.
def buildCorpus(englishFile,frenchFile):
	print "Building Corpus..."
	start = time.time()
	# freTest = open("writetest.txt","w+")
	engFile = open(englishFile,"r")
	freFile = open(frenchFile,"r")
	corpus=[]
	#iterates over the text file containing English sentences, and reads the corresponding French translation.
	for line in engFile:
		fline=freFile.readline()
		#Processing the read files to remove delimiter characters and convert to lowercase
		line1=""
		fline1=""
		if (line[-1]=='\n' or line[-1]==' '):
			if(len(line) >=2 and (line[-2]=='.' or line[-2]==',')) :
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
			if(fletter!='"'  and fletter!="," and fletter!="." and fletter!="!" and fletter!="?" and fletter!="'"):	#
				fline1+=fletter
			elif(fletter=="'"):
				fline1+=" "

		line1 = line1.lower()
		fline1 = fline1.lower()
		# freTest.write(fline1)
		corpus.append((line1,fline1))
	engFile.close()
	freFile.close()
	# freTest.close()
	print "done"
	print "Time taken: {} minutes".format((time.time()- start)/60)
	return corpus

#returns a constant function
def const(value):
	return lambda: value

#returns the alignment weight heuristic for a english word at position i and french word at position j
def align(i,j):
    return 0.9 ** abs(i - j)

def process_query(filename,lang):
	queryFile=open(filename,"r")
	query_Sentences=[]
	for qline in queryFile:
		if(qline[-1]=='\n' or qline[-1]==' '):
			if((len(qline)>2) and (qline[-2]=='.' or qline[-2]==",")):
				qline=qline[:-2]
			else:
				qline=qline[:-1]
		else:
			if(qline[-1]=="." or qline[-1]==","):
				qline=qline[:-1]
		qline=qline.lower()
		qline1=""
		if(lang=='e'):
			for letter in qline:
				if(letter.isalnum() or letter.isspace() or letter=="'"):		#edit if you want single quotes to be
					qline1+=letter
		elif(lang=='f'):
			for fletter in qline:
				if(fletter!='"'  and fletter!="," and fletter!="." and fletter!="!" and fletter!="?" and fletter!="'"):	#
					qline1+=fletter
				elif(fletter=="'"):
					qline1+=" "
		else:							#check this before calling the function so that it doesn't return null
			print("Invalid Input")
			return None
		query_Sentences.append(qline1)
	return query_Sentences

#returns the conditional probablities of translation an english word given a french word
def train(corpus, max_iter=1000):
	print "Calculating probabilities..."
	start = time.time()
	f_words = set() #unique french words
	for (es, fs) in corpus:
		for f in fs:
			f_words.add(f)
	t = collections.defaultdict(const(1.0/len(f_words)))
	t_old = None
	ctr = 0
	#implement IBM Algorithm
	while ctr < max_iter and t_old != t:
		t_old = copy.copy(t)
		count = collections.defaultdict(float)
		total = collections.defaultdict(float)
		s_total = collections.defaultdict(float)
		for (es, fs) in corpus:
			for i,e in enumerate(es):
				s_total[e] = float()
				for j,f in enumerate(fs):
					s_total[e] += t[(e, f)] * align(i,j)
			for i,e in enumerate(es):
				for j,f in enumerate(fs):
					count[(e, f)] += t[(e, f)] * align(i,j) / s_total[e]
					total[f] += t[(e, f)] * align(i,j) / s_total[e]
		for (e, f) in count.keys():
			t[(e, f)] = count[(e, f)] / total[f]
			if t[(e, f)] < 0.00001:
				t[(e, f)] = 0.00001
		ctr += 1
		print "{}% done".format(100 * ctr/max_iter)
	# for (e, f), val in t.items():
		# if val > 0.01: print("{}\t{}\t{}".format(e, f, val))
	print "done"
	print "Time taken: {} minutes".format((time.time()- start)/60)
	return t

#returns the french -> english word map, and backs up final result in a json file
def fre_to_eng(sentences, max_iter=100):
	tokenized_corpus = [(es.split(), fs.split()) for (es, fs) in sentences]
	t = train(tokenized_corpus, max_iter)
	with io.open('t_fe.json','w+') as fp:
		data = json.dumps(t,fp, ensure_ascii = False)
		fp.write(unicode(data))
	print "probabilities saved in t_fe.json"
	mp = tmap(t)
	with io.open('map_fe.json','w+') as fp:
		data = json.dumps(mp,fp, ensure_ascii = False)
		fp.write(unicode(data))
	print "map saved in map_fe.json"
	return mp

#returns the english -> french word map, and backs up final result in a json file
def eng_to_fre(sentences, max_iter=100):
	tokenized_corpus = [(fs.split(), es.split()) for (es, fs) in sentences]
	t = train(tokenized_corpus, max_iter)
	with io.open('t_ef.json','w+') as fp:
		data = json.dumps(t,fp, ensure_ascii = False)
		fp.write(unicode(data))
	print "probabilities saved in t_ef.json"
	mp = tmap(t)
	with io.open('map_ef.json','w+') as fp:
		data = json.dumps(mp,fp, ensure_ascii = False)
		fp.write(unicode(data))
	print "map saved in map_ef.json"
	return mp

#returns the word map using the word translation probabilties
def tmap(t):
	print "Building map..."
	start = time.time()
	mx = collections.defaultdict(float)
	mp = {}
	for (e,f), val in t.items():
		if not (f in mp.keys()):
			mp[f], mx[f] = e, val
		elif(abs(val - mx[f]) < 0.05): #words concatenated if similar probability
			mp[f] += " "
			mp[f] += e
		# mp[f], mx[f] = (e, val) if val >= mx[f] else (mp[f], mx[f])
		elif(val > mx[f]):
			mp[f], mx[f] = e, val
	print "done"
	print "Time taken: {} minutes".format((time.time()- start)/60)
	return mp

#applies the given word map on the tokenized query and returns the translated string
def translate(qs, mp):
	rs = [mp[q] if q in mp.keys() else q for q in qs]
	str = " ".join(rs)
	str += ".\n"
	return str

#start program execution
def run():
	with io.open('map_fe.json','r') as fp:
		f_to_e_s = fp.read()
		f_to_e = json.loads(f_to_e_s)
	with io.open('map_ef.json','r') as fp:
		e_to_f_s = fp.read()
		e_to_f = json.loads(e_to_f_s)
	print len(f_to_e), ", ", len(e_to_f)
	transFile = open('translation.txt','w+')		#declare translated_filename='translation.txt' in driver
	num_query = int(raw_input("Enter the number of query files: "))
	for i in range(0,num_query):
		query_lang=str(raw_input("Enter language of query file (source) <enter 'e' for english, 'f' for french>: "))
		query_lang=query_lang.lower()
		if(query_lang!='e' and query_lang!='f'):
			print("Invalid Input")
			continue
		query_file=str(raw_input("Enter the query file name: "))
		qs = process_query(query_file,query_lang)
		for q in qs:
			q_tokens=unicode(q).split()
			if(query_lang=='e'):
				translated=translate(q_tokens,e_to_f)
			elif query_lang=='f':
				translated=translate(q_tokens,f_to_e)
			else:
				print("Invalid Input")
				translated=""
			print translated
			transFile.write(translated)
	transFile.close()
	# call Jaccard Coefficient and Cosine similarity
	corTrans_filename = str(raw_input("Enter the filename of the correct translation: "))
	#pass corTrans_filename and translated_filename='translation.txt' as parameters


#rebuilds the french->english and english->french word maps using the corpus
def rebuild():
	# sent_pairs = [("the house", "Haus das"),
					# ("the book", "das Buch"),
					# ("a book", "ein Buch")]
	# queryf = ["Buch","Haus"]
	# sent_pairs = buildCorpus('english.txt','french.txt')
	sent_pairs = buildCorpus('readenglish.txt','readfrench.txt')
	f_to_e = fre_to_eng(sent_pairs)
	e_to_f = eng_to_fre(sent_pairs)
	print len(f_to_e), ", ", len(e_to_f)
	return f_to_e, e_to_f 			#not using the returned values as such

if __name__ == '__main__':
	rebuild()
	run()
