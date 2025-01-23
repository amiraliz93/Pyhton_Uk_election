
class Constituency:
    """class to encampsulate details for constituency attributes

    """
    constituency_list = [] # a list of constituency name

    def __init__(self, constituency_name, region_name, country_name, total_voted, total_voters):
        """
        Summary: initilise information to object

        Args:
            constituency_name (str): name of different constituency
            region_name (str): name of different region
            country_name (str): name of different country
            total_voted (int): accumulate of votes 
            total_voters (int): total of voters
        """
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
        """
        function to display constituency information 
        """

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
        """function to list constituency by region

        Args:
            consitituencies_list (int): list based on region
            region (str): name of region

        Returns:
            _type_: int 
        """
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