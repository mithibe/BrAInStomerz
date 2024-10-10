import pandas as pd
import random

# Function to generate random student data
def generate_student_data(num_students):
    first_names = ["John", "Mary", "Kevin", "Faith", "Ian", "Esther", "Stephen", "Lilian", "David", "Rose",
                   "James", "Agnes", "Dennis", "Mercy", "Peter", "Lucy", "Andrew", "Hannah", "Kennedy", 
                   "Irene", "Eliud", "Samuel", "Ann", "Henry", "Beatrice", "Charles", "Brenda", "Fredrick",
                   "Jacinta", "Tom", "Esther", "Nelson", "Faith", "Linet", "Joseph", "Paul", "Stella",
                   "Francis", "Grace", "Alex", "Sarah", "David", "Susan", "John", "Dorcas", "Elijah",
                   "Rose", "Martin", "Ann", "Samuel"]
    
    last_names = ["Doe", "Atieno", "Njoroge", "Wangechi", "Onyango", "Kiprop", "Kariuki", "Otieno", 
                  "Mutiso", "Mwende", "Kamau", "Wanjiku", "Kiplangat", "Mwikali", "Chege", "Achieng", 
                  "Ochieng", "Wairimu", "Otieno", "Mutiso", "Muthama", "Njoroge", "Wambui", "Oduor", 
                  "Nyambura", "Kibet", "Juma", "Simiyu", "Wanjiru", "Otieno", "Nduati", "Chirchir", 
                  "Rono", "Koome", "Makori", "Nyakundi", "Ngoya", "Chebet", "Kilonzo", "Kigen", 
                  "Kibera", "Mutua", "Kirui", "Kimeu", "Akinyi", "Chirchir", "Wamuyu", "Davis"]
    
    data = {
        "StudentID": [i for i in range(1, num_students + 1)],
        "Name": [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(num_students)],
        "GradeLevel": [f"Grade {random.choice(['6', '7', '8', '9', '10', '11', '12'])}" for _ in range(num_students)],
        "PhysicsScore": [random.randint(50, 100) if random.random() > 0.1 else None for _ in range(num_students)],
        "BiologyScore": [random.randint(50, 100) if random.random() > 0.1 else None for _ in range(num_students)],
        "MathematicsScore": [random.randint(50, 100) if random.random() > 0.1 else None for _ in range(num_students)],
        "EnglishScore": [random.randint(50, 100) if random.random() > 0.1 else None for _ in range(num_students)],
        "SportsParticipation": [random.choice(["Yes", "No"]) for _ in range(num_students)],
        "SportsAchievements": [random.choice(["None", "School Level", "County Level", "National Level"]) for _ in range(num_students)],
        "ExtracurricularActivities": [random.choice(["None", "Science Club", "Debate Club", "Drama Club", "Art Club", "Music Club"]) for _ in range(num_students)],
        "LeadershipRole": [random.choice([None, "Class Representative", "Club Leader"]) for _ in range(num_students)],
        "CareerAspiration": [random.choice(["Doctor", "Engineer", "Artist", "Teacher", "Musician", "Data Scientist", "Pilot", "Lawyer", "Athlete", "Pharmacist", "Accountant", "Surgeon"]) for _ in range(num_students)],
        "STEMPathway": [random.choice(["Yes", "No"]) for _ in range(num_students)]
    }
    
    return pd.DataFrame(data)

# Generate 2000 students data
num_students = 2000
student_data_df = generate_student_data(num_students)

# Save the DataFrame to a CSV file
csv_file_path = "student_career_data_2000.csv"  # Change this path as needed
student_data_df.to_csv(csv_file_path, index=False)

print(f"CSV file '{csv_file_path}' has been created with {num_students} student entries.")
