def get_sentiment_counts(df):
    return df["sentiment"].value_counts()


def get_total_comments(df):
    return len(df)


def get_sentiment_percentage(df, sentiment):
    total = len(df)

    if total == 0:
        return 0

    count = len(df[df["sentiment"] == sentiment])
    return round((count / total) * 100, 2)