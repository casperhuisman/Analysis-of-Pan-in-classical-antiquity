from bs4 import BeautifulSoup
import requests
import os
import sys
from target_texts import target_texts
    
    

# Retrieve relevant textual content from a single page on http://www.perseus.tufts.edu
# example link: www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0110%3Acard%3D1
def scrapePage(link):
    # enveloppe met html-tekst
    mainpage_response = requests.get(link)
    if mainpage_response.status_code != 200:
        print("Failed for page: {}".format(link))
        return ""
    mainpage_text = mainpage_response.text

    soup = BeautifulSoup(mainpage_text, "lxml")
    textmain_tag = soup.find(id='text_main')

    # Remove script tags (see: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#decompose)
    textmain_tag.script.decompose()
    textmain_text = textmain_tag.find(class_='text') # Ignore footnotes
    
    return(textmain_text.text)

def scrapeText(mainlink, filter=None):
    mainpage_response = requests.get(mainlink)
    mainpage_text = mainpage_response.text
    soup = BeautifulSoup(mainpage_text, "lxml")
    toc_tag = soup.find(id='side_toc')
    a_toc = toc_tag.find_all("a")
    base_url = "http://www.perseus.tufts.edu/hopper/text"
    result_text = ""
    for a in a_toc:
        a_href = a["href"]
        # Filter javascript HREF's for pages with multilevel toc
        if a_href.startswith("?doc"):                
            if filter and filter(a_href):
                print("\t skipping page: {}".format(base_url + a_href))
                continue
            print("\t scraping page: {}".format(base_url + a_href))
            scraped_text = scrapePage(base_url + a_href)
            result_text = result_text + "\n" + scraped_text
    return result_text

def main():
    script_location = os.path.dirname(__file__)
    print("starting scraping!")
    # modify to set scraping targets as a dict in following structure
    # tuftslink: [auteur, title, year, genre, filterfunction]
    # filterfunction is a function string -> bool that can apply aditional filters
    for link, metainfo in target_texts.items():
        print("Scraping target {}". format(metainfo[0] + " - " + metainfo[1]))
    
        
        folder = os.path.join(script_location, "corpus",  metainfo[0] + " - " + metainfo[1]) #os.join voegt 'slim' pathnames samen. Omdat op windows gebruik word gemaakt van \ en niet van /    
        if os.path.exists(folder): # als de folder al bestaat niks doen!
            print("[WARNING] found a folder {} so skipping this site.".format(folder))
            continue # dit laat de for loop doorgaan zonder dit item verder te verwerken

        print("scraping: {}".format(link))
        if metainfo[4]:        
            text = scrapeText(link, metainfo[4])
        else:
            text = scrapeText(link)
        os.makedirs(folder, exist_ok=True)
        
        text_file_path = os.path.join(folder, "text.txt") 
        text_file = open(text_file_path, "w")
        text_file.write(text)
        text_file.close()
        
        meta_file_path = os.path.join(folder, "meta.txt") 
        meta_file = open(meta_file_path, "w")
        meta_file.write("\n".join(metainfo[:-1])) #remove the filter here
        meta_file.close()
        print("finished scraping: {}".format(link))



if __name__ == '__main__':
    main()
