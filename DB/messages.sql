CREATE TABLE messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timereceived TIMESTAMP NOT NULL,
        message TEXT NOT NULL,
        was_displayed BOOLEAN NOT NULL
    );

