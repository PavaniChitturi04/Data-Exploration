import pandas as pd
import numpy as np
survey_dict={'language':['Python','Java','Haskell','Go','C++'],
             'salary':[120,85,95,80,90],
             'num_candidate':[18,22,34,10,np.NaN]}
survey_df=pd.DataFrame(survey_dict)
print("Before modify")
print(survey_df)
survey_df.replace(to_replace=np.nan,value=17,inplace=True)
survey_df.head()
print("After modify")
print(survey_df)
