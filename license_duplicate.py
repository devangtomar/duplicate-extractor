import pandas as pd

list_of_licenses = [{'licenseId': 'XXXAKHILXXX', 'product': {'code': 'WS', 'name': 'WebStorm'}, 'assignee': {'name': 'Random user', 'email': 'rrandom@gmail.com', 'type': 'USER'}, 'subscription': {'validUntilDate': '2023-05-20T00:00:00.000+03:00', 'isOutdated': False, 'subscriptionPackRef': '1215/1JGQR', 'isAutomaticallyRenewed': False}, 'team': {'id': 1874058, 'name': 'U370233323'}, 'isTransferableBetweenTeams': True, 'isTrial': False, 'isSuspended': False, 'isAvailableToAssign': False}, {'licenseId': 'XXXXXXXX', 'product': {'code': 'WS', 'name': 'WebStorm'}, 'assignee': {'name': 'Random user', 'email': 'random@gmail.com', 'type': 'USER'}, 'subscription': {'validUntilDate': '2023-05-20T00:00:00.000+03:00', 'isOutdated': False, 'subscriptionPackRef': '1215/1JGQR', 'isAutomaticallyRenewed': False}, 'team': {'id': 1874058, 'name': 'U370233323'}, 'isTransferableBetweenTeams': True, 'isTrial': False, 'isSuspended': False, 'isAvailableToAssign': False}, {'licenseId': 'randomXXXXXX', 'product': {'code': 'WS', 'name': 'WebStorm'}, 'assignee': {'name': 'random user', 'email': 'random@gmail.com', 'type': 'USER'}, 'subscription': {'validUntilDate': '2023-05-20T00:00:00.000+03:00',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'isOutdated': False, 'subscriptionPackRef': '1215/1JGQR', 'isAutomaticallyRenewed': False}, 'team': {'id': 1874058, 'name': 'U370233323'}, 'isTransferableBetweenTeams': True, 'isTrial': False, 'isSuspended': False, 'isAvailableToAssign': False}, {'licenseId': 'randomXXXXXX', 'product': {'code': 'WS', 'name': 'WebStorm'}, 'assignee': {'name': 'Random', 'email': 'random@gmail.com', 'type': 'USER'}, 'subscription': {'validUntilDate': '2023-05-20T00:00:00.000+03:00', 'isOutdated': False, 'subscriptionPackRef': '1215/1JGQR', 'isAutomaticallyRenewed': False}, 'team': {'id': 1874058, 'name': 'U370233323'}, 'isTransferableBetweenTeams': True, 'isTrial': False, 'isSuspended': False, 'isAvailableToAssign': False}]


email_list = []
for data in list_of_licenses:
    email_list.append(data['assignee']['email'])
# print(email_list)

duplicate_emails = []
for emails in email_list:
    if email_list.count(emails) > 1:
        duplicate_emails.append(emails)

duplicate_emails = list(set(duplicate_emails))
print(duplicate_emails)

res = {}

for emails in duplicate_emails:
    for data in list_of_licenses:
        if data['assignee']['email'] == emails:
            if not emails in res:
                res[emails] = []
            res[emails].append(data['licenseId'])

print(res)
