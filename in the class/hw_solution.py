
# list [ 1, 2, 3 ]
# dict { 'tom': 1.78, 'sandy': 1.55 } OrderedDict
# str1: str = "python"
# tuple ( 1, 2, #lst1, str1 )
#               [] clear
# str1 += "!"  # python!  #
# set { 1, 2, 3 }
# str -- immutable
# int float bool None
# ternary
# comprehension

oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

# a
oscar_winners.add("Emma Watson")
print(oscar_winners)

# b
oscar_copy = oscar_winners.copy()
if "Meryl Streep" in oscar_copy:
    oscar_copy.remove("Meryl Streep")
# safe remove
oscar_copy.discard("Meryl Streep")

# how to remove few items in set
# 1
print({name for name in oscar_copy \
       if not name in ["Meryl Streep", "Leonardo DiCaprio"]})
# 2
print(oscar_copy ^ {"Meryl Streep", "Leonardo DiCaprio"})

print(oscar_copy)
oscar_copy.clear()

# c
print(titanic_actors & dark_knight_actors)  # intersection

# d
print("d:")
print(iron_man_actors & avengers_actors)
print(True if (iron_man_actors & avengers_actors) else False)
print(not iron_man_actors.isdisjoint(avengers_actors))
# {1, 2}
# {4, 3}
# {}
# {""} any({""})
# {...}
# A - B ==> A

# e
print("e:")
print(actor_list <= oscar_winners)  # issubset

# f
print("f:")
print(actor_list >= avengers_actors)  # issuperset

# g
print("g:")
movie_cast.pop()

# h
movie_cast.discard("Matt Damon")

# i
print(titanic_actors - oscar_copy)  # diff

# j
print(titanic_actors ^ dark_knight_actors)  # symm diff

# k
oscar_copy.update({"Cate Blanchett", "Daniel Day-Lewis"})

# l
print(titanic_actors | dark_knight_actors)  # union

















