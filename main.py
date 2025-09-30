import matplotlib.pyplot as plt
import pandas as pd

def create_plot(df, x_column, y_column, title, x_label, y_label, plot_type):
    plt.figure(figsize=(10, 5))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label) 
    plt.grid(True)
    if plot_type == "scatter":
        plt.scatter(df[x_column], df[y_column], label=y_column)
    elif plot_type == "line":
        plt.plot(df[x_column], df[y_column], label=y_column)
    elif plot_type == "bar":
        plt.bar(df[x_column], df[y_column], label=y_column)
    else: 
        return
    plt.legend()
    plt.show()

if __name__ == "__main__":
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Units Sold': [150, 175, 210, 180, 250]
    }
    df = pd.DataFrame(data)

    # Call the fixed function to create a bar chart
    create_plot(
        df=df,
        x_column='Month',
        y_column='Units Sold',
        title='Monthly Unit Sales',
        x_label='Month',
        y_label='Number of Units Sold',
        plot_type='bar'
    )