import os
import csv
import plotly.plotly as py
import plotly.graph_objs as go
from target_texts import target_texts

def main():
    script_location = os.path.dirname(__file__)
    data = []
    for link, metainfo in target_texts.items():
        name = metainfo[0] + " - " + metainfo[1]
        # os.join voegt 'slim' pathnames samen. Omdat op windows gebruik word gemaakt van \ en niet van /
        folder = os.path.join(script_location, "corpus",  name) # voeg de map corpus/textnaam toe aan huidige pad 
        tfidf = os.path.join(folder, "tfidf.csv") 
        words = []
        tfidfs = []
        with open(tfidf) as csvfile: 
            reader = csv.reader(csvfile)
            next(reader)
            for woord, tfidf in reader:
                words.append(woord)
                tfidfs.append(tfidf)

        cutoff_percentage = 90
        cutoff_index = int((len(words)/100)*cutoff_percentage)


        words = words[:cutoff_index]
        tfidfs = tfidfs[:cutoff_index]

        words.reverse()
        tfidfs.reverse()
        # https://plot.ly/python/reference/#bar
        barvis = go.Bar(
            name=name,
            x=tfidfs,
            y=words,
            orientation= 'h'
        )

        # Per document
        # data = [barvis]
        # py.plot(data, filename = name, auto_open=True)
        # data=[]
        # all together
        data.append(barvis)
    py.plot(data, filename = "TF-IDF for context", auto_open=True)
        
if __name__ == "__main__":
    main()