import pytest
from pages.login_page import LoginPage
from api.base_client import BaseClient
from db.sqlite_client import SQLiteClient

def test_user_login_and_verify_db(page):

    # 2. API Interaction (Example)
    api = BaseClient("https://reqres.in/api")
    response = api.get("/users/2")
    assert response.status_code == 200
    
    # 3. DB Verification (Example)
    db = SQLiteClient("data/users.db")
    df = db.execute_query("SELECT * FROM users WHERE status='active'")
    assert not df.empty, "No active users found in DB"