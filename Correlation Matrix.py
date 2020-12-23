import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm


fm.get_fontconfig_fonts()
font_location = 'C:/Users/J Park/Jay/Fonts/KoPubWorld Dotum_Pro Medium.otf'   # User Font Location
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)


data = pd.read_excel(r'C:\Users\J Park\Desktop\data.xlsx')    # User Data Location

plt.figure(figsize=(20,200))
sns.heatmap(data = data.corr(), annot=True, fmt = '.4f', linewidths=.5, cmap='Blues')
