# mlb
# data taken from [baseball-reference.com](https://www.baseball-reference.com/)
## this project is to collect all data related to Cuban born players in the big league.
this will be the backend service for it


*reference files glossary*
### Rk -- Rank
    This is a count of the rows from top to bottom.
    It is recalculated following the sorting of a column.
### Name -- Player Name
    Bold can mean player is active for this team
    or player has appeared in MLB
    * means LHP or LHB,
    # means switch hitter,
    + can mean HOFer.
### Yrs -- Experience
    Years the player was/has been in the major leagues.
    1st indicates their first year in the majors,
    but does not indicate rookie status.
    Includes parts of any seasons.
### From -- First Year
### To -- Last Year
### ASG -- All-Star Game Selections
    This does not indicate if the player played or not.
### G -- Games Played or Pitched
### PA -- Plate Appearances
    When available, we use actual plate appearances from play-by-play game accounts
    Otherwise estimated using AB + BB + HBP + SF + SH,
    which excludes catcher interferences.
    When this color click for a summary of each PA.
### AB -- At Bats
### R -- Runs Scored/Allowed
### H -- Hits/Hits Allowed
### 2B -- Doubles Hit/Allowed
### 3B -- Triples Hit/Allowed
### HR -- Home Runs Hit/Allowed
### RBI -- Runs Batted In
### SB -- Stolen Bases
### CS -- Caught Stealing
### BB -- Bases on Balls/Walks
### SO -- Strikeouts
### BA -- Hits/At Bats
    For recent years, leaders need 3.1 PA
    per team game played
    Bold indicates highest BA using current stats
    Gold means awarded title at end of year.
### OBP -- (H + BB + HBP)/(At Bats + BB + HBP + SF)
    For recent years, leaders need 3.1 PA
    per team game played
### SLG -- Total Bases/At Bats or
    (1B + 2*2B + 3*3B + 4*HR)/AB
    For recent years, leaders need 3.1 PA
    per team game played
### OPS -- On-Base + Slugging Percentages
    For recent years, leaders need 3.1 PA
    per team game played
### WAR -- Wins Above Replacement
    A single number that presents the number of wins the player added
    to the team above what a replacement player (think AAA or AAAA) would add.
    Scale for a single-season: 8+ MVP Quality, 5+ All-Star Quality, 2+ Starter,
    0-2 Reserve, < 0 Replacement Level
    Developed by Sean Smith of BaseballProjection.com
### Birthplace -- City of Birth
### Pos -- Position
    ’*’ indicates 300+ games,
    ’/’ less than 30 games,
    no mark for 30-300.