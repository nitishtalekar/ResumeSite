from datetime import date

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
        self.edu = [
            {
                "university":"North Carolina State University",
                "location":"USA",
                "degree":"Master of Computer Science",
                "timeline":"August 2021 – Present",
                "courses":", ".join(["Automated Learning and Data Analysis",
                            "Design and Analysis of Algorithms",
                            "Internet Protocols"]),
                "gpa": "4.0/4.0"
            },
            {
                "university":"University of Mumbai",
                "location":"India",
                "degree":"Bachelor of Computer Engineering",
                "timeline":"June 2016 – October 2020",
                "courses": ", ".join(["Machine Learning","Data Structures", 
                            "Algorithms"," Operating Systems",
                            "Human Machine Interaction",
                            "Database Management Systems",
                            "Compiler Construction",
                            "Computer Organization",
                            "Software Engineering"]),
                "gpa": "8.96/10.0"
            },
            {
                "university":"Maharashtra State Board",
                "location":"India",
                "degree":"Higher Secondary School Certificate",
                "timeline":"June 2014 – May 2016",
                "courses": ", ".join(["Sorftware Science",
                            "Hardware Science",
                            "Applied Mathematics",
                            "Applied Chemistry",
                            "Applied Physics"
                            ]),
                "gpa": "88/100"
            },
            {
                "university":"Maharashtra State Board",
                "location":"India",
                "degree":"Secondary School Certificate",
                "timeline":"July 2002 – March 2014",
                "courses": ", ".join(["Science",
                            "Mathematics",
                            "History",
                            "Geography",
                            "ICT",
                            "English",
                            "Hindi",
                            "Marathi",
                            "Hindi",
                            "Sanskrit"
                            ]),
                "gpa": "94.8/100"
            }
        ]
        self.jobs = [
            {
                "title": "Developer",
                "title2": "Front End",
                "company":"Depronto Infotech ",
                "desc": [
                    "Designed user interface for online platform geared towards automating reward systems for insurance agents at HDFC Bank branches. Front-end functionalities were generated using JavaScript, Ajax, and jQuery.",
                    "Assisted in developing mailing interface directed towards broadcasting notices to Axis bank employees via the web-platform."
                ],
                "timeline": "October 2020 – March 2021"
            },
            {
                "title": "Intern",
                "title2": "Technology Developer",
                "company": "Naman Angels India Foundation",
                "desc":[
                    "Planned and launched a web platform which allows investors to interact with and invest in start-ups of their preference, and startups to display their value to investors.",
                    "Developed front-end and back-end technologies for the web-platform. Designed the user interface using HTML, CSS and PHP and maintained databases with help of MySQL."
                ],
                "timeline": "September 2018 – March 2019"
            }
        ]
        self.projects = [
            {
                "name": "Peer-to-Peer File System",
                "topic": "Socket Programming",
                "timeline": "November 2021",
                "desc": "Development of a P2P File distribution system for file transfers using TCP connection. Implementation of a central server for tracking files.",
                "link": "",
                "github" : "https://github.com/nitishtalekar/CSC-573-InternetProtocols/tree/main/P2P-CI",
                "img": "proj/ml.png",
                "lang": "Python, Socket Programming"
            },
            {
                "name": "Prediction of Rainfall",
                "topic": "Machine Learning",
                "timeline": "November 2021",
                "desc": "Construction of a stacked model to predict rainfall for the next day based on wether station data. Implemented stacking of base models and feature reduction.",
                "link": "",
                "github" : "https://github.ncsu.edu/uchhapr/engr-ALDA-fall2021-P27",
                "img": "proj/ml.png",
                "lang": "Python, Sci-Kit learn, Tensorflow"
            },
            {
                "name": "Japanese - English Translator",
                "topic": "Natural Language Processsing",
                "timeline": "March 2020",
                "desc": "Implemented natural language processing techniques to translate simple Japanese sentences to English text. Construction of deep learning model using POS tagging.",
                "link": "",
                "github" : "",
                "img": "proj/ml.png",
                "lang": "Python, Sci-Kit learn, Tensorflow"
            },
            {
                "name": "Predictive Model Comparator Platform",
                "topic": "Machine Learning",
                "timeline": "June 2020",
                "desc": "Comparison of predictive classification models on the basis of accuracy and efficiency for a given dataset using different classification techniques. Creation of web platform using Django.",
                "link": "http://coffeecoders.pythonanywhere.com/classifier/",
                "github" : "",
                "img": "proj/ml.png",
                "lang": "Python, Django, Sci-Kit learn, Tensorflow"
            },
            {
                "name": "Institute Feedback System",
                "topic": "Web Development",
                "timeline": "April 2020",
                "desc": "Construction of a web-based feedback system for the Institute with analysis of feedback. Recording and Analysis of Students’ feedback on curriculum and teachers. The system is being used by the institution. ",
                "link": "",
                "github" : "",
                "img": "proj/web.png",
                "lang": "PHP, JavaScript, HTML, Ajax"
            },
            {
                "name": "Crop Disease Detection and Diagnosis",
                "topic": "Deep Learning",
                "timeline": "March 2020",
                "desc": "Determination of underlying disease in crops from image input using Image Processing, Neural Networks and Classification techniques. Creation of web platform for effective use.",
                "link": "",
                "github" : "https://github.com/aayooush/CDDD",
                "img": "proj/ai.png",
                "lang": "Python, Tensorflow, Keras"
            },
            {
                "name": "Result Analysis",
                "topic": "Data Analysis",
                "timeline": "July 2019",
                "desc": "Analysis of Results of students at the institute and providing detailed reports based on observations in data. Design of GUI and an executable file for office use. The system is being used by the institution.",
                "link": "",
                "github" : "",
                "img": "proj/data.png",
                "lang": "Python, Pandas, Numpy, Tkinter"
            },
            {
                "name": "Chess Engine",
                "topic": "Machine Learning",
                "timeline": "March 2019",
                "desc": "Development of an algorithm to simulate human like thinking in the game of chess to play the best possible move using Decision tree and optimization techniques",
                "link": "",
                "github" : "",
                "img": "proj/ml.png",
                "lang": "Python, Tensorflow, Keras"
            }
        ]
        self.publish = [
            {
                "name":"A Comparative Study on Crop Disease Detection using Deep Learning Techniques",
                "publication": "International Research Journal of Engineering and Technology (IRJET) - Volume: 07 Issue: 05, May 2020",
                "timeline": "May 2020"
            }
        ]
        self.exp = [
            {
                "position":"Founder",
                "commitee": "CodeCell RGIT",
                "desc": "Founded Code Cell – a community of project developers and coding enthusiasts, with the participation of over 200 students. Organized City-level hackathon. Conducted seminars.",
                "timeline": "2019 - 2020"
            },
            {
                "position": "Lead Developer",
                "commitee": "Software Development Committee",
                "desc": "Lead cross functional teams on various software projects that helped the management and administration departments of the institution.",
                "timeline": "2019 - 2020"
            },
            {
                "position": "Editorial Secretary",
                "commitee": "ACM, CESS",
                "desc": "Managed database and documents for the standing committee. Edited and published monthly Newsletter and yearly Magazine.",
                "timeline": "2018 - 2020"
            },
            {
                "position": "Technical Secretary",
                "commitee": "Student Council",
                "desc": "Organized Technical inter-collegiate festival with a footfall of over 2000 participants. Supervised several technical workshops.",
                "timeline": "2018 - 2020"
            }
        ]
        self.artwork = [
            {
                "name": "Dive",
                "date": "2019",
                "img": "art/dive.png"
            },
            {
                "name": "Galaxy",
                "date": "2019",
                "img": "art/galaxy.png"
            },
            {
                "name": "Nebula",
                "date": "2020",
                "img": "art/nebula.png"
            },
            {
                "name": "Nebula",
                "date": "2020",
                "img": "art/nebula.png"
            },
            {
                "name": "Nebula",
                "date": "2020",
                "img": "art/nebula.png"
            },
            {
                "name": "Nebula",
                "date": "2020",
                "img": "art/nebula.png"
            }
        ]
        self.skills = {
                "non_technical":
                    ["Leadership",
                    "Project Management",
                    "Teamwork",
                    "Project Planning",
                    "Public Speaking",
                    "Technical Writing"
                    ],
                "technical":
                    ["Python",
                    "C",
                    "Java"
                    "Javascript",
                    "jQuery",
                    "HTML",
                    "CSS",
                    "MySQL",
                    "PHP",
                    "Ajax",
                    "Flask",
                    "Django"
                    ]
                }
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
        self.links = {
            "facebook":"https://www.facebook.com/nitish.talekar.9/",
            "linkedin":"https://www.linkedin.com/in/nitishtalekar/",
            "github":"https://github.com/nitishtalekar",
            "instagram":"https://www.instagram.com/nitishtalekar11/"
        }
        
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
        
        
        
        
        