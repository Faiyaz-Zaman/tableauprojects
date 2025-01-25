from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
columns = ["World Rank","National Rank","Name","Image URLs","Affilitaion","Country","D-index","Citations","#DBLP"]
def get_scholar_details(row):
        details = row.text.split("\n")
        contents = {}
        contents['World Rank'] = details[0]
        contents['National Rank']= details[1]
        contents['Name'] = details[2]
        contents['Affilitaion'] = details[3].split(',')[0]
        contents['Country'] = details[3].split(',')[1].strip()
        contents['D-index'] = details[4]
        contents['Citations'] = details[5].replace(',','')
        contents['#DBLP'] = details[6].replace(',','')
        contents['Image URLs'] = row.find_element(By.CLASS_NAME,'lazyload').get_attribute('src')
        return contents

def main():
    scholar_data=[]
    for page_id in range(1,8):
         driver = webdriver.Chrome()
         url = f"https://research.com/scientists-rankings/best-scientists/us?page={page_id}"
         driver.get(url)
         time.sleep(20)
         rankings = driver.find_element(By.ID,'rankingItems')
         rows = rankings.find_elements(By.CLASS_NAME, 'cols')         
         for idx,row in enumerate(rows):
           if idx%4==0:
                scholar_data.append(get_scholar_details(row))

         driver.close() 
    print(scholar_data) 
    df = pd.DataFrame(data=scholar_data, columns=columns) 
    df.to_csv("best_scientist_details.csv",index=False)  
    

    
    
    
    
    return
if __name__ =="__main__":
    main()