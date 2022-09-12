    
from datetime import date
import json
import requests

class LoadData:
    def __init__(self):
        self.data_sheet = 'https://sheetdb.io/api/v1/qp4aa41d02dmu'
        self.art_sheet = 'https://sheetdb.io/api/v1/bw3z9yxxwo7rw'
    
    def write_data(self,data,file):
        form_data = json.loads(data)
        final_data = json.dumps(form_data, indent=4)
        file_name = "data/" + file + ".json"
        with open(file_name, "w") as outfile:
            outfile.write(final_data)
                
    def update_data(self,name,link):
        res = requests.get(link)
        data = json.loads(res.text)
        if name == 'jobs':
            for i in data:
                i['desc'] = i['desc'].split('|')
        elif name == 'projects' or name == 'artwork':
            x = len(data)
            for i in data:
                i['srno'] = str(x)
                x -= 1
        fin_data = json.dumps(data)
        print("DONE")
        self.write_data(fin_data,name)
        
    def load_all(self):
        data_dict = {
            # 'artwork':'https://sheetdb.io/api/v1/bw3z9yxxwo7rw',
            'jobs':'https://sheetdb.io/api/v1/qp4aa41d02dmu',
            'exp':'https://sheetdb.io/api/v1/qp4aa41d02dmu?sheet=Exp',
            'projects':'https://sheetdb.io/api/v1/qp4aa41d02dmu?sheet=Projects',
            'edu':'https://sheetdb.io/api/v1/qp4aa41d02dmu?sheet=Edu'
        }
        for i in data_dict:
            self.update_data(i,data_dict[i])
            
    def load_jobs(self):
        self.update_data('jobs',self.data_sheet + '?sheet=Jobs')
        
    def load_exp(self):
        self.update_data('exp',self.data_sheet + '?sheet=Exp')
        
    def load_projects(self):
        self.update_data('projects',self.data_sheet +'?sheet=Projects')
    
    def load_edu(self):
        self.update_data('edu',self.data_sheet +'?sheet=Edu')
        
    def load_art(self):
        self.update_data('artwork',self.art_sheet)

        