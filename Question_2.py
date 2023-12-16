import pandas as pd

path = 'titles.csv'
df = pd.read_csv(path)

def vowelcounter(title):
    vowelset = set("aeiouAEIOU")
    counter = 0
    for letter in title:
        if letter in vowelset:
            counter += 1
    return counter

df['Vowels'] = df['title'].astype(str).apply(vowelcounter)
print(df.head(10))