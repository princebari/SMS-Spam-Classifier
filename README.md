<h1>EMAIL SPAM CLASSIFIER</h1>

1.Business Problem

1.1 Description
Email/SMS is the worldwide use of communication application. It is because of the ease of use and faster than other communication application. However, its inability to detect whether the message content is either spam or ham degrade its performance. Nowadays, lot of cases have been reported regarding stealing of personal information or phishing activities via message from the user

Nowadays, a big part of people rely on available email or messages sent by the stranger. The possibility that anybody can leave an email or message provides a golden opportunity for spammers to write spam message about our different interests. Spam fills inbox with number of ridiculous emails/messages. Degrades our internet speed to a great extent. Steals useful information like our details on our contact list. Identifying these spammers and also the spam content can be a hot topic of research and laborious tasks. Email/SMS spam is an operation to send messages in bulk by mail/SMS.

The dangers of spam messages for the users are many: undesired advertisement, exposure of private information, becoming a victim of a fraud or financial scheme, being lured into malware and phishing websites, involuntary exposition to inappropriate content, etc. For the network operator, spam messages result in an increased cost in operations.

A few common spam emails/SMS include fake advertisements, chain emails, and impersonation attempts. While these built-in spam detectors are usually pretty effective, sometimes, a particularly well-disguised spam email/SMS may fall through the cracks, landing in your inbox instead of your spam folder. Clicking on a spam/SMS email can be dangerous, exposing your computer and personal information to different types of malware. Therefore, it’s important to implement additional safety measures to protect your device, especially when it handles sensitive information like user data.

Our main goal of this case study is to design an email/SMS spam filtering system using machine learning. It is a binary classification problem. Given a new email/SMS we will predict whether it is spam or non-spam. The reason to do this is simple: by detecting unsolicited and unwanted emails/SMS, we can prevent spam messages from creeping into the user’s inbox, thereby improving user experience.

Problem Statement

Build a email/SMS spam detector system using machine learning algorithm
Predict whether the given message is ham or spam.
Classify the email/SMS into a ham or spam given the email/SMS text.

1.2 Source / Useful Links
Source :

https://www.kaggle.com/datasets/ganiyuolalekan/spam-assassin-email-classification-dataset

Useful links and References :

Email based spam detection Journal : https://www.researchgate.net/publication/342113653_Email_based_Spam_Detection

Spam detection using machine learning based binary classifier report : https://myfik.unisza.edu.my/www/fyp/fyp18sem2/report/43660.pdf

Kaggle Notebook of spam and ham classifer : https://www.kaggle.com/code/rumbleftw/beginner-friendly-spam-ham-sms-classification

Text preprocessing for spam classifer : https://www.naukri.com/learning/articles/text-pre-processing-for-spam-filtering/

Feature Engineering on text data :

https://towardsdatascience.com/text-analysis-feature-engineering-with-nlp-502d6ea9225d

https://www.analyticsvidhya.com/blog/2021/04/a-guide-to-feature-engineering-in-nlp/

https://betterprogramming.pub/beginners-to-advanced-feature-engineering-from-text-data-c228047a4813

https://www.pluralsight.com/guides/building-features-from-text-data

Data Preprocesing :

https://dev.to/saxenamansi/classifying-spam-emails-using-basic-python-

https://www.analyticsvidhya.com/blog/2021/06/must-known-techniques-for-text-preprocessing-in-nlp/

https://github.com/idevshoaib/Classification-with-Naive-Bayes/blob/master/Naive%20Bayes%20Classification.ipynb

Blog SMS spam classifier : https://medium.com/analytics-vidhya/sms-spam-classifier-natural-language-processing-1751e2b324ed


1.3 Real World /Business objective and Constraints
The Cost of mis-classification can be very high.
Probability of prediction can be useful.
No Strict Latency requirement.
Interpretability is not much important

2.Machine Learning Problem

2.1 Data
2.1.1 Data Overview

Refer : https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

We have one data file "spam.csv".

Size of csv file - 503.66 KB

The csv file composes of Four columns:

1.The "v1" column: which contains the labels (ham & spam)

2.The "v2" column: which contains actual raw text of email/SMS

2.1.2 Examples of a Data points

text

"Thanks a lot for your wishes on my birthday. Thanks you for making my birthday truly memorable."

target

0

text

"Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's"

target

1


2.2 Mapping the real-world problem to an ML problem
2.2.1 Type of Machine Learning Problem

This is supervised Machine learning Binary Class Classification Problem, for a given email/SMS we have to predict if it is a spam or not.

2.2.2 Perfomance Metric

Metric(s):

Accuracy
Precision and Recall
F1-Score
Binary Confusion Matrix
2.2.3 Machine Learning Objective and Constraints

Objective : Predict whether the email is spam or not and also predict its class probability.

Constraints:

No Strict latency Requirement.
Reduce False Positive.
Class Probability are needed.
