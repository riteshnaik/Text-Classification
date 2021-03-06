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

####Classifying new text

Once model file is created(spam.nb or sentiment.nb), use the model to classify new documents. 

Given a file formatted as follows:

    FEATURE_11 FEATURE_12 ... FEATURE_1N 
    FEATURE_21 FEATURE_22 ... FEATURE_2N 
    ... 
    FEATURE_M1 FEATURE_M2 ... FEATURE_MN 

where each line contains the features corresponding to one document, your program must write to STDOUT the same number of lines, and each line must contain exactly one string: the predicted label for the corresponding document.

For example, suppose we have the following file:

    subject : another meeting hello again can we meet tomorrow please . thanks . 
    subject : more low rates don 't miss out on our low rates today. 
    
Your program should write to STDOUT:

    HAM
    SPAM
    
To classify a file with new documents, your software will be invoked in the following way:

    python3 nbclassify.py MODELFILE TESTFILE

where MODELFILE is the name of the model file generated by nblearn, TESTFILE is the name of the file containing the features for the new documents to be classified.

Development data set for the spam filtering task that includes documents formatted in the same way as the training set. Use the development set to test the performance of your classifier. For the sentiment analysis task, it is your responsibillity to designate some of the available data as a development set so you can track your own progress.

Final testing will be done using a test set. It should take only a few minutes to classify the test data.

The test set will have the same format as the training set, that is, a directory containing text files, except that the file names of the test data will not reveal the correct label. The files are named TEST.00001.txt, TEST.00002.txt, etc. Output files should have one label per line, corresponding to each file in numerical order. In other words, the first line should be the label for TEST.00001.txt, the second line should be the label for TEST.00002.txt, and so on.

####Part 1 Files
* Model files: spam.nb and sentiment.nb
* Files containing the STDOUT output of the classification program on the test set: spam.out and sentiment.out.

###Part II

In the second part build classifiers using the same datasets as in part I, but using an off-the-shelf implementations of Maximum Entropy classification and Support Vector Machines.

For Support Vector Machines, use SVMlight . Read the documentation provided and format the training data according to the specifications. Use the default parameters (or tune them as you like). The software is setup for binary classification, where the labels are -1 and +1. This works just fine for our two tasks, but you will need to postprocess the output to be in the same format as the output of nbclassify.

For Maximum Entropy, use MegaM. Read the documentation provided. Use -nc for named classes, and the multiclass setting. Postprocess the output to be in the same format as the output of nbclassify. You may need to install ocaml to compile, and you may need to change the MegaM Makefile to have the right path on the line that starts with WITHCLIBS (WITHCLIBS =-I /opt/local/lib/ocaml/caml), and replace -lstr with -lcamlstr in the line that starts with WITHSTR).

####Part 2 Files
* Model files: spam.svm.model, sentiment.svm.model, spam.megam.model and sentiment.megam.model.
* Classification output files (postprocessed to have the same format as the output of nbclassify): pam.svm.out, sentiment.svm.out, spam.megam.out and sentiment.megam.out.

