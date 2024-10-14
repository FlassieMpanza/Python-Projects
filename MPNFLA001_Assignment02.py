import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel workbook
data = pd.read_excel('Temperature_data', engine='openpyxl')

# Select the rows corresponding to the countries and regions of interest
countries = ['South Africa', 'Namibia', 'Botswana', 'Zimbabwe', 'Mozambique', 'Lesotho', 'Eswatini']
regions = ['Africa']
selected_data = data[data['Country'].isin(countries + regions)]

# Calculate mean and standard deviation for each country and region
grouped_data = selected_data.groupby('Country')['Temperature Change']
mean_temperatures = grouped_data.mean()
std_temperatures = grouped_data.std()

# Set up the plots
num_plots = len(countries) + len(regions)
num_cols = 2
num_rows = (num_plots + 1) // num_cols

fig, axs = plt.subplots(num_rows, num_cols, figsize=(12, 16))
fig.suptitle('Temperature Changes', fontsize=20)

# Plot the temperature time series for each country and region
plot_counter = 0
for country in countries + regions:
    row = plot_counter // num_cols
    col = plot_counter % num_cols
    ax = axs[row, col]

    country_data = selected_data[selected_data['Country'] == country]
    years = country_data['Meteorological year']
    temperature_changes = country_data['Temperature Change']

    ax.plot(years, temperature_changes)
    ax.set_title(country, fontsize=14)
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature Change (°C)')

    # Add mean and standard deviation as text
    mean_temp = mean_temperatures[country]
    std_temp = std_temperatures[country]
    text = f"Mean: {mean_temp:.2f} °C ± {std_temp:.2f} °C"
    ax.text(0.05, 0.95, text, transform=ax.transAxes, fontsize=12, verticalalignment='top')

    plot_counter += 1

# Remove any unused subplots
if plot_counter < num_plots:
    for i in range(plot_counter, num_plots):
        row = i // num_cols
        col = i % num_cols
        fig.delaxes(axs[row, col])

# Adjust spacing between subplots
fig.tight_layout(rect=[0, 0, 1, 0.97])

# Save the output as a PDF
plt.savefig('Temperature Data.pdf')

# Show the plots
plt.show()

