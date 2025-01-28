def show_messages(text_messages):
    while text_messages:
        current_text = text_messages.pop()
        print(current_text)


txt_msg = ['Hey there!', 'Nothing much how about you',
           'Im good', 'Missing you']
show_messages(txt_msg)
