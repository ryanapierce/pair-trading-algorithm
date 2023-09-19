import pandas as pd
import matplotlib.pyplot as plt

pepsi_df = pd.read_csv('pepsi_df.csv')
plt.plot(pepsi_df['Close'])
plt.show()
# print(pepsi_df)