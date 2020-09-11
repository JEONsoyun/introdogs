import urllib.request
import datetime

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse, Element

import pandas as pd

def query_sender():
    url = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?'
    #queryParams='?'+urlencode({quote_plus('ServiceKey'):'ObWFAVIl%2BamakFKOFf0KFFn5zTf1cmpNokN5dwrPOAVdHZvC6M6yHTK4zKXPeKbJSbY8iyuiFh83FRWpejwQag%3D%3D'})
    key = 'ServiceKey=gLMQuL3Gk7RDv1o0iSjhqsPEQilpN5fCRBw1iQstJNQKppisNlp9aIg9XZc6yGGYND7p2hTJCY9vmOCx%2BZpKNA%3D%3D&&upkind=417000&&numOfRows=100000'
    request = urllib.request.Request(url+key)
    request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(request).read()
    u = str(response_body, "utf-8")
    return u

def xml_to_item_list(xml_string):
    result=[]
    root = ET.fromstring(xml_string)
    elements = root.findall('body/items/item')
    for item in elements:
        if "안락사" in str(item.find('processState').text):
            continue
        if "종료" in str(item.find('processState').text):
            continue
        
        try:
            item_list=[]
            item_list.append("N"+item.find('desertionNo').text) # desertionNo	:	441553202002732 (유기동물접수번호)
            item_list.append(item.find('age').text) # age	:	2020(년생)
            item_list.append(item.find('weight').text.replace(',', '.')) # weight	:	1(Kg)
            item_list.append(item.find('sexCd').text) # sexCd	:	M : 수컷, F : 암컷, Q : 미상
            item_list.append((item.find('kindCd').text).replace('[개] ', '')) # kindCd	:	[고양이] 한국 고양이
            item_list.append(item.find('colorCd').text.replace(',', '/').replace('.','/').replace('+', '/').replace('&', '/')) # colorCd	:	흰색, 검정
            item_list.append(item.find('neuterYn').text) # neuterYn	:	Y : 예 , N : 아니오, U : 미상

            item_list.append(item.find('filename').text) # filename	:	http://www.animal.go.kr/files/shelter/2020/07/202009100909621_s.jpg (썸네일)
            item_list.append(item.find('popfile').text) # popfile	:	http://www.animal.go.kr/files/shelter/2020/07/202009100909621.png (사진)

            item_list.append(item.find('careAddr').text.replace(',', '/')) # careAddr	:	경기도 화성시 남양읍 화성로 1483-27 (남양읍)(보호장소)
            item_list.append(item.find('careNm').text) # careNm	:	남양유기견보호센터
            
            item_list.append(item.find('specialMark').text.replace(',', '/').replace('.','/').replace('+', '/').replace('&', '/'))

            #item_list.append(makeone(item.find('specialMark').text)) # specialMark	:	턱시도냥이, 경계가 심한 편이며, 코 오른쪽에 점이 있음, 뒷발은 흰색 긴양말, 앞발은 짧은양말 신음.

            #item_list.append(item.find('happenDt').text)# happenDt	:	20200910 (발견 날짜)
            item_list.append(item.find('happenPlace').text.replace('&#49406;','샵').replace('&#47056;','례').replace(',', '-'))# happenPlace	:	남양읍 무하로 51번길 13(발견 장소)

            item_list.append(item.find('noticeSdt').text) # noticeSdt	:	20200910
            item_list.append(item.find('noticeEdt').text) # noticeEdt	:	20200921
                        
            
            result.append(item_list)
        except Exception as e:
            print("This row will be ignored. ", item_list)
    return result

'''
careNm	:	남양유기견보호센터
careTel	:	031-356-2281
chargeNm	:	성충현

noticeEdt	:	20200921
noticeNo	:	경기-화성-2020-01652
noticeSdt	:	20200910

officetel	:	031-5189-6381
orgNm	:	경기도 화성시
processState	:	보호중
'''
           

def main():
    s = query_sender()
    res = xml_to_item_list(s)
    
    f = open('dog.csv', "w")
    f.write("dog_id, age, weight, sex, kind, color, neuter, thumnail, profile, careAddr, careNm	, special, find_place , find_date , end_date\n")

    for items in res:
        input =""
        for item in items:
            input += item +","
        input = input[:-1]
        input += '\n'
        f.write(input)
    f.close()


    #print(res)
    #print("num : %d" %len(res))

if __name__ == "__main__":
    main()