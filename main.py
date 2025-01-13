def getPage(url):
    try:
        import urllib.request
        page = urllib.request.urlopen(url).read()
        page = page.decode("utf-8")
        return page
    except:
        return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote+1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def add_to_index(index, keyword, url):
    if keyword in index:
        # index[keyword].append(url)
        union(index[keyword], [url]) #THIS PREVENTS DUPLICATES IN INDEX
    else:
        index[keyword] = [url]

# HELPER FUNCTION TO CLEAN HTML CODE
# ----------------
def getclearpage(content):
    title = content[content.find("<title>")+7:content.find("</title>")]
    body = content[content.find("<body>")+6:content.find("</body>")]
    while body.find(">") != -1:
        start =  body.find("<")
        end =  body.find(">")
        body = body[:start] + body[end+1:]
    return title + body
# ----------------

def addPageToIndex(index, url, content):
    content = getclearpage(content)
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def addPageToIndexWithoutCleaning(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

# CRAWL WEB FUNCTION
def crawlWeb(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    graph = {}

    while tocrawl:
        page = tocrawl.pop()

        if page not in crawled:
            content = getPage(page)
            addPageToIndex(index, page, content)

            outlinks = get_all_links(content)
            graph[page] = outlinks

            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index, graph

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

crawlWeb("http://www.searchengineplaces.com.tr")
# The graph is represented in key, value pairs in a dictionary,
# where the keys are the websites in which the words in the index are found
# and the values are the lists containing the websites which those keys lead us to (outlinks)

# CREATING INDEX AND GRAPH
index1, graph1 = crawlWeb("http://www.searchengineplaces.com.tr")

print(f"The graph has {len(graph1)} elements. These are:")

i = 1
for key, value in graph1.items():
    print(f"  {i}.  [{key}]: {value}")
    i += 1

# RANKING PAGES PROCEDURE (PAGE RANK ALGORITHM)
def computeRanks(graph):

    d = 0.8 #damping factor
    N = len(graph) #number of pages
    numloops = 10 #effects the accuracy
    ranks = {}

    for page in graph:
        ranks[page] = 1 / N

    for i in range(0, numloops):
        newranks = {}

        for page in graph:
            newrank = (1 - d) / N

            for node in graph:

                if page in graph[node]:
                    newrank = newrank + d * ranks[node] / len(graph[node])

            newranks[page] = newrank
        ranks = newranks
    return ranks

ranks = computeRanks(graph1)

for key, value in ranks.items():
    print(f"The rank of the page {key}:    {value}")


def sortingAlgorithm(list_to_sort, keyword, ranks):
    while True:
            bilateral_change_counter = 0

            for i in range(len(list_to_sort[keyword]) - 1):

                backup = ""
                if ranks[list_to_sort[keyword][i + 1]] > ranks[list_to_sort[keyword][i]]:

                    backup = list_to_sort[keyword][i]
                    list_to_sort[keyword][i] = list_to_sort[keyword][i + 1]
                    list_to_sort[keyword][i + 1] = backup

                    bilateral_change_counter += 1

            if bilateral_change_counter == 0:
              break

# RANKED LOOKUP FUNCTION
def rankedLookup(index, keyword, graph):

    # I create a new dictionary with copied lists to break aliasing.
    # Otherwise, i cannot use original lookup() with unranked pages.
    # I want to ensure that the original index1 stays intact.
    index2 = {key: value[:] for key, value in index.items()}

    # THE FOLLOWING CODE COULD BE USED IF INDEX IS NOT REMOVED OF DUPLICATES.
    #index2 = {key: list(set(value)) for key, value in index.items()}

    ranks = computeRanks(graph)

    if keyword in index2:
        sortingAlgorithm(index2, keyword, ranks)

        return index2[keyword]
    else:
        return None

results = rankedLookup(index1, "in", graph1)

for result in results:
    print(result)


# THE FOLLOWING CODE IS THE GENERALIZED VERSION OF THE RANKED LOOKUP FUNCTION
errorMessage = """This procedure takes 4 outputs. These are:
        1-An index
        2-A key
        3-A graph
        4-A computing procedure
                respectively.
You have 2 options to use this lookup procedure: with or without ranking.
        -If you intended it to use it without page rank be sure you have given two inputs, index and key, respectively.
        -If you intended it to use it with page rank be sure you have given all four input in the given order.
INVALID INPUT COMBINATION: Please check the inputs."""

def lookup(*args):
    if len(args) == 2:
        index, keyword = args

        if keyword in index:
            return index[keyword]
        else:
            return []

    elif len(args) == 3:
        print(errorMessage)
        return None

    else:
        index, keyword, graph, rankingAlgorithm = args

        # I create a new dictionary with copied lists to break aliasing.
        # Otherwise, i cannot use this as the original lookup() with unranked pages.
        # I want to ensure that the original index stays intact.
        index2 = {key: value[:] for key, value in index.items()}

        # THE FOLLOWING CODE COULD BE USED IF INDEX IS NOT REMOVED OF DUPLICATES.
        #index2 = {key: list(set(value)) for key, value in index.items()}

        ranks = rankingAlgorithm(graph)

        if keyword in index2:
            sortingAlgorithm(index2, keyword, ranks)

            return index2[keyword]
        else:
            return None

see = lookup(index1, "in", graph1, computeRanks)
for e in see:
    print(e)

print("")

see1 = lookup(index1, "in")
for e in see1:
    print(e)

# TESTING THE RANKED LOOKUP FUNCTION WITH THE GENERALIZED LOOKUP FUNCTION
assert rankedLookup(index1, "in", graph1) == lookup(index1, "in", graph1, computeRanks)

# TESTING THE GENERALIZED LOOKUP FUNCTION
lookup(index1, "in", graph1)