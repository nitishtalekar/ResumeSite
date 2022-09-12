# res = requests.get('https://sheetdb.io/api/v1/vlatsw8dwdq8h')
# print(res.text)
# print("hi")
    
from datetime import date
import json
import requests

class LoadData:
    def __init__(self):
        self.id = 0
    
    def write_data(self,data,file):
        form_data = json.loads(data)
        final_data = json.dumps(form_data, indent=4)
        # final_data = data
        file_name = "data/" + file + ".json"
        with open(file_name, "w") as outfile:
            outfile.write(final_data)
                
    def update_job_data(self):
        res = requests.get('https://sheetdb.io/api/v1/qp4aa41d02dmu')
        data = json.loads(res.text)
        for i in data:
            i['desc'] = i['desc'].split('|')
        fin_data = json.dumps(data)
        print(fin_data)
        self.write_data(fin_data,"jobs")
        
    def load_all(self):
        data_dict = {
            'artwork':'https://sheetdb.io/api/v1/bw3z9yxxwo7rw',
            'jobs':'https://sheetdb.io/api/v1/qp4aa41d02dmu',
            'exp':'https://sheetdb.io/api/v1/qp4aa41d02dmu?sheet=Exp',
            'projects':'https://sheetdb.io/api/v1/qp4aa41d02dmu?sheet=Projects',
            'edu':'https://sheetdb.io/api/v1/qp4aa41d02dmu?sheet=Edu'
        }
        self.update_job_data()
        
    def get_art(self):
        print('ART')

        