import re
print(re.match('Hello[\t]*(.*) world','Hello      python world').group(1))
match = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
print(match.groups())

