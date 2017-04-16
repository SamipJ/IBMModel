#CROSS LINGUAL DOCUMENT TRANSLATOR
An implementation of text translation using statistical machine translation i.e. IBM Model 1 with alignment heuristics. We have used to text files one in french and one in english to make parallel corpus.

code available online at:https://github.com/SamipJ/SMT-using-IBMModel1.5


#FEATURES
* seperate word map from e to f anf f to e
* iterated em i.e. cond prob till convergence to increase translation accuracy
* one to many mapping also considered
* json to save in secondary memory
* to check accuracy jaccard and cosine
* alignment considered
* custom tokenizer

##Prerequisites
1. software required:
	- python2.7

2. python2.7 libraries required:
	- math
	- re
	- json
	- time
	- io
  - collections
  - copy
  - sys

##Assumptions
- This program must be run on a linux system
- The user enters a valid option when prompted
- The program was tested on a ubuntu 16.04LTS system with 12GB of ram


##Getting Started
1. Ensure all required software and libraries are installed
2. Run 'python driver.py' in a terminal to start the program
3. Rebuilding corpus and mapping is not advised unless you are changing the language in which to or from translation is done. Choose the option to rebuild corpus in case any changes are made to the corpus or during the first run of the program
4. The program will prompt for input as and when required
5. Entering the query/filename is expected to be entered either as absolute path or relative to the root of driver code.
6. Average of Performance matrix only available when multiple files are put during translation.


##Authors
1. Aadi       Jain 			(2015A7PS104P)
2. Aayushmaan Jain 			(2015A7PS043P)
3. Aradhya    Khandelwal 	(2015A7PS036P)
4. Samip      Jasani 		(2015A7PS127P)
5. Tanvi      Aggarwal 		(2015A7PS140P)
