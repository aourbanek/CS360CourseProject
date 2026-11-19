import pandas as pd

# Dataset importing and basic cleanup
df = pd.read_csv("rotten_tomatoes_movies.csv")
df = df.drop(columns=["rating","ratingContents","releaseDateTheaters","releaseDateStreaming","runtimeMinutes",
                      "originalLanguage","director","writer","boxOffice","distributor","soundMix"])
df = df[(df["audienceScore"] >= 0) & (df["tomatoMeter"] >= 0)]
# TOTO: Cleanup 'genre' fields with multiple listed entries

# Test outputs to verify successful cleanup
print(df.head())
print(df.columns.tolist())