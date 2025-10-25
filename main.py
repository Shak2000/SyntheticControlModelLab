import numpy as np


def main():
    db = np.genfromtxt(
        'gdp-per-capita-maddison-project-database.csv', delimiter=',',
        dtype=[('Entity', 'U100'), ('Code', 'U10'), ('Year', 'i4'), ('GDPPerCapita', 'f8'), ('annotations', 'U200')],
        encoding='utf-8')

    while True:
        quit = input('Please type "Q" to quit or anything else to continue: ')
        if len(quit) > 0 and quit[0].lower() == 'q':
            break
        country_selection = input('Please enter a comma-and-space-separated list of countries'
                                  '(e.g., "France, Germany, United Kingdom, United States"): ').strip()
        countries = country_selection.split(', ')

        min_year = None
        success = False
        while not success:
            try:
                min_year = int(input('Please enter the earliest year you would like to obtain data for: '))
                success = True
            except Exception as e:
                print(f'Error: {e}. The year should be an integer. Please try again.')

        max_year = None
        success = False
        while not success:
            try:
                max_year = int(input('Please enter the latest year you would like to obtain data for: '))
                if max_year < min_year:
                    raise ValueError(f'The latest year of {max_year} cannot be earlier than the earliest year of '
                                     f'{min_year}.')
                success = True
            except Exception as e:
                print(f"Error: {e}. The year should be an integer. Please try again.")

        country_column = db['Entity']
        year_column = db['Year']
        year_column_int = year_column.astype(int)
        country_mask = np.isin(country_column, countries)
        year_min_mask = year_column_int >= min_year
        year_max_mask = year_column_int <= max_year
        final_mask = country_mask & year_min_mask & year_max_mask
        filtered_data = db[final_mask]
        print(f'--- Data from {min_year} to {max_year} for the following countries: {country_selection} ---')
        print(filtered_data)


if __name__ == "__main__":
    main()
