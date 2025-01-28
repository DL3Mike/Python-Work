def make_shirt(size, text):
    """Print the size and text back to user"""
    print(
        f"The shirt you have created is a size {size}, and has '{text}' printed on the front.")


make_shirt(3, 'Hey Yaaa!')
make_shirt(text='SHOUT', size=6)

# Defaults


def make_shirt(size='L', text='Get Rich'):
    """Print the size and text back to user"""
    print(
        f"The shirt you have created is a size {size}, and has '{text}' printed on the front.")


make_shirt()
make_shirt('M')
make_shirt('L', 'I love python')
