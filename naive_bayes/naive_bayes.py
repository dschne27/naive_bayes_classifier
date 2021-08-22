import collections
import tkinter as tk

class NaiveBayes:
    def __init__(self) -> None:

        ##key: label, nested key: word, value: word count given label
        self.conditional_dict = {}
        ##unique number of elements among features
        self.n = 0
        ##feature array
        self.labels = {} 
        ##P(prior) for each label
        self.priors = {}
        ##vocab size
        self.size = 0
        #
        self.word_counts = {}
        self.x_given_c = {}

    ##calculate P(prior) for each label and store it in a dictionary 
    def p_prior(self):
        for lab in self.labels:
            self.priors[lab] = self.labels[lab] / self.n 

    # storing the occurence of words for each label in a dictionary
    def collect_conditional(self, X_train,y_train) -> None:
        i = 0
        for i in range(len(X_train)):
            for elem in X_train[i]:
                if y_train[i][0] in self.conditional_dict:
                    if elem in self.conditional_dict[y_train[i][0]]:
                        self.conditional_dict[y_train[i][0]][elem] += 1
                    else:
                        self.conditional_dict[y_train[i][0]][elem] = 1
                else:
                    self.conditional_dict[y_train[i][0]] = {}
                    self.conditional_dict[y_train[i][0]][elem] = 1
    
    def calc_conditional(self):
        for c in self.conditional_dict:
            self.x_given_c[c] = 0
        for c in self.conditional_dict:
            for x in self.conditional_dict[c]:
                self.x_given_c[c] += self.conditional_dict[c][x]


    
    #function that takes max of all possible class probs
    def assign_class(self, X_test) -> list:
        predictions = []
        for doc_n in range(len(X_test)):
            probs = {}
            for label in self.labels:
                product = self.bayes(X_test[doc_n], label)
                probs[label] = product
            predictions.append(max(probs, key=probs.get))
        return predictions
            


    # implementing the multinomial naive bayes formula
    def bayes(self, doc_in, label_in) -> float:
        prior = self.priors[label_in]
        for x in doc_in:
            if x in self.conditional_dict[label_in]:  
                x_c = self.conditional_dict[label_in][x] / self.x_given_c[label_in]
            else:
                x_c = 1 / self.x_given_c[label_in]
            prior *= x_c
        return prior
     

    #train the algorithm:
    # step 1. collect unique labels from y_train and calculate P(class)
    # step 2. create a dict for the occurence of words given a label
        # step 2.5: store the occurence of each unique word among all documents
    # step 3. calculate prior probabilities and store as a dict

    def fit(self, X_train, y_train):
        assert type(X_train) == list
        assert type(y_train) == list
        assert len(X_train) == len(y_train)

        #store labels and their counts and collect n unique labels in training data  
        for label in y_train:
            y = label[0]
            if y not in self.labels:
                self.labels[y] = 1
            else:
                self.labels[y] += 1
            self.n += 1

        self.collect_conditional(X_train, y_train)
        self.calc_conditional()
        self.p_prior()


    def predict(self, X_test, y_test):
        return print(self.assign_class(X_test),y_test,end="\n")




