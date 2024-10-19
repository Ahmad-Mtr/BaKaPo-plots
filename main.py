import pandas as pd
import matplotlib.pyplot as plt

# I hate white interfaces, so I've searched for ways to customize the Colors and used a Color Scheme
text = "#cdd6f4"
sky = "#89dceb"
mauve = "#cba6f7"
red = "#F56991"
blue = '#89b4fa'
green = '#a6e3a1'
peach = "#fab387"
yellow = "#f9e2af"
surface = "#585b70"
base = "#1e1e2e"
crust = "#11111b"

data = pd.read_excel('data/employees_jordan_data.xlsx')


def plotLine():
    # Load data
    line_data = data.sort_values('Experience (Years)')

    # Line chart: Salary by Experience
    plt.figure(figsize=(10, 6), facecolor=base, edgecolor='blue')
    # to set the Colors
    ax = plt.axes()
    ax.set_facecolor(base)
    ax.spines['left'].set_color(surface)
    ax.spines['bottom'].set_color(surface)

    plt.plot(line_data['Experience (Years)'], line_data['Salary'],
             marker='o',
             linestyle='-',
             color=sky,  # LIne COlor
             linewidth=1,  # Added to make lines more visible
             markersize=6, )

    plt.title('Salary vs Experience', color=text)
    plt.xlabel('Experience (Years)', color=text, )
    plt.ylabel('Salary', color=text)
    plt.xticks(color=text)
    plt.yticks(color=text)
    plt.grid(True, linestyle='--', color=surface)
    plt.tight_layout()
    plt.savefig('plot-line.png', dpi=300, bbox_inches='tight', facecolor=base)
    plt.close()


def plotPie():
    # 2. Pie Chart - Department Distribution
    plt.figure(figsize=(10, 8), facecolor=base, edgecolor='blue')

    dept_counts = data['Department'].value_counts()
    plt.pie(dept_counts.values, labels=dept_counts.index, autopct='%1.1f%%', startangle=90,
            colors=[red, peach, green, blue, mauve])
    plt.title('Employee Distribution by Department', color=text)
    plt.axis('equal')
    plt.savefig('plot-pie.png', dpi=300, bbox_inches='tight', facecolor=base)
    plt.close()


def plotStackedBar():
    # 3. Stacked Bar Chart - Gender Distribution across Departments
    plt.figure(figsize=(10, 8), facecolor=base)
    gender_dept = pd.crosstab(data['Department'], data['Gender'])
    axes = plt.axes()
    axes.set_facecolor(base)
    axes.spines['left'].set_color(surface)
    axes.spines['bottom'].set_color(surface)

    gender_dept.plot(kind='bar', stacked=True, color=[red, blue], ax=axes)  # Set bar colors

    plt.title('Gender Distribution Across Departments', color=text)
    plt.xlabel('Department', color=text)
    plt.ylabel('Number of Employees', color=text)

    legend = plt.legend(title='Gender')
    legend.get_frame().set_facecolor(color=crust)
    legend.get_title().set_color(text)
    for text_item in legend.get_texts():
        text_item.set_color(text)

    plt.xticks(rotation=45)
    # Customize tick colors
    plt.tick_params(colors=text, which='both')
    plt.grid(True, color=surface, linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.savefig('plot-stacked-bar.png', dpi=300, bbox_inches='tight', facecolor=base)
    plt.close()


def plotBar():
    # 4. Bar Chart - Average Performance Score by Department
    plt.figure(figsize=(10, 6), facecolor=base, edgecolor='blue')
    ax = plt.axes()
    ax.set_facecolor(base)
    ax.spines['left'].set_color(surface)
    ax.spines['bottom'].set_color(surface)

    avg_perf = data.groupby('Department')['Performance Score'].mean().sort_values(ascending=False)
    avg_perf.plot(kind='bar', color=sky)
    plt.title('Average Performance Score by Department', color=text)
    plt.xlabel('Department', color=text)
    plt.ylabel('Average Performance Score', color=text)
    plt.xticks(rotation=45)
    plt.tick_params(colors=text, which='both')
    plt.grid(True, color=surface, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig('plot-bar.png', dpi=300, bbox_inches='tight', facecolor=base)
    plt.close()


def plotBox():

    plt.figure(figsize=(12, 6), facecolor=base, edgecolor='blue')
    ax = plt.axes()
    ax.set_facecolor(base)

    ax.spines['left'].set_color(surface)
    ax.spines['bottom'].set_color(surface)
    ax.spines['top'].set_color(surface)
    ax.spines['right'].set_color(surface)

    # Extracting data for box plot
    age = data['Age']
    salary = data['Salary']/1000
    # Creating a box plot
    plt.boxplot([age, salary],
                tick_labels=['Age', 'Salary (In thousands)'],
                patch_artist=True,  # Fill boxes with color
                medianprops={'color': text},  # Median line color
                flierprops={'markerfacecolor': red,  # Outlier color
                               'marker': 'o'},
                boxprops={'facecolor': sky,  # Box fill color
                         'color': green},  # Box edge color
                whiskerprops={'color': surface},  # Whisker color
                capprops={'color': surface}
                )  # Cap color

    plt.title('Box Plot of Age & Salary ', color=text)
    plt.xlabel('Variable', color=text)
    plt.ylabel('Frequency', color=text)
    plt.tick_params(colors=text, which='both')
    plt.grid(True, color=surface, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig('plot-box.png', dpi=300, bbox_inches='tight', facecolor=base)
    plt.close()


def plotScatter():
    # 6. Scatter Plot - Experience vs Salary with Performance Score as color
    plt.figure(figsize=(10, 6), facecolor=base, edgecolor='blue')
    ax = plt.axes()
    ax.set_facecolor(base)
    ax.spines['left'].set_color(surface)
    ax.spines['bottom'].set_color(surface)
    plt.scatter(data['Experience (Years)'], data['Salary'],
                          color=sky,
                          s=100, )
    plt.title('Experience vs Salary', color=text)
    plt.xlabel('Experience (Years)', color=text)
    plt.ylabel('Salary', color=text)
    plt.tick_params(colors=text, which='both')
    plt.grid(True, color=surface, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig('plot-scatter.png', dpi=300, bbox_inches='tight', facecolor=base)
    plt.close()


# plt.xticks(color=text)
##plt.yticks(color=text)
# plt.grid(True, linestyle='--', color=surface)


# Convert Joining Date to datetime
data['Joining Date'] = pd.to_datetime(data['Joining Date'])



plotLine()
plotPie()
plotStackedBar()
plotBar()
plotBox()
plotScatter()
