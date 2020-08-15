def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import('csv')
install_and_import('xml')
import csv
import xml
list2=[]
with open('Stations.csv', 'r') as file:

    reader = csv.reader(file)
    i=0
    for row in reader:
        if i%3!=0:
            pass 
        else:
            list1=[]
            for i in range(0,len(row)):
                list1.append(row[i])
            list2.append(list1)
        i=i+1

list2_1=[]
with open('Queensland_Regions.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row==[]:
            pass
        else:
            list1=[]
            for i in range(0,len(row)):
                
                    list1.append(row[i])
            list2_1.append(list1)
           
len(list2_1)

first_attrib = ['RegionID']
for i in range(0,len(list2)):
    for x in range(0,len(list2_1)):
        if list2[i][1]==list2_1[x][1]:
            first_attrib.append(int(list2_1[x][0]))
len(first_attrib)
import xml
import xml.etree.ElementTree as ET
tree = ET.parse('Station_Locations.xml')
root = tree.getroot()
list2_4=[['Name','Longitude','Latitude']]
for e in root.findall('STATION'):
    Name = e.find('NAME').text
    Long = e.find('LONG').text
    Lat = e.find('LAT').text
    list1=[Name,Long,Lat]
    list2_4.append(list1)
another=[]
second_attrib=['Station Number']
third_attrib=['Station Name']
fourth_attrib = ['Station Type']
fifth_attrib = ['Street Address']
sixth_attrib = ['State']
seventh_attrib = ['Post Code']
eighth_attrib = ['Phone Number']
nineth_attrib = ['Fax Number']
tenth_attrib=['E-Mail']
eleventh_attrib=['Longitude']
twelvth_attrib = ['Latitude']
for i in range(1,len(list2)):
    flag=0
    second_attrib.append(int(list2[i][2]))
    third_attrib.append(list2[i][0])
    fourth_attrib.append(list2[i][3])
    full_address = list2[i][4]
    add = full_address[0:len(full_address)-4]
    post_C = full_address[len(full_address)-4:len(full_address)]
    fifth_attrib.append(add)
    sixth_attrib.append('Qld')
    seventh_attrib.append(post_C)
    eighth_attrib.append(list2[i][6])
    nineth_attrib.append(list2[i][7])
    name_for_email=(list2[i][0].replace(" ","")).lower()
    email = 'enquiry@' + name_for_email[0:len(name_for_email)-7] + '.qfes.gov.au'
    tenth_attrib.append(email)
    temp=list2[i][0].upper()
    temp2=temp[0:len(temp)-13]
    for ix in range(1,len(list2_4)):
        if list2_4[ix][0].replace(' ','')==temp2.replace(' ',''):
            flag=1
            eleventh_attrib.append(list2_4[ix][2])
            twelvth_attrib.append(list2_4[ix][1])
            
len(eleventh_attrib)
#diction.keys()
dict_data = []
for i in range(1,len(list2)):
    temp = { 'RegionID' : first_attrib[i], 'Station Number':second_attrib[i], 'Station Name':third_attrib[i], 'Station Type':fourth_attrib[i], 'Street Address':fifth_attrib[i], 'State':'Qld', 'Postcode':seventh_attrib[i], 'Phone Number':eighth_attrib[i], 'Fax Number':nineth_attrib[i], 'E-Mail':tenth_attrib[i],'Latitude':eleventh_attrib[i],'Longitude':twelvth_attrib[i] }
    dict_data.append(temp)
dict_data2=sorted(dict_data, key = lambda i: (i['Station Number']))
dict_data3=sorted(dict_data2, key = lambda i: (i['RegionID']))
#import csv
csv_columns = ['RegionID','Station Number','Station Name','Station Type','Street Address','State','Postcode','Phone Number','Fax Number','E-Mail','Longitude','Latitude']

csv_file = "Fire_Station_Locations.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data3:
            writer.writerow(data)
except IOError:
    print("I/O error")
