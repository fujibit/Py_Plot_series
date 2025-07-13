# Import all the necessary packages and libraries in the code
import matplotlib.pyplot as plt
# Creating a user-defined function called explode

def explode(values, months, colors):
    # Defining the size of the figure
    plt.figure(figsize=(9, 9))
    # Plotting the pie chart
    plt.pie(values, labels=months, shadow=True,
            colors=colors, startangle=90, radius=1.2)
    plt.legend(values, loc='center left', bbox_to_anchor=(-0.35, .5), fontsize=8)
    plt.title("Demonstrating to avoid overlapping in pie chart")
    # Displaying the pie chart
    plt.show()
# Creating the main function

def main():
    # Creating a dataset for the chart
    values = [24, 64, 54, 10, 45, 1, 3, 9, 2, 71, 77, 77]
    # Defining the label
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Defining the color of the pie chart sectors
    colors = ['yellowgreen', 'red', 'gold', 'lightskyblue',
              'white', 'lightcoral', 'blue', 'pink', 'darkgreen',
              'yellow', 'grey', 'violet', 'magenta', 'cyan']
    # Calling the function to plot the graph
    explode(values, months, colors)

# Calling the main function
if __name__ == '__main__':
    main()
Output:
