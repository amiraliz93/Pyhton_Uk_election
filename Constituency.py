class Constituency:
    def __init__(self, constituency_name, region_name, country_name, Constituency_type, total_vote):
        self.C_name = constituency_name
        self.region_name = region_name
        self.country_name = country_name
        self.C_type =  Constituency_type
        self.total_vote = total_vote
        self.candidate = []
        self.discreption = {'Constituency name': self.C_name, 'Region name':self.region_name,'Constituency type':self.C_type}

    def candidate_information(self):
        print(self.candidate)
    
    def get_description(self):
         return self.discreption
    
    def add_member(self, mp):
        self.candidate.append(mp)
    
    @staticmethod
    def list_of_contituency_by_region(consitituencies_list, region):
        return [item.C_name for item in consitituencies_list.values() if item.region_name.lower() == region.lower() ]
    

    def display_constituency_information(self):
        print(f"Constituency Name: {self.C_name}")
        print(f"Region Name: {self.region_name}")
        print(f"Country: {self.country_name}")
        print(f"Type: {self.C_type}")
        print("Candidates:")
        print(self.candidate[0].get_candidate_summary())
            #print(f"  - {candidate.candidate_full_name} - Candidate Party: ({candidate.party} total Vote: {candidate.v})")

    def get_candidate_by_name(self, surname):
        for candidate in self.candidates:
            if candidate.candidate_surname.lower() == surname.lower():
                return candidate
        return None