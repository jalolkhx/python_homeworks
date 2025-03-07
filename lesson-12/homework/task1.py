from bs4 import BeautifulSoup
with open("weather.html", 'r', encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

data = soup.find("tbody").find_all("tr")

weather_data = [] 
for i in data:
    daily_data = i.find_all("td")
    day = daily_data[0].text.strip()
    temp = int(daily_data[1].text.strip().replace("°C", ""))
    condition = daily_data[2].text.strip()
    weather_data.append({"day": day, "temperature": temp, "condition": condition})

print("5 Day Weather Forecast:")
for i in weather_data:
    print(str(i).replace('{','').replace('}','').replace("'", ""))

max_temp = max(i["temperature"] for i in weather_data)
for i in weather_data:
    if i["temperature"] == max_temp:
        print(i["day"])
        break

sum_temp = 0
num_days = 0
for i in weather_data:
    sum_temp += i["temperature"]
    num_days = num_days + 1

print(sum_temp/num_days)

