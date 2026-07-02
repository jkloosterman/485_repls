PRAGMA foreign_keys = ON;

CREATE TABLE users (
  username VARCHAR(20) NOT NULL,
  promoted INTEGER,
  PRIMARY KEY(username)
);

CREATE TABLE comments (
  commentid INTEGER PRIMARY KEY AUTOINCREMENT,
  owner VARCHAR(20) NOT NULL,
  text VARCHAR(1024) NOT NULL,

  FOREIGN KEY (owner)
    REFERENCES users(username)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);
