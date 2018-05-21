import string
import os

def cleanText(textfile, resultfile):
    puncttable = str.maketrans({key: None for key in string.punctuation})
    file = open(textfile, "r")
    result = open(resultfile, "w")
    for line in file:
        if line.strip():
            words = line.strip().translate(puncttable)
            result.write(words + "\n")
    file.close()
    result.close()

def main():
    target_texts = ['Euripides - Ion', 'Plato - Cratylus']

    for name in target_texts:
        print("Cleaning text for: {}".format(name))
        inputfile = "corpus\\" + name + "\\text.txt"
        outputfile = "corpus\\" + name + "\\cleaned.txt"
        if os.path.isfile(outputfile):
            print("Text '{}' already cleaned (remove cleaned.txt to reclean)".format(name))
        else:
            cleanText(inputfile, outputfile)

if __name__ == '__main__':
    main()
