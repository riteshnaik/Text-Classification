# Text-Classification

##Description
Develop a Text Classifier and apply it to two datasets corresponding to two tasks: 

1. Spam Filtering
2. Sentiment Analysis

###Part I

Naive Bayes classifier according to the specifications below:

* Without using any additional packages, libraries or modules.
* Python Script to learn the model (nblearn.py) and one python script to classify new text (nbclassify.py). 

####Learning from data 

A directory will then be created, containing the text files. Each text file is one document. In the spam dataset, a document is one email message. In the sentiment dataset, a document is one movie review. The classification label for each document is indicated in the file name. For example, in the spam dataset each file name begins with either SPAM or HAM, so the classes for your spam classifier should be SPAM and HAM.

First task is to format the training data. Classifier must accept training data in exactly one file in the following format:

  LABEL_1 FEATURE_11 FEATURE_12 ... FEATURE_1N 
  LABEL_2 FEATURE_21 FEATURE_22 ... FEATURE_2N 
  ... 
  LABEL_M FEATURE_M1 FEATURE_M2 ... FEATURE_MN 
  
Each line in the training data file corresponds to one document. Each line starts with the class label for the document, and continues with the feature vector that represents the document. For both tasks in this assignment, we will use (at least) bag-of-words features.

Suppose the training dataset consists of the following two files:

HAM.1.txt
subject : meeting today
hi , could we have a meeting today . 
thank you .
SPAM.1.txt
subject : low rates 
click here to apply for new low rates 
do not miss this chance !
You training file could look like this:

HAM subject : meeting today hi , could we have a meeting today . thank you . 
SPAM subject : low rates click here to apply for new low rates do not miss this chance !

To learn a classification model from the training data file, the software will be invoked in the following way:

python3 nblearn.py TRAININGFILE MODELFILE

where TRAININGFILE is the name of the training file (this should be spam_training.txt for the spam dataset, and sentiment_training.txt for the sentiment dataset), MODELFILE is the name of the file that will contain the model that your classifier will learn (for the spam dataset the file name should be spam.nb, and sentiment.nb for the sentiment dataset).


