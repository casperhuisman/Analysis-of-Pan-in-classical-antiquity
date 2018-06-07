import re

def herodotusFilter(string):
    # determines wether a link points to chapter 6 or 2 in herodutus the histories
    pattern = r'%3A(\w+)%3D(\d+)'
    matches = re.findall(pattern, string)
    book = matches[0][1]
    return (book != '6' and book != '2') 

target_texts = {
    "http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0110" : ['Euripides', 'Ion', '-413', 'Tragedy', None],
    "http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0126" : ['Herodotus', 'The Histories', '-440', 'Historical', herodotusFilter],
    "http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0032" : ['Aristophanes', 'Frogs', '-405', 'Comedy', None],
    "http://www.perseus.tufts.edu/hopper/text?doc=Soph.%20OT" : ['Sophocles', 'OT', '-429', 'Tragedy', None],
    "http://www.perseus.tufts.edu/hopper/text?doc=Eur.%20Ba" : ['Euripides', 'Bacchae', '-406', 'Tragedy', None],
    "http://www.perseus.tufts.edu/hopper/text?doc=Aesch.%20Eum" : ['Aeschylus', 'Eumenides', '-458', 'Tragedy', None],
    "http://www.perseus.tufts.edu/hopper/text?doc=Eur.%20Hipp" : ['Euripides', 'Hippolytos', '-428', 'Tragedy', None],
    "http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0114" : ['Euripides', 'Medea', '-431', 'Tragedy', None],
    "http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0120" : ['Euripides', 'Rhesus', 'Unknown', 'Tragedy', None],
    'http://www.perseus.tufts.edu/hopper/text?doc=Eur.%20El.' : ['Euripides', 'Elektra', '-420', 'Tragedy', None],
}