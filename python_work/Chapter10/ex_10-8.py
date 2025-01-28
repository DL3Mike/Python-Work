def read_file(filename):
    """Read the contents of the files and display them to the user"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except:
        print(f"File {filename} is missing.")
    else:
        print(contents)


filenames = ['chapter10/cats.txt', 'chapter10/dogs.txt']
for file in filenames:
    read_file(file)
