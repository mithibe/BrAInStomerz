import pandas as pd

# Define the data
data = {
    "StudentID": [i for i in range(101, 151)],
    "Name": [
        "John Doe", "Mary Atieno", "Kevin Njoroge", "Faith Wangechi", "Ian Onyango", "Esther Kiprop",
        "Stephen Kariuki", "Lilian Otieno", "David Mutiso", "Rose Mwende", "James Kamau", "Agnes Wanjiku",
        "Dennis Kiplangat", "Mercy Mwikali", "Peter Chege", "Lucy Achieng", "Andrew Ochieng", "Hannah Wairimu",
        "Kennedy Otieno", "Irene Mwangi", "Eliud Muthama", "Samuel Njoroge", "Ann Wambui", "Henry Oduor",
        "Beatrice Nyambura", "Charles Kibet", "Brenda Juma", "Fredrick Simiyu", "Jacinta Wanjiru", "Tom Otieno",
        "Esther Wambui", "Nelson Kipkorir", "Faith Njeri", "Linet Njiru", "Joseph Gikonyo", "Paul Wanjala",
        "Stella Njiru", "Francis Mwangi", "Grace Kilonzo", "Alex Kiprotich", "Sarah Odhiambo", "David Maina",
        "Susan Ouma", "John Makori", "Dorcas Otieno", "Elijah Nduta", "Rose Chepkoech", "Martin Ndungu",
        "Ann Kamau", "Samuel Mwangi"
    ],
    "GradeLevel": [
        "Grade 12", "Grade 11", "Grade 10", "Grade 9", "Grade 8", "Grade 12", "Grade 10", "Grade 6", "Grade 8", 
        "Grade 9", "Grade 12", "Grade 11", "Grade 10", "Grade 9", "Grade 8", "Grade 7", "Grade 12", "Grade 11", 
        "Grade 10", "Grade 9", "Grade 8", "Grade 7", "Grade 6", "Grade 12", "Grade 11", "Grade 10", "Grade 9", 
        "Grade 8", "Grade 7", "Grade 6", "Grade 12", "Grade 11", "Grade 10", "Grade 9", "Grade 8", "Grade 7", 
        "Grade 6", "Grade 12", "Grade 11", "Grade 10", "Grade 9", "Grade 8", "Grade 7", "Grade 6", "Grade 12", 
        "Grade 11", "Grade 10", "Grade 9", "Grade 8"
    ],
    "PhysicsScore": [85, 88, 70, 60, 75, 92, 55, None, 85, 82, 78, 88, 65, 62, 72, 80, 60, 70, 90, 85, 75, 65, None, 70, 88, 85, 55, 80, 75, None, 88, 72, 85, 70, 82, 60, None, 75, 88, 70, 80, 85, 75, None, 88, 70, 85, 78, 75],
    "BiologyScore": [78, 92, 65, 55, 68, 88, 72, None, 80, 90, 85, 80, 72, 80, 75, None, 78, 80, 85, 88, 70, 72, None, 75, 90, 72, 60, 85, 82, None, 85, 90, 88, 65, 85, 55, None, 70, 85, 80, 85, 80, 90, None, 80, 75, 88, 85, 70],
    "MathematicsScore": [90, 95, 85, 80, 78, 91, 65, 78, 88, 87, 90, 85, 88, 82, 85, 90, 65, 78, 80, 95, 85, 75, 88, 88, 92, 90, 75, 88, 80, 90, 92, 85, 78, 85, 70, 78, 80, 92, 85, 88, 85, 88, 90, 85, 78, 78, 85, 80, 85],
    "EnglishScore": [70, 80, 75, 85, 72, 85, 60, 82, 72, 80, 75, 78, 70, 60, 65, 88, 72, 85, 75, 85, 78, 82, 80, 72, 78, 65, 70, 78, 85, 85, 75, 65, 72, 78, 75, 82, 85, 72, 70, 78, 72, 80, 85, 75, 80, 78, 70, 72, 78],
    "SportsParticipation": ["Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"],
    "SportsAchievements": ["County"]
    "ExtracurricularActivities": ["Science Club", "Debate Club", "Drama Club", "None", "Science Club", "Debate Club", "None", "None", "Debate Club", "Art Club", "Debate Club", "Drama Club", "Science Club", "Music Club", "None", "None", "Art Club", "Science Club", "None", "Debate Club", "None", "None", "Music Club", "None", "Science Club", "None", "Drama Club", "Debate Club", "Music Club", "None", "None", "Science Club", "None", "Debate Club", "None", "Art Club", "None", "Music Club", "Debate Club", "None",
    "LeadershipRole": ["Class Representative", None, None, None, "Club Leader", None, None, None, "Class Representative", None, None, None, None, None, "Class Representative", None, None, None, None, "Class Representative", None, None, None, None, None, None, None, "Class Representative", None, None, None, None, "Class Representative", None, "Class Representative", None, None, None, "Class Representative", None, "Class Representative", None, "Class Representative", None, None, None, "Club Leader", None],
    "CareerAspiration": ["Doctor", "Biotechnologist", "Engineer", "Athlete", "Teacher", "Environmental Scientist", "Pilot", "Physiotherapist", "Surgeon", "Pharmacist", "Lawyer", "Actor", "Data Scientist", "Musician", "Politician", "Mathematician", "Graphic Designer", "Nurse", "Software Engineer", "Entrepreneur", "Accountant", "Athlete", "Dancer", "Doctor", "Chemist", "Engineer", "Journalist", "Politician", "Singer", "Physiotherapist", "Lawyer", "Pilot", "Doctor", "Athlete", "Journalist", "Teacher", "Artist", "Engineer", "Musician", "Software Engineer", "Doctor", "Engineer", "Athlete", "Politician", "Journalist", "Software Engineer", "Surgeon", "Chemist", "Biologist", "Accountant"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = "student_career_data.csv"
df.to_csv(csv_file_path, index=False)

csv_file_path  # Output the path to the generated CSV file
