
"""
Sklearn is very useful machine learning library for Python Prograaming Language. It has many 
classifiers, metrics calculations, implemented which we can make use of. 
Here we use 

**Decision Tree Classifier
**Naive Bayes
**Neural Network

for classification of our PoS Tagger

"""
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier

"""
NLTK is a natural language processing toolkit designed for Python.
"""
import nltk
from nltk.util import ngrams
"""
Numpy is a fundamental package for scientific Computing in Python
"""
import numpy as np
"""
Json is used to read read from the file which are in JSON format
"""
import json
"""
time_keeper.py is a file which is coded to keep track of time for each classifier.
count is a class in that file which is imported here.
"""
from time_keeper import count

# File names of each dataset file.
file_list = ["ewt", "gum", "lines", "partut"]




"""
To make a Machine Learning Classifier, we need to make sure a function which will focus on the set of features that are required to train the 
algorithm on. For example, 3-letter suffix will give us more insights of the tense of the word like, past tense, present participle, etc. Below function will 
generate feature for each word in our dataset so we can feed it into our machine learning algorithm.
"""
def features(sentence, index):
    currWord = sentence[index][0]
    if (index > 0):
        prevWord = sentence[index - 1][0]
        '''
        try:
            prepreWord=sentence[index - 2][0]
        except:
            prepreWord = '<START>'
        '''
            
    else:
        prevWord = '<START>'
        #prepreWord = '<START>'
    if (index < len(sentence)-1):
        nextWord = sentence[index + 1][0]
        '''
        try:
            nexnextword = sentence[index + 2][0]
        except:
            nexnextword = '<END>'
        '''
            
 
    else:
        nextWord = '<END>'
        #nexnextword = '<END>'
    return {
        'word': currWord,
        'is_first': index == 0,
        'is_last': index == len(sentence) - 1,
        'curr_is_title': currWord.istitle(),
        'prev_is_title': prevWord.istitle(),
        'next_is_title': nextWord.istitle(),
        'curr_is_lower': currWord.islower(),
        'prev_is_lower': prevWord.islower(),
        'next_is_lower': nextWord.islower(),
        'curr_is_upper': currWord.isupper(),
        'prev_is_upper': prevWord.isupper(),
        'next_is_upper': nextWord.isupper(),
        'curr_is_digit': currWord.isdigit(),
        'prev_is_digit': prevWord.isdigit(),
        'next_is_digit': nextWord.isdigit(),
        'curr_prefix-1': currWord[0],
        'curr_prefix-2': currWord[:2],
        'curr_prefix-3': currWord[:3],
        'curr_suffix-1': currWord[-1],
        'curr_suffix-2': currWord[-2:],
        'curr_suffix-3': currWord[-3:],
        'prev_prefix-1': prevWord[0],
        'prev_prefix-2': prevWord[:2],
        'prev_prefix-3': prevWord[:3],
        'prev_suffix-1': prevWord[-1],
        'prev_suffix-2': prevWord[-2:],
        'prev_suffix-3': prevWord[-3:],
        'next_prefix-1': nextWord[0],
        'next_prefix-2': nextWord[:2],
        'next_prefix-3': nextWord[:3],
        'next_suffix-1': nextWord[-1],
        'next_suffix-2': nextWord[-2:],
        'next_suffix-3': nextWord[-3:],
        'prev_word': prevWord,
        'next_word': nextWord,
        #'preprev_word' : prepreWord,
        #'nextnext_word' : nexnextword,
    }


# preparing dataset for training and testing
def transformDataset(sentences):
    wordFeatures = []
    wordLabels = []
    for sent in sentences:
        for index in range(len(sent)):
            wordFeatures.append(features(sent, index))
            wordLabels.append(sent[index][1])
    return wordFeatures, wordLabels

  """
  Below are the function used coded for three machine learning algorithms. The classifers are designed with the help of Sklearn libraries.
  """
def trainDecisionTree(trainFeatures, trainLabels):
    clf = make_pipeline(DictVectorizer(sparse=False), DecisionTreeClassifier(criterion='entropy'))
    scores = cross_val_score(clf, trainFeatures, trainLabels, cv=4)
    clf.fit(trainFeatures, trainLabels)
    return clf, scores.mean()
def trainNaiveBayes(trainFeatures, trainLabels):
    clf = make_pipeline(DictVectorizer(sparse=False), MultinomialNB())
    scores = cross_val_score(clf, trainFeatures, trainLabels, cv=4)
    clf.fit(trainFeatures, trainLabels)
    return clf, scores.mean()
def trainNN(trainFeatures, trainLabels):
    clf = make_pipeline(DictVectorizer(sparse=False),
                        MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100), random_state=1))
    scores = cross_val_score(clf, trainFeatures, trainLabels, cv=4)
    clf.fit(trainFeatures, trainLabels)
    return clf, scores.mean()

# Below for loop will go through the data of four files and calculate the various metrics for all of them.
for names in file_list:
    print("****For file {} ****".format(names))
    with open("corpus/en/en."+names+".train.json", "r") as write_file:
        data = write_file.read()

    cnt = count()
    obj = json.loads(data)
    words_trn=[]
    words_tst=[]

    brown_tagged_sents=[]
    for i in range(0,len(obj)):
        ts=[]
        for j in range(0,len(obj[i][0])):
            ts.append((obj[i][0][j], obj[i][1][j]))
            words_trn.append(obj[i][0][j])
        brown_tagged_sents.append(ts)


    with open("corpus/en/en."+names+".test.json", "r") as file:
        data_test = file.read()


    obj_test = json.loads(data_test)


    brown_tagged_sents_test=[]
    for i in range(0,len(obj_test)):
        ts=[]
        for j in range(0,len(obj_test[i][0])):
            ts.append((obj_test[i][0][j], obj_test[i][1][j]))
            words_tst.append(obj_test[i][0][j])
        brown_tagged_sents_test.append(ts)

    trainFeatures, trainLabels = transformDataset(brown_tagged_sents)

    testFeatures, testLabels = transformDataset(brown_tagged_sents_test)

    ingrams  = list(ngrams(words_trn,3)) # Here we divide the dataset into 3-grams. so an array like [1,2,3,4,5] when goes through here, will generete
    # sub arrays like [1,2,3], [2,3,4], [3,4,5] as we have 3-grams.
    ngrams1 = set(ingrams) # This will store only the unique words from our dataset.
    freq1 = nltk.FreqDist(ingrams)
    
    ingrams  = list(ngrams(words_tst,3))
    ngrams2 = set(ingrams)
    freq2 = nltk.FreqDist(ingrams)
    
        
    common_ngrams = ngrams1.intersection(ngrams2)
    unique_ngrams = ngrams1.difference(ngrams2)
    OOV=0

    for n in brown_tagged_sents_test:
        if n not in brown_tagged_sents:
            OOV+=1

     # OOV(Out of vocabulary) percent is the percentage of words that are in our test data which are not in training dataset.
    print("OOV Percent: {}".format((OOV/len(brown_tagged_sents_test))*100))
            
        
    D = 0
    P = 0
    for ngram in common_ngrams:
        D += freq1.freq(ngram)*np.log(freq1.freq(ngram)/freq2.freq(ngram))
        P += freq2.freq(ngram) * np.log(freq2.freq(ngram))

    #KL Divergence is a information loss metric. It should be as low as possible
    print("KL Divergence: {}".format(D))
    print("Perplexity: {}".format(2**-P))

    #From here we start our classification of training and testing datasets.
    print("Starting Decision Tree Classification")

    cnt.start()
    tree_model, tree_model_cv_score = trainDecisionTree(trainFeatures[:10000], trainLabels[:10000])
    print ("Cross Validation Score {}".format(tree_model_cv_score))
    print("Decision Tree Accraucy: {}".format(tree_model.score(testFeatures, testLabels)))


    stats = cnt.finish()
    print("Time Elasped: {} mins : {} secs".format(stats["mins"], stats["secs"]))



    cnt.start()
    print("Starting Naive Bayes Classification")
    nb_model, nb_model_cv_score = trainNaiveBayes(trainFeatures[:10000], trainLabels[:10000])
    print ("Cross Validation Score {}".format(nb_model_cv_score))
    print("Naive Bayes Accraucy: {}".format(nb_model.score(testFeatures, testLabels)))
    #print("KL Divergence: {}".format(KL(testFeatures, testLabels)))
    stats = cnt.finish()
    print("Time Elasped: {} mins : {} secs".format(stats["mins"], stats["secs"]))


    cnt.start()
    print("Starting Neural Network Classification")
    nn_model, nn_model_cv_score = trainNN(trainFeatures[:10000], trainLabels[:10000])
    print ("Cross Validation Score {}".format(nn_model_cv_score))
    print("Neural Network Accraucy: {}".format(nn_model.score(testFeatures, testLabels)))
    #print("KL Divergence: {}".format(KL(testFeatures, testLabels)))
    stats = cnt.finish()
    print("Time Elasped: {} mins : {} secs".format(stats["mins"], stats["secs"]))


