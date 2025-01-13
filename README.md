- This project aims to demonstrate how the Google Team created the first Web Search Engine based on the PageRank Algorithm.

- This is totally developed in Programming with Python course, which is taught by Assoc.Prof. H.Oktay Altun at Data Science and Artificial Intelligence Institute at Boğaziçi University.

- The Page Rank algorithm was developed by Larry Page and Sergey Brin around 1996-1998.
- It leveraged the web's structure as a graph, with pages as nodes and hyperlinks as edges.

Core Concepts:

- The web was modeled as a directed graph, where pages linked to one another.
- A hyperlink from page 𝐴 to page 𝐵 was considered a "vote" for 𝐵's importance.

Recursive Importance:

- A page's importance was determined not just by the number of links to it, but also by the importance of the linking pages.
- The more important the pages linking to a given page, the higher its rank.

PageRank Formula:
The PageRank of a page 𝑃 was computed using:

𝑃𝑅(𝑃) = (1 − 𝑑) /𝑁 + 𝑑 \* (for 𝑖 ∈ In(𝑃)) ∑(𝑃𝑅(𝑖) / Out(𝑖))

Where:

𝑃𝑅(𝑃) : PageRank of page
𝑁 : Total number of pages on the web.
𝑑 : Damping factor, typically set to 0.85, representing the likelihood that a user continues following links.
In(P) : Set of pages linking to 𝑃.
Out(𝑖) : Number of outbound links on page 𝑖.

Iterative Computation

- Initialization:
  Each page was assigned an equal PageRank,
  𝑃𝑅(𝑃) = 1 / 𝑁
  ​
  Iteration:
- The formula was applied repeatedly until the PageRank values converged (changes between iterations became negligible).

The Damping Factor ensured all pages received a minimum baseline rank and avoided rank sinks (e.g., loops in the graph).

Early Impact

- It prioritized pages with both high link counts and links from authoritative sources.
  Unlike earlier ranking systems (e.g., based purely on keywords), PageRank leveraged the structure of the web itself, leading to more relevant search results.

- This original algorithm laid the foundation for Google's dominance in search engines, though modern implementations have evolved significantly to account for spam, user behavior, and other factors.
