class Party:
     """Encapsulate attribute related to the party class
     """
     def __init__(self, P_name):
          self.P_name = P_name
          self.total_selected_votes = 0
          self.total_votes = 0
          self.members = []
        
     def __str__(self):
       members_str = "\n".join(str(member) for member in self.members)
       return f'{self.P_name}\n Number of parliament seats that were ach'
     

     def add_vote_of_selected(self, votes):
        self.total_selected_votes += votes
     
     def calculate_avg_vote(self):
          return self.total_votes / len(self.members) if len(self.members) >0 else 0
    

     def add_member_party(self, member):
          if member not in self.members:
             self.members.append(member)