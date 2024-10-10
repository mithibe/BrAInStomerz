import pandas as pd

# Load the CSV file
data = pd.read_csv('student_career_data_2000.csv')

# Check for missing values
print(data.isnull().sum())

# Filling missing scores with the mean
data.fillna(data.mean(), inplace=True)

from sklearn.preprocessing import LabelEncoder

label_encoders = {}
categorical_cols = ['SportsParticipation', 'SportsAchievements', 'ExtracurricularActivities', 'LeadershipRole', 'CareerAspiration', 'STEMPathway']

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

from sklearn.model_selection import train_test_split

x = data.drop('CareerAspiration', axis=1) # features
y = data['CareerAspiration'] # Target variable

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Initialize the model
model = RandomForestClassifier(random_state=42)

# Fit the model on the training data
model.fit(x_train, y_train)

# Make predictions on the test set
predictions = model.predict(x_test)

# Evaluate the model
print(classification_report(y_test, predictions))
print("Accuracy: ", accuracy_score(y_test, predictions))

from sklearn.metrics import confustion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

cm = confustion_matrix(y_test, predictions)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()