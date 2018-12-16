import string
import os
import pprint
from insignificant import leestekens, digits, infixes
from target_texts import target_texts
import csv


def contextualiseText(textfile, resultfile, targetlist, contextlength):
    file = open(textfile, "r")
    result = open(resultfile, "w")
    filecontents = file.read()
    filecontents = filecontents.replace('\n', ' ')
    wordlist = filecontents.split(' ')
    contexts = {}
    for word in targetlist:
        contexts[word] = []
    for position, word in enumerate(wordlist):
        if word in targetlist:
            # : syntax leest als 'tot' dus + 1
            context = ' '.join(wordlist[position-contextlength:position+contextlength+1])
            contexts[word].append((position, context))  # (,) is een tuple!
    resultwriter = csv.writer(result, delimiter=",")
    resultwriter.writerow(["word", "locations", "context", "contextlength"])
    for word in contexts:
        for pos_context in contexts[word]:
            resultwriter.writerow([word, pos_context[0], pos_context[1], contextlength])
    file.close()
    result.close()


def main():
    # Geeft directoryname van huidige script en slaat op in script_location
    script_location = os.path.dirname(__file__)
    targetlist = ['pan', 'mountain', 'agora']
    contextlength = 50  # IDEE: contextlength afhankelijk van textlength (in procenten)
    for link, metainfo in target_texts.items():  # Geeft Key, value paren in list
        # os.join voegt 'slim' pathnames samen. Omdat op windows gebruik word gemaakt van \ en niet van /
        folder = os.path.join(script_location, "corpus",  metainfo[0] + " - " + metainfo[1])
        name = metainfo[0] + " - " + metainfo[1]  # Geeft auteur en titel
        print("Generating context data for: {}".format(name))
        inputfile = os.path.join(folder, "cleaned.txt")
        outputfile = os.path.join(folder, "context.csv")
        if os.path.isfile(outputfile):
            os.remove(outputfile)
            print("Text '{}' already contextualised, removing context.csv to re-analyse".format(name))
        contextualiseText(inputfile, outputfile, targetlist, contextlength)


if __name__ == '__main__':
    main()
