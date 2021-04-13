
def read_csv(path, header=False):
    import csv
    records = []
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            records = [r for r in csv.reader(csvfile, delimiter=',')]            
    except:
        raise 
    else:
        return records
    

