import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }

#Define month and day lists, with all included to choose.
months = {'all', 'january', 'february', 'march' , 'april', 'may', 'june'}
days = {'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('\nHello! Let\'s Explore Some US Bikeshare Data! First Please Select City, Seccondly Month And Then Day.')

    # Get user input for a city filter from the dataframe (chicago, new york city, washington).
    while True:
        city = input('\nPlease Select First Chicago, New York City Or Washington: ').lower()
        if city in CITY_DATA:
            print("\nGreat!, {} Is Selected.".format(city.capitalize()))
            break
        else:
            print("\nOps!, Please Choose One Of The Three Cities: Chicago, New York City or Washington.")

    # Get user input for a month filter from the dataframe (all, january, february, ... , june).
    while True:
        month = input('Please, Choose One Of The Following Months: January, February, March, April, May, June or All: ').lower()
        if month in months:
            print ("\nGreat!, {} Is Selected.".format(month.capitalize()))
            break
        elif month == 'all':
            print("\nNo Filter For Month Chosen.")
            break
        else:
            print("\nOps!, Please Choose A Valid Month Between January And June Or All.")

    # Get user input for a day filter from the dataframe (all, monday, tuesday, ... sunday).
    while True:
        day = input('Please, Choose One Day Of The Week, E.G. Friday Or All: ').lower()
        if day in days:
            print("\nGreat!, {} Is Selected.".format(day.capitalize()))
            break
        elif day == 'all':
            print("\nNo Filter For Days Chosen.")
            break
        else:
            print('\nOps!, Please Choose A Valid Day Of The Week, E.G. Friday Or All')
            
    # Print a line for better overview and return city, month and day.
    print('-'*40)
    return city, month, day

def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
    df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # Load the chosen data file for city into a dataframe.
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start Time column to datetime.
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month from the Start Time column to create an month column.
    df['month'] = df['Start Time'].dt.month
 
    # Extract day from the Start Time column to create an weekday column.   
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Extract hour from the Start Time column to create an hour column.
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable.
    if month != 'all':

        # Use the index of the months list to get the corresponding int.
        month_name = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month_name.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable.
    if day != 'all':
    
        # Use the index of the days list to get the corresponding int.
        day_name = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = day_name.index(day)
        
        # Filter by day of week to create the new dataframe.
        df[df['day_of_week'] == day]

    return df

def show_head_of_data(df):
    
    # Ask the user: start by viewing the first few rows of the chosen dataset!
    print('One More Question. Are You Interested To See The Head Of The Chosen City Data?')
    
    i = 0
    feedback = input('\nPlease, Choose Yes Or No To Continue With Data Analytics: ').lower()
    pd.set_option('display.max_columns',200)

    while True:            
        if feedback == 'no':
            break
        elif feedback == 'yes':
            print(df.head())
            feedback = input("\nPlease, Choose 'Yes' Again For Head Of Data Or 'No' To Continue With Data Analytics: ")
            i += 5
        else:
            feedback = input("\nYour Input Is Invalid. Please Enter Only 'Yes' Or 'No': ").lower()
   
    print('-'*40)

    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Find and display the most common month.
    most_common_month = df['month'].mode()[0]
    print('Most Popular Month Is: ', most_common_month)

    # Find and display the most common day of week.
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Popular Day Is: ', most_common_day)

    # Find and display the most common start hour.
    most_common_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour Is: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Find and display the most common start station.
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station Is: ', most_common_start_station)

    # Find and display the most common end station.
    most_common_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station Is: ', most_common_end_station)

    # Find and display the most common combination of start station and end station.
    df['start_end'] = df['Start Station']+ 'to' + df['End Station']
    most_common_combistatin = df['start_end'].mode().values[0]
    print('Most Popular Combination Of Start Station And End Station Is: ', most_common_combistatin)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Find and display the total travel time.
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = time.strftime("%H:%M:%S", time.gmtime(total_travel_time))
    print('The Total Travel Time Is (H:M:S): ', total_travel_time)

    # Find and display the mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = time.strftime("%H:%M:%S", time.gmtime(mean_travel_time))
    print('The Mean Travel Time Is (H:M:S): ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Find and Display the counts of user types.
    user_types = df['User Type'].value_counts()
    print('The Count of User Type Is: ', user_types)

    # Find and Display the counts of gender (only available for Chicago and NYC).
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print('\nThe Counts Of Genders Are:\n', gender)
    else:
        print("\nNo Gender Data For Washington DC Available.")
    
    # Find and Display the earliest, the most recent, and the most common year of birth (only available for Chicago and NYC).
    if city != 'washington':
        earliest_year_of_birth = int(df['Birth Year'].min()) # int for date in correct view 1989 not 1989.0
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print('\nThe Earlist Year Of Birth Is: {}\nThe Most Recent Year Of Birth Is: {}\nThe Most Common Year Of Birth Is: {}' \
            .format(earliest_year_of_birth, most_recent_year_of_birth, most_common_year_of_birth))
    else:
        print("\nNo Birth Data For Washington DC Available.")
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        show_head_of_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
