
import csv
from  Classes import Constituency, MP, Party


def options_menu():
    print("\n--- Voting Analysis Program ---")
    print("1. View a Constituency Information")
    print("2. Display Total Votes for a Party")
    print("3. List all the constituencies by Region name ")
    print("4. View Party Information")
    print("5. View Candidate information")
    print('6. Find out who your MP is')
    print("7. Exit")

def data_manage(database):
    """Create object from classes to encapsulate data

    Args:
        database (Dictionary): consis of list of row data

    Returns:
        return list: of dictionary of objects from Party and Constituency classes_
    """
    contituencies_info = {}
    party_info = {}
    #party_columns = ['Con', 'Lab', 'LD', 'RUK', 'Green', 'SNP', 'PC', 'DUP', 'SF', 'SDLP', 'UUP', 'APNI', "Of which other winner"]
    # low to get each row from dataset
    for row in database:
        contituencies_name  = row['Constituency name']
        country = row["Country name"]
        region = row['Region name']
        first_name = row['Member first name']
        last_name = row['Member surname']
        gender = row['Member gender']
        party = row['First party']
        votes_of_winner = add_votes(row, party)
        #total_vote_of_party = sum(int(row[party].replace(',','') for each_party in party_columns))
        
        total_voted = row['Valid votes'].replace(",", '') + row['Invalid votes'].replace(",", '')
        electotal  = row["Electorate"]
       # votes = row.get(s_party, '0').replace(',', '')

        mp = MP(first_name, last_name,gender, party, votes_of_winner)
        # create objects from constituency class 
        if contituencies_name not in contituencies_info:
            contituencies_info[contituencies_name] = Constituency(contituencies_name, region, country, total_voted, electotal)
            contituencies_info[contituencies_name].add_member(mp)


        if party not in party_info:
             party_info[party] = Party(party )
        party_info[party].add_vote_of_selected(votes_of_winner)
        party_info[party].add_member_party(mp.candidate_full_name)
    return contituencies_info, party_info

def total_vote_each_party(data):
    """get total vote for each party

    Args:
        data (list of dictionary): return number of total vote for given party
    """
    party_columns = ['Con', 'Lab', 'LD', 'RUK', 'Green', 'SNP', 'PC', 'DUP', 'SF', 'SDLP', 'UUP', 'APNI', "Of which other winner"]
    while True:
        print('\n'.join([f' {count}-\t {i}' for count, i in enumerate(party_columns, 1)]))
        try: 
            p_name = int(input(f' select the number of the party form the list (1- {len(party_columns)}) ')) 
            if  0 < p_name <= len(party_columns):
                party = party_columns[p_name - 1]
                total_vote = 0
                for row in data:
                    if party in row:
                        total_vote += int(row[party].replace(",", '') )
                print(f" the total vote for the party: {party} \n \t is: {total_vote} ")
                break
            else:
                print(f"Invalid input. Please enter a number in the range (1 - {len(party_columns)}).")
        except ValueError:
                print("Invalid input. Please enter a valid number.")

def get_candidat_information(consitituencies):

    candidate_name = input('type a candidate full name: ').lower().strip()
    found = False
    for value in consitituencies.values():
        #print(value)
        if  value.candidate[0].candidate_full_name.lower() == candidate_name: 
             #print( value.candidate[0].get_candidate_summary())
             print(value.candidate[0])
             found = True
             break
    if not found:
             print(' the name not found')


def add_votes(row, party):
        C_votes = 0
        if party in ['Ind', 'Spk', 'TUV']:
                C_votes = row['Independent winner vote'].replace(',', '')
        else:
                C_votes = row[party].replace(',', '')
        return int(C_votes)

def read_file(file_path):   
        row_data = []
        try:
            with open(file_path, 'r', encoding='latin1') as f:
                next(f)
                #next(f)
                read = csv.DictReader(f)
                #unwanted_key = ['ONS ID', 'ONS region ID']
                #filtered_row = {key: row[key] for key in row if key not in ['ONS ID', 'ONS region ID']}
                for row in read:
                   #  for key in unwanted_key:
                    #    del row[key]
                     row_data.append(row)
                #any(row_data.append(row) for row in read)
                row_data = row_data[:-15]
        except FileNotFoundError:
            print('file not exit')
        return row_data

# for option one from menue
def constituncy_information(contituencies_info):
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
            name = input('what consitituency name do you want to see: ').lower()
            if not name.replace(' ', '').isalpha():
                 raise ValueError('only alphabet please')
            found = False
            #print(name)
            for value in contituencies_info.values(): 
                #print(value.C_name.lower())
                if value.C_name.lower() == name:
                        print(value.get_description())
                        found = True
            if not found:
                 print("Region not found, please try again.")
    
                    # Validate user input for continuation
            while True:
                get_answer = input('\nDo you want to try another name? Answer Y or N (Y/N): ').lower()
                if get_answer == 'y':
                    break  # Valid input, continue to the next iteration of the main loop
                elif get_answer == 'n':
                    return False # Valid input, exit the function
                else:
                    print("Invalid input. Please enter 'Y' or 'N'.")
        except ValueError as e:
             print(e)

def find_your_MP(consitituencies):
    # show list of the region
    # first show the country name list and let user choose 
    # choose region
    # base on region show list of the constituncy
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
        list = Constituency.list_of_contituency_by_region(consitituencies, region_input)
        print("".join([f" {count}:\t {i} \n" for count , i  in enumerate(list,1)]))
        while True:
             try:
                C_input = int(input(f'Enter the number of constituency: in a range (1 -{len(list)}): '))
                constituency_name = list[C_input - 1]
                consitituencies[constituency_name].display_constituency_information()
                break
             except ValueError:
                  print("Invalid input. Please enter a number.")
             except IndexError:
                  print(f"Invalid input. Please enter a number in the range (1 - {len(list)}).")

    elif country_input == "wales":
        list =  Constituency.list_of_contituency_by_region(consitituencies, country_input)
        print("\n choose the name of the name of your constituency from the list \n")
        print("".join([f" {count}:\t {i} \n" for count , i  in enumerate(list,1)]))
        while True:
             try:
                C_input = int(input(f'Enter the number of constituency: in a range (1 -{len(list)}): '))
                constituency_name = list[C_input - 1]
                consitituencies[constituency_name].display_constituency_information()
                break
             except ValueError:
                  print("Invalid input. Please enter a number.")
             except IndexError:
                  print(f"Invalid input. Please enter a number in the range (1 - {len(list)}).")
    
    elif country_input == "scotland":
        list =  Constituency.list_of_contituency_by_region(consitituencies, country_input)
        print("\n choose the name of the name of your constituency from the list \n")
        print("".join([f" {count}:\t {i} \n" for count , i  in enumerate(list,1)]))
        while True:
             try:
                C_input = int(input(f'Enter the number of constituency: in a range (1 -{len(list)}): '))
                constituency_name = list[C_input - 1]
                consitituencies[constituency_name].display_constituency_information()
                break
             except ValueError:
                  print("Invalid input. Please enter a number.")
             except IndexError:
                  print(f"Invalid input. Please enter a number in the range (1 - {len(list)}).")

    elif country_input == "northern ireland":
        list =  Constituency.list_of_contituency_by_region(consitituencies, country_input)
        print("\n choose the name of the name of your constituency from the list \n")
        print("".join([f" {count}:\t {i} \n" for count , i  in enumerate(list,1)]))
        while True:
             try:
                C_input = int(input(f'Enter the number of constituency: in a range (1 -{len(list)}): '))
                constituency_name = list[C_input - 1]
                consitituencies[constituency_name].display_constituency_information()
                break
             except ValueError:
                  print("Invalid input. Please enter a number.")
             except IndexError:
                  print(f"Invalid input. Please enter a number in the range (1 - {len(list)}).")
    else:
        Constituency.list_of_contituency_by_region(consitituencies, country_input)


def main():
    while True:
        options_menu()
        try: 
            choice = input("Enter your choice (1, 2, 3,4, 5, 6 or 7 to exit): ")
            if not choice.isdigit():
                raise ValueError
            options = ['1','2','3','4','5', '6']     
            if choice in options:
                    if choice == "1":
                          constituncy_information(contituencies_info)
                        # get_candidat_information(contituencies_info)
                    elif choice == "2":
                        total_vote_each_party(database)
                    elif choice == "3":
                        pass
                    elif choice == '4':
                         get_candidat_information(contituencies_info)
                    elif choice == "5" :
                        find_your_MP(contituencies_info)
                    elif choice == '6':
                        break
                    break
            else:
                        print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError as e:
                print('incorrect value')

file_path ='FullDataFor2024.csv'
database = read_file(file_path)

contituencies_info, party_info = data_manage(database)

main()