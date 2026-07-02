PRAGMA foreign_keys = ON;

INSERT INTO users (username, promoted) VALUES ('jklooste', 0);
INSERT INTO users (username, promoted) VALUES ('awdeorio', 1);
INSERT INTO users (username, promoted) VALUES ('almomani', 1);

INSERT INTO comments (owner, text) VALUES ('jklooste', 'It is cold outside');
INSERT INTO comments (owner, text) VALUES ('almomani', 'Brrrrr');
INSERT INTO comments (owner, text) VALUES ('jklooste', 'At least it is not as cold as Alaska');