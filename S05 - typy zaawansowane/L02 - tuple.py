'''
tuple - listy statyczne, niezmienne - brak możliwości ich edycji w locie (trochę jak str, nie jak listy).
możliwości definicji zmiennych i crossowania
(a, b, c) = tuple - inicjacja 3 zmiennych na podstawie tuple
(a,b) = (b,a) - zamiana wartości bez miennej tymczasowej
'''

marketing = ['loyality program', 'client promotion', 'market research']
print(marketing)
marketing.append('public relations')
print(marketing)
marketing.insert(2, 'investor relations')
print(marketing)
emailMarketing = marketing.copy()
emailMarketing.sort()
print(emailMarketing)
internalEmails = ['internal communication']
emailMarketing.extend(internalEmails)
print(emailMarketing)
emailTuple = tuple(emailMarketing)
print(emailTuple)