import pandas as pd

GI_data = pd.read_csv('GIreviewtest6.csv', encoding="ISO-8859-1", error_bad_lines=False)

print(GI_data.head(5))

categories =("title", "score", "author", "r_platform", "o_platform", "publisher", "developer", "release_date", "rating")
GI_data.drop(GI_data.columns[GI_data.columns.str.contains('unnamed', case = False)], axis = 1, inplace=True)
for category in categories:
    GI_data[category].fillna("Unknown", inplace=True)
GI_data.applymap(str)

print(GI_data.head(5))

GI_data.to_csv('GI_review_complete.csv')
