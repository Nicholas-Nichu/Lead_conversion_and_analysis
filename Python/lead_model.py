#Importing libraries and changing column types
import pandas as pd
PX1=pd.read_csv('PX1.csv')
PX1['Created Date']=pd.to_datetime(PX1['Created Date'])
PX1['Site-Visit Done Date']=pd.to_datetime(PX1['Site-Visit Done Date'])
PX1['Applicant DOB']=pd.to_datetime(PX1['Applicant DOB'])
PX1['Booking Date']=pd.to_datetime(PX1['Booking Date'])

#Adding columns which will help in analysing the data further
PX1['Converted']=PX1['Booking Date'].notna().astype(int)
PX1['Days_to_book']=(PX1['Booking Date']-PX1['Site-Visit Done Date']).dt.days
PX1['Days_to_visit']=(PX1['Site-Visit Done Date']-PX1['Created Date']).dt.days
PX1['Age']=(pd.Timestamp.today()-PX1['Applicant DOB']).dt.days//365.25.astype(int)

#To check the statistical summary of the data
PX1.describe()
PX1.groupby('Converted')['Site Visit Count'].mean()
PX1.groupby('Converted')['Days_to_visit'].mean()

#Creation of model to see which leads have higher probability of conversion
PX1_model = PX1[['Site Visit Count', 'Days_to_visit', 'Converted']].dropna()
from sklearn.model_selection import train_test_split
X = PX1_model[['Site Visit Count', 'Days_to_visit']]
y = PX1_model['Converted']
X_train, X_test,y_train, y_test = train_test_split(X, y, test_size=0.2)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
PX1_model['Probability'] = model.predict_proba(X)[:,1]

#Fetching the top 15 to create an hypothesis
PX1_model.sort_values(by='Probability', ascending=False).head(15)
