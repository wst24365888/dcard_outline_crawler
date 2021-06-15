class ArticleOutline:
    def __init__(self, title, link, emoji_amount, reply_amount):
        super().__init__()

        self.title = title
        self.link = link
        self.emoji_amount = emoji_amount
        self.reply_amount = reply_amount

    def toJSON(self):
        return {"title": self.title, "link": self.link, "emoji_amount": self.emoji_amount, "reply_amount": self.reply_amount}

    def printJSON(self):
        print({"title": self.title, "link": self.link,
              "emoji_amount": self.emoji_amount, "reply_amount": self.reply_amount})
