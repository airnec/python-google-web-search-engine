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
# FIRST TRY WITHOUT LOOPS
# -------------------------------------------------------------------------

link1_tag_pos = index.find("<a href")
link1_first_quote_pos = index.find('"', link1_tag_pos)
link1_second_quote_pos = index.find('"', link1_first_quote_pos + 1)
link1 = index[link1_first_quote_pos + 1 : link1_second_quote_pos]
index = index[link1_tag_pos + 1 : ]

link2_tag_pos = index.find("<a href")
link2_first_quote_pos = index.find('"', link2_tag_pos)
link2_second_quote_pos = index.find('"', link2_first_quote_pos + 1)
link2 = index[link2_first_quote_pos + 1 : link2_second_quote_pos]
index = index[link2_tag_pos + 1 : ]

link3_tag_pos = index.find("<a href")
link3_first_quote_pos = index.find('"', link3_tag_pos)
link3_second_quote_pos = index.find('"', link3_first_quote_pos + 1)
link3 = index[link3_first_quote_pos + 1 : link3_second_quote_pos]

print("First link: " + link1)
print("Second link: " + link2)
print("Third link: " + link3)