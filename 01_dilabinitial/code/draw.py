import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data.xls')
df.iloc[:,0] = pd.to_datetime(df.iloc[:,0], format='%b-%y')
df.columns = ['Date', 'Cost per GB (USD)', 'Cost per Genome (USD)']

# Plotting 'Cost per GB'
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Cost per GB (USD)'], marker='o', label='Cost per GB')
plt.yscale('log')
plt.title('Cost per GB Analysis')
plt.xlabel('Date')
plt.ylabel('Cost per GB (log scale in USD)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plotting 'Cost per Genome'
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Cost per Genome (USD)'], marker='o', label='Cost per Genome')
plt.yscale('log')
plt.title('Cost per Genome Analysis')
plt.xlabel('Date')
plt.ylabel('Cost per Genome (log scale in USD)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
