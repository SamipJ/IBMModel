Information Retrieval Assignment-2
Design Document

#DATASET:
Two parallel corpora -one of English text and its French translation- provided as part of the assignment statement.

#META DATA


#LIBRARIES:
* 're' for regular expressions,
* 'collections' for enhanced dictionary functions,
* 'copy' for checking for convergence during iterations of IBM Model 1,
* 'math' for mathematical functionals,
* 'json' for backing up index in secondary memory,
* 'io' for file I/O,
* 'sys' for setting up default encoding,
* 'time' for measuring execution time.

#OPTIMISATION:
* Limiting number of iteration in Expectation Maximization step in case of slow convergence to save on execution time
* Preventing underflow of conditional probablity values at 10^-5 to limit needless floating point computation
* python collections used instead of 'dict' datatype to provide faster access and dynamic initialization
* Saving entire Mapping in secondary memory to remove needless building everytime by using json
* Exponential Decay function (alpha = 0.9) used to weigh alignment to increase accuracy

#PREPROCESSING
* latin1 encodinf scheme to handle both french and english character symbols
* used our own custom tokenizer to be able to process special french characters
* to prevent multple instance of same words from occurening in dict we converted all words to lowercase

#TRANSLATION
* using cond prob we built word map with max prob from e to f and f to e
* if prob value are close by then both are considered and are concatenated
* Word map are backed up in json files

#MODEL:
IBM Model 1 - The statistical machine translation model that has been implemented is IBM Model 1,
model

#PERFORMANCE MATRIX

##JACCARD Coefficient

##COSINE Simillarity
