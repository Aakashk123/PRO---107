
import pandas as pd
import csvimport pandas as pd
import ploty.graph_objects as go

df = pd.read_csv("data.csv")

student_df = df.loc[df['student_id']=="TRL_987"]