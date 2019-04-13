
import pandas as pd
from sqlalchemy import create_engine



csv_file1 = "low_income_performance.csv"
csv_file2 = "grad_rates1.csv"

low_income_performance_df = pd.read_csv(csv_file1)
grad_rates_df = pd.read_csv(csv_file2)


new_df = low_income_performance_df[['State','NcesCharterSchool', 'NcesMagnetSchool', 'Reading Est Prof','Math Est Prof']].copy()
new_df = new_df.fillna(0)
new_df.columns = ['State', 'Charter','Magnet','Reading Prof','Math Prof']


state_df = new_df[['State','Reading Prof','Math Prof']].copy()

state_df['Reading Prof'] = (state_df['Reading Prof'].str[:-1].astype(int))
state_df['Math Prof'] = (state_df['Math Prof'].str[:-1].astype(int))


new_state_df = state_df.groupby('State').mean()
new_state_df = new_state_df.round(decimals=0)


grad_rates_df = grad_rates_df[['State + US','Total', 'Economically disadvantaged']].copy()


csv_file = "StudentsPerformance.csv"
student_data_df = pd.read_csv(csv_file)


student_data_df.reset_index(level=0, inplace=True)
student_data_df.head()


student_gender_data_df = student_data_df[['index', 'gender', 'math score', 'reading score', 'writing score','average score']].copy()
student_gender_data_df.head()


parent_education_df = student_data_df[['index', 'parental level of education', 'math score', 'reading score', 'writing score', 'average score']].copy()
parent_education_df.head()


race_file = "graduation_race.csv"
college_enrollment_data_df = pd.read_csv(race_file)


college_enrollment_data_df = college_enrollment_data_df.fillna(0).set_index("Unnamed: 0")
college_enrollment_data_df

del college_enrollment_data_df.index.name

college_enrollment_data_df = college_enrollment_data_df.T
college_enrollment_data_df


asian_home = "asian_home.csv"
black_home = "black_home.csv"
hispanic_home = "hispanic.csv"
white_home = "white_home.csv"

asian_home_df = pd.read_csv(asian_home)
asian_home_df = asian_home_df.set_index("Unnamed: 0")

del asian_home_df.index.name

asian_home_df = asian_home_df.T
asian_home_df

black_home_df = pd.read_csv(black_home)
black_home_df = black_home_df.set_index("Black, non-Hispanic")

del black_home_df.index.name

black_home_df = black_home_df.T
black_home_df

hispanic_home_df = pd.read_csv(hispanic_home)
hispanic_home_df = hispanic_home_df.set_index("Hispanic")

del hispanic_home_df.index.name

hispanic_home_df = hispanic_home_df.T
hispanic_home_df

white_home_df = pd.read_csv(white_home)
white_home_df = white_home_df.set_index("White non-Hispanic")

del white_home_df.index.name

white_home_df = white_home_df.T
white_home_df

