import plotly as py
import plotly.graph_objs as go
import numpy as np
from plotly import tools
import collections



with open("data/who_suicide_statistics.csv") as file:

    header = file.readline()
    header_list = header.strip().rstrip().split(",")

    dataset = dict()

    line = file.readline()
    LIST = []

    while line:

        line_list = line.rstrip().strip().split(",")

        row_dict = dict(zip(header_list,line_list))
        LIST.append( line_list )

        if row_dict["country"] in dataset.keys():

            if row_dict["year"] in dataset[row_dict["country"]].keys():

                if row_dict["sex"] in dataset[row_dict["country"]][row_dict["year"]].keys():

                    dataset[row_dict["country"]][row_dict["year"]][row_dict["sex"]][row_dict["age"]] = {
                        "suicides_no": row_dict["suicides_no"],
                        "population": row_dict["population"]
                    }
                else:
                    dataset[row_dict["country"]][row_dict["year"]][row_dict["sex"]] = {
                            row_dict["age"]:
                                {
                                    "suicides_no": row_dict["suicides_no"],
                                    "population": row_dict["population"]
                                }
                        }
            else:
                dataset[row_dict["country"]][row_dict["year"]] = {
                    row_dict["sex"]:
                        {
                            row_dict["age"]:
                                {
                                    "suicides_no": row_dict["suicides_no"],
                                    "population": row_dict["population"]
                                }
                        }
                }
        else:
            dataset[row_dict["country"]] = {
                row_dict["year"]:
                    {
                        row_dict["sex"]:
                            {
                                row_dict["age"]:
                                    {
                                        "suicides_no": row_dict["suicides_no"],
                                        "population": row_dict["population"]
                                    }
                            }
                    }
            }

        line = file.readline()



    data_1=dict()
    suicides_year=0
    suicides_country=0
    suicides_country_list=[]
    countries=[]
    suicides_male=0
    suicides_female=0
    for country in dataset.keys():
        for year in dataset[country].keys():
            for sex in dataset[country][year].keys():
                for age in dataset[country][year][sex].keys():
                    suicides_no = dataset[country][year][sex][age]["suicides_no"]
                    if suicides_no=="":
                        suicides_no=0
                    else:
                        suicides_no=int(suicides_no)

                    suicides_country += suicides_no
                    suicides_year+=suicides_no

                    if sex=="male":
                            suicides_male+=suicides_no
                    else:
                            suicides_female+=suicides_no

            if year in data_1.keys():
                data_1[year] += suicides_year
            else:
                data_1[year] = suicides_year
            suicides_year = 0

        suicides_country_list.append(suicides_country)
        countries.append(country)
        suicides_country = 0
    data_1_sorted = collections.OrderedDict(sorted(data_1.items()))




    DATA_1 = go.Scatter(
        x=list(data_1_sorted.keys()),
        y=list(data_1_sorted.values()),
        name="suisides for the year"
    )
    DATA_2 = go.Pie(
        labels=["male", "female"],
        values=[suicides_male, suicides_female]
    )
    DATA_3 = go.Bar(
        x=countries,
        y=suicides_country_list,
        name="suisides per year"
    )

    fig = tools.make_subplots(rows=1, cols=2)

    fig.append_trace(DATA_1, 1, 1)

    fig.append_trace(DATA_3, 1, 2)

    py.offline.plot(fig, filename='plotly_1_3.html')
    py.offline.plot([DATA_2], filename='plotly_2.html')