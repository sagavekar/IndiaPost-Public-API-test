import requests
import pandas as pd
from urllib import request
# first will check internet connectivity
def connect(host='http://google.com'):
    try:
        request.urlopen(host)
        
        return True
    except:
        return False

print( "Connected to internet ! \n " if connect() else "No internet!" )

#System will try API hit only if intenet is connected
if connect():
    
    def save_file(df_selective_columns,pin,POSTOFFICEBRANCHNAME):
        
        df_selective_columns.to_csv(f'{pin}{POSTOFFICEBRANCHNAME}.csv')
        print( f"File has been saved with name ' {pin}{POSTOFFICEBRANCHNAME} ' in directory same as program directory")
        

    def Search_Pin():
        pin = input("Enter PIN code ")
        print("Search progress has been started.......")

        URL1 = f"https://api.postalpincode.in/pincode/{pin}"

        response = requests.get(URL1)
        response_json = response.json()

        if response_json[0]['Message'] == "No records found":
            print(response_json[0]['Message'], "\n")
        else:
            print(response_json[0]['Message'], "\n")

            df = pd.DataFrame((response_json[0]['PostOffice'])[0:])
            df_selective_columns = df[['Name', 'BranchType', 'Circle',
                                    'District', 'Division', 'Block', 'State']
                                    ]
            print(df_selective_columns)
            save = input("\n Do you want to save this data to local machine ? Press (Y) for yes and any other key for no ")
            
            if save == "Y" or save ==  "y":
                save_file(df_selective_columns,pin, POSTOFFICEBRANCHNAME = "")
                pass
            elif save != "Y" or save != "y":
                print("Ok buddy ! exiting program...")   
            


    def Search_post():
        POSTOFFICEBRANCHNAME = input("Enter post office name ")
        print("Search progress has been started.......")

        URL2 = f"https://api.postalpincode.in/postoffice/{POSTOFFICEBRANCHNAME}"

        response = requests.get(URL2)
        response_json = response.json()
        if response_json[0]['Message'] == "No records found":
            print(response_json[0]['Message'], "\n")
        else:
            print(response_json[0]['Message'], "\n")

            df = pd.DataFrame((response_json[0]['PostOffice'])[0:])
            df_selective_columns = df[["Pincode", 'Name', 'BranchType', 'Circle',
                                'District', 'Division', 'State']
                                ]
            print(df_selective_columns)
            save = input("\n Do you want to save this data to local machine ? Press (Y) for yes and any other key for no ")

            if save == "Y" or save ==  "y":
                pin = "" # for function adjustment only
                save_file(df_selective_columns,pin, POSTOFFICEBRANCHNAME)
                pass
            elif save != "Y" or save != "y":
                print("Ok buddy ! exiting program...")  

        


    select = input(""" 
    Press (1) To get data of PIN code
    Press (2) To get data of POST OFFICE Branch Name 
    """)

    if select == "1":
        Search_Pin()
    elif select == "2":
        Search_post()
    else:
        print("Invalid selection ! Exiting the program....")

#Internet is not connected hence exiting from program
else:
    print("Please check network and try again ")