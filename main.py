from mac_notifications import client
import schedule
import time as tm


# Dealing only seconds case for scheduling
def send_notification(message):
    print('notfication prints',message)
    # client.create_notification(title='reminder from slack cli', subtitle=message)
    # return schedule.CancelJob

def start_schedule(message, argument1, argument2):
    print('start schedule',message,argument1,argument2,argument2 == 'seconds')
    if(argument2 == 'seconds'):
        print('schedule started',int(argument1))
        schedule.every(5).seconds.do(send_notification)
        schedule.every(3).seconds.do(send_notification)


if __name__ == '__main__':
    input_argument = input("Enter reminder: ");
    input_argument = input_argument.split(" in ");
    message = input_argument[0];
    [argument1, argument2] = input_argument[1].split(" ");
    print(f"message: {message}, argument1: {argument1}, argument2: {argument2}")
    start_schedule(message, argument1, argument2)

