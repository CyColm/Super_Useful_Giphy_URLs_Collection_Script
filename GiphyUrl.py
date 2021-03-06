# -*- coding: utf-8 -*-

import re
import sys

# All URLs get from browser option
# It consists in setup starting tab by all presents tabs
# It generates a string of all URls separated by a pipe

urls = ""  # put your string generated by your browser here
if len(urls)>1:
  list_of_urls = urls.split('|')
elif len(sys.argv)>1:
  urls=sys.argv[1]
  list_of_urls = urls.split('|')
else:
  urls=input("copy the string of urls here : ")
  list_of_urls = urls.split('|')


# Remove no Giphy URL
list_of_index_to_remove = []
for idx, url in enumerate(list_of_urls):
    if not url.__contains__('giphy'):
        list_of_index_to_remove.append(url)
for i in list_of_index_to_remove:
    list_of_urls.remove(url)

# Generate new URL
prefix = "https://media.giphy.com/media/"
suffix = "/giphy.gif"
list_of_gifs = []
for url in list_of_urls:
    if url.__contains__('giphy.com/gifs'):
        m = re.findall(r'[^-\/]\w*', url)
        if len(m) > 0:
            ref_gif = m[len(m) - 1]
            list_of_gifs.append(prefix + ref_gif + suffix)

# Save list of URLS
file = open('getURLs.txt', 'w')
file.write('\n'.join(list_of_gifs))
file.close()
print("\n".join(list_of_gifs))
