glossary = {
    'string': 'sequence of characters wrapped in quotes',
    'boolean': 'truth values - either True or False',
    'list': 'mutable, ordered sequence of elements',
    'tuples': 'immutable, ordered sequence of values',
    'dictionary': 'collection of a key-value pairs',
}

# ex4_Glossary 2
for term, definition in glossary.items():
    print(f"\n{term.title()}: {definition}")

# Longer version of print out method
#print(f"string: {glossary['string']}.\n")
#print(f"Boolean: {glossary['boolean']}.\n")
#print(f"List: {glossary['list']}.\n")
#print(f"Tuple: {glossary['tuples']}.\n")
#print(f"Dictionary: {glossary['dictionary']}.\n")
