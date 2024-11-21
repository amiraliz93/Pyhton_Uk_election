
import csv

class MP:
    def __init__(self, f_name, l_name, gender, party, votes):
        self.f_name = f_name
        self.l_name = l_name
        self.candidate_full_name = (self.f_name) + ' ' +(self.l_name)
        self.party = party
        self.votes = votes if votes is not None else 0
        self.gender = gender
    def __str__(self): # need to change
        return f"{self.f_name}  {self.l_name},\nParty: {self.party},\nVotes: {self.votes},\nGender: {self.gender}"

    def get_candidate_summary(self):
        return {
            'Full Name': self.candidate_full_name,
            'Party': self.party,
            'Votes': self.votes,
            'Gender': self.gender
        }

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
          
     

def options_menu():
    print("\n--- Voting Analysis Program ---")
    print("1. View a Constituency Information")
    print("2. Display Total Votes for a Party")
    print("3. List all the constituencies by Region name ")
    print("4. View Party Information")
    print("5. View Candidate information")
    print('6. Find out who your MP is')
    print("7. Exit")


def read_file(file_path): 
        row_data = []
        try:
            with open(file_path, 'r', encoding='latin1') as f:
                next(f)
                next(f)
                read = csv.DictReader(f)
                unwanted_key = ['ONS ID', 'ONS region ID']
                #filtered_row = {key: row[key] for key in row if key not in ['ONS ID', 'ONS region ID']}
                for row in read:
                     for key in unwanted_key:
                        del row[key]
                     row_data.append(row)
                #any(row_data.append(row) for row in read)
                row_data = row_data[:-15]
        except FileNotFoundError:
            print('file not exit')
        return row_data