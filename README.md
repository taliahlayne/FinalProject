# FinalProject

Variables I Chose:

For my project, I chose the variables Country, Age, Gender, tech_company,family_history,treatment and wellness_program. 
I chose country because the question said how does it vary by geographical location so I thought country was necessary.  Since the data was a tech survey,
I thought it necessary to use the tech_company variable and then using family_history to see how many people were already susceptible to mental illness
as well as treatment to see who had experienced mental illness issues and lastly wellness_program so I could see the emphasis their job placed on mental health for employees.

Struggles with My Code:

During my assignment I had many struggles.  Firstly, I could not figure out how to group my ages into categories.  I was using the .loc notation with a condition
but was still receiving an error on my code.  I googled and found a solution which had me import the library numpy.  Then, I had issues loading my dataframe
after I had grouped it to my empty csv file I created.  This was solved by using .count() and .reset_index() on my groupby function.  Lastly, after I installed
my dash by plotly library, it would not import and was giving me an error but I solved my problem by figuring out the location of my install as well as the version of my python.


My Analysis Thought Process:

To begin with, since it was so many countries, I chose to work with North America.  I wanted to have an idea of how many men vs women worked in tech in North America as well as the age groups working in tech in North America.  I then went on to dive in the age group with the majority of people who had a family history of mental illness in North America.  This gave me an idea of which age group would be most susceptible to mental health issues in North America. I took it one step further and then loooked at the amount of people that had a family history of mental illness that work in tech and then the amount of people that seek treatment for mental illness that work in tech.  Lastly, I made a chart from the amount of people have have a wellness program at their job in tech that has allowances for employeees with mental health issues.  These charts to me gave me at first a broad picture of who was affected by mental illness in North America and then gave me a more narrow view of people in tech who have mental health issues and those who have jobs that make provisions for their employees that do.



