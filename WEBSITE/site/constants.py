from dataclasses import dataclass

class Constants:
    CATEGORIES = [
        "Business",
        "Canada",
        "Education",
        "Entertainment",
        "Health",
        "Lifestyle",
        "Politics",
        "Science",
        "Sports",
        "Technology",
        "World",
    ]

    @classmethod
    def num_categories(cls):
        return len(cls.CATEGORIES)
