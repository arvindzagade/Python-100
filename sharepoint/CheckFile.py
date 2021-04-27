import pandas as pd
import numpy as np
import os.path, datetime,time
from sharefile import Share ## Pyfile to download file from sharepoint
from datetime import datetime,timedelta
import pytz



def is_file_older(file,delta):
    
    cutoff = datetime.utcnow() - delta
    #cutoff = datetime.now(pytz.utc) - delta
    print(cutoff)
    mtime = datetime.utcfromtimestamp(os.path.getmtime(file))
    print(mtime)
    if mtime < cutoff:
        return True
    return False


def process():
    
    try:
    
        file = 'filename.csv'
        check_file = os.path.exists(file)
        print(check_file)
        
        if check_file == False:
            print("No file found....downloading the file")
            Share.download_apac() ## This is method to download file from sharepoint.. which is written in another file
        
        
        
        elif check_file == True: 
            print('File is present...Calculating Time')
            """
            def is_file_older(file,delta):
                cutoff = datetime.utcnow() - delta
                #cutoff = datetime.now(pytz.utc) - delta
                print(cutoff)
                mtime = datetime.utcfromtimestamp(os.path.getmtime(file))
                print(mtime)
                if mtime < cutoff:
                    return True
                return False"""
    
        time_diff = is_file_older(file, timedelta(days=1)) # this is calculating this no.of min..
        print(time_diff)
        
        if time_diff==True:
            print("Downloading Latest File from sharepoint")
            Share.download_apac()
            
            
    except Exception as e:
        
        print('Error Occured:'+str(e))
        
    finally:   
        try:
          
        
            #elif time_diff == True:
            
            print("File is present")
            
             
            df = pd.read_csv('filename.csv')
        
            df.drop(df.columns.difference(["DD_RETAILER_ID", "CT_HEA_DISPLAY_GROUP1", "CT_HEA_DISPLAY_GROUP2", 
                                           "CT_HEA_DISPLAY_GROUP3", "CT_HEA_DISPLAY_GROUP4", 
                                           "CT_NUMERIC_DISTRIBUTION_WEEKLY_CAUSAL_CATALOGUE_INSIDE_PAGE", 
                                           "CT_NUMERIC_DISTRIBUTION_WEEKLY_CAUSAL_CATALOGUE_FRONT_PAGE_OR_BACK_PAGE"]), 1, inplace=True)
            
            
            grp1 = df.groupby(['DD_RETAILER_ID'])['CT_HEA_DISPLAY_GROUP1'].max().reset_index()
            grp2 = df.groupby(['DD_RETAILER_ID'])['CT_HEA_DISPLAY_GROUP2'].max().reset_index()
            main = grp1.copy()
            main['CT_HEA_DISPLAY_GROUP2'] = grp2['CT_HEA_DISPLAY_GROUP2']
            grp3 = df.groupby(['DD_RETAILER_ID'])['CT_HEA_DISPLAY_GROUP3'].max().reset_index()
            grp4 = df.groupby(['DD_RETAILER_ID'])['CT_HEA_DISPLAY_GROUP4'].max().reset_index()
            grp5 = df.groupby(['DD_RETAILER_ID'])['CT_NUMERIC_DISTRIBUTION_WEEKLY_CAUSAL_CATALOGUE_INSIDE_PAGE'].max().reset_index()
            grp6 = df.groupby(['DD_RETAILER_ID'])['CT_NUMERIC_DISTRIBUTION_WEEKLY_CAUSAL_CATALOGUE_FRONT_PAGE_OR_BACK_PAGE'].max().reset_index()
            
            main['CT_HEA_DISPLAY_GROUP3'] = grp3['CT_HEA_DISPLAY_GROUP3']
            main['CT_HEA_DISPLAY_GROUP4'] = grp4['CT_HEA_DISPLAY_GROUP4']
            main['CT_NUMERIC_DISTRIBUTION_WEEKLY_CAUSAL_CATALOGUE_INSIDE_PAGE'] = grp5['CT_NUMERIC_DISTRIBUTION_WEEKLY_CAUSAL_CATALOGUE_INSIDE_PAGE']
            main['CT_NUMERIC_DISTRIBUTION_WEEKLY_CAUSAL_CATALOGUE_FRONT_PAGE_OR_BACK_PAGE'] = grp6['CT_NUMERIC_DISTRIBUTION_WEEKLY_CAUSAL_CATALOGUE_FRONT_PAGE_OR_BACK_PAGE']
            
            main.to_csv('Err_Distribution.csv',index=False)
            print('Operations performed Successfully')
                
            
        except Exception as e:
           
            print('Error Occured:'+str(e))
  
    
if _name_ == "_main_":
    process()
