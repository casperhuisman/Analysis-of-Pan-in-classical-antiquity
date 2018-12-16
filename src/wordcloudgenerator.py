from target_texts import target_texts
import os
from os import path
from wordcloud import WordCloud
import csv

def main(): 
    script_location = os.path.dirname(__file__)
    for link, metainfo in target_texts.items():
        name = metainfo[0] + " - " + metainfo[1]
        # os.join voegt 'slim' pathnames samen. Omdat op windows gebruik word gemaakt van \ en niet van /
        folder = os.path.join(script_location, "corpus",  name) # voeg de map corpus/textnaam toe aan huidige pad 
        tfidf = os.path.join(folder, "tfidf.csv") 
        imagepath = os.path.join(folder, "wordcloud.png")
        frequencies = {}
        with open(tfidf) as csvfile: 
            reader = csv.reader(csvfile)
            next(reader)
            for word, tfidf in reader:
                frequencies[word] = float(tfidf)
        if len(frequencies) == 0:
            continue
        # Generate a word cloud image
        wordcloud = WordCloud(width=800, 
                            height=400, 
                            mode='RGBA', 
                            background_color='white',
                            colormap='inferno').fit_words(frequencies)

        # The pil way (if you don't have matplotlib)
        image = wordcloud.to_image()
        if os.path.exists(imagepath):
            os.remove(imagepath)
        image.save(imagepath, 'PNG')
        

if __name__ == "__main__":
    main()