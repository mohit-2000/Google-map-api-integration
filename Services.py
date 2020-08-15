def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import('bottle')
install_and_import('json')
install_and_import('csv')
from bottle import *
import json
import csv
@route('/')
def index():
    json1=getregions()
    return template('stations_map.html',queenslanddata = json1,id='x',name1='nothing')
@route("/index/text.txt")
def index1():
    return template("text.txt")

def getregions():
    list2=[]
    output=[]
    dict_data=[]
    with open('Queensland_Regions.csv', 'r') as datata:
        reader = csv.reader(datata)
        i = 0
        for row in reader:
            list2.append(row)
    for i in range(0, len(list2), 2):
        output.append(list2[i])
    for i in range(1, len(output)):
        temp = {'Region Name': output[i][2],'RegionID': output[i][0]}
        dict_data.append(temp)
    avar = json.dumps(dict_data)
    return avar

@route('/index/getdata')
def particular():
    regionid = request.query.regionid
    list2 = []
    output=[]
    dict_data = []
    if (str(regionid) != '0'):
        with open('Fire_Station_Locations (Solution).csv', 'r') as datata:
            reader = csv.reader(datata)
            i=0
            for row in reader:
                list2.append(row)
        for i in range(0,len(list2),2):
            if list2[i][0]==str(regionid):
                output.append(list2[i])
        data=[]
        file = open('text.txt', 'w') 

        for i in range(0, len(output)):
            temp = { 'Station Number': output[i][1], 'Station Name': output[i][2],
                     'Street Address': output[i][4], 'State': 'Qld',
                    'Postcode': output[i][6], 'Phone Number': output[i][7],
                    'Email': output[i][9], 'Longitude': output[i][10], 'Latitude': output[i][11]}
            dict_data.append(temp)
            data.append(output[i][2])
            data.append((output[i][11]))
            data.append(output[i][10])
            file.write(output[i][10])
            file.write("\n")
            file.write(output[i][11])
            file.write("\n")
            file.write("Station:")
            file.write(output[i][2])
            file.write("\n")
            file.write("Station Address:")
            file.write(output[i][4])
            file.write(', Qld, ')
            file.write(output[i][6])
            file.write("\n")
            file.write("Phone Number:")
            file.write(output[i][7])
            file.write("\n")
            file.write(output[i][9])
            file.write("\n")
            #print(dict_data)
        avar=json.dumps(dict_data)
        html=json.dumps(data)
        file.close() 
    elif (str(regionid) == '0'):
        with open('Fire_Station_Locations (Solution).csv','r') as datata:
            reader = csv.reader(datata)
            for row in reader:
                list2.append(row)
        for i in range(0,len(list2),2):
            output.append(list2[i])
        for i in range(0, len(output)):
            temp = {'Station Name': output[i][2]}
            dict_data.append(temp)
        avar=json.dumps(dict_data)
    return template('stations_map.html',name1=avar,id=str(regionid))
@route('/mapping')
def mapsgoogle():
    return template('mapping.html')
if __name__ == '__main__':
    run(debug=True,port=8082)
