# 🛫 Flight Fare Analysis (Python + Pandas)

A clean and insightful **Flight Fare Analysis** project built using Python and Pandas. It analyzes airline pricing data to discover the **cheapest routes**, **best departure time slots**, **most cost-effective airlines**, and **popular flight paths visualized via a heatmap**. Perfect for beginners in data analysis and airline pricing studies.

---

## 📊 Features

- ✅ Top 5 cheapest city-to-city flight routes
- ⏰ Analyzes **average fare by departure time slot**
- ✈️ Finds **best airline for each route**
- 🧭 Visualizes flight **route frequency using a heatmap**
- 📌 Provides clear **recommendations** for cost-saving travel
- 🧠 Uses real-world data and powerful `groupby` + aggregation logic
- 📂 Clean, modular script ready for Jupyter or Python execution

---

## 📁 Dataset Requirements

Your CSV file should include the following columns:

| Column Name        | Description                                             |
|--------------------|---------------------------------------------------------|
| `source_city`      | City where the flight originates                        |
| `destination_city` | City where the flight lands                             |
| `price`            | Ticket price in INR                                     |
| `duration`         | Duration of the flight (in minutes/hours)               |
| `airline`          | Name of the airline                                     |
| `departure_time`   | Time slot when flight departs (e.g., Morning, Evening)  |
| `flight`           | Flight identifier or count for route frequency analysis |

📝 **Filename Example**: `airlines_flights_data.csv`

---

## 🖼️ Screenshots

<img width="1052" height="778" alt="Screenshot 2025-08-08 221302" src="https://github.com/user-attachments/assets/1b56b2e6-97c8-4f83-abca-0b8a1a17090a" />
<img width="698" height="637" alt="Screenshot 2025-08-08 221329" src="https://github.com/user-attachments/assets/ba684ae9-370e-4662-88d0-068c20bb9e7c" />

---

## 🚀 How to Run

1. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn
