
import requests
import pandas as pd
from sqlalchemy import create_engine
import schedule 
from datetime import time, timedelta, datetime


def extract() -> dict:
    API_URL = "http://universities.hipolabs.com/search?country=Poland"
    data = requests.get(API_URL).json()
    return data


def transform(data:dict) -> pd.DataFrame:
    df = pd.DataFrame(data)
    print(f"Total numbers of universities in Poland: {len(data)}")
    df["domains"] = [','.join(map(str,l)) for l in df["domains"]]
    df["web_pages"] = [','.join(map(str,l)) for l in df["web_pages"]]
    
    uni_type_dict = {
        "Akademia": "Academy",
        "Uniwersytet": "University",
        "Politechnika": "Polytechnic",
        "School": "Higher School",
        "Academy": "Academy",
        "University": "University",
        "Academy": "Academy",
        "College": "College",
        "Higher School": "Higher School",
        "Collegium": "Collegium",
        "Institute": "Institute",
    }

    def check_type(name:str):
        for keyword, type_ in uni_type_dict.items():
            if keyword in name:
                return type_
        return "Other"
    
    df["type"] = df["name"].apply(check_type)

    df = df.reset_index(drop=True)
    return df[["domains", "country", "web_pages", "name", "type"]]



def load(df:pd.DataFrame):
    engine = create_engine("postgresql://postgres:123@localhost:5432/universities_etl")
    df.to_sql("universities", con=engine, if_exists="replace", index=False)


data = extract()
df = transform(data)
load(df)