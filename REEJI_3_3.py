emailadr = ["alice@company.com", "bob@gmail.com", "invalid_email", "carol@company.com", "dave@yahoo.com"]
delim_str = [i.strip() for i in emailadr]
domains = set()
for i in delim_str:
    if '@'in i:
        domain = i.split('@')[1]
        domains.add(domain)

print(sorted(domains))