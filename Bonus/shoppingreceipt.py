# Print all articles
# User chooses an article to buy by inputting ID
# Generate a receipt with the following
"""
Receipt nr.
Article:
Price
"""
# Update the associated ID with stock -1

import pandas
from pdf_code import Receipt

FILEPATH_TO_CSV = "../Files/articles.csv"
df = pandas.read_csv(FILEPATH_TO_CSV, dtype={"id": str, "in_stock": int})


class Article:
    def __init__(self, article_id):
        self.id = article_id
        self.name = df.loc[df["id"] == self.id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.id, "price"].squeeze()

    def articleExists(self):
        return not df.loc[df["id"] == self.id].empty

    def bought(self):
        stock: int = df.loc[df["id"] == self.id, "in_stock"].squeeze()
        new_stock = stock - 1
        df.loc[df["id"] == self.id, "in_stock"] = new_stock
        df.to_csv(FILEPATH_TO_CSV, index=False)

    def in_stock(self):
        """Check if article is in stock"""
        in_stock = df.loc[df["id"] == self.id, "in_stock"].squeeze()
        return in_stock

    def getDetails(self):
        return self.name, self.price


print(df)
article_ID = input("Enter the ID of the article you wish to purchase: ")
article = Article(article_ID)
if article.articleExists():
    if article.in_stock():
        article_name, article_price = article.getDetails()
        article.bought()
        receipt = Receipt(article_ID, article_name, article_price)
        receipt.generateReceipt()
        print("You have successfully bought.")
    else:
        print("Not in stock.")
else:
    print("ID does not exist.")