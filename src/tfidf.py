from target_texts import target_texts 
import math
import os
import csv
# TF-IDF:
# https://en.wikipedia.org/wiki/Tf%E2%80%93idf

# Een document: Alle 'contexten' van een tekst

# TF: Term Frequency
# Die hebben we al in contextcount.csv gedeeld door totaal aantaal woorden (= #context*101)
#
# IDF: Ineverse Document Frequency
# LOG(N_Docs/N_Docs_met_Woord) =  IDF (woord, Documenten)

"rock"
def inverseDocumentFrequency(word, target_texts):
    N_docs = len(target_texts)
    N_docs_with_word = 0
    script_location = os.path.dirname(__file__)
    for link, metainfo in target_texts.items():
        name = metainfo[0] + " - " + metainfo[1]
        # os.join voegt 'slim' pathnames samen. Omdat op windows gebruik word gemaakt van \ en niet van /
        folder = os.path.join(script_location, "corpus",  name) # voeg de map corpus/textnaam toe aan huidige pad 
        context = os.path.join(folder, "contextcount.csv") # voeg hier weer contextcount.csv aan toe
        with open(context) as csvfile:  # open neemt als argument een String (Filename)
            contextreader = csv.reader(csvfile)
            for key, frequency in contextreader:
                if word == key:
                    N_docs_with_word += 1       
    return math.log(N_docs/N_docs_with_word)


def main():
    script_location = os.path.dirname(__file__)
    for link, metainfo in target_texts.items():
        frequencies = {}
        name = metainfo[0] + " - " + metainfo[1]
        # os.join voegt 'slim' pathnames samen. Omdat op windows gebruik word gemaakt van \ en niet van /
        folder = os.path.join(script_location, "corpus",  name) # voeg de map corpus/textnaam toe aan huidige pad 
        context = os.path.join(folder, "contextcount.csv") # voeg hier weer contextcount.csv aan toe
        
        total_wordcount = 0 # totaal aantal woorden in context
        with open(context) as csvfile:  # open neemt als argument een String (Filename)
            contextreader = csv.reader(csvfile)
            next(contextreader) # skip de eerste rij
            for key, value in contextreader:
                total_wordcount += int(value)
        
        # tf-idf berekenen
        with open(context) as csvfile:  # open neemt als argument een String (Filename)
            contextreader = csv.reader(csvfile)
            next(contextreader) # skip de eerste rij
            for key, value in contextreader: # line = lijst van [key, value]
                frequencies[key] = (int(value)/total_wordcount) * inverseDocumentFrequency(key, target_texts) 
        
        sorted_frequencies = sorted(
            frequencies, key=lambda word: frequencies[word], reverse=True)
        # for k in sorted_frequencies:
        #     print(f"{k} -> {frequencies[k]}")
        # print(sorted_frequencies)

        resultfile_path = os.path.join(folder, "tfidf.csv")
        if os.path.exists(resultfile_path):
            os.remove(resultfile_path)
        with open(resultfile_path, 'w') as resultfile:
            resultwriter = csv.writer(resultfile, delimiter=",")
            resultwriter.writerow(["woord", "tfidf"])
            for woord in sorted_frequencies:
                resultwriter.writerow([woord, frequencies[woord]])

if __name__ == '__main__':
    main()