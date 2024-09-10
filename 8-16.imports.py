import show_messages

short_messages = ["message 1", "message 2", "message 3"]
show_messages.show_messages(short_messages)


from show_messages import show_messages

show_messages(short_messages)


from show_messages import show_messages as sm

sm(short_messages)


import show_messages as sm

short_messages = ["message 1", "message 2", "message 3"]
sm.show_messages(short_messages)


from show_messages import *

show_messages(short_messages)
