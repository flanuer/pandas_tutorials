import pandas as pd

url = "https://simple.wikipedia.org/wiki/List_of_U.S._states"

fiddy_states = pd.read_html(url)

print(fiddy_states)

