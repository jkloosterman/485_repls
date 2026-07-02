PRAGMA foreign_keys = ON;

/* Clear out tables. DO NOT include this section
   in your data.sql in Project 2. */
.headers on
.mode columns
DELETE FROM users;
DELETE FROM comments;

/* Checkpoint 1: Add you and your partners to users.
  Make sure at least one person is promoted and one person is not.

   Add at least one comment to the comments table.
*/

/* Example */
INSERT INTO users (username, promoted) VALUES ('jklooste', 0);

/* your code here */


/* Prints the contents of the database to the console. */
SELECT * FROM users;
SELECT * from comments;

/* Checkpoint 2: Print the text of all comments by one of your users */

/* Checkpoint 3: Print the text of all comments by all users who are promoted. */
