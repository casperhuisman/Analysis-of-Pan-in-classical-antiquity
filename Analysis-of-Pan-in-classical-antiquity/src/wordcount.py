from target_texts import target_texts
import os
import csv

# open cleaned.txt
# make dictionary {word:freq}
    # for word in string
    # if word not in dict, append word (key = word, value = 1)
    # if word is in dict: value +1   

def main():
    script_location = os.path.dirname(__file__)
    for link, metainfo in target_texts.items():
        wordcount = {}
        name = metainfo[0] + " - " + metainfo[1]
        folder = os.path.join(script_location, "corpus",  name) #os.join voegt 'slim' pathnames samen. Omdat op windows gebruik word gemaakt van \ en niet van /    
        cleaned_file = os.path.join(folder , "cleaned.txt")
        # file opener
        with open(cleaned_file) as cleaned_text:
            for line in cleaned_text:
                stripped = line.strip()
                splitted = stripped.split(" ")
                for word in splitted:
                    if word in wordcount:
                        wordcount[word] += 1
                    else:
                        wordcount[word] = 1    
        print(name)
        sorted_wordcount = sorted(wordcount, key=lambda woord: wordcount[woord], reverse=True)
        resultfile_path = os.path.join(folder, "wordcount.csv")
        if os.path.exists(resultfile_path):
            os.remove(resultfile_path)
        with open(resultfile_path, 'w') as resultfile:
            resultwriter = csv.writer(resultfile, delimiter=",")
            resultwriter.writerow(["woord", "frequency"])
            for woord in sorted_wordcount:
                resultwriter.writerow([woord, wordcount[woord]])
                         
                









if __name__ == '__main__':
    main()


