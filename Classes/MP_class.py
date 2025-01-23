
class MP:
    """encapsulate MP attribute
    """
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
        'Full Name': {self.candidate_full_name}, 
        'gender': {self.gender}
        'Party': {self.party},  
        'Votes': {self.votes},
        'Gender': {self.gender}"""
