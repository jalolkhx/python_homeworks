import pandas as pd

# Load Titanic dataset
titanic = pd.read_csv("titanic.csv")
# Group by 'Pclass' and aggregate
titanic_grouped = titanic.groupby("Pclass").agg(
    Avg_Age=("Age", "mean"),
    Total_Fare=("Fare", "sum"),
    Passenger_Count=("PassengerId", "count")
)
print("Grouped Aggregations on Titanic:")
print(titanic_grouped)

# Load Movie dataset
movies = pd.read_csv("movies.csv")
# Group by 'color' and 'director_name', then aggregate
movies_grouped = movies.groupby(["color", "director_name"]).agg(
    Total_Critic_Reviews=("num_critic_for_reviews", "sum"),
    Avg_Duration=("duration", "mean")
)
print("\nMulti-level Grouping on Movie Data:")
print(movies_grouped)

# Load Flights dataset
flights = pd.read_csv("flights.csv")
# Group by 'Year' and 'Month', then aggregate
flights_grouped = flights.groupby(["Year", "Month"]).agg(
    Total_Flights=("FlightNum", "count"),
    Avg_Arrival_Delay=("ArrDelay", "mean"),
    Max_Departure_Delay=("DepDelay", "max")
)
print("\nNested Grouping on Flights:")
print(flights_grouped)