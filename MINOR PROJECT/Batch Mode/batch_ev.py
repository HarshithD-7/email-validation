import re

# Function to validate the local part of the email address
def ValidateLocal(local):
    local_pattern = r'^[a-zA-Z0-9._-]+$'
    return re.fullmatch(local_pattern, local) and len(local) >= 3 and local[0] != '.'

# Function to validate the domain part of the email address
def ValidateDomain(domain):

    # This regex pattern matches a domain name
    domain_pattern = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # This regex pattern matches an IP address in the format of X.X.X.X, where X represents a number ranging from 0 to 255
    ip_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.fullmatch(domain_pattern, domain) or re.fullmatch(ip_pattern, domain)

    # Extract the last domain and check if it is one of the specified valid domains
    last_domain = domain.split('.')[-1]
    return last_domain in ['org', 'edu', 'com', 'gov', 'net', 'web']

# Function for interactive email validation
def ValidateEmail(email):
    if '@' not in email or email.count('@') > 1 or ' ' in email:
        return False
    if len(email) >= 320:
        return False

    local, domain = email.split('@')
    print(local, domain)
    local_status = ValidateLocal(local)
    domain_status = ValidateDomain(domain)

    return local_status and domain_status

# Open the input file for reading the email addresses and the output file for writing
with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    for email in input_file:
        status = ValidateEmail(email)

        # Check if the email is valid and write the corresponding message to the output file
        if status:
            output_file.write('**VALID** -- {}\n'.format(email))
        else:
            output_file.write('INVALID -- {}\n'.format(email))






