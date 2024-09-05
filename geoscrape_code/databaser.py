# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 12:47:20 2020

@author: ErinMartin
"""
'''
This code follows from figshare_search.py

The code iterates through the sqlite database created in fighshare_search and 
downloads files that have not been retrieved to the working folder
'''
#%%

# STEP 1: Enter the details and execute this block of code

#   Specify the path to the folder in which you want to save your downloaded file. Place the folder path
#   inside the "" after the r, e.g. folder = (r"C:\myfolder\")
folder = (r"I:\figshare")
          
#   Specify the name of the sqlite database you created in the figshare_search
#   code. Download SQLite files from: https://doi.org/10.6084/m9.figshare.16870603.v1
sqlite_filename = "copper.sqlite"

#   Set the limit of the number of articles you wish to download (integer)

limit = 999


#%%

# STEP 2: Execute this block of code to define the function

def databaser(sqlite_filename, limit):

    import urllib.request, urllib.parse, urllib.error
    import sqlite3
    import re
    import os

    

    conn = sqlite3.connect(sqlite_filename)
    cur = conn.cursor()
    
    status = "unretrieved"
    new_status = "retrieved"
    relevance = "relevant"
    batch_size = limit
    
     
    cur.execute('''SELECT download_url, file_type, articlenum
                FROM Files
                INNER JOIN article
                ON article.article_id = Files.article_id
                WHERE Files.status=? 
                AND article.relevance=?
                ORDER BY RANDOM()''', (status, relevance)      
                )
    try:  
        while True: 
            rows = cur.fetchmany(batch_size)
            if not rows: break
            ent = 1
            for row in rows:
                print ("Entry", ent)
                ent = ent + 1
                print (row)
                row_id = row[0]
                filetype =  row[1]
                art_num = row[2]
                suffix = re.findall('[A-Za-z0-9]+$', filetype)
                suf = suffix[0]
                dlnum = re.findall('[0-9]+$', row_id)
                dl = dlnum[0]
                filename = (art_num+'_'+dl+'.'+suf)
                file_path = os.path.join(folder, filename)
               
                url = str(row_id)
                print('Accessing download URL', url)
                try:
                    urllib.request.urlretrieve(url, file_path)
                    print("Saving", filename)
                    cur.execute('''UPDATE Files 
                            SET status=?
                            WHERE download_url=?''', 
                            (new_status, row_id, ))
                    print("Status updated")
                except:
                    print("ERROR: Entity not found")
                    cur.execute('''UPDATE Files 
                            SET status=?
                            WHERE download_url=?''', 
                            (new_status, row_id, ))
                    print("Status updated")        
                # cur.execute('''UPDATE Files 
                #             SET status=?
                #             WHERE download_url=?''', 
                #             (new_status, row_id, ))
                # print("Status updated")
                conn.commit()
                
             #   if ent-1 == batch_size:break
    
    except sqlite3.Error as error:
        print("Request failed", error)
        
    
    cur.close()
    
#%%

# STEP 3: Execute the function calling the variables assigned in STEP 1.
# Those variables can be modified and STEP 3 repeated without executing STEP 2.

databaser(sqlite_filename, limit)    
    