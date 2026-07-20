import os

os.environ["TESTING"] = "true"

import unittest

import app
from app import TimelinePost, mydb

MODELS = [TimelinePost]


class AppTestCase(unittest.TestCase):
    def setUp(self):
        # Make sure the model is bound to the app's in-memory database and the
        # table exists, regardless of what other test modules did to it.
        mydb.bind(MODELS, bind_refs=False, bind_backrefs=False)
        if mydb.is_closed():
            mydb.connect()
        mydb.create_tables(MODELS)
        self.client = app.app.test_client()

    def tearDown(self):
        # Clear the table between tests so each test starts clean.
        mydb.drop_tables(MODELS)

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_timeline(self):
        # GET on an empty timeline returns an empty list.
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # POST a timeline post, then confirm it comes back on GET.
        post_response = self.client.post(
            "/api/timeline_post",
            data={
                "name": "John Doe",
                "email": "john@example.com",
                "content": "Hello world, I'm John!",
            },
        )
        assert post_response.status_code == 200

        get_response = self.client.get("/api/timeline_post")
        json = get_response.get_json()
        assert len(json["timeline_posts"]) == 1
        assert json["timeline_posts"][0]["name"] == "John Doe"
        assert json["timeline_posts"][0]["content"] == "Hello world, I'm John!"

    def test_timeline_page(self):
        response = self.client.get("/mh/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<form" in html

    # --- Edge case / error tests ---
    def test_malformed_timeline_post(self):
        # POST with no name should not succeed.
        response = self.client.post(
            "/api/timeline_post",
            data={"email": "john@example.com", "content": "Hello world, I'm John!"},
        )
        assert response.status_code == 400
        assert "Invalid" in response.get_data(as_text=True)

        # POST with empty content should not succeed.
        response = self.client.post(
            "/api/timeline_post",
            data={"name": "John Doe", "email": "john@example.com", "content": ""},
        )
        assert response.status_code == 400
        assert "Invalid" in response.get_data(as_text=True)

        # POST with a malformed email should not succeed.
        response = self.client.post(
            "/api/timeline_post",
            data={"name": "John Doe", "email": "not-an-email", "content": "Hello"},
        )
        assert response.status_code == 400
        assert "Invalid" in response.get_data(as_text=True)


if __name__ == "__main__":
    unittest.main()