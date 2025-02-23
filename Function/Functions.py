from . import utility
import csv
from  Classes.Constituency_class import Constituency
from  Classes.MP_class import MP
from  Classes.Party_class import Party



class VotingAnalysis:
    def __init__(self, file_path):
        self._file_path = file_path
        self._constituencies_info = {}
        self._party_info = {}
        self._database = self.read_file()
        self.initialize_data()
   


    def display_menu(self):
        menu_option =  {
            '1': self.sub_menu,
            '2': self.total_vote_each_party,
            '3': self.extract_party_static,
            '4': self.get_candidat_information,
            '5': self.find_MP_or_constituency,
            '6': self.exit_program
            
        }
        while True:
            print("\n--- Voting Analysis Program ---")
            print("1. View a Constituency Information")
            print("2. Display Total Votes for a Party")
            print("3. View Party Information")
            print("4. View Candidate information")
            print('5. Find out who your MP is')
            print("6. Exit")

            choice = self._validate_input("Enter your choice: (1-6):", 1, 6)      
            action = menu_option.get(str(choice))  # convert choice to string
            if action:
                action()
            else:
                print("Invalid choice. Please select a valid option.")

   

    def read_file(self):   
            """read data from csv file and store in a list
            Args:
                file_path (csv): initial dataset

            Returns:
                list: list of rows 
            """
            row_data = []
            try:
                    with open(self._file_path, 'r', encoding='latin1') as f:
                        next(f)
                        read = csv.DictReader(f)
                        for row in read:
                            row_data.append(row)
            except Exception as e:
                if e.__class__ == FileNotFoundError:
                    print(f" {utility.color_red}Error: File {utility.color_reset} '{self._file_path}' not found.") 
                    return []    
                else:
                    print(f"An error occurred: {e}")
                    return []
            return row_data


    def initialize_data(self):
            """Create object from classes to encapsulate data
            Args:
                database (Dictionary): consis of list of row data
            Returns:
                return list: of dictionary of objects from Party and Constituency classes_
            """
            # low to get each row from dataset
            for row in self._database:
                contituencies_name  = row['Constituency name']
                country = row["Country name"]
                region = row['Region name']
                first_name = row['Member first name']
                last_name = row['Member surname']
                gender = row['Member gender']
                party = row['First party']
                electotal  = row["Electorate"]
                votes_of_winner = self.add_votes(row, party)
                #total_vote_of_party = sum(int(row[party].replace(',','') for each_party in party_columns))
                
                total_voted = int(row['Valid votes'].replace(",", '')) + int(row['Invalid votes'].replace(",", ''))
                # votes = row.get(s_party, '0').replace(',', '')
                mp = MP(first_name, last_name,gender, party, votes_of_winner)
                # create objects from constituency class 
                if contituencies_name not in self._constituencies_info:
                    self._constituencies_info[contituencies_name] = Constituency(contituencies_name, region, country, total_voted, electotal)
                    self._constituencies_info[contituencies_name].add_member(mp)

                if party not in self._party_info:
                    self._party_info[party] = Party(party )
                self._party_info[party].add_vote_of_selected(votes_of_winner)
                self._party_info[party].add_member_party(mp._candidate_full_name)


    def add_votes(self, row, party):
            """calculate total vote for winner party for each constituency
            """
            try:

                if party in ['Ind', 'Spk', 'TUV']:
                        return int( row['Independent winner vote'].replace(',', ''))
                else:
                            return int( row[party].replace(',', '')) 
            except (KeyError, ValueError):
                print(f"Invalid data for party: {party}")
                return 0


    def get_candidat_information(self):

                candidate_name = input('type a candidate full name: ').lower().strip()
                found = False
                for value in self.consitituencies_info.values():
                    #print(value)
                    if  value.candidate[0].candidate_full_name.lower() == candidate_name: 
                        #print( value.candidate[0].get_candidate_summary())
                        print(value.candidate[0])
                        found = True
                        break
                if not found:
                        print(' the name not found')

    def total_vote_each_party(self, party_name= None):
            """get total vote for each party

            Args:
                data (list of dictionary): return number of total vote for given party
            """
            
            if party_name is None:
                party_columns = ['Constitution:', 'Labour Party', 'Liberal Democrats', 'RUK', 'Green', 'Scottish National Party (SNP)', 'PC', 'Democratic Unionist Party (DUP)', 'Sinn Féin (SF)', 'Social Democratic and Labour Party (SDLP)', 'Ulster Unionist Party (UUP)', 'APNI', "Of which other winner"]
                while True:
                    print('\n'.join([f' {count}-\t {i}' for count, i in enumerate(party_columns, 1)]))
                    try: 
                        p_name = int(input(f' select the number of the party form the list (1- {len(party_columns)}) ')) 
                        p_name = self._vaidate_input('select the number of the party form the list (1- {len(party_columns)', 1, len(party_columns))
                        if  0 < p_name <= len(party_columns):
                            party = party_columns[p_name - 1]
                            total_vote = 0
                            for row in self._database:
                                if party in row:
                                    total_vote += int(row[party].replace(",", '') )
                            print("*" * 50)
                            print(f" The total vote for the party: s{party} \n \t is: {total_vote} ")
                            print("*" * 50)
                            break
                        else:
                            print(f"Invalid input. Please enter a number in the range (1 - {len(party_columns)}).")

                    except ValueError:
                            print("Invalid input. Please enter a valid number.")
            else:
                for row in self._database:
                    if party_name in row:
                        total_vote += int(row[party].replace(",", '') )
                    return total_vote

    def extract_party_static(self):
            party_statics = {}
            party_list = ['Con', 'Lab', 'LD', 'RUK', 'Green', 'SNP', 'PC', 'DUP', 'SF', 'SDLP', 'UUP', 'APNI', "Of which other winner"]
            print("".join([f"{count}:, {i}\n" for count , i in party_list]))
            p_name = int(input('choose a number of the party'))
            if 0< p_name <= len(party_list):  
                for obj in self._party_info.values:
                    if obj.name.lower() == p_name.lower():
                        party_statics[obj.name] = {
                            'total_vote_of_selected': obj.total_selected_votes,
                            'average_vote_for_this_Party': obj.calculate_avg_vote(),
                            'Number_of_member_list': len(obj.members),
                            'total_vote_for_party':  self.total_vote_each_party(obj.name),
                            'Member_List': obj.members
                        }   
                return party_statics
            else:
                print("invalid input")  

    def sub_menu(self):
            while True:
                try:
                    print(" ---- Choose your option ----")
                    print("1. View Constituency list")
                    print("2. Know your constituency name")
                    print("3. Find your constituency based on your region and country")
                    print("4. Get back to main menu")
                    print("5. Exit program")

                    choice = self._validate_input("Enter your choice (1, 2, 3, or 4 to exit): ",1, 4)
                    #input("Enter your choice (1, 2, 3, or 4 to exit): ")
                    match str(choice):
                        case "1":
                                    print( "".join([f" _____ \n {count}\t: {i} \n"for count, i in enumerate(Constituency.constituency_list, 1)]))
                        case "2":
                                    self.constituncy_information()
                        case "3":
                                    self.find_MP_or_constituency(order=1)
                        case "4":
                                    break
                        case '5':
                                    self.exit_program()
                        case _:
                            print(f"Invalid choice \"{choice}\" is not an option. Please choose carfully!")
                except Exception as e:
                    print(f'the error is {e}')

    def get_candidate_by_name(self, surname):
        return self._constituencies_info.get(surname.lower(), None)


    def constituncy_information(self):
            """ for option one from menue
            Args:
                contituencies_info (Dicts): dictionary contain list of objects from contituencies class
            Raises:
                ValueError: face of invalid input
            Returns:
                _type_: name of the contituency 
            """
            while True:
                try:    
                    print("*" * 50 , "\n", " Choose Your Option ")
                    name = input('what consitituency name do you want to see: ').lower()
                    if not name.replace(' ', '').isalpha():
                        raise ValueError('Not Valid input, Only alphabet please')
                    found = False
                    #print(name)
                    for value in self._constituencies_info.values(): 
                        #print(value.C_name.lower())
                        if value.C_name.lower() == name:
                                print(value.display_constituncy_info())
                                found = True
                    if not found:
                        print("Region not found, please try again.")
            
                            # Validate user input for continuation

                        
                    if not self._ask_to_exit():
                                exit()  
                except Exception as e:
                     if e.__class__ == ValueError:
                          print(f" {utility.color_red}Error: Value erro  .")            


    def find_MP_or_constituency(self,order=0):
            # show list of the region
            # first show the country name list and let user choose 
            # choose region
            # base on region show list of the constituncy
            # order value define this function tent to work for which oprion menu for option 5 or option 3. Find your constituency based on your region and country
            list_of_country = ["Wales", "Scotland", "England", "Northern Ireland"]
            region_list = ["East Midlands", "East of England", "London", "North East", "North West", "South East", "South West", "West Midlands", "Yorkshire and The Humber"]
            print(" List Of the Country ")
            count = 1
            for i in list_of_country:
                print(count ,"\t:", i)
                count += 1
            #print("\n".join([f"{count}\t: {country}" for count, country in enumerate(list_of_country, 1)]))

            country_input = str(input('Enter the name of the country: ').lower())
            assert country_input.isalpha(), f"the input is not alphabet"
            if country_input == "england":
                print("choose one of the Region")
                print("\n".join([f" {count} \t: {i}" for count, i in enumerate(region_list, 1)]))

                region_input = str(input('Enter the name of the region: ').lower())
                assert country_input.isalpha(), f"the input is not alphabet"
                list = Constituency.list_of_contituency_by_region(self._constituencies_info, region_input)
                print("".join([f" {count}:\t {i} \n" for count , i  in enumerate(list,1)]))
                while True:
                    try:
                        C_input = int(input(f'Enter the number of constituency: in a range (1 -{len(list)}): '))
                        constituency_name = list[C_input - 1]
                        if order == 0: 
                            self._constituencies_info[constituency_name].display_candidate_info()
                        else:
                            self._constituencies_info[constituency_name].display_constituncy_info() 
                        if not self._ask_to_exit:
                            exit()    
                        else:
                            break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    except IndexError:
                        print(f"Invalid input. Please enter a number in the range (1 - {len(list)}).")

            elif country_input == "wales":
                list =  Constituency.list_of_contituency_by_region(self._constituencies_info, country_input)
                print("\n choose the name of the name of your constituency from the list \n")
                print("".join([f" {count}:\t {i} \n" for count , i  in enumerate(list,1)]))
                while True:
                    try:
                        C_input = int(input(f'Enter the number of constituency: in a range (1 -{len(list)}): '))
                        constituency_name = list[C_input - 1]
                        if order == 0:
                            self._constituencies_info[constituency_name].display_candidate_info()
                        else:
                            self._constituencies_info[constituency_name].display_constituncy_info()
                        if not self._ask_to_exit():
                            exit()    
                        else:
                            break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    except IndexError:
                        print(f"Invalid input. Please enter a number in the range (1 - {len(list)}).")
            
            elif country_input == "scotland":
                list =  Constituency.list_of_contituency_by_region(self._constituencies_info, country_input)
                print("\n choose the name of the name of your constituency from the list \n")
                print("".join([f" {count}:\t {i} \n" for count , i  in enumerate(list,1)]))
                while True:
                    try:
                        C_input = int(input(f'Enter the number of constituency: in a range (1 -{len(list)}): '))
                        constituency_name = list[C_input - 1]
                        if order == 0:
                            self._constituencies_info[constituency_name].display_candidate_info()
                        else:
                            self._constituencies_info[constituency_name].display_constituncy_info()
                        if not self._ask_to_exit():
                            exit()    
                        else:
                            break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    except IndexError:
                        print(f"Invalid input. Please enter a number in the range (1 - {len(list)}).")

            elif country_input == "northern ireland":
                list =  Constituency.list_of_contituency_by_region(self._constituencies_info, country_input)
                print("\n choose the name of the name of your constituency from the list \n")
                print("".join([f" {count}:\t {i} \n" for count , i  in enumerate(list,1)]))
                while True:
                    try:
                        C_input = int(input(f'Enter the number of constituency: in a range (1 -{len(list)}): '))
                        constituency_name = list[C_input - 1]
                        if order == 0:
                            self._constituencies_info[constituency_name].display_candidate_info()
                        else:
                            self._constituencies_info[constituency_name].display_constituncy_info()
                        if not self._ask_to_exit():
                            exit()    
                        else:
                            break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    except IndexError:
                        print(f"Invalid input. Please enter a number in the range (1 - {len(list)}).")
            else:
                Constituency.list_of_contituency_by_region(self._constituencies_info, country_input)


    def exit_program(self):
            print("Exit Program, Goodbay!")
            exit()
    
    def _validate_input(self, prompt, min_val, max_val):
         
         while True:
            try:
                    choice = int(input(prompt))

                    if  min_val <= choice <= max_val:
                            return choice 

                    else:
                         print(f" the {choice} is not valid. Please enter a number between {min_val} and {max_val}.")
            except ValueError:
                 print("Invalid input. Please enter a number!")

    def _ask_to_exit(self):
            while True:
                
                input_user = input(" To get back to main menu type Y or N to exit program (Y/N): ").lower()
                match input_user:
                    case 'y':
                        return True
                    case "n":
                        print("Exiting the program. Goodbye!")
                        return False
                    case _:
                        print("Inalid Value please type Y or N")

