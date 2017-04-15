import jaccard as jac
import cosine as cos
import ibm_temp2 as ibm

def main():
	while True:
		op=int(raw_input("Enter \n 1: If you want to translate a document.\n 2: If you want to get jaccard coeff or cosine similarity.\n 0: If you want to exit. \n >> "))
		if op==1:	
			continue
		if op==2:
			doc1=str(raw_input("Enter relative\\absolute paths of the docs\n DOC1 >> "))
			doc2=str(raw_input(" DOC2 >> "))
			jacco=jac.computeJaccard(doc1,doc2)
			cossim=cos.computeCosine(doc1,doc2)
			print "Jaccard Coeff is "+str(jacco)+" and Cosine Simillarity is "+str(cossim)
			continue
		if op==0:
			break
	return
	
if __name__ == '__main__':
  main()
	
