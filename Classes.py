


class MP:
    def __init__(self, f_name, l_name, gender, party, votes):
        self.f_name = f_name
        self.l_name = l_name
        self.candidate_full_name = (self.f_name) + ' ' +(self.l_name)
        self.party = party
        self.votes = int(votes if votes is not None else 0)
        self.gender = gender

    def __str__(self): # need to change
        return f"{self.f_name}  {self.l_name},\nParty: {self.party}"

    def get_candidate_summary(self):
        return f"""
        'Full Name': {self.candidate_full_name} , 
        'gender': {self.gender}
        'Party': {self.party}, 
        'Votes': {self.votes}, 
        'Gender': {self.gender}"""

class Party:
     def __init__(self, P_name):
          self.P_name = P_name
          self.total_selected_votes = 0
          self.total_votes = 0
          self.members = []
        
     def __str__(self):
       return f' {self.P_name} \n Number of parliament seats that were achieved {len(self.members)} \n Member: \n {self.members} '
     

     def add_vote_of_selected(self, votes):
        self.total_selected_votes += votes
     
     def calculate_avg_vote(self):
          self.total_votes / len(self.members) if len(self.members) >0 else 0


     def add_member_party(self, member):
          if member not in self.members:
            self.members.append(member)

class Constituency:

    constituency_list = []
    def __init__(self, constituency_name, region_name, country_name, total_voted, total_voters):

        self.C_name = constituency_name
        self.region_name = region_name
        self.country_name = country_name
        self.total_voted = int(total_voted if total_voted is not None else 0)
        self.totalvoters = total_voters
        self.candidate = []
        self.discreption = {'Constituency name': self.C_name, 'Region name':self.region_name, 'Total Voted':self.totalvoters}

        Constituency.constituency_list.append(self.C_name)
    def __str__(self):
        f" the name of constituency is {self.name}"

    def display_constituncy_info(self):
        print("*" * 50)
        print(f""" Constituency name: {self.C_name},
            \tRegion name: \t {self.region_name},
            \t\tTotal Voted: {self.totalvoters},
            \t\t\tSelected Candidate: {self.candidate[0].candidate_full_name} """)
        print("*" * 50)

    
    def add_member(self, mp):
        self.candidate.append(mp)
    

    @staticmethod
    def list_of_contituency_by_region(consitituencies_list, region):
        return [item.C_name for item in consitituencies_list.values() if item.region_name.lower() == region.lower() ]
    
    def display_candidate_info(self):
        percentage_vote = (self.candidate[0].votes /self.total_voted) * 100
        print("*" * 50)
        print(f""" Constituency Name: {self.C_name},
            \tCandidates who selected: \t {self.candidate[0].get_candidate_summary()},
            \t\tthe total voted is {self.total_voted} and winner voted is {self.candidate[0].votes},
            \t\t\tPercentage winner vote: {round(percentage_vote, 2)} """)
        print("*" * 50)
            #print(f"  - {candidate.candidate_full_name} - Candidate Party: ({candidate.party} total Vote: {candidate.v})")

    def get_candidate_by_name(self, surname):
        for candidate in self.candidates:
            if candidate.candidate_surname.lower() == surname.lower():
                return candidate
        return None