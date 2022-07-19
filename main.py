import pandas as pd

list_of_licenses = [{'licenseId': 'XXXXXXXX', 'product': {'code': 'WS', 'name': 'WebStorm'}, 'assignee': {'name': 'Random user', 'email': 'random@gmail.com', 'type': 'USER'}, 'subscription': {'validUntilDate': '2023-05-20T00:00:00.000+03:00', 'isOutdated': False, 'subscriptionPackRef': '1215/1JGQR', 'isAutomaticallyRenewed': False}, 'team': {'id': 1874058, 'name': 'U370233323'}, 'isTransferableBetweenTeams': True, 'isTrial': False, 'isSuspended': False, 'isAvailableToAssign': False}, {'licenseId': 'randomXXXXXX', 'product': {'code': 'WS', 'name': 'WebStorm'}, 'assignee': {'name': 'random user', 'email': 'random@gmail.com', 'type': 'USER'}, 'subscription': {'validUntilDate': '2023-05-20T00:00:00.000+03:00',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'isOutdated': False, 'subscriptionPackRef': '1215/1JGQR', 'isAutomaticallyRenewed': False}, 'team': {'id': 1874058, 'name': 'U370233323'}, 'isTransferableBetweenTeams': True, 'isTrial': False, 'isSuspended': False, 'isAvailableToAssign': False}, {'licenseId': 'randomXXXXXX', 'product': {'code': 'WS', 'name': 'WebStorm'}, 'assignee': {'name': 'Random', 'email': 'random@gmail.com', 'type': 'USER'}, 'subscription': {'validUntilDate': '2023-05-20T00:00:00.000+03:00', 'isOutdated': False, 'subscriptionPackRef': '1215/1JGQR', 'isAutomaticallyRenewed': False}, 'team': {'id': 1874058, 'name': 'U370233323'}, 'isTransferableBetweenTeams': True, 'isTrial': False, 'isSuspended': False, 'isAvailableToAssign': False}]

duplicate_emails = []
# duplicate_emails = {}
checker = []

for license in list_of_licenses:
    # print(license['assignee']['email'])

    checker.append(str(license['assignee']['email']))

    n = checker.count(license['assignee']['email'])

    if n > 1 and license['assignee']['email'] not in duplicate_emails:
        # if n > 1 and license['assignee']['email'] not in duplicate_emails.values():

        duplicate_emails.append(license['assignee']['email'])


print('Checler list : \n')
print(checker)
print('\n\nDuplicate list : \n')
print(duplicate_emails)
