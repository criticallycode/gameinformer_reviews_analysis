import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from collections import Counter

GI_data = pd.read_csv('GIreviewcomplete3.csv', encoding = "ISO-8859-1")
print(GI_data.head(5))

GI_data2 = pd.get_dummies(GI_data)

scores = GI_data['score'].value_counts()
print(scores)


# display violin plot for author and avg score
sns.lmplot(x='author', y='score', data=GI_data, hue='author', fit_reg=False)
sns.violinplot(x='author',y='score', data=GI_data)
plt.xticks(rotation=-90)
plt.show()

# get all reviews by certain author over a certain score

EF_reviews = GI_data[(GI_data.author == 'Elise Favis') & (GI_data.score >= 8)]
print(EF_reviews)

# count plots are bar plots, will automatically plot chosen variable against count of that variable

plt.figure(figsize=(10, 4))
scores = sns.countplot(x='score', data=GI_data2)
plt.xticks()
plt.show(scores)

plt.figure(figsize=(10, 4))
r_platform = sns.countplot(x="r_platform", data=GI_data)
plt.xticks(rotation=-90)
plt.show(r_platform)

plt.figure(figsize=(10, 4))
rating = sns.countplot(x="rating", data=GI_data)
plt.xticks(rotation=-90)
plt.show(rating)

plt.figure(figsize=(10, 4))
plt.xticks(rotation=-90)
barplot_score = sns.barplot(x="rating", y="score", data=GI_data)
plt.show(barplot_score)

# gives a histogram of the chosen column
histogram = sns.distplot(GI_data2['score'])
plt.show(histogram)

# easy to separate factor plots by categorical classes
plt.figure(figsize=(16, 6))
factorplot_score = sns.swarmplot(x="rating", y="score", data=GI_data, hue='rating')
plt.xticks(rotation= -90)
plt.show(factorplot_score)

# visualize publisher and developer data

publishers = Counter(GI_data['publisher'])
developers = Counter(GI_data['developer'])

pub_list = []
dev_list = []

for item, freq in publishers.most_common(100):
    pub_list.append(item)

for item, freq in developers.most_common(100):
    dev_list.append(item)

# print(pub_list)
# create new dataframe

pub_df = pd.DataFrame(index=None)
dev_df = pd.DataFrame(index=None)

print(pub_list[:10])
print("--------------")
print(dev_list[:10])

# append rows for individual publishers to dataframe

def custom_mean(group):
    group['mean'] = group['score'].mean()
    return group

def custom_median(group):
    group['median'] = group['score'].median()
    return group

for pub in pub_list:
    scores = pd.DataFrame(GI_data[(GI_data.publisher == pub) & (GI_data.score)], index=None)
    pub_df = pub_df.append(scores, ignore_index=True)

pub_mean_df = pub_df.groupby('publisher').apply(custom_mean)
pub_median_df = pub_df.groupby('publisher').apply(custom_median)
pub_median = pub_median_df['median']
pub_merged_df = pub_mean_df.join(pub_median)
print(pub_merged_df.head(3))

for dev in dev_list:
    scores = pd.DataFrame(GI_data[(GI_data.developer == dev) & (GI_data.score)], index=None)
    dev_df = dev_df.append(scores, ignore_index=True)

dev_mean_df = dev_df.groupby('developer').apply(custom_mean)
dev_median_df = dev_df.groupby('developer').apply(custom_median)
dev_median = dev_median_df['median']
dev_merged_df = dev_mean_df.join(dev_median)
print(dev_merged_df.head(3))

# ----- #

dev_data = pd.read_csv('dev_merged.csv')
dev_data = dev_data.drop(dev_data.columns[0], axis=1)
developer_names = list(dev_data['developer'].unique())
print(developer_names)

dev_examples = pd.DataFrame(index=None)

for dev in developer_names:
   dev_examples = dev_examples.append(dev_data[dev_data.developer == dev].iloc[0])

dev_stats = dev_examples[['developer', 'mean', 'median']]
print(dev_stats.head(10))

# check for unique values of
print(GI_data['publisher'].unique())
print(GI_data['developer'].unique())

# you can filter for just one criteria and then pull out only the columns you care about
print(GI_data[GI_data.score <= 4].title)
# this is actually the preferred method...
print(GI_data.loc[GI_data.score <= 4, 'title'])

# how to filter by multiple criteria: use "&" or "|"
print(GI_data[(GI_data.author == 'Elise Favis') & (GI_data.score >= 8)])

# can use "isin" in a series...
# spaces are in this, be sure to include them

r = GI_data[GI_data['publisher'].isin([' Nintendo'])]
print(r)

plt.figure(figsize=(8, 10))
dev_score = sns.swarmplot(x="developer", y="score", data=r, hue='developer')
plt.grid()
plt.xticks(range(50), rotation=-90)
plt.show(dev_score)
