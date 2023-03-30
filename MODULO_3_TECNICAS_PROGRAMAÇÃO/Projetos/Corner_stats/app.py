from bs4 import BeautifulSoup
import pandas as pd
import requests

team_url = input("Acesse o site www.totalcorner.com, busque o time que deseja saber as estatisticas e cole a URL da pagina aqui\n")

html = requests.get(team_url).content

soup = BeautifulSoup(html, 'html.parser')

team_name = soup.find("meta", {"name":"description"})["content"]
team_name = team_name.split(",")[0].replace('Team: ','')
print(team_name)
first_half_corners_for = []
second_half_corners_for = []
match_corners_for = []
first_half_corners_against = []
second_half_corners_against = []
match_corners_against = []
total_match_corners = []
total_first_half_corners = []
total_second_half_corners =[]
home_or_away = []
corners_balance =[]



table_rows = soup.findAll("tr")
for rows in table_rows:
    if rows.find("span", class_="span_half_corner hide"):
        continue
    match = rows.find("td", class_="match_home")
    if match != None:
        home_team = match.find('a').text
    else:
        continue
    match = rows.find("td", class_="match_away")
    if match != None:
        away_team = match.find('a').text
    half_corners = rows.find("span", class_="span_half_corner").text
    match_corners = rows.find("span", class_="span_match_corner").text
    home_half_corners = half_corners.replace('(','').replace(')','').split('-')[0]
    away_half_corners = half_corners.replace('(','').replace(')','').split('-')[1]
    home_match_corners = match_corners.split(' ')[0]
    away_match_corners = match_corners.split(' ')[-1]
    home_second_half_corners = int(home_match_corners) - int(home_half_corners)
    away_second_half_corners = int(away_match_corners) - int(away_half_corners)
    if home_team == team_name:
        balance = int(home_match_corners) - int(away_match_corners)
        second_half_corners_for.append(home_second_half_corners)
        match_corners_for.append(home_match_corners)
        first_half_corners_against.append(away_half_corners)
        second_half_corners_against.append(away_second_half_corners)
        match_corners_against.append(away_match_corners)
        total_match_corners.append(int(home_match_corners) + int(away_match_corners))
        total_first_half_corners.append(int(home_half_corners) + int(away_half_corners))
        total_second_half_corners.append(int(home_second_half_corners) + int(away_second_half_corners))
        home_or_away.append('Home')
        corners_balance.append(balance)
    else:
        balance = int(away_match_corners) - int(home_match_corners)
        first_half_corners_for.append(away_half_corners)
        second_half_corners_for.append(away_second_half_corners)
        match_corners_for.append(away_match_corners)
        first_half_corners_against.append(home_half_corners)
        second_half_corners_against.append(home_second_half_corners)
        match_corners_against.append(home_match_corners)
        total_match_corners.append(int(home_match_corners) + int(away_match_corners))
        total_first_half_corners.append(int(home_half_corners) + int(away_half_corners))
        total_second_half_corners.append(int(home_second_half_corners) + int(away_second_half_corners))
        home_or_away.append('Home')
        corners_balance.append(balance)
    
df = pd.DataFrame(list(zip(
        first_half_corners_for,
        second_half_corners_for,
        match_corners_for,
        first_half_corners_against,
        second_half_corners_against,
        match_corners_against,
        total_match_corners,
        total_first_half_corners,
        total_second_half_corners,
        home_or_away,
        corners_balance,
    )),
    columns=[
        'first_half_corners_for',
        'second_half_corners_for',
        'match_corners_for',
        'first_half_corners_against',
        'second_half_corners_against',
        'match_corners_against',
        'total_match_corners',
        'total_first_half_corners',
        'total_second_half_corners',
        'home_or_away',
        'corners_balance',
    
    ])
print(df[['total_first_half_corners',
        'total_second_half_corners',
        'total_match_corners',
        'corners_balance']].describe())
    