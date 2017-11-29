#website users
unconfirmed_users = ['tsofa', 'giulio', 'peter', 'sarah']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying current users: " + current_user.title())
    confirmed_users.append(current_user)

#Displaying confirmed users
print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())