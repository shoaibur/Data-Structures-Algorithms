def unique_email_addresses(emails):
    if len(emails) == 0: return None
    d = {}
    for email in emails:
        if '@' in email:
            email = email.split('@')
            name, domain = email[0], email[1]
            name = name.replace('.','').split('+')[0]
            email = name + '@' + domain
            if email not d:
                d[email] = 1
        else:
            print('invalid email')
    emails = []
    for email in d:
        print(email)
        emails.append(email)
    return emails
