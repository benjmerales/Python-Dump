email = input("Enter your email: ")

at_location = email.find('@')
username = email[:at_location]
domain = email[at_location+1:]

print("Username: ", username)
print("Domain: ", domain)