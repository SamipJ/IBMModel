import jaccard as jac
import cosine as cos
import ibm2 as ibm

def main():
	buildflag=0
	while True:
		op=int(raw_input("Enter \n 1: If you want to translate documents.\n 2: If you want to get jaccard coeff or cosine similarity.\n 0: If you want to exit. \n >> "))
		if op==1:
			if buildflag==0 :
				builder=str(raw_input("Do you want to rebuild the corpus? Enter 'Y' or 'N'\n >> "))
				if builder == 'Y' or builder=='y':
					ibm.rebuild("parallel_corpus_IR2/english.txt","parallel_corpus_IR2/french.txt")
				buildflag=1
			itr=int(raw_input("Enter No. of documents to be translated \n >> "))
			sumjac=0
			sumcos=0
			if itr!=0 :
				for i in range(1,itr+1):
					valid=0
					transFile = open('translation.txt','w+')
					while (valid==0):
						query_lang=str(raw_input("Enter language of query file (source) < Enter 'E' for English, 'F' for French > \n >> "))
						query_lang=query_lang.lower()
						if(query_lang!='e' and query_lang!='f'):
							print("Invalid Input")
							continue
						valid=1
					query_file=str(raw_input("Enter the relative\\absolute path of query file\n >> "))
					ibm.run(transFile,query_file,query_lang)
					transFile.close()
					check=str(raw_input("Do you want to check this against your correct translated File? Enter 'Y' or 'N'\n >> "))
					if check =='Y' or check =='y':
						doc=str(raw_input("Enter relative\\absolute paths of the correct translation \n FILE >> "))
						jacco=jac.computeJaccard(doc,'translation.txt','e' if query_lang=='f' else 'f' )
						cossim=cos.computeCosine(doc,'translation.txt')
						sumjac=sumjac+jacco
						sumcos=sumcos+cossim
						print " Jaccard Coeff is "+str(jacco)+" and Cosine Simillarity is "+str(cossim)+"\n Average Jaccard Coeff is "+str(sumjac/(i))+" Average Cosine Similarity is "+str(sumcos/(i))
			continue
		if op==2:
			doc1=str(raw_input("Enter relative\\absolute paths of the docs\n DOC1 >> "))
			doc2=str(raw_input(" DOC2 >> "))
			jacco=jac.computeJaccard(doc1,doc2,'f')
			cossim=cos.computeCosine(doc1,doc2)
			print " Jaccard Coeff is "+str(jacco)+" and Cosine Simillarity is "+str(cossim)
			continue
		if op==0:
			break
	return

if __name__ == '__main__':
  main()
