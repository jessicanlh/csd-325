#Jessica Long-Heinicke Assignment 4.2 11.10.24

import csv
from datetime import datetime
from matplotlib import pyplot as plt
import sys

#file path to the data
filename = 'sitka_weather_2018_simple.csv'

#reads dates and temperatures from a CSV file, based on temp_type
def read_data(filename, temp_type='high'):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

    # Get dates and high temperatures from this file.
        dates, temps = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            #check if we want highs or lows
            temp = int(row[5] if temp_type == 'high' else row[6])
            temps.append(temp)
    return dates, temps

# Plot temperatures with dates and formats the graph
def plot_data(dates, temps, temp_type):
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c='red' if temp_type == 'high' else 'blue')

    # Format plot.
    plt.title("Daily {temp_type} temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

#main function to run the menu and user selection loop
def main():
    while True:
        #display menu options
        print("Please select an option from the menu:")
        print("1 - View High Temperatures")
        print("2 - View Low Temperatures")
        print("3 - Exit")

        choice = input("Enter your choice (1/2/3):")

        if choice == '1': #high temps
            dates, highs = read_data(filename, temp_type='high')
            plot_data(dates, highs, temp_type='high')

        elif choice == '2': #low temps
            dates, lows = read_data(filename, temp_type='low')
            plot_data(dates, lows, temp_type='low')

        elif choice == '3': #exit
            print("exiting the program. Thank you!")
            sys.exit()

        else: #invalid input
            print ("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()