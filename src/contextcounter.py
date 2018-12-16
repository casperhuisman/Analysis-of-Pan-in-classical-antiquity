from target_texts import target_texts  # Maakt de volgorde iets uit?
import string
import os
import pprint
import csv

# open contextfile
# Make dictionaries {word:frequency}
# If word in list: add 1 to value
# Else: Add word as key.


def main():
    script_location = os.path.dirname(__file__)
    for link, metainfo in target_texts.items():
        contextcount = {}
        name = metainfo[0] + " - " + metainfo[1]
        # os.join voegt 'slim' pathnames samen. Omdat op windows gebruik word gemaakt van \ en niet van /
        folder = os.path.join(script_location, "corpus",  name)
        context = os.path.join(folder, "context.csv")
        # file opener
        with open(context.csv) as csvfile:  # context not defined
            for line in context.csv:
                stripped = line.strip()
                splitted = stripped.split(" ")
                for word in splitted:
                    if word in contextcount:
                        contextcount[word] += 1
                    else:
                        contextcount[word] = 1
        print(name)
        sorted_contextcount = sorted(
            contextcount, key=lambda woord: contextcount[woord], reverse=True)
        resultfile_path = os.path.join(folder, "contextcount.csv")
        if os.path.exists(resultfile_path):
            os.remove(resultfile_path)
        with open(resultfile_path, 'w') as resultfile:
            resultwriter = csv.writer(resultfile, delimiter=",")
            resultwriter.writerow(["woord", "frequency"])
            for woord in sorted_contextcount:
                resultwriter.writerow([woord, contextcount[woord]])


if __name__ == '__main__':
    main()