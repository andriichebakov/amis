input_file = 'data/who_suicide_statistics.csv'
import re



def getCountry(line):
    result = re.split(r",", line, maxsplit=1)
    return result[0], result[1]

def getYear(line):
    result = re.split(r",", line, maxsplit=1)
    year = re.findall(r"\d{4}", result[0])
    return year[0], result[1]

def getSex(line):
    result = re.split(r",", line, maxsplit=1)
    return result[0], result[1]

def getAge(line):
    result = re.split(r",", line, maxsplit=1)
    if "+" in result[0]:
        age = re.findall(r"\d{2}\+", result[0])
    else:
        age = re.findall(r"\d{1,2}-\d{2}", result[0])
    return age[0], result[1]

def getSuicides_no(line):
    result = re.split(r",", line, maxsplit=1)
    return result[0], result[1]

def getPopulation(line):
    result = re.split(r",", line, maxsplit=1)
    return result[0], result[1]