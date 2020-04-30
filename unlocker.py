import os
import sys
import urllib.request as urllib2
from urllib.parse import urlparse
from lxml import html


def main(argv):
    for url in argv:
        # download the page
        print("Downloading page:", url)
        response = urllib2.urlopen(url)
        page_source = response.read()
        
        # parsing page
        print("Parsing...")
        root = html.document_fromstring(page_source)
        aside_tags = root.findall("aside")
        for item in aside_tags:
            item.getparent().remove(item)
        
        
        # save
        a = urlparse(url)
        path = os.path.basename(a.path)
        print("Saving to", path)
        with open(path, 'wb') as f: 
            f.write(html.tostring(root, pretty_print=True) )
        
        print("Done")
        

if __name__ == "__main__":
    main(sys.argv[1:])

