def send_messages(short_messages, sent_messages):
    """Sends each received message from a list and move them to a different list."""
    while short_messages:
        current_message = short_messages.pop()
        print(f"Message sent: {current_message}")
        sent_messages.append(current_message)


def show_messages(list_of_messages):
    """Prints each received message from a list."""
    for short_message in list_of_messages:
        print(short_message)


sent_messages = []
short_messages = ["message 1", "message 2", "message 3"]

send_messages(short_messages[:], sent_messages)

print("Sent messages:")
show_messages(sent_messages)

print("Messages to send (should not be empty):")
show_messages(short_messages)
