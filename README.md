# [Hack n Lead 2019](https://womenplusplus.ch/hacknlead)

# Complain.app
===

## Table of Contents

- [Introduction](#introduction)
- [Data Reference](#data_reference)
- [Modelling](#modelling)
- [App and Visual](#app_and_visual)
- [Summary](#summary)


## Introduction
After a hard day of work, everyone knows the feeling when they want to complain about the job conditions. In some situations it could be solved with a psychology session. While in other cases the situation might be really threatening. So, in order to understand at which point the user is and to raise awareness of what the modern slavery is,  we proposed a PoC in a form of an app which will help to classify the problem and take an action.

## Data Reference

### Data Used
- [Human Trafficking Data](http://www.humantraffickingdata.org/search?no_results=1)
	* Abstract of Court Cases from the US. eg:http://www.humantraffickingdata.org/search/2:10-cr-00159-PD
	* Obtained by scraping --> [Casefile_df.ipynb](https://github.com/maffka123/hack-n-lead2019/blob/master/Data_Mining/Casefile_df.ipynb)
- [Glassdoor](https://www.glassdoor.co.uk/index.htm)
	* Employee Reviews
	* Combine data --> [Data_preprocessing.ipynb](https://github.com/maffka123/hack-n-lead2019/blob/master/Data_Mining/Data_preprocessing.ipynb)

### Potential Data
- Case Files in pdf format --> [pdf_parser.ipynb](https://github.com/maffka123/hack-n-lead2019/blob/master/Data_Mining/pdf_parser.ipynb)
- Thomson Reuters api --> [RTapi.ipynb](https://github.com/maffka123/hack-n-lead2019/blob/master/Data_Mining/RTapi.ipynb)

## Modelling
- Doc2Vec
Doc2vec is an unsupervised algorithm to generate vectors for sentence, paragraphs or documents.
Classification done based on relative distance between vectors.
	* [Intro](https://medium.com/@mishra.thedeepak/doc2vec-simple-implementation-example-df2afbbfbad5)
	* [doc2vec_experiment.ipynb](https://github.com/maffka123/hack-n-lead2019/blob/master/Modelling/doc2vec_experiment.ipynb)
- TF-IDF with Cosine-Similarities 
Term Frequency–Inverse Document Frequency is a numerical statistic that reflect how important a word is to a document in a collection or corpus.
	* [Intro](https://towardsdatascience.com/natural-language-processing-feature-engineering-using-tf-idf-e8b9d00e7e76)
	* [Model_Tfidf_cossim.ipynb](https://github.com/maffka123/hack-n-lead2019/blob/master/Modelling/Model_Tfidf_cossim.ipynb)

## App and Visual
- dashboard_hnl19 --> Experimental webapp using bokeh
- Visuals --> Visuals generated from Model indicating prominant word vectors identified by models

## Summary

- Our project is designed to detect a slavery situation based on the user text input. It finds similar patterns in the complaint provided by a potential victim and already existing court cases which were solved in a favor of victims of modern slavery.
- We use natural language processing (NLP) model to classify the complaint as one of the following types of human rights violation: labor, minor sex, adult sex, and also identifies cases not related to either of those.
- It also proposes action depending on situation
