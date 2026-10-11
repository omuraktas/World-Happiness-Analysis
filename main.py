import pandas as pd
import numpy as np


df = pd.read_csv("data/world_happiness.csv")


df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")
df.columns = df.columns.str.replace(".", "", regex=False)
df.columns = df.columns.str.replace(":", "", regex=False)


top10Happy = df.sort_values(by="happiness_score", ascending=False).head(10)

print("\n--- EN MUTLU 10 ÜLKE ---")
print(top10Happy[["country", "happiness_score"]])


bottom10Happy = df.sort_values(by="happiness_score", ascending=True).head(10)

print("\n--- EN MUTSUZ 10 ÜLKE ---")
print(bottom10Happy[["country", "happiness_score"]])


regionHappiness = df.groupby("region")["happiness_score"].mean().sort_values(ascending=False)

print("\n--- BÖLGELERE GÖRE ORTALAMA MUTLULUK ---")
print(regionHappiness)


happinessArray = np.array(df["happiness_score"])

meanScore = np.mean(happinessArray)
medianScore = np.median(happinessArray)
stdScore = np.std(happinessArray)
maxScore = np.max(happinessArray)
minScore = np.min(happinessArray)

print("\n--- MUTLULUK SKORU İSTATİSTİKLERİ ---")
print("Ortalama Mutluluk Skoru:", meanScore)
print("Medyan Mutluluk Skoru:", medianScore)
print("Standart Sapma:", stdScore)
print("En Yüksek Skor:", maxScore)
print("En Düşük Skor:", minScore)


aboveAverage = df[df["happiness_score"] > meanScore]

print("\n--- ORTALAMANIN ÜSTÜNDEKİ ÜLKELER ---")
print(aboveAverage[["country", "happiness_score"]])


def happinessLevel(score):
    if score >= 7:
        return "High Happiness"
    elif score >= 5:
        return "Medium Happiness"
    else:
        return "Low Happiness"


df["happiness_level"] = df["happiness_score"].apply(happinessLevel)

print("\n--- MUTLULUK SEVİYESİ SINIFLANDIRMASI ---")
print(df[["country", "happiness_score", "happiness_level"]])


levelDistribution = df["happiness_level"].value_counts()

print("\n--- MUTLULUK SEVİYESİ DAĞILIMI ---")
print(levelDistribution)


turkeyData = df[
    df["country"].str.lower().str.contains("turkey|turkiye|türkiye", na=False)
]

print("\n--- TÜRKİYE ANALİZİ ---")
print(turkeyData)


top10Happy.to_csv("outputs/top_10_happiest_countries.csv", index=False)

bottom10Happy.to_csv("outputs/bottom_10_happiest_countries.csv", index=False)

regionHappiness.to_csv("outputs/region_happiness_analysis.csv")

df.to_csv("outputs/cleaned_world_happiness.csv", index=False)

print("\nCSV çıktıları outputs klasörüne kaydedildi.")