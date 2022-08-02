# FinalProject

For my project, I chose the variables Country, Age, Gender, tech_company,family_history,treatment and wellness_program. 
I chose country because the question said how does it vary by geographical location so I thought country was necessary.  Since the data was a tech survey,
I thought it necessary to use the tech_company variable and then using family_history to see how many people were already susceptible to mental illness
as well as treatment to see who had experienced mental illness issues and lastly wellness_program so I could see the emphasis their job placed on mental health for employees.

During my assignment I had many struggles.  Firstly, I could not figure out how to group my ages into categories.  I was using the .loc notation with a condition
but was still receiving an error on my code.  I googled and found a solution which had me import the library numpy.  Then, I had issues loading my dataframe
after I had grouped it to my empty csv file I created.  This was solved by using .count() and .reset_index() on my groupby function.  Lastly, after I installed
my dash by plotly library, it would not import and was giving me an error but I solved my problem by figuring out the location of my install as well as the version of my python.

