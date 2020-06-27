import pickle
import os

basepath=os.path.dirname(os.path.realpath(__file__))
path_model=os.path.join(basepath,'lang_detect.model')
path_vect=os.path.join(basepath,'vectorizer.pkl')

naive_classifier=pickle.load(open(path_model,'rb'))
vectorizer=pickle.load(open(path_vect,'rb'))

def detect(text):
    test=vectorizer.transform([text])
    return naive_classifier.predict(test)
