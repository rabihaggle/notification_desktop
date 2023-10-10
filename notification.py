import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title="Alert",
        message="Test",
        timeout=10,
        app_name='MyApp' 
    )