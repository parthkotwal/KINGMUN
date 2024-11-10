import pandas as pd

class Clean2022:
    def __init__(self) -> None:
        self.del_cleaned= False

    def clean_del(self):
        # self.del_df = pd.read_csv("king22/export_204_delegates (1).csv")
        # self.del_df = self.del_df[['firstName','lastName','school','grade','assignedCommittee']][self.del_df['grade'] < 10]
        # comm_to_body = {
        #     'CTC':'ECOSOC',
        #     'CORP CABINET':'Specialized',
        #     'OP-HCC':'Specialized',   
        #     'AACC':'Specialized',
        #     'CNGOS':'ECOSOC',
        #     'IMO':'Principal',
        #     'ARCTIC COUNCIL':'ECOSOC',
        #     'H-DISEC':'Principal',
        #     'UN-JIU':'Principal',
        #     'BILDER-BERG GROUP':'Specialized',
        #     'H-AFL-CIO':'Principal',
        #     'HLFCP':'ECOSOC'
        # }
        # self.del_df['assignedCommittee'] = self.del_df['assignedCommittee'].map(comm_to_body)
        self.del_df = pd.read_csv("king22/KING 22 Delegates.csv").drop("Unnamed: 0",axis=1)
        return self.del_df
    
    def clean_adv(self):
        df = pd.read_csv("king22/export_204_delegates (1).csv")
        df = df[['firstName','lastName','school']]
        schoolfix = {
            'Bellarmine Preparatory':'Bellarmine Preparatory School',
            'Inglemoor Highschool':'Inglemoor High School',
            'Roosevelt':'Roosevelt High School',
            'Inglemoor high school':'Inglemoor High School',
            'ics':'International Community School',
            'International Community school':'International Community School',
            'International School Bellevue':'International School',
            'Bellarmine':'Bellarmine Preparatory School'
        }
        
        df = df[['firstName','lastName','school']]

        df['school'] = df['school'].replace(schoolfix)
        schoolreps = {}
        for item, row in df.iterrows():
            if row['school'] in schoolreps:
                schoolreps[row['school']] += 1
            else:
                schoolreps[row['school']] = 1

        self.adv_df = pd.DataFrame(list(schoolreps.items()), columns=['School', 'Num. of Dels'])
        self.adv_df.to_csv("king22/KING 22 Delegations.csv",index=False)
        return self.adv_df


cleaner2022 = Clean2022()
dele = cleaner2022.clean_del()
adv = cleaner2022.clean_adv()
print(adv)