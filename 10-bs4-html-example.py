#10-bs4-html-example
from bs4 import BeautifulSoup
data = """
<ul>
<li class="item">item1</li>
<li class="item">item2</li>
<li class="item">item3</li>
</ul>
"""
soup = BeautifulSoup(data, "html.parser")
for item in soup.select("li.item"):
    print(item.get_text())
