import string
import os
import pprint
from insignificant import leestekens, digits, infixes
from target_texts import target_texts
import csv


def disperseText(textfile, resultfile, targetlist):
    file = open(textfile, "r")
    result = open(resultfile, "w")
    filecontents = file.read()
    filecontents = filecontents.replace('\n', ' ')
    wordlist = filecontents.split(' ')
    positions = {}
    for word in targetlist:
        positions[word] = []
    for position, word in enumerate(wordlist):
        if word in targetlist:
            positions[word].append(position)

    resultwriter = csv.writer(result, delimiter=",")
    resultwriter.writerow(["word", "locations", "total_length"])
    for word in positions:
        resultwriter.writerow([word, positions[word], len(wordlist)])
    file.close()
    result.close()


def main():
    # Geeft directoryname van huidige script en slaat op in script_location
    script_location = os.path.dirname(__file__)
    targetlist = ['pan', 'mountain', 'agora']
    for link, metainfo in target_texts.items():  # Geeft Key, value paren in list
        # os.join voegt 'slim' pathnames samen. Omdat op windows gebruik word gemaakt van \ en niet van /
        folder = os.path.join(script_location, "corpus",  metainfo[0] + " - " + metainfo[1])
        name = metainfo[0] + " - " + metainfo[1]  # Geeft auteur en titel
        print("Generating dispersion data for: {}".format(name))
        inputfile = os.path.join(folder, "cleaned.txt")
        outputfile = os.path.join(folder, "dispersion.csv")
        if os.path.isfile(outputfile):  #
            os.remove(outputfile)
            print("Text '{}' already dispersed, removing dispersion.csv to re-analyse".format(name))
        disperseText(inputfile, outputfile, targetlist)


if __name__ == '__main__':
    main()
