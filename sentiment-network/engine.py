from collections import Counter
import numpy as np


def pretty_print_review_and_label(i):
    print(labels[i] + "\t:\t" + reviews[i][:80] + "...")

g = open('reviews.txt','r') # What we know!
reviews = list(map(lambda x:x[:-1],g.readlines()))
g.close()

g = open('labels.txt','r') # What we WANT to know!
labels = list(map(lambda x:x[:-1].upper(),g.readlines()))
g.close()

len(reviews)


reviews[0]
labels[0]

print("labels.txt \t : \t reviews.txt\n")
pretty_print_review_and_label(2137)
pretty_print_review_and_label(12816)
pretty_print_review_and_label(6267)
pretty_print_review_and_label(21934)
pretty_print_review_and_label(5297)
pretty_print_review_and_label(4998)

# Create three Counter objects to store positive, negative and total counts
positive_counts = Counter()
negative_counts = Counter()
total_counts = Counter()

# TODO: Loop over all the words in all the reviews and increment the counts in the appropriate counter objects

reviews_length = len(reviews)

for i in range(reviews_length):
    if labels[i] is 'POSITIVE':
        for word in reviews[i].split(' '):
            positive_counts[word] += 1
            total_counts[word] += 1
    elif labels[i] is 'NEGATIVE':
        for word in reviews[i].split(' '):
            negative_counts[word] += 1
            total_counts[word] += 1









    #     positive_counts += i
    # else label[i] is 'NEGATIVE':
    #     negative_counts += i
    # total_counts += i














