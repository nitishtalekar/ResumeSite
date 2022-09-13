from datetime import date
import json
import requests

class LoadData:
    def __init__(self):
        self.data_sheet = 'https://sheetdb.io/api/v1/qp4aa41d02dmu'
        self.art_sheet = 'https://sheetdb.io/api/v1/bw3z9yxxwo7rw'
    def add_srno(self,data):
        x = len(data)
        for i in data:
            i['srno'] = str(x)
            x -= 1
        return data
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
            data = self.add_srno(data)
        fin_data = json.dumps(data)
        print("DONE")
        self.write_data(fin_data,name)
            
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

        