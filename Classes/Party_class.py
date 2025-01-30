class Party:
     """Encapsulate attribute related to the party class
     """
     def __init__(self, P_name):
          self._P_name = P_name
          self._total_selected_votes = 0
          self._total_votes = 0
          self._members = []
        
     def __str__(self):
       members_str = "\n".join(str(self.member) for self.member in self._members)
       return f'{self.P_name}\n Number of parliament seats that were ach'
     

     def add_vote_of_selected(self, votes):
        self._total_selected_votes += votes
     
     def calculate_avg_vote(self):
          return self._total_votes / len(self._members) if len(self._members) >0 else 0
    

     def add_member_party(self, member):
          if member not in self._members:
             self._members.append(member)