__author__ = 'SFU'

import os
import string
from collections import Counter
my_path = "C:/Users/SFU/PycharmProjects/data"
file_name = os.path.join(my_path, "GettysburgAddress.txt")
#Read the text file, remove the punctuation, and write this to a new file
remove_punctuation = dict.fromkeys(map(ord, string.punctuation))
with open(file_name, "r") as my_input, open("basic_file.txt", "w") as my_output:
    no_punctuation = my_input.read().translate(remove_punctuation)
    my_output.write(no_punctuation)
#Take the recently made file as the new input
new_file_name = os.path.join("C:/Users/SFU/PycharmProjects/Word_Reader", "basic_file.txt")
with open(new_file_name, "r") as new_input:
    reader = new_input.read()
    words = reader.split()
#Count the most used words using the Counter import
    c = Counter(words)
    for word, count in c.most_common(15):
        print(word, count)




