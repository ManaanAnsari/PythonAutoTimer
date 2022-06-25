from datetime import date

def get_file_name(): 
    today = date.today()
    print("Today's date:", today)
    return "data/"+str(today)+".json"
