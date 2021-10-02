## TODO: model the following tables
- [x] customers
- [x] melon_types
- [ ] storage_spaces
- [ ] melons
- [ ] orders
- [ ] melon_orders

notes on process:

I'm starting with the `customers` table and the `melon_types` table because neither has foreign keys so I can test them out before setting up the other tables. 

## In the codeblock under  `if __name__== '__main__':`

First I have some imports, then my code will drop the existing db `melon_bites` if there is one `os.system("dropdb melon_bites --if-exists")` and then created it again `os.system("createdb melon_bites")` so that while I am working on model.py, I can just run the file directly and start with a fresh slate. TODO: have a different db name for the db I will seed with data I care about and the one I use for testing.



I have created one instance of each class I've written and committed them to the database. Now, after each time I run model, I should see that may tables each have at least one row.

## I run my code before each commit, regardless of how confident I am that it is correct 