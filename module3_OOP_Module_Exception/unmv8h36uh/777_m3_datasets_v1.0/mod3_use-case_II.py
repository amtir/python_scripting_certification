import csv

def read_csv(file_name):
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

def get_unique_jobs(data):
    return set(row['job'].lower() for row in data)

def get_age_limits(data):
    ages = [int(row['age']) for row in data]
    return {'min_age': min(ages), 'max_age': max(ages)}

def check_eligibility(profession, unique_jobs):
    return profession.lower() in unique_jobs

def main():
    file_name = 'bank-data.csv'
    data = read_csv(file_name)
    unique_jobs = get_unique_jobs(data)
    age_limits = get_age_limits(data)
    
    print(f"Unique professions: {unique_jobs}")
    print(f"Age limits for loan eligibility: {age_limits}")
    
    while True:
        profession = input("Enter the profession (type 'END' to stop): ")
        if profession == "END":
            break
        if check_eligibility(profession, unique_jobs):
            print(f"The client with profession '{profession}' is eligible for the marketing campaign.")
        else:
            print(f"The client with profession '{profession}' is not eligible for the marketing campaign.")
        
if __name__ == "__main__":
    main()
