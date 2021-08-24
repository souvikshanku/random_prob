# https://regex101.com/ rocks!
import re

regex = re.compile("[A-Za-z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}\Z", re.I)

def fun(s):
    # return True if s is a valid email, else return False
    match = regex.match(s)
    if match:
        return True
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
