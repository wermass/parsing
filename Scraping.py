import requests  
from bs4 import BeautifulSoup
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.YnsmwvNBzIU")  #  скачиваем страницу    
soup = BeautifulSoup(page.content, 'html.parser')  #  магия 
seven_day = soup.find(id="seven-day-forecast")  #  находим div (что такое див, магия)
forecast_items = seven_day.find_all(class_="tombstone-container")  #  в div ищем контейнер, который выделяет все периоды времени (именно div контейнер)
tonight = forecast_items[0]  #  выделяем первый прогноз
period = tonight.find(class_="period-name").get_text()  #  из переменной tonight при помози методы .find извлекаем из класса 'period-name' информацию, .get_text() это магия, но она убирает теги.
short_desc = tonight.find(class_='short-desc').get_text()
temp = tonight.find(class_='temp').get_text()
print(period, short_desc, temp, sep='\n')