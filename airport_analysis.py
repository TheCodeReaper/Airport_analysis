import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r'C:\Users\Souvik\OneDrive\Desktop\airlines_flights_data.csv')
route_matrix = df.pivot_table(
    index='source_city',         
    columns='destination_city',       
    values='flight',             
    aggfunc='count',
    fill_value=0)
plt.figure(figsize=(10, 7))
sns.heatmap(route_matrix, annot=True, fmt='d', cmap='YlGnBu')
plt.title('Heatmap of Flight Counts by Route')
plt.xlabel('Destination City')
plt.ylabel('Source City')
plt.tight_layout()
plt.show()

import pandas as pd
df = pd.read_csv(r'C:\Users\Souvik\OneDrive\Desktop\airlines_flights_data.csv') 
cheapest_routes = (
    df.groupby(['source_city', 'destination_city'])
      .agg({'price': 'mean', 'duration': 'mean', 'airline': lambda x: x.mode()[0]})
      .sort_values('price')
      .reset_index())
print("Top 5 Cheapest Routes:")
for idx, row in cheapest_routes.head(5).iterrows():
    print(f"- {row['source_city']} → {row['destination_city']}: {row['airline']} | Avg. price: ₹{int(row['price'])} | Duration: {row['duration']:.2f}hrs")
avg_price_by_departure = (
    df.groupby('departure_time')['price'].mean().sort_values())
print("\nAverage Price by Departure Time:")
for time_slot, price in avg_price_by_departure.items():
    print(f"{time_slot}: ₹{price:,.2f}")
best_time = avg_price_by_departure.idxmin()
print(f"\nRecommended Departure Time Slot for Cheapest Fares: {best_time}\n")
route_airline_prices = (
    df.groupby(['source_city', 'destination_city', 'airline'])['price'].mean().reset_index())
idx = route_airline_prices.groupby(['source_city', 'destination_city'])['price'].idxmin()
best_airline_route = route_airline_prices.loc[idx].sort_values('price')
print("Best Airline on Each Route (lowest avg price):")
for _, row in best_airline_route.head(5).iterrows():
    print(f"- {row['source_city']} → {row['destination_city']}: {row['airline']} | Avg. price: ₹{int(row['price'])}")
print("\nKey Recommendations:")
print(f"- Book flights departing in '{best_time}' time slot for lowest fares.")
print(f"- Cheapest route overall: {cheapest_routes.loc[0, 'source_city']} → {cheapest_routes.loc[0, 'destination_city']} with {cheapest_routes.loc[0, 'airline']} (₹{int(cheapest_routes.loc[0, 'price'])})")
print("- For each major route, prefer these airlines for lowest prices:")
for _, row in best_airline_route.head(5).iterrows():
    print(f"  {row['source_city']} → {row['destination_city']}: {row['airline']} (₹{int(row['price'])})")
