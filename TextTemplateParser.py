from ttp import ttp

# Load file
with open("template.txt", "r") as file:
    content = file.read()

# TTP Parser
parser = ttp(content)
parsedTemplate = parser.parse()

# data
data = {"name": "Aman", "date": "12-12-12", "time": "12:12"}

# put data
template1 = parsedTemplate.result(data)

print(template1)
