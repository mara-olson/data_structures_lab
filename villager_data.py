"""Functions to parse a file containing villager data."""

def all_species(filename):
    """Return a set of unique species in the given file.
    Arguments:
        - filename (str): the path to a data file
    Return:
        - set[str]: a set of strings
    """
    file = open(filename)

    species = []
    for line in file:
        items_in_line = line.split('|')
        species.append(items_in_line[1])

    return set(species)
# print(all_species("villagers.csv"))


#----------------------------------------------------------


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.
    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species
    Return:
        - list[str]: a list of names
    """
    file = open(filename)

    villagers = []
    for line in file:
        items_in_line = line.split('|')
        # villager_name = line[0]
        # species = line[1]
        if items_in_line[1] == search_string:
            villagers.append(items_in_line[0])
        elif search_string == 'All':
            villagers.append(items_in_line[0])
        elif not items_in_line[1]:
            villagers.append(items_in_line[0])
        #assuming user doesn't enter a species that isn't in the list

    return sorted("villagers.csv")
# print(get_villagers_by_species(villager_file, 'Hamster'))


#----------------------------------------------------------

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.
    Arguments:
        - filename (str): the path to a data file
    Return:
        - list[list[str]]: a list of lists containing names
    """

    file = open(filename)

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []
    for line in file: 
    # line is one long string for each line in the file
        items_in_line = line.split('|')
        # items_in_line is a list of all the items delimited by |
        
        if items_in_line[3] == 'Fitness':
            fitness.append(items_in_line[0])
        elif items_in_line[3] == 'Nature':
            nature.append(items_in_line[0])
        elif items_in_line[3] == 'Education':
            education.append(items_in_line[0])
        elif items_in_line[3] == 'Music':
            music.append(items_in_line[0])
        elif items_in_line[3] == 'Fashion':
            fashion.append(items_in_line[0])
        elif items_in_line[3] == 'Play':
            play.append(items_in_line[0])

    return [sorted(fitness), sorted(nature), sorted(education), sorted(music), sorted(fashion), sorted(play)]

# print(all_names_by_hobby("villagers.csv"))


#----------------------------------------------------------


def all_data(filename):
    """Return all the data in a file.
    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).
    Arguments:
        - filename (str): the path to a data file
    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    file = open(filename)
    
    all_data = []

    for line in file:
        items_in_line = set(line.rstrip().split('|'))
        # print(items_in_line)
        all_data.append(items_in_line)

    return all_data
print(all_data("villagers.csv"))



#----------------------------------------------------------


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
