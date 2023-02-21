import schedule
import time

from service.send_request_cronjob.send_request import send_request


def run_timely():
    print("This function is run at 6pm every day.")


# Schedule the function to run every day at 6am
schedule.every().day.at("18:00").do(send_request)

# Keep the program running so the scheduled functions can be executed
while True:
    schedule.run_pending()
    time.sleep(1)
