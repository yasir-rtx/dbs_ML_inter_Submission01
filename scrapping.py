# Import Libraries
from google_play_scraper import  reviews, Sort
from pandas import DataFrame

# Downloading Data from API
print("Downloading data from google play API...")
pubg_reviews = reviews(
    'com.tencent.ig',
    lang = 'id',
    country = 'id',
    sort = Sort.MOST_RELEVANT,
    count = 20000
)
print("Download COMPLETE!")

# Create Dataframe
pubg_df = DataFrame(pubg_reviews[0])

# Printing Dimension
x_review, y_review = pubg_df.shape
print("\nDimensi Table :")
print("Record :", x_review, "baris")
print("Field  :", y_review, "kolom")

# Printing Sample
print("\nPrinting Sample...")
print(pubg_df[['reviewId', 'content']])

# Saving daataset
print("\nSaving Dataset to CSV file...")
pubg_df.to_csv("pubg_dataset.csv", index=False)
print("Dataset is saved!")