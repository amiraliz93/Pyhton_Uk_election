
class MP:
    """encapsulate MP attribute
    """
    def __init__(self, f_name, l_name, gender, party, votes):
        self._f_name = f_name
        self._l_name = l_name
        self._candidate_full_name = (self.f_name) + ' ' +(self.l_name)
        self._party = party
        self._votes = int(votes if votes is not None else 0)
        self._gender = gender

    def __str__(self): # need to change
        return f"{self.f_name}  {self.l_name},\nParty: {self.party}"

    def get_candidate_summary(self):
        return f"""
        'Full Name': {self._candidate_full_name}, 
        'gender': {self._gender}
        'Party': {self._party},  
        'Votes': {self._votes},
        'Gender': {self._gender}"""
