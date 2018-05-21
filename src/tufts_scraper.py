from bs4 import BeautifulSoup
import requests
import os

# Retrieve relevant textual content from a single page on http://www.perseus.tufts.edu
# example link: www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0110%3Acard%3D1
def scrapePage(link):
    # enveloppe met html-tekst
    mainpage_response = requests.get(link)
    if mainpage_response.status_code != 200:
        print("Failed for page: {}".format(link))
        return ""
    mainpage_text = mainpage_response.text

    soup = BeautifulSoup(mainpage_text, "html.parser")
    textmain_tag = soup.find(id='text_main')
    # Remove script tags (see: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#decompose)
    textmain_tag.script.decompose()
    return(textmain_tag.text)

def scrapeText(mainlink):
    mainpage_response = requests.get(mainlink)
    mainpage_text = mainpage_response.text
    soup = BeautifulSoup(mainpage_text, "html.parser")
    toc_tag = soup.find(id='side_toc')
    a_toc = toc_tag.find_all("a")
    base_url = "http://www.perseus.tufts.edu/hopper/text"
    result_text = ""
    for a in a_toc:
        a_href = a["href"]
        # Filter javascript HREF's for pages with multilevel toc
        if a_href.startswith("?doc"):
            print("\t scraping page: {}".format(base_url + a_href))
            scraped_text = scrapePage(base_url + a_href)
            result_text = result_text + "\n" + scraped_text
    return result_text

def main():
    print("starting scraping!")
    # modify to set scraping targets as a dict in following structure
    # tuftslink: [auteur, title, year, genre]
    target_texts = {
    # "http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0110" : ['Euripides', 'Ion', '-413', 'Tragedy'],
    "http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0126" : ['Herodotus', 'The Histories', '-440', 'Historical'],
    }
    for link, metainfo in target_texts.items():
        print("scraping: {}".format(link))
        text = scrapeText(link)
        folder = "corpus\\" + metainfo[0] + " - " + metainfo[1]
        os.makedirs(folder, exist_ok=True)
        text_file = open(folder + "\\text.txt", "w")
        text_file.write(text)
        text_file.close()
        text_file = open(folder + "\\meta.txt", "w")
        text_file.write("\n".join(metainfo))
        text_file.close()
        print("finished scraping: {}".format(link))



if __name__ == '__main__':
    main()
