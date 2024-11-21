
import csv

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