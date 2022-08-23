import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.cbook as cbook
import matplotlib.dates as mdates
import numpy as np
from sqlalchemy import create_engine



engine = create_engine('sqlite:///db.sqlite3')

df = pd.read_sql_table(
                       'listOfTokens_bsctoken',
                       con=engine)

df['networkName'] = ''
df['networkName'] = np.select(condlist=[df['networkName_id'] == 1,
                                       df['networkName_id'] == 2,
                                       df['networkName_id'] == 3,
                                       df['networkName_id'] == 4],
                             choicelist=['BSC', 'ETH', 'MATIC', 'FTM'] )

df['date'] = pd.to_datetime(df['created_on']).dt.strftime('%Y-%m-%d')
newframe = df.groupby(['date', 'networkName']).count()
newframe.rename(columns={'id':'Count'}, inplace=True)


fig, axes = plt.subplots()

colors = {'BSC':'tab:orange', 'ETH':'tab:blue', 'MATIC':'tab:green', 'FTM':'tab:red'}

handles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=v, label=k, markersize=8) for k, v in colors.items()]
axes.legend(title='Networks', handles=handles, bbox_to_anchor=(1.05, 1), loc='upper left')
fig.autofmt_xdate()
axes.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
plt.xticks(fontsize=8)
plt.ylabel('Count', fontsize=8)



graf = plt.scatter(newframe.index.get_level_values('date'), newframe['Count'], c=newframe.index.get_level_values('networkName').map(colors))

plt.title("Daily token count graph")




annotation = axes.annotate(text='',
                          xy=(0, 0),
                          xytext=(15,15),
                          textcoords='offset points',
                          bbox={'boxstyle': 'round', 'fc': 'w'},
                          arrowprops={'arrowstyle': '->'})

annotation.set_visible(False)
def motion_hover(event):
  annotation_visibility = annotation.get_visible()
  if event.inaxes == axes:
    is_contained, annotation_index = graf.contains(event)
    if is_contained:
      data = graf.get_offsets()[annotation_index['ind'][0]]
      annotation.xy = data

      text_label = f'Created: {data[1]}'
      annotation.set_text(text_label)
      annotation.set_visible(True)
      fig.canvas.draw_idle()
    else:
      if annotation_visibility:
        annotation.set_visible(False)
        fig.canvas.draw_idle()

fig.canvas.mpl_connect('motion_notify_event', motion_hover)
plt.show(block=True)
