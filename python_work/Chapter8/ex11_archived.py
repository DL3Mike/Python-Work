def send_messages(text_messages, sent_messages):
    while text_messages:
        sending_text = text_messages.pop()
        print(sending_text)
        sent_messages.append(sending_text)


txt_msg = ['Hey there!', 'Nothing much how about you',
           'Im good', 'Missing you']
sent_txt = []

send_messages(txt_msg[:], sent_txt)
print(txt_msg)
print(sent_txt)
