import re

content = 'Hello 123 4567 World_This is a Regex Demo'
content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))

# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
result = re.match('^Hello\s(\d+)\sWorld',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span)


result = re.match("^Hello .*Demo",content)
print(result)
print(result.group())
print(result.span())