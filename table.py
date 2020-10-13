import pandas as pd

path = 'Resources/cities.csv'
df = pd.read_csv(path)
df_html = df.to_html()

file = open("sample.html", "w")
file.write(df_html)
