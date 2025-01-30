

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
        self._C_name = constituency_name
        self._region_name = region_name
        self._country_name = country_name
        self._total_voted = int(total_voted if total_voted is not None else 0)
        self._totalvoters = total_voters
        self._candidate = []
        
        self._discreption = {'Constituency name': self._C_name, 'Region name':self._region_name, 'Total Voted':self._totalvoters}
        
        Constituency.constituency_list.append(self._C_name)

        @property
        def C_name(self):
            return self._C_name

        @property
        def region_name(self):
            return self._region_name
        @property
        def country_name(self):
            return self._country_name
        
        @property
        def total_voted(self):
            return self._total_voted
        
        @property
        def discreption(self):
            return self._discreption
        
        
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
        self._candidate.append(mp)
    

    @staticmethod
    def list_of_contituency_by_region(consitituencies_list: dict, region):
        """function to list constituency by region

    Args:
        consitituencies_list (dict): dictionary of constituencies
        region (str): name of region

    Returns:
        list: list of constituency names in the specified region
        """
        return [item._C_name for item in consitituencies_list.values() if item._region_name.lower() == region.lower() ]
    
    def display_candidate_info(self):
        percentage_vote = (self.candidate[0].votes /self.total_voted) * 100
        print("*" * 50)
        print(f""" Constituency Name: {self.C_name},
            \tCandidates who selected: \t {self.candidate[0].get_candidate_summary()},
            \t\tthe total voted is {self.total_voted} and winner voted is {self.candidate[0].votes},
            \t\t\tPercentage winner vote: {round(percentage_vote, 2)} """)
        print("*" * 50)
            #print(f"  - {candidate.candidate_full_name} - Candidate Party: ({candidate.party} total Vote: {candidate.v})")


