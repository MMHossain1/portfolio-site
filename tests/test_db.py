import os

os.environ["TESTING"] = "true"

import unittest

from app import TimelinePost, mydb

MODELS = [TimelinePost]


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind the model to the app's in-memory database and create fresh
        # tables before each test.
        mydb.bind(MODELS, bind_refs=False, bind_backrefs=False)
        if mydb.is_closed():
            mydb.connect()
        mydb.create_tables(MODELS)

    def tearDown(self):
        # Drop tables after each test so tests stay isolated. The connection is
        # left open so other test modules sharing this database still work.
        mydb.drop_tables(MODELS)

    def test_timeline_post(self):
        # Save two posts to the database.
        first_post = TimelinePost.create(
            name="John Doe", email="john@example.com", content="Hello world, I'm John!"
        )
        assert first_post.id == 1

        second_post = TimelinePost.create(
            name="Jane Doe", email="jane@example.com", content="Hello world, I'm Jane!"
        )
        assert second_post.id == 2

        # Retrieve the timeline posts and verify they were saved.
        posts = TimelinePost.select()
        assert posts.count() == 2

        # The application returns posts newest-first (created_at descending).
        ordered = list(
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        )
        assert ordered[0].name == "Jane Doe"
        assert ordered[1].name == "John Doe"


if __name__ == "__main__":
    unittest.main()