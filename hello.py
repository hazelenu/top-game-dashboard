from preswald import connect, get_df, query, text, table, plotly
import pandas as pd
import plotly.express as px

connect()

df = get_df("Top_Selling_Games_csv")

text("# Top-Selling Games")
table(df)

nintendo_df = query(
    "SELECT * FROM Top_Selling_Games_csv WHERE \"PLATFORM(S)\" = 'Nintendo Switch'",
    "Top_Selling_Games_csv"
)
text("## Nintendo Switch Games")
table(nintendo_df, title="Games on Nintendo Switch")

df["Initial release date"] = pd.to_datetime(df["Initial release date"], errors="coerce")
df["Units Sold (millions)"] = pd.to_numeric(df["Units Sold (millions)"], errors="coerce")

df["Release Year"] = df["Initial release date"].dt.year
release_counts = df["Release Year"].value_counts().reset_index()
release_counts.columns = ["Year", "Game Count"]
release_counts = release_counts.sort_values("Year")

text("## Number of Top-Selling Games by Year")
fig1 = px.line(
    release_counts,
    x="Year",
    y="Game Count",
    markers=True,
)
plotly(fig1)


series_counts = df["Series"].value_counts().reset_index().head(10)
series_counts.columns = ["Series", "Game Count"]

text("## Top 10 Game Series")
fig2 = px.bar(
    series_counts,
    x="Series",
    y="Game Count",
    text_auto=True
)
plotly(fig2)

publisher_counts = df["Publisher(s)[b]"].value_counts().reset_index().head(10)
publisher_counts.columns = ["Publisher", "Game Count"]