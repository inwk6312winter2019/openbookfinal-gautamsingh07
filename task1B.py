from collections import counter

 f1= ("Book1.txt", 'r')
l1= f1.readline()
string1= [0]
stringsplit1 = string1.split

f2= ("Book2.txt", 'r')
l2= f2.readline()
string2=  [0]
stringsplit2= string2.split

f3= ("Book3.txt", 'r')
l3= f3.readline()
stringsplit3= string3.split

word_counter = collections.counter(wordcount)
for word, count in word_counter.most_common(20):
 print (word, count)



