import time
from plyer import notification

def desktop_notifier(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification will be visible for 10 seconds
    )

if __name__ == "__main__":
    # Test the desktop notifier
    desktop_notifier("Notification Title", "This is a sample notification.")
