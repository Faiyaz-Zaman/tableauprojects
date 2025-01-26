#Problem Statement
The goal of this project is to gather information of best 1000 computer Science researchers from here: https://research.com/scientists-rankings/best-scientists/us?page={page_id}%22
Later we used the scraped data to understand the following demographics and correlations using Tableau dashboard:
1. Scientists and the average publication in European countries
2. Average citations in each university in Asia
3. Average Citation per country
4. Which column is directly correlated to World Rank.

#Findings
1. The United Kingdom has the most number of scientists from the European countries and Sweden has the highest average publications among them
2. Xi'an Jiaotong University has the highest average citation (126,469) in Asia
3. New Zealand has the highest average citation among all the countries with 155,117 citations
4. The H-index is the most correlated with World Rank

You can visit the public dashboard [here]: https://public.tableau.com/app/profile/faiyaz.zaman/viz/demographicsofbestcs/Dashboard1?publish=yes
## Build From Sources
1. Clone the repo 
```bash
git clone: https://github.com/Faiyaz-Zaman/tableauprojects.git
```
2. Initialize and activate virtual env 
```bash
virtualenv --no-site-packages venv
source venv/bin/activate
```
3.Install dependencies
```bash
pip install -r requirements.txt
```
4.Check the scrapped data
```bash
https://github.com/Faiyaz-Zaman/tableauprojects/blob/main/bestcsscientistsproject/best_cs_scientist_details.csv

```



Tableau Public view: https://public.tableau.com/app/profile/faiyaz.zaman/viz/demographicsofbestcs/Dashboard1?publish=yes
