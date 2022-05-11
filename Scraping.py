import requests  
from bs4 import BeautifulSoup
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.YnsmwvNBzIU")  #  скачиваем страницу    
soup = BeautifulSoup(page.content, 'html.parser')  #  магия 
seven_day = soup.find(id="seven-day-forecast")  #  находим div (что такое див, магия)
forecast_items = seven_day.find_all(class_="tombstone-container")  #  в div ищем контейнер, который выделяет все периоды времени (именно div контейнер)
tonight = forecast_items[0]  #  выделяем первый прогноз
print(tonight)