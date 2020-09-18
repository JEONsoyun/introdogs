import urllib.request
import datetime

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element

import pandas as pd
import csv

def get_sido():#ok
    url = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sido?'
    key = 'ServiceKey=gLMQuL3Gk7RDv1o0iSjhqsPEQilpN5fCRBw1iQstJNQKppisNlp9aIg9XZc6yGGYND7p2hTJCY9vmOCx%2BZpKNA%3D%3D&&numOfRows=20'
    request = urllib.request.Request(url+key)
    request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(request).read()
    u = str(response_body, "utf-8")

    #make sido table
    result=[]
    root = ET.fromstring(u)
    elements = root.findall('body/items/item')
    for item in elements: 
        try:
            item_list=[]
            item_list.append(item.find('orgCd').text)
            item_list.append(item.find('orgdownNm').text) 
            result.append(item_list)
        except Exception as e:
            print("This row will be ignored. ", item_list)

    f = open('sido.csv', "w", encoding='utf-8')
    f.write("orgCd, orgdownNm\n")

    for items in result:
        input =""
        for item in items:
            input += item +","
        input = input[:-1]
        input += '\n'
        f.write(input)
    f.close()

    return result

def get_sigugun(sido):#ok
    url = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sigungu?upr_cd='
    key = ''
    result=[]

    for item in sido:
        key = item[0]
        servicekey = '&&ServiceKey=gLMQuL3Gk7RDv1o0iSjhqsPEQilpN5fCRBw1iQstJNQKppisNlp9aIg9XZc6yGGYND7p2hTJCY9vmOCx%2BZpKNA%3D%3D&&numOfRows=30'
        request = urllib.request.Request(url+key+servicekey)
        request.get_method = lambda: 'GET'
        response_body = urllib.request.urlopen(request).read()
        u = str(response_body, "utf-8")

        #make sigugun table
        root = ET.fromstring(u)
        elements = root.findall('body/items/item')
        for data in elements: 
            try:
                item_list=[]
                item_list.append(item[0])
                item_list.append(item[1])
                item_list.append(data.find('orgCd').text)
                item_list.append(data.find('orgdownNm').text) 
                result.append(item_list)
            except Exception as e:
                print("This row will be ignored. ", item_list)

    f = open('sigugun.csv', "w", encoding='utf-8')
    f.write("orgCd, orgdownNm\n")

    for items in result:
        input =""
        for item in items:
            input += item +","
        input = input[:-1]
        input += '\n'
        f.write(input)
    f.close()

    return result

def get_id_name(item):
    url = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/shelter?upr_cd='
    upr_cd = ''
    org_cd = ''
    result=[]
    
    upr_cd = item[0]
    org_cd = item[2]
    servicekey = '&ServiceKey=gLMQuL3Gk7RDv1o0iSjhqsPEQilpN5fCRBw1iQstJNQKppisNlp9aIg9XZc6yGGYND7p2hTJCY9vmOCx%2BZpKNA%3D%3D'
    request = urllib.request.Request(url+upr_cd+'&org_cd='+org_cd+servicekey)
    request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(request).read()
    u = str(response_body, "utf-8")

    #make sigugun table
    root = ET.fromstring(u)
    elements = root.findall('body/items/item')
    for data in elements: 
        try:
            item_list=[]
            item_list.append(item[1]+item[3])
            name = data.find('careNm').text
            if "," in str(name):
                inputs = str(name).split(',')
                item_list.append(inputs[0])
                item_list.append(inputs[1])
            else:
                item_list.append(name) 
                item_list.append(data.find('careRegNo').text)
            result.append(item_list)
        except Exception as e:
            print("This row will be ignored. ", item_list)
    print(result)
    return result

def get_detail(bohoso):
    #'311303200900001', '한국동물구조관리협회'
    url = 'http://openapi.animal.go.kr/openapi/service/rest/animalShelterSrvc/shelterInfo?care_reg_no='
    key=''
    care_nm=''
    result=[]

    for item in bohoso:
        key = item[0]
        care_nm = item[1]
        servicekey = '&&ServiceKey=gLMQuL3Gk7RDv1o0iSjhqsPEQilpN5fCRBw1iQstJNQKppisNlp9aIg9XZc6yGGYND7p2hTJCY9vmOCx%2BZpKNA%3D%3D'
        request = urllib.request.Request(url+key+servicekey)
        #request = urllib.request.Request(url+key+'&care_nm='+care_nm+servicekey)
        request.get_method = lambda: 'GET'
        response_body = urllib.request.urlopen(request).read()
        u = str(response_body, "utf-8")

        #make sigugun table
        root = ET.fromstring(u)
        elements = root.findall('body/items/item')
        for data in elements: 
            try:
                item_list=[]
                item_list.append(item[0])
                item_list.append(item[1])
                item_list.append(data.find('careAddr').text)
                item_list.append(data.find('jibunAddr').text)
                item_list.append(data.find('lat').text)
                item_list.append(data.find('lng').text)
                item_list.append(data.find('careTel').text)
                result.append(item_list)
            except Exception as e:
                print("This row will be ignored. ", item_list)

    return result
           
def get_detail2(item):
    #'311303200900001', '한국동물구조관리협회'
    url = 'http://openapi.animal.go.kr/openapi/service/rest/animalShelterSrvc/shelterInfo?care_reg_no='
    key=''
    care_nm =''
    result=[]

    key = item[2]
    care_nm = item[1]
    servicekey = '&&ServiceKey=gLMQuL3Gk7RDv1o0iSjhqsPEQilpN5fCRBw1iQstJNQKppisNlp9aIg9XZc6yGGYND7p2hTJCY9vmOCx%2BZpKNA%3D%3D'
    servicekey2 = '&&ServiceKey=UdGdSXDDzPzNkDHf1ebt0FFiAAzf%2B%2F4uzCilbZkaiCCX3SFlAsRGOtU%2BdV%2Fg%2Fhkf06KC%2Bv%2FBxHoaj8a6scYmHQ%3D%3D'
    print(url+key+servicekey)#'&care_nm='+care_nm+
    request = urllib.request.Request(url+key+servicekey) #'&care_nm='+care_nm+
    request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(request).read()
    u = str(response_body, "utf-8")
    print(u)

    #make sigugun table
    root = ET.fromstring(u)
    elements = root.findall('body/items/item')
    for data in elements:
        try:
            item_list=[]
            item_list.append(item[1])
            item_list.append(item[2])
            item_list.append(data.find('careAddr').text)
            item_list.append(data.find('lat').text)
            item_list.append(data.find('lng').text)
            item_list.append(data.find('careTel').text)
            result.append(item_list)
        except Exception as e:
            print("This row will be ignored. ", item_list)
    
    return result
    
    return u
def main():
    #sido = get_sido()
    #print(sido)
    '''
    f = open('C:/git/bigdata/open/sido.csv', 'r', encoding='utf-8')
    data = csv.reader(f)
    print(data)
    sido=[]
    cnt=0
    for line in data:
        if cnt != 0:
            sido.append(line)
        cnt += 1
    print(sido)
    f.close()
    '''
    #sigugun = get_sigugun(sido)
    #print(sigugun)

    '''
    f = open('C:/git/bigdata/open/sigugun.csv', 'r', encoding='utf-8')
    data = csv.reader(f)
    print(data)
    sigugun=[]
    cnt=0
    for line in data:
        if cnt != 0:
            sigugun.append(line)
        cnt += 1
    print(sigugun)
    f.close()

    f = open('bohoso.csv', "w", encoding='utf-8')
    f.write("address, orgdownNm, orgCd\n")
    f.close()
    bohoso = []
    for now in sigugun:
        tmp = get_id_name(now)
        f = open('bohoso.csv', "a", encoding='utf-8')
        for items in tmp:
            input =""
            for item in items:
                input += item +","
            input = input[:-1]
            input += '\n'
            f.write(input)
        f.close()
    print(bohoso)
    '''
    f = open('C:/git/bigdata/open/bohoso1.csv', 'r', encoding='utf-8')
    data = csv.reader(f)
    #print(data)
    bohoso=[]
    cnt=0
    for line in data:
        if cnt != 0:
            bohoso.append(line)
        cnt += 1
    f.close()    

    f = open('bohoso_detail.csv', "w", encoding='utf-8')
    f.write("orgCd, orgdownNm, careAddr, lat, lng, careTel\n")
    f.close()
    for now in bohoso:
        print(now)
        f = open('bohoso_detail.csv', "a", encoding='utf-8')
        tmp = get_detail2(now)
        
        for items in tmp:
            input =""
            for item in items:
                input += item +","
            input = input[:-1]
            input += '\n'
            f.write(input)
        f.close()
        
        

if __name__ == "__main__":
    main()