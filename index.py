index = r"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Gardening Tips</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f0f8ff;
        color: #333;
        margin: 0;
        padding: 20px;
      }
      header {
        text-align: center;
        margin-bottom: 20px;
      }
      h1 {
        color: #4caf50;
      }
      nav {
        text-align: center;
        margin-bottom: 20px;
      }
      nav a {
        margin: 0 10px;
        text-decoration: none;
        color: #4caf50;
      }
      nav a:hover {
        text-decoration: underline;
      }
      section {
        max-width: 800px;
        margin: 0 auto;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Gardening Tips</h1>
    </header>
    <nav>
      <a href="https://www.example.com/planting-basics">Planting Basics</a>
      <a href="https://www.example.com/soil-preparation">Soil Preparation</a>
      <a href="https://www.example.com/garden-tools">Garden Tools</a>
    </nav>
    <section>
      <h2>Welcome to Gardening Tips</h2>
      <p>
        Whether you're a seasoned gardener or just starting out, our tips and
        guides will help you cultivate a beautiful and bountiful garden. Explore
        the links above to learn more about planting basics, soil preparation,
        and essential garden tools.
      </p>
      <p>Happy gardening!</p>
    </section>
  </body>
</html>
"""

# -------------------------------------------------------------------------
# HELPER PROCEDURES FOR WEB CRAWLER
# -------------------------------------------------------------------------

# def get_page(url):
#     try:
#         import urllib.request
#         page = urllib.request.urlopen(url).read()
#         return page.decode("utf−8")
#     except:
#         return ""
    
# # -------------------------------------------------------------------------
# # TO PREVENT SOME WEBSITES FROM BLOCKING A RESPONSE BACK
# # -------------------------------------------------------------------------
def get_page(url):
    try:
        import urllib.request
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        req = urllib.request.Request(url, headers=headers)
        page = urllib.request.urlopen(req).read()
        return page.decode("utf-8")
    except Exception as e:
        print(f"Error: {e}")
        return ""

def get_next_target(page):
    start_link = page.find("<a href=")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos + 1:]
        else:
            break
    return links
# print(get_all_links(index))

# -------------------------------------------------------------------------
# INDEX
# -------------------------------------------------------------------------

# [[kw1, [url1, url2]], [kw2, [url2, url3]], ...]
# [[..., [...]], [..., [...]], ...]

# index = []

print("🤔")
# print(my_index[0])

def add_to_index(index, kw, url):
    for element in index:
        if kw == element[0]:
            element[1] = list(set(element[1]).union([url]))
            return
    index.append([kw, [url]])
    return

# add_to_index(my_index, "abc", "www.abc.com")
# print(my_index)

def add_page_to_index(index, url):
    # print("🎈")
    page = get_page(url)
    content = page.split()
    # print("🥇")
    # print(content)
    for element in content:
        add_to_index(index, element, url)

# print(get_page("https://engoo.com/").split())

def look_up(my_index, kw):
    for my_element in my_index:
        if my_element[0] == kw:
            return my_element[1]
    return []
# -------------------------------------------------------------------------
# WEB CRAWLER
# -------------------------------------------------------------------------

def crawl_web(seed):
    tocrawl = [seed]
    # print(tocrawl)
    crawled = []
    index = []
    while tocrawl:
        url = tocrawl.pop()
        # print(url)
        # print(get_page(url))
        # print(get_all_links(get_page(url)))
        if url not in crawled:
            add_page_to_index(index, url)
            tocrawl = list(set(tocrawl).union(get_all_links(get_page(url))))
            # print("🎈")
            # print(tocrawl)
            crawled.append(url)
            # print("✅")
            # print(crawled)
    return crawled, index

seed = "https://searchengineplaces.com.tr/"
crawled, index = crawl_web(seed)

# print("⏩")
# print(crawled)
# print("🎃")
print(index)