from mac_notifications import client
import schedule
import time as tm

# input_argument = input("Enter reminder:")
# input_argument = input_argument.split(" in ");
# message = input_argument[0];
# [number, unit] = input_argument[1];

# Dealing only seconds case for scheduling

def send_notification():
    client.create_notification(title='reminder', subtitle="message")

schedule.every(5).seconds.do(send_notification)

while True:
    schedule.run_pending()
    tm.sleep(1)

# if __name__ == "__main__":
#     client.create_notification(title="Meeting starts now!", subtitle="Team Standup")
