import json

data = {
    "facebook":"https://www.facebook.com/nitish.talekar.9/",
    "linkedin":"https://www.linkedin.com/in/nitishtalekar/",
    "github":"https://github.com/nitishtalekar",
    "instagram":"https://www.instagram.com/nitishtalekar11/"
}

final = json.dumps(data, indent=4)
with open("data/links.json", "w") as outfile:
    outfile.write(final)
