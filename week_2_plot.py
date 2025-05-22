import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

data = '''
month_number,facecream,facewash,toothpaste,bathingsoap,shampoo,moisturizer,total_units,total_profit
1,2500,1500,5200,9200,1200,1500,21100,211000
2,2630,1200,5100,6100,2100,1200,18330,183300
3,2140,1340,4550,9550,3550,1340,22470,224700
4,3400,1130,5870,8870,1870,1130,22270,222700
5,3600,1740,4560,7760,1560,1740,20960,209600
6,2760,1555,4890,7490,1890,1555,20140,201400
7,2980,1120,4780,8980,1780,1120,29550,295500
8,3700,1400,5860,9960,2860,1400,36140,361400
9,3540,1780,6100,8100,2100,1780,23400,234000
10,1990,1890,8300,10300,2300,1890,26670,266700
11,2340,2100,7300,13300,2400,2100,41280,412800
12,2900,1760,7400,14400,1800,1760,30020,300200
'''

# Read the CSV data into a DataFrame
df = pd.read_csv(StringIO(data))

# Exercise 1: Line plot for total profit
plt.figure(figsize=(10, 5))
plt.plot(df['month_number'], df['total_profit'], marker='o', color='green', linewidth=2)
plt.title('Company Profit per Month')
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.grid(True)
plt.xticks(df['month_number'])
plt.tight_layout()
plt.show()

# Exercise 2: Subplots for bathing soap and facewash
plt.figure(figsize=(12, 6))

# Subplot for Bathing Soap
plt.subplot(2, 1, 1)
plt.plot(df['month_number'], df['bathingsoap'], color='blue', marker='o')
plt.title('Sales of Bathing Soap per Month')
plt.ylabel('Units Sold')
plt.xticks(df['month_number'])

# Subplot for Facewash
plt.subplot(2, 1, 2)
plt.plot(df['month_number'], df['facewash'], color='orange', marker='o')
plt.title('Sales of Facewash per Month')
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.xticks(df['month_number'])

plt.tight_layout()
plt.show()
