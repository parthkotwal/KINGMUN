import pandas as pd

class Clean2023:
    def __init__(self) -> None:
        self.del_cleaned = False

    def clean_del(self):
        self.del_df = pd.read_csv("king23/KING 23 Delegates.csv")
        self.del_df = self.del_df[self.del_df['grade'] < 11]

        schoolfix = {
            'Hazen Highschool':'Hazen High School',
            'Woodinville HS':'Woodinville High School',
            'Hanford HS':'Hanford High School',
            'Summit Sierra High School':'Summit Public Schools: Sierra',
            'Kentwood High School MUN':'Kentwood High School',
            'the Downtown School':'The Downtown School',
            'Inglemoor high schol':'Inglemoor High School', 
            'Enumclaw Highschool':'Enumclaw High School',
            'st francis of assisi school':'St. Francis of Assisi School',
            'lake washington high school':'Lake Washington High School', 
            'Hanford':'Hanford High School', 
            'International community school':'International Community School', 
            'Inglemoor':'Inglemoor High School',
            'Lake Washington Highshcool':'Lake Washington High School'
        }
        self.del_df['school'] = self.del_df['school'].replace(schoolfix)

        self.del_df.to_csv("king23/KING 23 Delegates.csv", index=False)
        self.del_cleaned = True
        return self.del_df
    
    def clean_adv(self):
        df = pd.read_csv("king23/KING23 Del Data  - Sheet1.csv")
        
        df = df[['firstName','lastName','school']]

        schoolfix = {
            'Hazen Highschool':'Hazen High School',
            'Woodinville HS':'Woodinville High School',
            'Hanford HS':'Hanford High School',
            'Summit Sierra High School':'Summit Public Schools: Sierra',
            'Kentwood High School MUN':'Kentwood High School',
            'the Downtown School':'The Downtown School',
            'Inglemoor high schol':'Inglemoor High School', 
            'Enumclaw Highschool':'Enumclaw High School',
            'st francis of assisi school':'St. Francis of Assisi School',
            'lake washington high school':'Lake Washington High School', 
            'Hanford':'Hanford High School', 
            'International community school':'International Community School', 
            'Inglemoor':'Inglemoor High School',
            'Lake Washington Highshcool':'Lake Washington High School'
        }
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

cleaner2023 = Clean2023()
dele = cleaner2023.clean_del()
adb = cleaner2023.clean_adv()
print(adb)