import pandas as pd

df=pd.read_csv("/Users/oguztunc/Downloads/city_day.csv")


df["Date"]=pd.to_datetime(df["Date"])

df.drop_duplicates(inplace=True)
df2=df.dropna(thresh=3)

mapping={"Serve":1,
         "Very poor":2,
         "Poor":3,
         "Moderate":4,
         "Satisfactory":5,
         "Good":6
         }
df2["AQI_Bucket"]=df2["AQI_Bucket"].map(mapping)
df2=df2.fillna({"AQI_Bucket":"No Data",
                "AQI": "No Data"
                })
df2.to_csv("clean_data",index=False)

