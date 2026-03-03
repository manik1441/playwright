from db.sqlite_client import SQLiteClient

def test_verify_db():
    # DB Verification (Example)
    db = SQLiteClient("data/users.db")
    df = db.execute_query("SELECT * FROM users WHERE status='active'")
    assert not df.empty, "No active users found in DB"