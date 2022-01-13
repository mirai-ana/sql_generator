# sql_generator

## What might this be?
This is something I wrote a long time ago so that I could get SQL statements faster and spend more time on the actual schema while working.

## How to use it?
It requires you to have the database schema.
First enter the names of all the tables.
Then, enter the columns names and their type (maybe I'll add something more convenient).
Then, just enter the values to be entered as mentioned in the prompt.

```python
Enter table names
friends
Enter columns of friends
name VARCHAR,birthdays DATE

CREATE TABLE friends (
 name VARCHAR,
birthdays DATE );


Enter table= friends columns= name,birthdays
friends1,'10-01'
INSERT INTO friends ( name,birthdays ) VALUES ( friends1,'10-01' );
```

## Compatibility
Anything supporting `print()`.

## Future Plans
None really...
