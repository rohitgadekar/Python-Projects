def replace_domain(email, old_domain, new_domain):
    if '@' + old_domain in email:
        index = email.index('@' + old_domain)
        new_email = email[:index] + '@'+new_domain
        return new_email
    return email


print('\n*** This Works Only For .txt Files ***\n')
filename = input('Enter File Name (Dont include file extension) : ') + '.txt'
new_domain = input('Enter New Domain (Dont include \'@\'): ')


file = open(filename, 'r')
read = file.readlines()

new_list = []
for line in read:
    if line[-1] == '\n':
        new_list.append(line[:-1])

for x in new_list:
    var = x.split('@')
old_domain = var[1]

final = []
for x in range(len(new_list)):
    final.append(replace_domain(new_list[x], old_domain, new_domain) + '\n')


file = open(filename, 'w')
for items in final:
    file.write(items)
file.close()
print('*** Done ***')
