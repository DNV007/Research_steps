import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import DateFormatter, MonthLocator, DayLocator
import matplotlib.dates as mdates
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects

# Define your tasks and their schedules
tasks = [
    {"Task": "Literature Review", "Start": "2024-07-25 09:00", "End": "2024-08-05 10:00"},  # 2 weeks
    {"Task": "Model Development", "Start": "2024-07-25 10:00", "End": "2024-09-01 12:00"},  # 5 weeks
    {"Task": "Algorithm Design", "Start": "2024-07-22 13:00", "End": "2024-08-19 16:00"},  # 4 weeks
    {"Task": "Implementation", "Start": "2024-07-23 09:00", "End": "2024-10-11 11:00"},  # 12 weeks
    {"Task": "Verification", "Start": "2024-07-23 11:00", "End": "2024-07-30 13:00"},  # 1 week
    {"Task": "Validation", "Start": "2024-07-27 14:00", "End": "2024-12-27 15:00"},  # 20 weeks
    {"Task": "Experimentation", "Start": "2024-07-25 09:00", "End": "2024-11-24 12:00"},  # 16 weeks
    {"Task": "Analysis", "Start": "2024-07-24 13:00", "End": "2024-10-24 16:00"},  # 12 weeks
    {"Task": "Visualization", "Start": "2024-09-25 09:00", "End": "2024-11-25 11:00"},  # 6 weeks
    {"Task": "Documentation", "Start": "2024-09-25 09:00", "End": "2024-10-25 11:00"},  # 10 weeks
    {"Task": "Dissemination", "Start": "2024-08-25 09:00", "End": "2024-10-25 11:00"},  # 10 weeks    
]

# Convert data into a DataFrame
df = pd.DataFrame(tasks)
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])
df['Duration'] = df['End'] - df['Start']

# Plotting
fig, ax = plt.subplots(figsize=(14, 8))

# Define a color map for tasks
colors = plt.cm.tab20.colors

# Create a list of patches for legend
patches_list = []

for task_index, task_row in df.iterrows():
    start_num = mdates.date2num(task_row['Start'])
    duration_days = task_row['Duration'].total_seconds() / (3600 * 24)
    color = colors[task_index % len(colors)]
    
    ax.barh(task_row['Task'], duration_days, left=start_num, color=color, edgecolor='black', height=0.4, 
            path_effects=[path_effects.SimpleLineShadow(), path_effects.Normal()])

    patches_list.append(patches.Patch(color=color, label=task_row['Task']))

# Formatting
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_minor_locator(DayLocator())
ax.xaxis.set_major_formatter(DateFormatter("%b %Y"))
#ax.set_xlabel('Time')
#ax.set_ylabel('Tasks')
#ax.set_title('Projects Gantt Chart')

# Add legend
#ax.legend(handles=patches_list, title='Tasks', bbox_to_anchor=(1.05, 1), loc='upper left', 
#           frameon=False, ncol=2, fontsize=10)

# Add grid lines and style
ax.grid(True, which='both', linestyle='--', linewidth=0.15, color='lightgray')
plt.tight_layout()

plt.savefig("gantt.png", bbox_inches='tight')
# Show plot
plt.show()
