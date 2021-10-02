
# notes on process:

I'm starting with the `customers` table and the `melon_types` table because neither has foreign keys so I can test them out before setting up the other tables. 

### In the codeblock under  `if __name__== '__main__':`

First I have some imports, then my code will drop the existing db `melon_bites` if there is one `os.system("dropdb melon_bites --if-exists")` and then created it again `os.system("createdb melon_bites")` so that while I am working on model.py, I can just run the file directly and start with a fresh slate. TODO: have a different db name for the db I will seed with data I care about and the one I use for testing.



I have created one instance of each class I've written and committed them to the database. Now, after each time I run model, I should see that may tables each have at least one row.

### I run my code before each commit, regardless of how confident I am that it is correct 

And if there is something I am less confident of, I will test it separately from other parts of the class: for example, I wasn't 100% sure I had the right syntax for the date field on the melons table, so I ran the code for that before also adding in the foreign keys in that table.

### I run my code as often as possible in case I'm on the wrong track

For example, I test out the foreign key and sqlalchemy relationship I create from `Melon` to `MelonType` before I create a virtually identical relationship to `StorageSpace`. I create two sqlalchemy `Melon` objects and use the relationship from both directions: 

- `Melon` object -> `MelonType` obj
    
        `melon1 = Melon(initial_slices=20, arrival_date=datetime.datetime.now())`
        `cren.melons.append(melon1)` 
- `MelonType` object -> `Melon` object
    
        ```
        melon2 = Melon(initial_slices=15, 
                    arrival_date=datetime.datetime.now(), 
                    melon_type=cren)
        ```