from datetime import date
import json

class ResumeData:
    def __init__(self):
        with open('data/description.json') as json_file:
            self.data_desc = json.load(json_file)
        self.name = self.data_desc['name']
        self.oneline = self.data_desc['oneline']
        self.dob = self.data_desc['dob']
        age_date = self.data_desc['age'].split("/")
        self.age = self.calculateAge(date(int(age_date[2]), int(age_date[1]), int(age_date[0])))
        self.profile = self.data_desc['profile']
        self.desc_title = self.data_desc['desc_title']
        self.resume = self.data_desc['resume']
        self.desc = self.data_desc['desc']


        with open('data/edu.json') as json_file:
            self.data_edu = json.load(json_file)
        self.edu = self.data_edu

        with open('data/coffeecoders.json') as json_file:
            self.data_coffeecoders = json.load(json_file)
            age_cc_date = self.data_coffeecoders['cc_dob'].split("/")
            self.data_coffeecoders['cc_dob'] = self.calculateAge(date(int(age_cc_date[2]), int(age_cc_date[1]), int(age_cc_date[0])))
        self.coffeecoders = self.data_coffeecoders

        with open('data/jobs.json') as json_file:
            self.data_jobs = json.load(json_file)
        self.jobs = self.data_jobs

        with open('data/projects.json') as json_file:
            self.data_projects = json.load(json_file)
        self.projects = self.data_projects

        with open('data/publish.json') as json_file:
            self.data_publish = json.load(json_file)
        self.publish = self.data_publish

        with open('data/exp.json') as json_file:
            self.data_exp = json.load(json_file)
        self.exp = self.data_exp

        with open('data/artwork.json') as json_file:
            self.data_artwork = json.load(json_file)
        self.artwork = self.data_artwork

        with open('data/skills.json') as json_file:
            self.data_skills = json.load(json_file)
        self.skills = self.data_skills

        self.email = self.data_desc['email']
        self.phone = self.data_desc['phone']
        self.address = self.data_desc['address']

        with open('data/links.json') as json_file:
            self.data_links = json.load(json_file)
        self.links = self.data_links

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
            "proj_list"     : self.projects,
            "artwork"       : self.artwork,
            "edu"           : self.divide(self.edu,2),
            "exp"           : self.divide(self.exp,4),
            "publish"       : self.publish,
            "email"         : self.email,
            "coffeecoders"  : self.coffeecoders
        }
        return resumedata

    def editdata(self):
        resumedata = {
            "data_description"      : self.data_desc,
            "data_artwork"          : self.data_artwork,
            "data_edu"              : self.data_edu,
            "data_exp"              : self.data_exp,
            "data_jobs"             : self.data_jobs,
            "data_links"            : self.data_links,
            "data_projects"         : self.data_projects,
            "data_publish"          : self.data_publish,
            "data_skills"           : self.data_skills,
            "data_coffeecoders"     : self.coffeecoders
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
