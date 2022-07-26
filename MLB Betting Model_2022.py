import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


class ChromeDriverManager:
    pass


driver = webdriver.Chrome(executable_path='/Users/dylanelder/Desktop/Python-SL/chromedriver')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'}

#Lines 16-18 below access local files which are downloaded daily using the program titled "FanGraphs Exports"
df_SP = pd.read_csv(r'/Users/dylanelder/Downloads/FanGraphs Leaderboard - 2022-07-26T150928.690.csv')
df_splits_L = pd.read_csv(r'/Users/dylanelder/Downloads/Splits Leaderboard Data vs LHP - 2022-07-26T150933.218.csv')
df_splits_R = pd.read_csv(r'/Users/dylanelder/Downloads/Splits Leaderboard Data vs RHP - 2022-07-26T150934.378.csv')

df_SP = df_SP[((df_SP['Name'] == 'Luis Garcia') & (df_SP['Team'] != 'HOU') == False)] #This line handles an exception for two players with the same name


#Lines 24-126 create dictionaires to later be filled with data
output = {
    'Away Team': [],
    'Home Team': [],
    'Away Players': [],
    'Home Players': [],
    'Away Salary': [],
    'Home Salary': [],
    'Away Pitcher Salary': [],
    'Home Pitcher Salary': [],
    'Away Pitcher Hand': [],
    'Home Pitcher Hand': [],
    'Away Pitcher Name': [],
    'Home Pitcher Name': [],
}

odds = {
    'DK Teams': [],
    'ML': [],
    'DK Name': [],
}

strikeouts_batting = {
    'TR Teams': [],
    '2022 Strikeout% Batting': [],
    'Last3 Strikeout% Batting': [],
    'Last1 Strikeout% Batting': [],
}

hr_batting = {
    'TR Teams': [],
    '2022 HR% Batting': [],
    'Last3 HR% Batting': [],
    'Last1 HR% Batting': [],
}

total_bases_batting = {
    'TR Teams': [],
    '2022 Total Bases': [],
    'Last3 Total Bases': [],
    'Last1 Total Bases': [],
}

stolen_bases = {
    'TR Teams': [],
    '2022 Stolen Bases': [],
    'Last3 Stolen Bases': [],
    'Last1 Stolen Bases': [],
}

iso = {
    'TR Teams': [],
    '2022 ISO': [],
    'Last3 ISO': [],
    'Last1 ISO': [],
}

babip = {
    'TR Teams': [],
    '2022 BABIP': [],
    'Last3 BABIP': [],
    'Last1 BABIP': [],
}

ops = {
    'TR Teams': [],
    '2022 OPS': [],
    'Last3 OPS': [],
    'Last1 OPS': [],
}

rpg = {
    'TR Teams': [],
    '2022 RPG': [],
    'Last3 RPG': [],
    'Last1 RPG': [],
}

errors = {
    'TR Teams': [],
    '2022 Errors': [],
    'Last3 Errors': [],
    'Last1 Errors': [],
    '2021 Errors': [],
}

statcast = {
    'FG Teams': [],
    'maxEV': [],
    'LA': [],
    'Barrel%': [],
    'HardHit%': [],
}

bullpen = {
    'FG Teams': [],
    'Bullpen K/BB': [],
    'Bullpen HR/9': [],
    'Bullpen AVG': [],
    'Bullpen WHIP': [],
    'Bullpen ERA': [],
    'Bullpen xFIP': [],

}




#Lines 132-384 are a series of functions that scrape data from various websites
def getStrikeouts():
    url = 'https://www.teamrankings.com/mlb/stat/strikeout-pct'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        strikeouts_batting['TR Teams'].append(td[1].text)
        strikeouts_batting['2022 Strikeout% Batting'].append(td[2].text)
        strikeouts_batting['Last3 Strikeout% Batting'].append(td[3].text)
        strikeouts_batting['Last1 Strikeout% Batting'].append(td[4].text)

    return


def getHR():
    url = 'https://www.teamrankings.com/mlb/stat/home-run-pct'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        hr_batting['TR Teams'].append(td[1].text)
        hr_batting['2022 HR% Batting'].append(td[2].text)
        hr_batting['Last3 HR% Batting'].append(td[3].text)
        hr_batting['Last1 HR% Batting'].append(td[4].text)

    return


def getTotalBases():
    url = 'https://www.teamrankings.com/mlb/stat/total-bases-per-game'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        total_bases_batting['TR Teams'].append(td[1].text)
        total_bases_batting['2022 Total Bases'].append(td[2].text)
        total_bases_batting['Last3 Total Bases'].append(td[3].text)
        total_bases_batting['Last1 Total Bases'].append(td[4].text)

    return


def getStolenBases():
    url = 'https://www.teamrankings.com/mlb/stat/stolen-bases-per-game'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        stolen_bases['TR Teams'].append(td[1].text)
        stolen_bases['2022 Stolen Bases'].append(td[2].text)
        stolen_bases['Last3 Stolen Bases'].append(td[3].text)
        stolen_bases['Last1 Stolen Bases'].append(td[4].text)

    return


def getISO():
    url = 'https://www.teamrankings.com/mlb/stat/isolated-power'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        iso['TR Teams'].append(td[1].text)
        iso['2022 ISO'].append(td[2].text)
        iso['Last3 ISO'].append(td[3].text)
        iso['Last1 ISO'].append(td[4].text)

    return


def getBABIP():
    url = 'https://www.teamrankings.com/mlb/stat/batting-average-on-balls-in-play'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        babip['TR Teams'].append(td[1].text)
        babip['2022 BABIP'].append(td[2].text)
        babip['Last3 BABIP'].append(td[3].text)
        babip['Last1 BABIP'].append(td[4].text)

    return


def getOPS():
    url = 'https://www.teamrankings.com/mlb/stat/on-base-plus-slugging-pct'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        ops['TR Teams'].append(td[1].text)
        ops['2022 OPS'].append(td[2].text)
        ops['Last3 OPS'].append(td[3].text)
        ops['Last1 OPS'].append(td[4].text)

    return


def getRPG():
    url = 'https://www.teamrankings.com/mlb/stat/runs-per-game'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        rpg['TR Teams'].append(td[1].text)
        rpg['2022 RPG'].append(td[2].text)
        rpg['Last3 RPG'].append(td[3].text)
        rpg['Last1 RPG'].append(td[4].text)

    return


def getErrors():
    url = 'https://www.teamrankings.com/mlb/stat/errors-per-game'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        errors['TR Teams'].append(td[1].text)
        errors['2022 Errors'].append(td[2].text)
        errors['Last3 Errors'].append(td[3].text)
        errors['Last1 Errors'].append(td[4].text)
        errors['2021 Errors'].append(td[7].text)

    return


def getOdds():
    driver = webdriver.Chrome(executable_path='/Users/dylanelder/Desktop/Python-SL/chromedriver')
    driver.get('https://sportsbook.draftkings.com/leagues/baseball/88670847')
    print('Acquiring Current MLB Betting Odds...')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    stat_table = soup.find('div', class_='parlay-card-10-a')
    print(len(stat_table), stat_table)

    for item in stat_table:
        rows = item.find_all('tr')

    for name in rows:
        name = name.find_all('div', class_='event-cell__name-text')

        if name == []:
            continue

        odds['DK Teams'].append(name[0].text)

    for ML in rows:
        ML = ML.find_all('span', class_='sportsbook-odds american no-margin default-color')

        if ML == []:
            continue

        odds['ML'].append(ML[0].text)

    for pitcher in rows:
        pitcher = pitcher.find_all('div', class_='event-cell__label')

        if pitcher == []:
            continue

        odds['DK Name'].append(pitcher[0].text)

    return


def getStatcast():
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=24&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=&enddate='
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', class_='rgMasterTable')
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        statcast['FG Teams'].append(td[1].text)
        statcast['maxEV'].append(td[5].text)
        statcast['LA'].append(td[6].text)
        statcast['Barrel%'].append(td[8].text)
        statcast['HardHit%'].append(td[10].text)

    return


def getBullpen():
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=rel&lg=all&qual=0&type=1&season=2022&month=1000&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-10-01'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', class_='rgMasterTable')
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        bullpen['FG Teams'].append(td[1].text)
        bullpen['Bullpen K/BB'].append(td[4].text)
        bullpen['Bullpen HR/9'].append(td[5].text)
        bullpen['Bullpen AVG'].append(td[9].text)
        bullpen['Bullpen WHIP'].append(td[10].text)
        bullpen['Bullpen ERA'].append(td[16].text)
        bullpen['Bullpen xFIP'].append(td[19].text)

    return


#Lines 388-399 call the functions to scrape the data
getOdds()
getStrikeouts()
getHR()
getTotalBases()
getStolenBases()
getISO()
getBABIP()
getOPS()
getRPG()
getErrors()
getBullpen()
getStatcast()



if odds:
    odds_df = pd.DataFrame(odds)
else:
    odds_df = False

#Lines 409-419 organize the data into dataframes
df_strikeouts = pd.DataFrame(strikeouts_batting)
df_hr = pd.DataFrame(hr_batting)
df_totalbases = pd.DataFrame(total_bases_batting)
df_stolenbases = pd.DataFrame(stolen_bases)
df_iso = pd.DataFrame(iso)
df_babip = pd.DataFrame(babip)
df_ops = pd.DataFrame(ops)
df_rpg = pd.DataFrame(rpg)
df_errors = pd.DataFrame(errors)
df_bullpen = pd.DataFrame(bullpen)
df_statcast = pd.DataFrame(statcast)


#Lines 423-456 create new dataframes to later join data based on the different team names on different websites
df_odds_target = pd.DataFrame({'DK Teams': ['ARI Diamondbacks', 'ATL Braves', 'BAL Orioles', 'BOS Red Sox', 'CHI Cubs',
                                            'CHI White Sox', 'CIN Reds', 'CLE Guardians', 'COL Rockies', 'DET Tigers',
                                            'HOU Astros', 'KC Royals', 'LA Angels', 'LA Dodgers', 'MIA Marlins',
                                            'MIL Brewers', 'MIN Twins', 'NY Mets', 'NY Yankees', 'OAK Athletics',
                                            'PHI Phillies', 'PIT Pirates', 'SD Padres', 'SEA Mariners', 'SF Giants',
                                            'STL Cardinals', 'TB Rays', 'TEX Rangers', 'TOR Blue Jays',
                                            'WAS Nationals'],
                               'TR Teams': ['Arizona', 'Atlanta', 'Baltimore', 'Boston', 'Chi Cubs', 'Chi Sox',
                                            'Cincinnati', 'Cleveland', 'Colorado', 'Detroit', 'Houston', 'Kansas City',
                                            'LA Angels', 'LA Dodgers', 'Miami', 'Milwaukee', 'Minnesota', 'NY Mets',
                                            'NY Yankees', 'Oakland', 'Philadelphia', 'Pittsburgh', 'San Diego',
                                            'Seattle', 'SF Giants', 'St. Louis', 'Tampa Bay', 'Texas', 'Toronto',
                                            'Washington']})

df_target = pd.DataFrame({'TR Teams': ['Arizona', 'Atlanta', 'Baltimore', 'Boston', 'Chi Cubs', 'Chi Sox', 'Cincinnati',
                                       'Cleveland', 'Colorado', 'Detroit', 'Houston', 'Kansas City', 'LA Angels',
                                       'LA Dodgers', 'Miami', 'Milwaukee', 'Minnesota', 'NY Mets', 'NY Yankees',
                                       'Oakland', 'Philadelphia', 'Pittsburgh', 'San Diego', 'Seattle', 'SF Giants',
                                       'St. Louis', 'Tampa Bay', 'Texas', 'Toronto', 'Washington']})

df_odds_target1 = pd.DataFrame({'DK Teams': ['ARI Diamondbacks', 'ATL Braves', 'BAL Orioles', 'BOS Red Sox', 'CHI Cubs',
                                             'CHI White Sox', 'CIN Reds', 'CLE Guardians', 'COL Rockies', 'DET Tigers',
                                             'HOU Astros', 'KC Royals', 'LA Angels', 'LA Dodgers', 'MIA Marlins',
                                             'MIL Brewers', 'MIN Twins', 'NY Mets', 'NY Yankees', 'OAK Athletics',
                                             'PHI Phillies', 'PIT Pirates', 'SD Padres', 'SEA Mariners', 'SF Giants',
                                             'STL Cardinals', 'TB Rays', 'TEX Rangers', 'TOR Blue Jays',
                                             'WAS Nationals'],
                                'FG Teams': ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET',
                                             'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK',
                                             'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']})

df_target1 = pd.DataFrame({'FG Teams': ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU',
                                        'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT',
                                        'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']})


#Lines 460-591 merge dataframes together and clean/organize data into a usable format
inner_join_odds = pd.merge(odds_df,
                           df_odds_target,
                           on='DK Teams',
                           how='left')

inner_join1 = pd.merge(df_target,
                       df_strikeouts,
                       on='TR Teams',
                       how='left')

inner_join2 = pd.merge(inner_join1,
                       df_hr,
                       on='TR Teams',
                       how='left')

inner_join3 = pd.merge(inner_join2,
                       df_totalbases,
                       on='TR Teams',
                       how='left')

inner_join4 = pd.merge(inner_join3,
                       df_stolenbases,
                       on='TR Teams',
                       how='left')

inner_join5 = pd.merge(inner_join4,
                       df_iso,
                       on='TR Teams',
                       how='left')

inner_join6 = pd.merge(inner_join5,
                       df_rpg,
                       on='TR Teams',
                       how='left')

inner_join7 = pd.merge(inner_join6,
                       df_errors,
                       on='TR Teams',
                       how='left')

inner_joinOPS = pd.merge(inner_join7,
                         df_ops,
                         on='TR Teams',
                         how='left')

inner_joinBABIP = pd.merge(inner_joinOPS,
                           df_babip,
                           on='TR Teams',
                           how='left')

inner_join8 = pd.merge(df_target1,
                       df_statcast,
                       on='FG Teams',
                       how='left')

inner_join10 = pd.merge(inner_join8,
                        df_bullpen,
                        on='FG Teams',
                        how='left')

inner_join9 = inner_join_odds



df_splits_L = df_splits_L.drop(df_splits_L.columns[[0, 2, 3, 4, 7, 8]], axis=1)
df_splits_R = df_splits_R.drop(df_splits_R.columns[[0, 2, 3, 4, 7, 8]], axis=1)

df_splits_L['FG Teams'] = df_splits_L['Tm']
df_splits_L['ISO vs L'] = df_splits_L['ISO']
df_splits_L['AVG vs L'] = df_splits_L['AVG']
df_splits_L['BB/K vs L'] = df_splits_L['BB/K']
df_splits_L['OPS vs L'] = df_splits_L['OPS']
df_splits_L['BABIP vs L'] = df_splits_L['BABIP']
df_splits_L['wRC vs L'] = df_splits_L['wRC']
df_splits_L['wRAA vs L'] = df_splits_L['wRAA']
df_splits_L['wOBA vs L'] = df_splits_L['wOBA']
df_splits_L['wRC+ vs L'] = df_splits_L['wRC+']

df_splits_R['FG Teams'] = df_splits_R['Tm']
df_splits_R['ISO vs R'] = df_splits_R['ISO']
df_splits_R['AVG vs R'] = df_splits_R['AVG']
df_splits_R['BB/K vs R'] = df_splits_R['BB/K']
df_splits_R['OPS vs R'] = df_splits_R['OPS']
df_splits_R['BABIP vs R'] = df_splits_R['BABIP']
df_splits_R['wRC vs R'] = df_splits_R['wRC']
df_splits_R['wRAA vs R'] = df_splits_R['wRAA']
df_splits_R['wOBA vs R'] = df_splits_R['wOBA']
df_splits_R['wRC+ vs R'] = df_splits_R['wRC+']

df_splits_L1 = df_splits_L[
    ['FG Teams', 'ISO vs L', 'AVG vs L', 'BB/K vs L', 'OPS vs L', 'BABIP vs L', 'wRC vs L', 'wRAA vs L', 'wOBA vs L',
     'wRC+ vs L']]
df_splits_R1 = df_splits_R[
    ['FG Teams', 'ISO vs R', 'AVG vs R', 'BB/K vs R', 'OPS vs R', 'BABIP vs R', 'wRC vs R', 'wRAA vs R', 'wOBA vs R',
     'wRC+ vs R']]

inner_join11 = pd.merge(inner_join10,
                        df_splits_L1,
                        on='FG Teams',
                        how='left')

inner_join12 = pd.merge(inner_join11,
                        df_splits_R1,
                        on='FG Teams',
                        how='left')

inner_join9 = inner_join9.set_index('TR Teams')
inner_joinBABIP.set_index('TR Teams', inplace=True)
full_data = inner_joinBABIP.join(inner_join9)
inner_joinBABIP.reset_index()

full_data.reset_index(inplace=True)

TR_to_FG = pd.DataFrame({'TR Teams': ['Arizona', 'Atlanta', 'Baltimore', 'Boston', 'Chi Cubs', 'Chi Sox', 'Cincinnati',
                                      'Cleveland', 'Colorado', 'Detroit', 'Houston', 'Kansas City', 'LA Angels',
                                      'LA Dodgers', 'Miami', 'Milwaukee', 'Minnesota', 'NY Mets', 'NY Yankees',
                                      'Oakland', 'Philadelphia', 'Pittsburgh', 'San Diego', 'Seattle', 'SF Giants',
                                      'St. Louis', 'Tampa Bay', 'Texas', 'Toronto', 'Washington'],
                         'FG Teams': ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU',
                                      'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT',
                                      'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']})

full_data = pd.merge(full_data,
                     TR_to_FG,
                     on='TR Teams',
                     how='left')



full_data = full_data.set_index('FG Teams')

full_data1 = pd.merge(full_data, inner_join12, left_index=True, right_on='FG Teams')


#The function from lines 595-603 handles an exception in the data organizing process
def list_replace(lst, old='', new='2'):
    """replace list elements (inplace)"""
    i = -1
    try:
        while True:
            i = lst.index(old, i + 1)
            lst[i] = new
    except ValueError:
        pass


#Lines 607-698 collect the starting lineups for each team, along with relevant accompanying player data
def getRotoGrinders():
    url = 'https://rotogrinders.com/lineups/mlb?site=fanduel'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    largetable = soup.find('ul', class_='lst lineup')

    rows = largetable.find_all('div', class_='blk crd lineup')

    for row in rows:
        game = row.find_all('span', class_='shrt')
        away_team = [item.text.strip() for item in game][0]
        home_team = [item.text.strip() for item in game][1]

        phand = row.find_all('span', class_='meta stats')
        away_phand = [item.text.strip() for item in phand][0]
        home_phand = [item.text.strip() for item in phand][1]

        away_phand_strip = str(away_phand[0])
        home_phand_strip = str(home_phand[0])

        pitcher_name = row.find_all('div', class_='pitcher players')
        away_pitcher_name = [item.text.strip() for item in pitcher_name][0]
        home_pitcher_name = [item.text.strip() for item in pitcher_name][1]

        away_pitcher_name_strip = away_pitcher_name.split()[:2]
        home_pitcher_name_strip = home_pitcher_name.split()[:2]

        s = ' '.join(away_pitcher_name_strip)
        y = ' '.join(home_pitcher_name_strip)

        plr = row.find_all('div', class_='long-pitcher')
        if 'PLR' in plr[0].text:
            add = 1
        else:
            add = 0
        if 'PLR' in plr[1].text:
            added = 1
        else:
            added = 0

        pitcher = row.find_all('span', class_='salary')

        away_pitcher_salary = [item.text.strip() for item in pitcher][0]
        home_pitcher_salary = [item.text.strip() for item in pitcher][10 + add]

        away_pitcher_strip = str(away_pitcher_salary[1:-1])

        home_pitcher_strip = str(home_pitcher_salary[1:-1])

        name = row.find_all('span', class_='pname')
        players = [item.text.strip() for item in name]
        away_players = players[0:9]
        home_players = players[9:18]

        salary = row.find_all('span', class_='salary')
        all_salary = [item.text.strip() for item in salary]
        away_salary = all_salary[1 + add:10 + add]
        home_salary = all_salary[11 + add + added:20 + add + added]

        away_salary_list = [i.replace('$', '') for i in away_salary]
        away_salary_list2 = [i.replace('K', '') for i in away_salary_list]

        home_salary_list = [i.replace('$', '') for i in home_salary]
        home_salary_list2 = [i.replace('K', '') for i in home_salary_list]

        list_replace(away_salary_list2, old='', new='2')
        list_replace(home_salary_list2, old='', new='2')

        output['Away Team'].append(away_team)
        output['Home Team'].append(home_team)
        output['Away Players'].append(away_players)
        output['Home Players'].append(home_players)
        output['Away Salary'].append(away_salary_list2)
        output['Home Salary'].append(home_salary_list2)
        output['Away Pitcher Salary'].append(away_pitcher_strip)
        output['Home Pitcher Salary'].append(home_pitcher_strip)
        output['Away Pitcher Hand'].append(away_phand_strip)
        output['Home Pitcher Hand'].append(home_phand_strip)
        output['Away Pitcher Name'].append(s)
        output['Home Pitcher Name'].append(y)

    return


getRotoGrinders()

df = pd.DataFrame(output)

df.loc[:, ['Away Pitcher Salary', 'Home Pitcher Salary']] = df.loc[:,
                                                            ['Away Pitcher Salary', 'Home Pitcher Salary']].replace(
    r'^\s*$', '6', regex=True)


#Lines 702-712 create an ID for each game
game_id = []

team_rows = len(df['Home Team'])

count = 0

while (count < team_rows):
    count = count + 1
    game_id.append(count)

df['Game ID'] = game_id


#Lines 716-749 further organize data into the appropriate lists and columns
split_df = pd.DataFrame(df['Away Salary'].to_list(),
                        columns=['as1', 'as2', 'as3', 'as4', 'as5', 'as6', 'as7', 'as8', 'as9'])

df2 = pd.concat([df, split_df], axis=1)

split_df2 = pd.DataFrame(df2['Home Salary'].tolist(),
                         columns=['hs1', 'hs2', 'hs3', 'hs4', 'hs5', 'hs6', 'hs7', 'hs8', 'hs9'])

df3 = pd.concat([df2, split_df2], axis=1)

rg_away = df3[
    ['Game ID', 'Away Team', 'Away Pitcher Salary', 'as1', 'as2', 'as3', 'as4', 'as5', 'as6', 'as7', 'as8', 'as9',
     'Away Pitcher Hand', 'Away Pitcher Name']]
rg_home = df3[
    ['Game ID', 'Home Team', 'Home Pitcher Salary', 'hs1', 'hs2', 'hs3', 'hs4', 'hs5', 'hs6', 'hs7', 'hs8', 'hs9',
     'Home Pitcher Hand', 'Home Pitcher Name']]

rg_away['RG Teams'] = rg_away['Away Team']
rg_home['RG Teams'] = rg_home['Home Team']

rg_away['Away Location'] = 'Away'
rg_home['Home Location'] = 'Home'

rg_away1 = rg_away[
    ['Game ID', 'RG Teams', 'Away Pitcher Salary', 'as1', 'as2', 'as3', 'as4', 'as5', 'as6', 'as7', 'as8', 'as9',
     'Away Location', 'Away Pitcher Hand', 'Away Pitcher Name']]
rg_home1 = rg_home[
    ['Game ID', 'RG Teams', 'Home Pitcher Salary', 'hs1', 'hs2', 'hs3', 'hs4', 'hs5', 'hs6', 'hs7', 'hs8', 'hs9',
     'Home Location', 'Home Pitcher Hand', 'Home Pitcher Name']]

rg_away1['Name'] = rg_away1['Away Pitcher Name']
rg_home1['Name'] = rg_home1['Home Pitcher Name']

df_SP = df_SP.drop(df_SP.columns[[1, 2, 3, 6, 7, 21]], axis=1)


#Lines 753-932 are a series of merges and renaming of columns
pitcher_join_away = pd.merge(rg_away1,
                             df_SP,
                             on='Name',
                             how='left')

pitcher_join_home = pd.merge(rg_home1,
                             df_SP,
                             on='Name',
                             how='left')

full_data1 = pd.merge(full_data1.drop(['DK Teams'], axis=1), df_odds_target1, on='FG Teams', how='left')

df_rg_target = pd.DataFrame({'RG Teams': ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU',
                                          'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT',
                                          'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WAS'],
                             'DK Teams': ['ARI Diamondbacks', 'ATL Braves', 'BAL Orioles', 'BOS Red Sox', 'CHI Cubs',
                                          'CHI White Sox', 'CIN Reds', 'CLE Guardians', 'COL Rockies', 'DET Tigers',
                                          'HOU Astros', 'KC Royals', 'LA Angels', 'LA Dodgers', 'MIA Marlins',
                                          'MIL Brewers', 'MIN Twins', 'NY Mets', 'NY Yankees', 'OAK Athletics',
                                          'PHI Phillies', 'PIT Pirates', 'SD Padres', 'SEA Mariners', 'SF Giants',
                                          'STL Cardinals', 'TB Rays', 'TEX Rangers', 'TOR Blue Jays', 'WAS Nationals']})

inner_join_away = pd.merge(pitcher_join_away,
                           df_rg_target,
                           on='RG Teams',
                           how='left')

inner_join_home = pd.merge(pitcher_join_home,
                           df_rg_target,
                           on='RG Teams',
                           how='left')

inner_join_away1 = pd.merge(inner_join_away,
                            full_data1,
                            on='DK Teams',
                            how='left')

inner_join_home1 = pd.merge(inner_join_home,
                            full_data1,
                            on='DK Teams',
                            how='left')

full_away = inner_join_away1[
    ['Game ID', 'DK Teams', 'ML', 'Name', 'Away Pitcher Hand', 'K/BB', 'xFIP', 'HR/9', '2022 RPG', '2021 Errors',
     'Last1 HR% Batting', '2022 Total Bases', 'Last3 Stolen Bases', 'Barrel%', 'maxEV', 'Bullpen ERA', 'ISO vs L',
     'ISO vs R', 'AVG vs L', 'AVG vs R', 'Away Pitcher Salary', 'as1', 'as2', 'as3', 'as4', 'as5', 'as6', 'as7', 'as8',
     'as9', 'Away Location', 'BB/K vs L', 'BB/K vs R', 'OPS vs L', 'OPS vs R', 'BABIP vs L', 'BABIP vs R', 'wRC vs L',
     'wRC vs R', 'wRAA vs L', 'wRAA vs R', 'wOBA vs L', 'wOBA vs R', 'wRC+ vs L', 'wRC+ vs R', 'K-BB%', 'AVG', 'WHIP',
     'BABIP', 'LOB%', 'ERA-', 'FIP-', 'xFIP-', 'ERA', 'FIP', 'E-F', 'SIERA', '2022 Strikeout% Batting',
     'Last3 Strikeout% Batting', 'Last1 Strikeout% Batting', '2022 HR% Batting', 'Last3 HR% Batting',
     '2022 Stolen Bases', 'Last1 Stolen Bases', '2022 ISO', 'Last3 ISO', 'Last1 ISO', '2022 BABIP', 'Last3 BABIP',
     'Last1 BABIP', '2022 OPS', 'Last3 OPS', 'Last1 OPS', 'Last3 RPG', 'Last1 RPG', '2022 Errors', 'Last3 Errors',
     'Last1 Errors', 'LA', 'HardHit%', 'Bullpen K/BB', 'Bullpen HR/9', 'Bullpen AVG', 'Bullpen WHIP', 'Bullpen xFIP']]
full_home = inner_join_home1[
    ['Game ID', 'DK Teams', 'ML', 'Name', 'Home Pitcher Hand', 'K/BB', 'xFIP', 'HR/9', '2022 RPG', '2021 Errors',
     'Last1 HR% Batting', '2022 Total Bases', 'Last3 Stolen Bases', 'Barrel%', 'maxEV', 'Bullpen ERA', 'ISO vs L',
     'ISO vs R', 'AVG vs L', 'AVG vs R', 'Home Pitcher Salary', 'hs1', 'hs2', 'hs3', 'hs4', 'hs5', 'hs6', 'hs7', 'hs8',
     'hs9', 'Home Location', 'BB/K vs L', 'BB/K vs R', 'OPS vs L', 'OPS vs R', 'BABIP vs L', 'BABIP vs R', 'wRC vs L',
     'wRC vs R', 'wRAA vs L', 'wRAA vs R', 'wOBA vs L', 'wOBA vs R', 'wRC+ vs L', 'wRC+ vs R', 'K-BB%', 'AVG', 'WHIP',
     'BABIP', 'LOB%', 'ERA-', 'FIP-', 'xFIP-', 'ERA', 'FIP', 'E-F', 'SIERA', '2022 Strikeout% Batting',
     'Last3 Strikeout% Batting', 'Last1 Strikeout% Batting', '2022 HR% Batting', 'Last3 HR% Batting',
     '2022 Stolen Bases', 'Last1 Stolen Bases', '2022 ISO', 'Last3 ISO', 'Last1 ISO', '2022 BABIP', 'Last3 BABIP',
     'Last1 BABIP', '2022 OPS', 'Last3 OPS', 'Last1 OPS', 'Last3 RPG', 'Last1 RPG', '2022 Errors', 'Last3 Errors',
     'Last1 Errors', 'LA', 'HardHit%', 'Bullpen K/BB', 'Bullpen HR/9', 'Bullpen AVG', 'Bullpen WHIP', 'Bullpen xFIP']]

preseason_target = pd.DataFrame({'DK Teams': ['ARI Diamondbacks', 'ATL Braves', 'BAL Orioles', 'BOS Red Sox',
                                              'CHI Cubs', 'CHI White Sox', 'CIN Reds', 'CLE Guardians', 'COL Rockies',
                                              'DET Tigers', 'HOU Astros', 'KC Royals', 'LA Angels', 'LA Dodgers',
                                              'MIA Marlins', 'MIL Brewers', 'MIN Twins', 'NY Mets', 'NY Yankees',
                                              'OAK Athletics', 'PHI Phillies', 'PIT Pirates', 'SD Padres',
                                              'SEA Mariners', 'SF Giants', 'STL Cardinals', 'TB Rays', 'TEX Rangers',
                                              'TOR Blue Jays', 'WAS Nationals'],
                                 'Preseason Win Totals': ['66', '89', '61.5', '86', '73.5', '91.5', '73.5', '76.5',
                                                          '70', '79.5', '92', '75.5', '84.5', '97.5', '77.5', '90',
                                                          '81.5', '87', '92', '70.5', '86.5', '64', '86.5', '85.5',
                                                          '86', '86', '89.5', '73', '91', '70.5']})

join_preseason_away = pd.merge(full_away,
                               preseason_target,
                               on='DK Teams',
                               how='left')

join_preseason_home = pd.merge(full_home,
                               preseason_target,
                               on='DK Teams',
                               how='left')

FIP_park_target = pd.DataFrame({'DK Teams': ['ARI Diamondbacks', 'ATL Braves', 'BAL Orioles', 'BOS Red Sox', 'CHI Cubs',
                                             'CHI White Sox', 'CIN Reds', 'CLE Guardians', 'COL Rockies', 'DET Tigers',
                                             'HOU Astros', 'KC Royals', 'LA Angels', 'LA Dodgers', 'MIA Marlins',
                                             'MIL Brewers', 'MIN Twins', 'NY Mets', 'NY Yankees', 'OAK Athletics',
                                             'PHI Phillies', 'PIT Pirates', 'SD Padres', 'SEA Mariners', 'SF Giants',
                                             'STL Cardinals', 'TB Rays', 'TEX Rangers', 'TOR Blue Jays',
                                             'WAS Nationals'],
                                'FIP Park': ['98', '99', '106', '99', '100', '103', '104', '99', '105', '100', '99',
                                             '98', '102', '100', '97', '100', '100', '97', '102', '98', '103', '100',
                                             '99', '98', '95', '97', '96', '100', '99', '101']})

join_FIP_away = pd.merge(join_preseason_away,
                         FIP_park_target,
                         on='DK Teams',
                         how='left')

join_FIP_home = pd.merge(join_preseason_home,
                         FIP_park_target,
                         on='DK Teams',
                         how='left')

BBF_park_target = pd.DataFrame({'DK Teams': ['ARI Diamondbacks', 'ATL Braves', 'BAL Orioles', 'BOS Red Sox', 'CHI Cubs',
                                             'CHI White Sox', 'CIN Reds', 'CLE Guardians', 'COL Rockies', 'DET Tigers',
                                             'HOU Astros', 'KC Royals', 'LA Angels', 'LA Dodgers', 'MIA Marlins',
                                             'MIL Brewers', 'MIN Twins', 'NY Mets', 'NY Yankees', 'OAK Athletics',
                                             'PHI Phillies', 'PIT Pirates', 'SD Padres', 'SEA Mariners', 'SF Giants',
                                             'STL Cardinals', 'TB Rays', 'TEX Rangers', 'TOR Blue Jays',
                                             'WAS Nationals'],
                                'BBF Park': ['99', '107', '103', '109', '100', '100', '113', '101', '112', '96', '101',
                                             '105', '102', '100', '98', '101', '97', '95', '100', '95', '99', '98',
                                             '92', '95', '98', '92', '92', '99', '104', '95']})

join_BBF_away = pd.merge(join_FIP_away,
                         BBF_park_target,
                         on='DK Teams',
                         how='left')

join_BBF_home = pd.merge(join_FIP_home,
                         BBF_park_target,
                         on='DK Teams',
                         how='left')

HR_park_target = pd.DataFrame({'DK Teams': ['ARI Diamondbacks', 'ATL Braves', 'BAL Orioles', 'BOS Red Sox', 'CHI Cubs',
                                            'CHI White Sox', 'CIN Reds', 'CLE Guardians', 'COL Rockies', 'DET Tigers',
                                            'HOU Astros', 'KC Royals', 'LA Angels', 'LA Dodgers', 'MIA Marlins',
                                            'MIL Brewers', 'MIN Twins', 'NY Mets', 'NY Yankees', 'OAK Athletics',
                                            'PHI Phillies', 'PIT Pirates', 'SD Padres', 'SEA Mariners', 'SF Giants',
                                            'STL Cardinals', 'TB Rays', 'TEX Rangers', 'TOR Blue Jays',
                                            'WAS Nationals'],
                               'HR Park': ['95', '98', '111', '97', '100', '108', '112', '101', '109', '97', '101',
                                           '92', '105', '106', '91', '103', '99', '96', '105', '94', '108', '94', '96',
                                           '98', '89', '93', '93', '97', '100', '104']})

join_HR_away = pd.merge(join_BBF_away,
                        HR_park_target,
                        on='DK Teams',
                        how='left')

join_HR_home = pd.merge(join_BBF_home,
                        HR_park_target,
                        on='DK Teams',
                        how='left')

attendance_target = pd.DataFrame({'DK Teams': ['ARI Diamondbacks', 'ATL Braves', 'BAL Orioles', 'BOS Red Sox',
                                               'CHI Cubs', 'CHI White Sox', 'CIN Reds', 'CLE Guardians', 'COL Rockies',
                                               'DET Tigers', 'HOU Astros', 'KC Royals', 'LA Angels', 'LA Dodgers',
                                               'MIA Marlins', 'MIL Brewers', 'MIN Twins', 'NY Mets', 'NY Yankees',
                                               'OAK Athletics', 'PHI Phillies', 'PIT Pirates', 'SD Padres',
                                               'SEA Mariners', 'SF Giants', 'STL Cardinals', 'TB Rays', 'TEX Rangers',
                                               'TOR Blue Jays', 'WAS Nationals'],
                                  'Attendance': ['22.8', '34.5', '20.8', '27.9', '30.4', '22.6', '24.2', '18.8', '27.5',
                                                 '22', '27.9', '18.1', '29.1', '37.5', '19.3', '27.3', '18.6', '31.1',
                                                 '30', '16.1', '29.7', '22.3', '31.5', '23.6', '28.4', '31.5', '16.9',
                                                 '23', '28.9', '21.9']})

join_ATT_away = pd.merge(join_HR_away,
                         attendance_target,
                         on='DK Teams',
                         how='left')

join_ATT_home = pd.merge(join_HR_home,
                         attendance_target,
                         on='DK Teams',
                         how='left')

join_ATT_home.rename(
    columns={'Home Pitcher Hand': 'Pitcher hand', 'hs1': 's1', 'hs2': 's2', 'hs3': 's3', 'hs4': 's4', 'hs5': 's5',
             'hs6': 's6', 'hs7': 's7', 'hs8': 's8', 'hs9': 's9', 'Home Location': 'Location',
             'Home Pitcher Salary': 'Pitcher Salary'}, inplace=True)
join_ATT_away.rename(
    columns={'Away Pitcher Hand': 'Pitcher hand', 'as1': 's1', 'as2': 's2', 'as3': 's3', 'as4': 's4', 'as5': 's5',
             'as6': 's6', 'as7': 's7', 'as8': 's8', 'as9': 's9', 'Away Location': 'Location',
             'Away Pitcher Salary': 'Pitcher Salary'}, inplace=True)


#Lines 936-1034 collect the weather data for each game and adds it to the main dataframe
weather_output_away = {

    'Team1': [],
    'temp': [],
    'precip': [],
    'MPH': [],
}


weather_output_home = {

    'Team2': [],
    'temp': [],
    'precip': [],
    'MPH': [],
}

def getWeatheraway():
    url = 'https://rotogrinders.com/weather/mlb'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    largetable = soup.find('div', class_='blk forecast-cards')

    rows = largetable.find_all('div', class_='blk crd')

    for row in rows:
        team1 = row.find_all('span', class_='shrt')[0].text
        forecast = row.find_all('div', class_= 'blk current-forecast')

        for data in forecast:
            temp = data.find_all('span', class_='value')[0].text
            precip = data.find_all('span', class_='value')[1].text
            windMPH = data.find_all('span', class_= 'value')[3].text

            weather_output_away['Team1'].append(team1)
            weather_output_away['temp'].append(temp)
            weather_output_away['precip'].append(precip)
            weather_output_away['MPH'].append(windMPH)


def getWeatherhome():
    url = 'https://rotogrinders.com/weather/mlb'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    largetable = soup.find('div', class_='blk forecast-cards')
    rows = largetable.find_all('div', class_='blk crd')

    for row in rows:
        team2 = row.find_all('span', class_='shrt')[1].text
        forecast = row.find_all('div', class_= 'blk current-forecast')

        for data in forecast:
            temp = data.find_all('span', class_='value')[0].text
            precip = data.find_all('span', class_='value')[1].text
            windMPH = data.find_all('span', class_= 'value')[3].text

            weather_output_home['Team2'].append(team2)
            weather_output_home['temp'].append(temp)
            weather_output_home['precip'].append(precip)
            weather_output_home['MPH'].append(windMPH)
    return


getWeatherhome()
getWeatheraway()


weather_home = pd.DataFrame(weather_output_home)
weather_away = pd.DataFrame(weather_output_away)

weather_home['RG Teams'] = weather_home['Team2']
weather_away['RG Teams'] = weather_away['Team1']


weather_join_home = pd.merge(weather_home,
                           df_rg_target,
                           on='RG Teams',
                           how='left')

weather_join_away = pd.merge(weather_away,
                           df_rg_target,
                           on='RG Teams',
                           how='left')



join_weather_home = pd.merge(join_ATT_home,
                         weather_join_home,
                         on='DK Teams',
                         how='left')

join_weather_away = pd.merge(join_ATT_away,
                         weather_join_away,
                         on='DK Teams',
                         how='left')

jointdf = pd.concat([join_weather_away, join_weather_home])


#Lines 1038-1047 further organize and sort the main dataframe
complete_join = jointdf[
    ['Game ID', 'DK Teams', 'ML', 'Name', 'Pitcher hand', 'Pitcher Salary', 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'FIP Park', 'HR Park', 'BBF Park', 'Attendance', 'Preseason Win Totals',
     'temp', 'precip', 'MPH',
     'K/BB', 'xFIP', 'HR/9', 'K-BB%', 'AVG', 'WHIP', 'BABIP', 'LOB%', 'ERA-', 'FIP-', 'xFIP-', 'ERA', 'FIP', 'E-F', 'SIERA',
     'ISO vs L', 'ISO vs R', 'AVG vs L', 'AVG vs R', 'BB/K vs L', 'BB/K vs R', 'OPS vs L', 'OPS vs R', 'BABIP vs L', 'BABIP vs R', 'wRC vs L', 'wRC vs R', 'wRAA vs L', 'wRAA vs R', 'wOBA vs L', 'wOBA vs R', 'wRC+ vs L', 'wRC+ vs R',
     '2022 RPG', 'Last1 RPG', '2022 Stolen Bases', 'Last3 Stolen Bases', '2022 Errors', 'Last3 Errors', 'Last1 Errors', '2021 Errors', '2022 HR% Batting', 'Last3 HR% Batting', 'Last1 HR% Batting', '2022 Strikeout% Batting', 'Last3 Strikeout% Batting', 'Last1 Strikeout% Batting', '2022 ISO', 'Last3 ISO', 'Last1 ISO', '2022 BABIP', 'Last3 BABIP', 'Last1 BABIP',  'Last3 OPS', 'Last1 OPS',
     'Barrel%', 'maxEV', 'HardHit%', 'LA',
     'Bullpen ERA', 'Bullpen K/BB', 'Bullpen HR/9', 'Bullpen AVG', 'Bullpen WHIP', 'Bullpen xFIP', 'Location']]

complete_join.sort_values(['Game ID', 'Location'], inplace=True)


#Lines 1051-1170 create more dictionaries to store more data
pbb = {
    'FG Teams': [],
    'PBB_BABIP': [],
    'PBB_GB/FB': [],
    'PBB_LD%': [],
    'PBB_GB%': [],
    'PBB_FlyB%': [],
    'PBB_IFFB%': [],
    'PBB_HR/FB': [],
    'PBB_RS': [],
    'PBB_RS/9': [],
    'PBB_Balls': [],
    'PBB_Strikes': [],
    'PBB_Pitches': [],
    'PBB_Pull%': [],
    'PBB_Cent%': [],
    'PBB_Oppo%': [],
    'PBB_Soft%': [],
    'PBB_Med%': [],
    'PBB_Hard%': [],
}


bbb = {
    'FG Teams': [],
    'BBB_BABIP': [],
    'BBB_GB/FB': [],
    'BBB_LD%': [],
    'BBB_GB%': [],
    'BBB_FlyB%': [],
    'BBB_IFFB%': [],
    'BBB_HR/FB': [],
    'BBB_IFH': [],
    'BBB_IFH%': [],
    'BBB_BUH': [],
    'BBB_BUH%': [],
    'BBB_Pull%': [],
    'BBB_Cent%': [],
    'BBB_Oppo%': [],
    'BBB_Soft%': [],
    'BBB_Med%': [],
    'BBB_Hard%': [],
}

bptype = {
    'FG Teams': [],
    'b_FB%': [],
    'b_FBv': [],
    'b_SL%': [],
    'b_SLv': [],
    'b_CT%': [],
    'b_CTv': [],
    'b_CB%': [],
    'b_CBv': [],
    'b_CH%': [],
    'b_CHv': [],
}

pptype = {
    'FG Teams': [],
    'p_FB%': [],
    'p_FBv': [],
    'p_SL%': [],
    'p_SLv': [],
    'p_CT%': [],
    'p_CTv': [],
    'p_CB%': [],
    'p_CBv': [],
    'p_CH%': [],
    'p_CHv': [],
}


ppvalue = {
    'FG Teams': [],
    'p_wFB/C': [],
    'p_wSL/C': [],
    'p_wCT/C': [],
    'p_wCB/C': [],
    'p_wCH/C': [],
}

bpvalue = {
    'FG Teams': [],
    'b_wFB/C': [],
    'b_wSL/C': [],
    'b_wCT/C': [],
    'b_wCB/C': [],
    'b_wCH/C': [],
}

pdisc = {
    'FG Teams': [],
    'p_oswing': [],
    'p_zswing': [],
    'p_swing': [],
    'p_ocontact': [],
    'p_zcontact': [],
    'p_contact': [],
    'p_zone': [],
    'p_fstrike': [],
    'p_swstrike': [],
    'p_cstr': [],
    'p_csw': [],
}

bdisc = {
    'FG Teams': [],
    'b_oswing': [],
    'b_zswing': [],
    'b_swing': [],
    'b_ocontact': [],
    'b_zcontact': [],
    'b_contact': [],
    'b_zone': [],
    'b_fstrike': [],
    'b_swstrike': [],
    'b_cstr': [],
    'b_csw': [],
}


#Lines 1174-1397 are more functions to scrape more data
def getPBB():
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=0&type=2&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', class_='rgMasterTable')
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        pbb['FG Teams'].append(td[1].text)
        pbb['PBB_BABIP'].append(td[2].text)
        pbb['PBB_GB/FB'].append(td[3].text)
        pbb['PBB_LD%'].append(td[4].text)
        pbb['PBB_GB%'].append(td[5].text)
        pbb['PBB_FlyB%'].append(td[6].text)
        pbb['PBB_IFFB%'].append(td[7].text)
        pbb['PBB_HR/FB'].append(td[8].text)
        pbb['PBB_RS'].append(td[9].text)
        pbb['PBB_RS/9'].append(td[10].text)
        pbb['PBB_Balls'].append(td[11].text)
        pbb['PBB_Strikes'].append(td[12].text)
        pbb['PBB_Pitches'].append(td[13].text)
        pbb['PBB_Pull%'].append(td[14].text)
        pbb['PBB_Cent%'].append(td[15].text)
        pbb['PBB_Oppo%'].append(td[16].text)
        pbb['PBB_Soft%'].append(td[17].text)
        pbb['PBB_Med%'].append(td[18].text)
        pbb['PBB_Hard%'].append(td[19].text)

    return

def getBBB():
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=2&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', class_='rgMasterTable')
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        bbb['FG Teams'].append(td[1].text)
        bbb['BBB_BABIP'].append(td[2].text)
        bbb['BBB_GB/FB'].append(td[3].text)
        bbb['BBB_LD%'].append(td[4].text)
        bbb['BBB_GB%'].append(td[5].text)
        bbb['BBB_FlyB%'].append(td[6].text)
        bbb['BBB_IFFB%'].append(td[7].text)
        bbb['BBB_HR/FB'].append(td[8].text)
        bbb['BBB_IFH'].append(td[9].text)
        bbb['BBB_IFH%'].append(td[10].text)
        bbb['BBB_BUH'].append(td[11].text)
        bbb['BBB_BUH%'].append(td[12].text)
        bbb['BBB_Pull%'].append(td[13].text)
        bbb['BBB_Cent%'].append(td[14].text)
        bbb['BBB_Oppo%'].append(td[15].text)
        bbb['BBB_Soft%'].append(td[16].text)
        bbb['BBB_Med%'].append(td[17].text)
        bbb['BBB_Hard%'].append(td[18].text)

    return

def getBptype():
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=4&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', class_='rgMasterTable')
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        bptype['FG Teams'].append(td[1].text)
        bptype['b_FB%'].append(td[2].text)
        bptype['b_FBv'].append(td[3].text)
        bptype['b_SL%'].append(td[4].text)
        bptype['b_SLv'].append(td[5].text)
        bptype['b_CT%'].append(td[6].text)
        bptype['b_CTv'].append(td[7].text)
        bptype['b_CB%'].append(td[8].text)
        bptype['b_CBv'].append(td[9].text)
        bptype['b_CH%'].append(td[10].text)
        bptype['b_CHv'].append(td[11].text)


    return

def getPptype():
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=0&type=4&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', class_='rgMasterTable')
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        pptype['FG Teams'].append(td[1].text)
        pptype['p_FB%'].append(td[2].text)
        pptype['p_FBv'].append(td[3].text)
        pptype['p_SL%'].append(td[4].text)
        pptype['p_SLv'].append(td[5].text)
        pptype['p_CT%'].append(td[6].text)
        pptype['p_CTv'].append(td[7].text)
        pptype['p_CB%'].append(td[8].text)
        pptype['p_CBv'].append(td[9].text)
        pptype['p_CH%'].append(td[10].text)
        pptype['p_CHv'].append(td[11].text)


    return

def getPpvalue():
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=0&type=7&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', class_='rgMasterTable')
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        ppvalue['FG Teams'].append(td[1].text)
        ppvalue['p_wFB/C'].append(td[9].text)
        ppvalue['p_wSL/C'].append(td[10].text)
        ppvalue['p_wCT/C'].append(td[11].text)
        ppvalue['p_wCB/C'].append(td[12].text)
        ppvalue['p_wCH/C'].append(td[13].text)


    return

def getBpvalue():
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=7&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', class_='rgMasterTable')

    tbody = table.find('tbody')

    rows = tbody.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        bpvalue['FG Teams'].append(td[1].text)
        bpvalue['b_wFB/C'].append(td[9].text)
        bpvalue['b_wSL/C'].append(td[10].text)
        bpvalue['b_wCT/C'].append(td[11].text)
        bpvalue['b_wCB/C'].append(td[12].text)
        bpvalue['b_wCH/C'].append(td[13].text)


    return


def getPdisc():
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=0&type=5&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', class_='rgMasterTable')
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        pdisc['FG Teams'].append(td[1].text)
        pdisc['p_oswing'].append(td[2].text)
        pdisc['p_zswing'].append(td[3].text)
        pdisc['p_swing'].append(td[4].text)
        pdisc['p_ocontact'].append(td[5].text)
        pdisc['p_zcontact'].append(td[6].text)
        pdisc['p_contact'].append(td[7].text)
        pdisc['p_zone'].append(td[8].text)
        pdisc['p_fstrike'].append(td[9].text)
        pdisc['p_swstrike'].append(td[10].text)
        pdisc['p_cstr'].append(td[11].text)
        pdisc['p_csw'].append(td[11].text)


    return


def getBdisc():
    url = 'https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=5&season=2022&month=0&season1=2022&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=2022-01-01&enddate=2022-12-31'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('table', class_='rgMasterTable')
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        bdisc['FG Teams'].append(td[1].text)
        bdisc['b_oswing'].append(td[2].text)
        bdisc['b_zswing'].append(td[3].text)
        bdisc['b_swing'].append(td[4].text)
        bdisc['b_ocontact'].append(td[5].text)
        bdisc['b_zcontact'].append(td[6].text)
        bdisc['b_contact'].append(td[7].text)
        bdisc['b_zone'].append(td[8].text)
        bdisc['b_fstrike'].append(td[9].text)
        bdisc['b_swstrike'].append(td[10].text)
        bdisc['b_cstr'].append(td[11].text)
        bdisc['b_csw'].append(td[11].text)


    return


#Lines 1401-1408 are call the functions above
getPBB()
getBBB()
getBptype()
getPptype()
getPpvalue()
getBpvalue()
getPdisc()
getBdisc()

#Lines 1411-1418 organize the new data into dataframes
df_pbb = pd.DataFrame(pbb)
df_bbb = pd.DataFrame(bbb)
df_bptype = pd.DataFrame(bptype)
df_pptype = pd.DataFrame(pptype)
df_ppvalue = pd.DataFrame(ppvalue)
df_bpvalue = pd.DataFrame(bpvalue)
df_pdisc = pd.DataFrame(pdisc)
df_bdisc = pd.DataFrame(bdisc)


#Lines 1422-1488 provide the code for a series of merges to merge the new data into the main dataframe
fg_target1 = pd.DataFrame({'FG Teams': ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET', 'HOU',
                                        'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK', 'PHI', 'PIT',
                                        'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']})


newjoin1 = pd.merge(fg_target1,
                    df_pbb,
                    on='FG Teams',
                    how='left')

newjoin2 = pd.merge(newjoin1,
                    df_bbb,
                    on='FG Teams',
                    how='left')

newjoin3 = pd.merge(newjoin2,
                    df_bptype,
                    on='FG Teams',
                    how='left')

newjoin4 = pd.merge(newjoin3,
                    df_pptype,
                    on='FG Teams',
                    how='left')

newjoin5 = pd.merge(newjoin4,
                    df_ppvalue,
                    on='FG Teams',
                    how='left')

newjoin6 = pd.merge(newjoin5,
                    df_bpvalue,
                    on='FG Teams',
                    how='left')

newjoin7 = pd.merge(newjoin6,
                    df_pdisc,
                    on='FG Teams',
                    how='left')

newjoin8 = pd.merge(newjoin7,
                    df_bdisc,
                    on='FG Teams',
                    how='left')


fg_comp_target = pd.DataFrame({'DK Teams': ['ARI Diamondbacks', 'ATL Braves', 'BAL Orioles', 'BOS Red Sox', 'CHI Cubs',
                                             'CHI White Sox', 'CIN Reds', 'CLE Guardians', 'COL Rockies', 'DET Tigers',
                                             'HOU Astros', 'KC Royals', 'LA Angels', 'LA Dodgers', 'MIA Marlins',
                                             'MIL Brewers', 'MIN Twins', 'NY Mets', 'NY Yankees', 'OAK Athletics',
                                             'PHI Phillies', 'PIT Pirates', 'SD Padres', 'SEA Mariners', 'SF Giants',
                                             'STL Cardinals', 'TB Rays', 'TEX Rangers', 'TOR Blue Jays',
                                             'WAS Nationals'],
                                'FG Teams': ['ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET',
                                             'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK',
                                             'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN']})

comp_all = pd.merge(complete_join,
                         fg_comp_target,
                         on = 'DK Teams',
                         how='left')


compfull = pd.merge(comp_all,
                    newjoin8,
                    on = 'FG Teams',
                    how = 'left')


#Lines 1492-1545 create more dictionaries for further data collection
walks_b = {
    'TR Teams': [],
    '2022 Walks_b': [],
    'Last3 Walks_b': [],
    'Last1 Walks_b': [],

}

walks_p = {
    'TR Teams': [],
    '2022 Walks_p': [],
    'Last3 Walks_p': [],
    'Last1 Walks_p': [],

}

hbp = {
    'TR Teams': [],
    '2022 hbp': [],
    'Last3 hbp': [],
    'Last1 hbp': [],

}

risp = {
    'TR Teams': [],
    '2022 RISP': [],
    'Last3 RISP': [],
    'Last1 RISP': [],

}

gidp = {
    'TR Teams': [],
    '2022 GIDP': [],
    'Last3 GIDP': [],
    'Last1 GIDP': [],

}

closepercent = {
    'TR Teams': [],
    '2022 Close%': [],
    'Last3 Close%': [],
    'Last1 Close%': [],

}

RPG_789 = {
    'TR Teams': [],
    '2022 789RPG': [],
    'Last3 789RPG': [],
    'Last1 789RPG': [],
}


#Lines 1549-1676 are functions to scrape even more data
def getWalks_b():
    url = 'https://www.teamrankings.com/mlb/stat/walks-per-game'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        walks_b['TR Teams'].append(td[1].text)
        walks_b['2022 Walks_b'].append(td[2].text)
        walks_b['Last3 Walks_b'].append(td[3].text)
        walks_b['Last1 Walks_b'].append(td[4].text)

    return

def getWalks_p():
    url = 'https://www.teamrankings.com/mlb/stat/walks-per-9'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        walks_p['TR Teams'].append(td[1].text)
        walks_p['2022 Walks_p'].append(td[2].text)
        walks_p['Last3 Walks_p'].append(td[3].text)
        walks_p['Last1 Walks_p'].append(td[4].text)

    return



def getHBP():
    url = 'https://www.teamrankings.com/mlb/stat/hit-by-pitch-per-game'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        hbp['TR Teams'].append(td[1].text)
        hbp['2022 hbp'].append(td[2].text)
        hbp['Last3 hbp'].append(td[3].text)
        hbp['Last1 hbp'].append(td[4].text)

    return

def getRISP():
    url = 'https://www.teamrankings.com/mlb/stat/runners-left-in-scoring-position-per-game'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        risp['TR Teams'].append(td[1].text)
        risp['2022 RISP'].append(td[2].text)
        risp['Last3 RISP'].append(td[3].text)
        risp['Last1 RISP'].append(td[4].text)

    return


def getGIDP():
    url = 'https://www.teamrankings.com/mlb/stat/grounded-into-double-plays-per-game'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        gidp['TR Teams'].append(td[1].text)
        gidp['2022 GIDP'].append(td[2].text)
        gidp['Last3 GIDP'].append(td[3].text)
        gidp['Last1 GIDP'].append(td[4].text)

    return

def getClosePercent():
    url = 'https://www.teamrankings.com/mlb/stat/win-pct-close-games'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        closepercent['TR Teams'].append(td[1].text)
        closepercent['2022 Close%'].append(td[2].text)
        closepercent['Last3 Close%'].append(td[3].text)
        closepercent['Last1 Close%'].append(td[4].text)

    return

def get789RPG():
    url = 'https://www.teamrankings.com/mlb/stat/last-3-innings-runs-per-game'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    table = soup.find('tbody')
    rows = table.find_all('tr')

    for td in rows:
        td = td.find_all('td')

        RPG_789['TR Teams'].append(td[1].text)
        RPG_789['2022 789RPG'].append(td[2].text)
        RPG_789['Last3 789RPG'].append(td[3].text)
        RPG_789['Last1 789RPG'].append(td[4].text)

    return

#Lines 1679-1685 call the above functions
getWalks_b()
getWalks_p()
getHBP()
getRISP()
getGIDP()
getClosePercent()
get789RPG()

#Lines 1688-1694 organize the data from the above functions into dataframes
df_walks_b = pd.DataFrame(walks_b)
df_walks_p = pd.DataFrame(walks_p)
df_hbp = pd.DataFrame(hbp)
df_risp = pd.DataFrame(risp)
df_gidp = pd.DataFrame(gidp)
df_close = pd.DataFrame(closepercent)
df_789RPG = pd.DataFrame(RPG_789)

#Lines 1697-1762 are a series of merges to join the new data into the main dataframe
tr_target1 = pd.DataFrame({'TR Teams': ['Arizona', 'Atlanta', 'Baltimore', 'Boston', 'Chi Cubs', 'Chi Sox', 'Cincinnati',
                                      'Cleveland', 'Colorado', 'Detroit', 'Houston', 'Kansas City', 'LA Angels',
                                      'LA Dodgers', 'Miami', 'Milwaukee', 'Minnesota', 'NY Mets', 'NY Yankees',
                                      'Oakland', 'Philadelphia', 'Pittsburgh', 'San Diego', 'Seattle', 'SF Giants',
                                      'St. Louis', 'Tampa Bay', 'Texas', 'Toronto', 'Washington']})


trjoin1 = pd.merge(tr_target1,
                    df_walks_b,
                    on='TR Teams',
                    how='left')


trjoin2 = pd.merge(trjoin1,
                    df_walks_p,
                    on='TR Teams',
                    how='left')

trjoin3 = pd.merge(trjoin2,
                    df_hbp,
                    on='TR Teams',
                    how='left')

trjoin4 = pd.merge(trjoin3,
                    df_risp,
                    on='TR Teams',
                    how='left')

trjoin5 = pd.merge(trjoin4,
                    df_gidp,
                    on='TR Teams',
                    how='left')

trjoin6 = pd.merge(trjoin5,
                    df_close,
                    on='TR Teams',
                    how='left')

trjoin7 = pd.merge(trjoin6,
                    df_789RPG,
                    on='TR Teams',
                    how='left')


tr_comp_target = pd.DataFrame({'DK Teams': ['ARI Diamondbacks', 'ATL Braves', 'BAL Orioles', 'BOS Red Sox', 'CHI Cubs',
                                             'CHI White Sox', 'CIN Reds', 'CLE Guardians', 'COL Rockies', 'DET Tigers',
                                             'HOU Astros', 'KC Royals', 'LA Angels', 'LA Dodgers', 'MIA Marlins',
                                             'MIL Brewers', 'MIN Twins', 'NY Mets', 'NY Yankees', 'OAK Athletics',
                                             'PHI Phillies', 'PIT Pirates', 'SD Padres', 'SEA Mariners', 'SF Giants',
                                             'STL Cardinals', 'TB Rays', 'TEX Rangers', 'TOR Blue Jays',
                                             'WAS Nationals'],
                                'TR Teams': ['Arizona', 'Atlanta', 'Baltimore', 'Boston', 'Chi Cubs', 'Chi Sox', 'Cincinnati',
                                      'Cleveland', 'Colorado', 'Detroit', 'Houston', 'Kansas City', 'LA Angels',
                                      'LA Dodgers', 'Miami', 'Milwaukee', 'Minnesota', 'NY Mets', 'NY Yankees',
                                      'Oakland', 'Philadelphia', 'Pittsburgh', 'San Diego', 'Seattle', 'SF Giants',
                                      'St. Louis', 'Tampa Bay', 'Texas', 'Toronto', 'Washington']})



comp_all2 = pd.merge(compfull,
                         tr_comp_target,
                         on = 'DK Teams',
                         how='left')


compfull2 = pd.merge(comp_all2,
                    trjoin7,
                    on = 'TR Teams',
                    how = 'left')


print(compfull2)

#Line 1771 exports the data to excel. In all, the program will collect and organize 6,000 data points each day
compfull2.to_excel('MLB_Daily_Betting_Data.xlsx')

print('Todays MLB Data is Ready!')