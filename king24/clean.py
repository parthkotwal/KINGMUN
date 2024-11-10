import pandas as pd
import numpy as np
class Clean2024:
    def __init__(self) -> None:
        self.del_cleaned= False

    def clean_del(self):
        self.del_df = pd.read_csv("king24/export_331_delegates.csv")
        self.del_df = self.del_df[['firstName','lastName','school','grade','assignedCommittee']][self.del_df['grade'] < 12]
        comm_to_body = {
            'H-GC':'ECOSOC',
            'COO':'Specialized',
            'OP-HCC':'Crisis',   
            'AD-HOC':'Specialized',
            'OSHA':'ECOSOC',
            'FAO':'Principal',
            'ICAO':'ECOSOC',
            'IOC':'Principal',
            'TRUSTEES':'Principal',
            'DOJ':'Specialized',
            'F-GA':'Principal',
            'ABA':'ECOSOC',
            'HCC':'Crisis',
            'FCC':'Crisis'
        }
        self.del_df['assignedCommittee'] = self.del_df['assignedCommittee'].map(comm_to_body)

        schoolfix = {
            'summit public schools-sierra':'Summit Public Schools: Sierra',
            'redmond high school':'Redmond High School',
            'Newport':'Newport High School',
            'bellevue high school':'Bellevue High School',
            'interlake':'Interlake High School',
            'Seattle Prep':'Seattle Preparatory School',
            'Overlake School':'The Overlake School',
            'Tesla STEM':'Tesla STEM High School', 
            'Cleveland High School STEM':'Grover Cleveland STEM High School',
            'North Creek Highschool':'North Creek High School', 
            'Newport High':'Newport High School',
            'Forest Ridge School':'Forest Ridge School of the Sacred Heart',
            'Newport Senior High School':'Newport High School',
            'Newport Highschool':'Newport High School',
            'Eastlake':'Eastlake High School', 
            'Evergreen Middle School (Redmond)':'Evergreen High School',
            'Newport High School (Bellevue, WA)':'Newport High School',
            'Newport high school':'Newport High School',
            'Henry M. Jackson':'Henry M. Jackson High School',
            'Inglemoor Highschool':'Inglemoor High School', 
            'Lake Washington High':'Lake Washington High School',
            'Green River running start':'Green River College',
            'Liberty':'Liberty High School'
        }
        self.del_df['school'] = self.del_df['school'].replace(schoolfix)
        
        self.del_df = pd.read_csv("king24/KING 24 Delegates.csv")
        self.del_cleaned = True
        return self.del_df
    
    def clean_adv(self):
        # if self.del_cleaned:
        #     schoolreps = {}
        #     for item, row in self.del_df.iterrows():
        #         if row['school'] in schoolreps:
        #             schoolreps[row['school']] += 1
        #         else:
        #             schoolreps[row['school']] = 1

        #     self.adv_df = pd.DataFrame(list(schoolreps.items()), columns=['School', 'Num. of Dels'])
        #     print(sum(schoolreps.values()))

        #     self.adv_df.to_csv("king24/KING 24 Delegations.csv",index=False)
        #     return self.adv_df
        # else:
        #     print("Clean dels file first!")

        df = pd.read_csv("king24/export_331_delegates.csv")
        df = df[['firstName','lastName','school']]
        schoolfix = {
            'summit public schools-sierra':'Summit Public Schools: Sierra',
            'redmond high school':'Redmond High School',
            'Newport':'Newport High School',
            'bellevue high school':'Bellevue High School',
            'interlake':'Interlake High School',
            'Seattle Prep':'Seattle Preparatory School',
            'Overlake School':'The Overlake School',
            'Tesla STEM':'Tesla STEM High School', 
            'Cleveland High School STEM':'Grover Cleveland STEM High School',
            'North Creek Highschool':'North Creek High School', 
            'Newport High':'Newport High School',
            'Forest Ridge School':'Forest Ridge School of the Sacred Heart',
            'Newport Senior High School':'Newport High School',
            'Newport Highschool':'Newport High School',
            'Eastlake':'Eastlake High School', 
            'Evergreen Middle School (Redmond)':'Evergreen High School',
            'Newport High School (Bellevue, WA)':'Newport High School',
            'Newport high school':'Newport High School',
            'Henry M. Jackson':'Henry M. Jackson High School',
            'Inglemoor Highschool':'Inglemoor High School', 
            'Lake Washington High':'Lake Washington High School',
            'Green River running start':'Green River College',
            'Liberty':'Liberty High School',
            'liberty high school':'Liberty High School'
        }
        df['school'] = df['school'].replace(schoolfix)

        schoolreps = {}
        for item, row in df.iterrows():
            if row['school'] in schoolreps:
                schoolreps[row['school']] += 1
            else:
                schoolreps[row['school']] = 1

        self.adv_df = pd.DataFrame(list(schoolreps.items()), columns=['School', 'Num. of Dels'])

        self.adv_df.to_csv("king24/KING 24 Delegations.csv",index=False)
        return self.adv_df

cleaner2022 = Clean2024()
dele = cleaner2022.clean_del()
adv = cleaner2022.clean_adv()
# print(cleaner2022.adv_df)