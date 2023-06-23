import requests
from bs4 import BeautifulSoup


def extract_links(url, element, class_name, link_attr='href', base_url=''):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.find_all(element, class_=class_name)

    links = []
    for title in titles[:3]:
        url_link = title.find('a')
        if url_link:
            link = url_link.get(link_attr)
            if link:
                res_link = f"{base_url}{link}"
                links.append(res_link)

    return links


url1 = "https://www.redcrescent.kg/ru/press-center/events/"
url2 = "https://www.unicef-irc.org/events/"
url3 = "https://www.giz.de/en/worldwide/99887.html"
url4 = "https://soros.kg/category/contests/"

links1 = extract_links(url1, 'p', 't-1 my-2 t-title с-text-primary l-inherit l-hover-primary l-hover-underline-none transition', base_url='https://www.redcrescent.kg')
print("Links from url1:")
for link in links1:
    print(link)

links2 = extract_links(url2, 'div', 'storyBoxReadmore', link_attr='href', base_url='https://www.unicef-irc.org/events/')
print("\nLinks from url2:")
for link in links2:
    print(link)

links3 = extract_links(url3, 'section', 'newEvent', base_url='https://www.giz.de')
print("\nLinks from url3:")
for link in links3:
    print(link)

links4 = extract_links(url4, 'div', 'fusion-rollover-content')
print("\nLinks from url4:")
if len(links4) > 0:
    for link in links4:
        print(link)
else:
    print("No links found in url4.")
