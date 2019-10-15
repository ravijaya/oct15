"""ipc using queues"""

import multiprocessing
from smtplib import SMTP
from email.mime.text import MIMEText
import requests

smtp_server = 'localhost' # relay.amadeus.net


def send_alert_mail(from_addr, to_addr, subject, message):
    mesg = MIMEText(message)
    mesg['To'] = to_addr
    mesg['From'] = from_addr
    mesg['Subject'] = subject

    smtp = SMTP(smtp_server)
    # smtp.debuglevel = 1
    smtp.sendmail(from_addr, to_addr, mesg.as_string())
    smtp.close()


def web_crawler(q):
    try:
        url = q.get()
        p_name = multiprocessing.current_process().name
        response = requests.get(url)
        print(f'{p_name}: {url}: {response.content[:128]}')
    except requests.exceptions.ConnectionError as err:
        subject = f'failed request {p_name}: {url}'
        send_alert_mail('ravi@localhost', 'training@localhost', subject, str(err))


def main():
    """parent process"""

    urls = ['http://linux.org', 'http://kernel.org', 'http://python.org',
            'http://golang.org', 'http://perllang.org']

    queue = multiprocessing.Queue()  # ipc using queues

    for _ in urls:
        p = multiprocessing.Process(target=web_crawler, args=(queue,))
        p.start()

    for url in urls:
        queue.put(url)

    for child in multiprocessing.active_children():
        child.join()


if __name__ == '__main__':
    main()
