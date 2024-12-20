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

def split_content(page):
    content = ""
    start_tag = page.find("<body")
    while True:
        start_tag_bracket = page.find('>', start_tag)
        end_tag_bracket = page.find('<', start_tag_bracket + 1)
        content += page[start_tag_bracket + 1: end_tag_bracket]
        page = page[end_tag_bracket:]
        if page[0:6] == "</body":
            break
    return content

print(split_content(index))