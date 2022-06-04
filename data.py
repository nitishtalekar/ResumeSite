from datetime import date
import json

class ResumeData:
    def __init__(self):
        self.name = "Nitish Pravin Talekar"
        self.oneline = "Developer. Engineer. Designer."
        self.dob = "19th November 1998"
        self.age = self.calculateAge(date(1998, 11, 19))
        self.profile = "img/profile.jpg"
        self.desc_title = "Nitish Talekar"
        self.resume = "https://drive.google.com/file/d/1K1DvCRH16UCzRhUrGEZA3pmy2aktX1Dj/preview"
        self.desc = "Software engineer with a desire to learn and adapt to different challenges thrown at him. An individual who believes in being a team player with demonstrated leadership skills. Result oriented, creative minded & solution driven."
        with open('data/edu.json') as json_file:
            data_edu = json.load(json_file)
        self.edu = data_edu
        with open('data/jobs.json') as json_file:
            data_jobs = json.load(json_file)
        self.jobs = data_jobs
        with open('data/projects.json') as json_file:
            data_projects = json.load(json_file)
        self.projects = data_projects
        with open('data/publish.json') as json_file:
            data_publish = json.load(json_file)
        self.publish = data_publish
        with open('data/exp.json') as json_file:
            data_exp = json.load(json_file)
        self.exp = data_exp
        with open('data/artwork.json') as json_file:
            data_artwork = json.load(json_file)
        self.artwork = data_artwork
        with open('data/skills.json') as json_file:
            data_skills = json.load(json_file)
        self.skills = data_skills
        self.email = [
            "ntaleka@ncsu.edu",
            "nitishtalekar.nt503@gmail.com"
        ]
        self.phone = [
            "+1 (919) 349 8823"
        ]
        self.address = [
            "3802 Lexington Dr.",
            "Apt G",
            "Raleigh NC 27606"
        ]
        with open('data/links.json') as json_file:
            data_links = json.load(json_file)
        self.links = data_links

    def createdata(self):
        resumedata = {
            "name"          : self.name,
            "profile"       : self.profile,
            "resume"        : self.resume,
            "age"           : self.age,
            "dob"           : self.dob,
            "oneline"       : self.oneline,
            "desc_title"    : self.desc_title,
            "desc"          : self.desc,
            "jobs"          : self.divide(self.jobs,2),
            "links"         : self.links,
            "address"       : self.address,
            "phone"         : self.phone,
            "tskills"       : self.divide(self.skills["technical"],(len(self.skills["technical"])+1)//2),
            "ntskills"      : self.divide(self.skills["non_technical"],(len(self.skills["non_technical"])+1)//2),
            "projects"      : self.divide(self.projects,3),
            "artwork"       : self.artwork,
            "edu"           : self.divide(self.edu,2),
            "exp"           : self.divide(self.exp,4),
            "publish"       : self.publish,
            "email"         : self.email
        }
        return resumedata

    def divide(self,l,num):
        sol = []
        for i in range(len(l)):
          if i == 0:
              k = []
          if i%num == 0 and i!=0:
              sol.append(k)
              k = []
          k.append(l[i])
        if len(k)>0:
          sol.append(k)
        return sol

    def calculateAge(self,birthDate):
        today = date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

        return age
