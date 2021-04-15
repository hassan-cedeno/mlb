import datetime

from core import file_manager, parsers

def get_batting_players():    
    return parsers.clean_reference_files(file_manager.read_csv('reference_batting.csv', header=True))

def get_pitching_players():    
    return parsers.clean_reference_files(file_manager.read_csv('reference_pitching.csv', header=True))

def get_active_players():
    current_year = datetime.datetime.now().year
    active_batting = [p for p in get_batting_players() if int(p.get('To')) == current_year]
    active_pitching = [p for p in get_pitching_players() if int(p.get('To')) == current_year]
    return {'batting': active_batting, 'pitching': active_pitching}