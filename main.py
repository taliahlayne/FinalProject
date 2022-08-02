
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np



pd.set_option("display.max_columns",50)
pd.set_option("display.max_rows",500)

df = "survey.csv"
survey_df = pd.read_csv(df)

final_survey_df = survey_df[["Country","Age","Gender","family_history","tech_company","wellness_program","treatment"]]
# print("=="*30)
# print(final_survey_df["Country"].unique())

#Choosing a Specific Continent

Continent_North_America = ["United States","Canada","Mexico","Bahamas, The" ]

final_survey_df.loc[(final_survey_df["Country"].isin(Continent_North_America)), "Country"] = "North_America"
final_survey_df["North_America"] = final_survey_df["Country"]


#Cleaning Gender Data
genders_female = ["female","Cis Female","F","Woman","f","Femake","woman","cis-female/femme","Female (cis)","femail","Female "]
genders_male = ["M","male","m","Male-ish","maile","something kinda male?","Cis Male","Mal","Male (CIS)","Make","Guy (-ish) ^_^","male leaning androgynous","Man","msle","Mail","cis male","Malr","Cis Man","ostensibly male, unsure what that really means","Male "]
genders_non_binary = ["Trans-female","queer/she/they","Nah","All","Enby","fluid","Genderqueer","Androgyne","Agender","Trans woman","Neuter","Female (trans)","queer","A little about you","p","non-binary"]

final_survey_df.loc[(final_survey_df["Gender"].isin(genders_female)), "Gender"] = "Female"
final_survey_df.loc[(final_survey_df["Gender"].isin(genders_male)), "Gender"] = "Male"
final_survey_df.loc[(final_survey_df["Gender"].isin(genders_non_binary)), "Gender"] = "Non-binary"


#Cleaning Age Data
conditions = [(final_survey_df["Age"] <= 11), (final_survey_df["Age"] >= 18)  & (final_survey_df["Age"] <= 24),
(final_survey_df["Age"] <= 34), (final_survey_df["Age"] <= 44), (final_survey_df["Age"] <= 54), (final_survey_df["Age"] <= 64),(final_survey_df["Age"] <= 74)]

values = ['Under 18', '18-24', '25-34','35-44','45-54','55-64','65-74']

final_survey_df['age_categories'] = np.select(conditions, values)
final_survey_df["Age"] = final_survey_df["age_categories"]

# print("=="* 30)
# print(final_survey_df["age_categories"].head(50))


#Cleaning Wellness Program Data
wellness_program_yes = ["Yes"]
wellness_program_no = ["No"]
wellness_program_unsure = ["Don't know"]

final_survey_df.loc[(final_survey_df["wellness_program"].isin(wellness_program_yes)), "wellness_program"] = "Yes"
final_survey_df.loc[(final_survey_df["wellness_program"].isin(wellness_program_no)), "wellness_program"] = "No"
final_survey_df.loc[(final_survey_df["wellness_program"].isin(wellness_program_unsure)), "wellness_program"] = "Unsure"

# print("=="* 30)
# print(final_survey_df.head(50))

#Survey Information Grouped
final_survey_grouped = final_survey_df.groupby(["Country","Age","Gender","family_history","tech_company","wellness_program","treatment"]).count().reset_index()

# print("=="*30)
# print(final_survey_grouped.head())

# print("=="*30)
# for key, item in final_survey_grouped:
#  print(final_survey_grouped.get_group(key))

#Creating a New Csv and Putting Grouped Dataframe in the Created Csv

with open('Survey_Updated.csv', 'w') as my_new_csv_file:
 pass
final_survey_grouped.to_csv('Survey_Updated.csv', index=False, header=True)


#Visualization of Analysis - PLEASE UNCOMMENT FOR EACH GRAPH YOU WOULD LIKE TO SEE

#FIGURE1
# app = Dash(__name__)
# fig = px.bar(final_survey_grouped, x="Gender", y="North_America", color="tech_company", barmode="group")

# app.layout = html.Div(children=[
#     html.H1(children='Gender of People Working in Tech in North America'),

#     html.Div(children='''
#         Dash: A web application framework for your data.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)

#FIGURE2
# app = Dash(__name__)
# fig = px.bar(final_survey_grouped, x="Age", y="North_America", color="tech_company", barmode="group")

# app.layout = html.Div(children=[
#     html.H1(children='Age of People Working in Tech in North America'),

#     html.Div(children='''
#         Dash: A web application framework for your data.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

#FIGURE3
# app = Dash(__name__)

# fig = px.bar(final_survey_grouped, x="Age", y="North_America", color="family_history", barmode="group")

# app.layout = html.Div(children=[
#     html.H1(children='Age of People with a Family History of Mental Illness in North America'),

#     html.Div(children='''
#         Dash: A web application framework for your data.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)

#FIGURE4

# app = Dash(__name__)

# fig = px.bar(final_survey_grouped, x="tech_company", y="North_America", color="family_history", barmode="group")

# app.layout = html.Div(children=[
#     html.H1(children='Amount of People Who Have a Family History of Mental Illness That Work in Tech'),

#     html.Div(children='''
#         Dash: A web application framework for your data.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)

#FIGURE5


app = Dash(__name__)

fig = px.bar(final_survey_grouped, x="treatment", y="North_America", color="tech_company", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Amount of People That Have Seeked Treatment for Mental Illness That Work in Tech'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

#FIGURE6

# app = Dash(__name__)

# fig = px.bar(final_survey_grouped, x="wellness_program", y="North_America", color="tech_company", barmode="group")

# app.layout = html.Div(children=[
#     html.H1(children='Amount of People in Tech That Has a Job with a Wellness Program'),

#     html.Div(children='''
#         Dash: A web application framework for your data.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)



