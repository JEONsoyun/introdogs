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

def get_id_name(sigugun):
    url = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/shelter?upr_cd='
    upr_cd = ''
    org_cd = ''
    result=[]

    for item in sigugun:
        upr_cd = item[0]
        org_cd = item[2]
        servicekey = '&ServiceKey=gLMQuL3Gk7RDv1o0iSjhqsPEQilpN5fCRBw1iQstJNQKppisNlp9aIg9XZc6yGGYND7p2hTJCY9vmOCx%2BZpKNA%3D%3D'
        request = urllib.request.Request(url+upr_cd+'&org_cd='+org_cd+servicekey)
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
                item_list.append(item[1]+item[3])
                item_list.append(data.find('careRegNo').text)
                item_list.append(data.find('careNm').text) 
                result.append(item_list)
            except Exception as e:
                print("This row will be ignored. ", item_list)

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
    
    #bohoso = get_id_name(sigugun)
    #print(bohoso)
    #print(len(bohoso))

    #detail_bohoso = get_detail(bohoso)
    #print(detail_bohoso)
    #print(len(detail_bohoso))


if __name__ == "__main__":
    main()