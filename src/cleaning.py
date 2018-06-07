import string
import os
from insignificant import leestekens, digits, infixes
from target_texts import target_texts

def cleanText(textfile, resultfile):
    # To solve unicode errors use ISO-8859-1 source: https://stackoverflow.com/questions/19699367/unicodedecodeerror-utf-8-codec-cant-decode-byte
    file = open(textfile, "r")
    result = open(resultfile, "w")
    for line in file:
            for leesteken in leestekens:
                line = line.replace(leesteken, "")
            for digit in digits:
                line = line.replace(digit, "")
            for infix in infixes:
                line = line.replace(infix, " ")
            stripped = line.strip()
            stripped = stripped.lower()
            if stripped: # Als de regel nog inhoud heeft na het verwijderen van whitespace
                result.write(stripped + "\n")
    file.close()
    result.close()

def main():
    script_location = os.path.dirname(__file__)

    for link, metainfo in target_texts.items():
        folder = os.path.join(script_location, "corpus",  metainfo[0] + " - " + metainfo[1]) #os.join voegt 'slim' pathnames samen. Omdat op windows gebruik word gemaakt van \ en niet van /    
        name = metainfo[0] + " - " + metainfo[1]
        print("Cleaning text for: {}".format(name))
        inputfile = os.path.join(folder, "text.txt")
        outputfile = os.path.join(folder, "cleaned.txt")
        if os.path.isfile(outputfile):
            os.remove(outputfile)
            print("Text '{}' already cleaned, removing cleaned.txt to re-clean".format(name))
            cleanText(inputfile, outputfile)

if __name__ == '__main__':
    main()
