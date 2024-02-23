import sqlite3


def create_users_table():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (user_id TEXT PRIMARY KEY, email TEXT, username TEXT, password TEXT)"
    )
    connection.commit()
    connection.close()


def insert_users_data(user_data):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO users VALUES (?, ?, ?, ?)", user_data)
    connection.commit()
    connection.close()


def create_posts_table():
    connection = sqlite3.connect("posts.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS posts (post_id TEXT PRIMARY KEY, post_body TEXT, image_url TEXT, user_id TEXT, FOREIGN KEY(user_id) REFERENCES users(user_id))"
    )
    connection.commit()
    connection.close()


def insert_posts_data(post_data):
    connection = sqlite3.connect("posts.db")
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO posts VALUES (?, ?, ?, ?)", post_data)
    connection.commit()
    connection.close()


if __name__ == "__main__":
    user_data = [
        ("sddfgsdfgsfgerergdf", "john@example.com", "JohnDoe", "Nevewvwek"),
        ("dssadfreferf", "alice@example.com", "AliceSmith", "Sawerwrecsco"),
    ]
    post_data = [
        (
            "dsferfsdreffewferffesfsdr",
            "something somethiung bla ewfa bla",
            "https://why-are-there-so-many-bucket-naming-rules.…naws.com/999bdf30-215c-49dd-bd38-ab11d4a67666.jpg",
            "dsferf343erf434dsfer",
        ),
        (
            "dsfederrffverfwgwfesdfr",
            "something something",
            "https://why-are-there-so-many-bucket-naming-rules.…naws.com/999bdf30-215c-49dd-bd38-ab11d4a67666.jpg",
            "dsferfdsrewsdafq344rfer",
        ),
    ]

    create_users_table()
    insert_users_data(user_data)
    create_posts_table()
    insert_posts_data(post_data)
