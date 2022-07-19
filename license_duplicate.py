import pandas as pd

list_of_licenses = [{'licenseId': 'XXXAKHILXXX', 'product': {'code': 'WS', 'name': 'WebStorm'}, 'assignee': {'name': 'Random user', 'email': 'rrandom@gmail.com', 'type': 'USER'}, 'subscription': {'validUntilDate': '2023-05-20T00:00:00.000+03:00', 'isOutdated': False, 'subscriptionPackRef': '1215/1JGQR', 'isAutomaticallyRenewed': False}, 'team': {'id': 1874058, 'name': 'U370233323'}, 'isTransferableBetweenTeams': True, 'isTrial': False, 'isSuspended': False, 'isAvailableToAssign': False}, {'licenseId': 'XXXXXXXX', 'product': {'code': 'WS', 'name': 'WebStorm'}, 'assignee': {'name': 'Random user', 'email': 'random@gmail.com', 'type': 'USER'}, 'subscription': {'validUntilDate': '2023-05-20T00:00:00.000+03:00', 'isOutdated': False, 'subscriptionPackRef': '1215/1JGQR', 'isAutomaticallyRenewed': False}, 'team': {'id': 1874058, 'name': 'U370233323'}, 'isTransferableBetweenTeams': True, 'isTrial': False, 'isSuspended': False, 'isAvailableToAssign': False}, {'licenseId': 'randomXXXXXX', 'product': {'code': 'WS', 'name': 'WebStorm'}, 'assignee': {'name': 'random user', 'email': 'random@gmail.com', 'type': 'USER'}, 'subscription': {'validUntilDate': '2023-05-20T00:00:00.000+03:00',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         'isOutdated': False, 'subscriptionPackRef': '1215/1JGQR', 'isAutomaticallyRenewed': False}, 'team': {'id': 1874058, 'name': 'U370233323'}, 'isTransferableBetweenTeams': True, 'isTrial': False, 'isSuspended': False, 'isAvailableToAssign': False}, {'licenseId': 'randomXXXXXX', 'product': {'code': 'WS', 'name': 'WebStorm'}, 'assignee': {'name': 'Random', 'email': 'random@gmail.com', 'type': 'USER'}, 'subscription': {'validUntilDate': '2023-05-20T00:00:00.000+03:00', 'isOutdated': False, 'subscriptionPackRef': '1215/1JGQR', 'isAutomaticallyRenewed': False}, 'team': {'id': 1874058, 'name': 'U370233323'}, 'isTransferableBetweenTeams': True, 'isTrial': False, 'isSuspended': False, 'isAvailableToAssign': False}]

res = {}
email_list = []
for data in list_of_licenses:
    emails = data['assignee']['email']
    if not emails in res:
        res[emails] = {'count': 0, 'licenseId': []}
    res[emails]['count'] += 1
    res[emails]['licenseId'].append(data['licenseId'])
# print(res)
dup = {}
for k,v in res.items():
    if v['count'] > 1:
        dup[k] = v['licenseId']

print(dup)
