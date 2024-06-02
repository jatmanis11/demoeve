import requests
from django.shortcuts import render , HttpResponse, HttpResponseRedirect
from bs4 import BeautifulSoup
import time
from api import active_companies_dict
#from autoslug import AutoSlugField
def jatmanis1(request):
    return render(request, "jatmanis1.html")
def ee(request):
    ak=False
    id1="500327"
    id1=request.POST.get("search")
    
    
    #id1="erewrer"
    print(id1,"yusss")
    """nse_url="https://www.google.com/finance/quote/{id}:NSE"
    bse_url="https://www.google.com/finance/quote/500325:BOM"
    bse2="https://www.bseindia.com/stock-share-price/pil-italica-lifestyle-ltd/pilita/500325/"
    print(bse_url)
    response= requests.get(bse2)
    print(response,"123123")"""
    data=active_companies_dict.data
    #print(data)
    m=[]
    n=[]
    k=[]
    
    #print(id1.lower(),"id1")
    #a=str(input("find company here"))
    for n in data.keys():
        #print(n)
        if id1!=None:
            id1=id1.lower() 
            if id1 in n.lower():
                #print(n)
                ak=True
                m.append(data[n])
        else:
            ak=False
            m.append("search company ")
            #print(n)
            #print(data[n])
            #print(m)
    #com_name=m[0][1]
    #print(com_name)
    #com_slug=
    #com_slug =AutoSlugField(populate_from=com_name,unique=True, null=True, default=None)
    #print(com_slug)
    """for i in m:
        l=data[i]
        k.append(l)"""
    """soup = BeautifulSoup(response.text, "html.parser")
    if len(soup)>0:
        print("yeeeeeeeeeesssssssssss")
    else:
        print("nooooooooooooooooooo")
    price_class="YMlKec fxKbKc"
    volume_class="P6K39c"
    revenue_class="QXDnM"
    price=soup.find(class_=price_class).text
    traded_volume=soup.find(class_=volume_class).text
    revenue=soup.find(class_=revenue_class).text
    for n in soup :"""
    if ak:    
        data1={
            #"price":price,
            "id1":id1, 
            "list":m,
            #"listd":k,
        }
    else:
        data1={
            "list1":"NO DATA FOUND"
        }
            

    
    return render(request, "ee.html",data1)


def detail(request, id1):
    id1=id1
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    #bse2=f"https://www.bseindia.com/stock-share-price/pil-italica-lifestyle-ltd/pilita/{id1}"
    bse2=f"https://www.google.com/finance/quote/{id1}:BOM"
    response= requests.get(bse2, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    if len(soup)>0:
        a=True
    else:
        a=False
    data=active_companies_dict.data
    price_class="YMlKec fxKbKc"
    price=soup.find(class_=price_class).text
    m=[]
    k=[]
    for n in data.values():

        #print(n[0])
        if id1!=None:
            
            if id1 == n[0]:
                com_data=n
                m=n[0]
                #m.append(data[n])
    
    t1=[]
    kj=1
    if a:
        tb_elements = soup.find_all("table", {"class":"slpEwd"})
        print(len(tb_elements),"elelelele")
        for m in tb_elements:
            tr_element = m.find_all('tr', {'class': 'roXhBd'})
            print(len(tr_element),"tr3e")
            #tr_element= tr_element[1:8]+tr_element[9:15]+tr_element[17:len(tr_element)-1]
            for n in tr_element[1:len(tr_element)]:
            
                print(n.index, kj)

                v1=[]    
                tr1_value = n.find('td', {'class': "QXDnM"}).text
                
                tr1_desc = n.find('td', {'class': "J9Jhg"}).text
                tr1_name = n.find('div', {'class': "rsPbEe"}).text
                v1.append(tr1_name)
                v1.append(tr1_value)
                v1.append(tr1_desc)
                
                t1.append(v1)
                #print(t1,"t1")
            
        print(t1,"t12")
    
        t2=[]
        tb_elements= soup.find('div', {'class': 'eYanAe'})
        
        #print(tb_elements,"tb222")
        tr_1 = soup.find_all('div', {'class': 'vvDK2c'})
        tr_2 = tb_elements.find_all('div', {'class': 'gyFHrc'})
        for n in tr_2:
            v1=[]
            tr_value= n.find("div", {"class":"P6K39c"}).text
            tr_name= n.find("div", {"class":"mfs7Fc"}).text
            tr_desc= n.find("div", {"class":"EY8ABd-OWXEXe-TAWMXe"}).text
            
            v1.append(tr_name)
            v1.append(tr_value)
            v1.append(tr_desc)
            t2.append(v1)
        data2={
            "price":price,
            "t1":t1,
            "t2":t2,
            "id1":id1,
            "data":m,
            "com_data":com_data,
        }
    else:
        data2={}
    return render(request, "detail.html",data2)
"""
def filter1(request):
    value=request.POST.get("peratio")
    data=active_companies_dict.data
    for n in data:
        id  
    id1="500325"
    bse2=f"https://www.google.com/finance/quote/{id1}:BOM"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    response= requests.get(bse2, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup)
    if len(soup)>0:
        print("yeeeeeeeeeesssssssssss")
    else:
        print("nooooooooooooooooooo")
    price_class="YMlKec fxKbKc"
    price=soup.find(class_=price_class).text
    cl_1="mfs7Fc"
    cl_2="P6K39c"
    cl2=soup.find(class_=cl_2).text
    cl1=soup.find(class_=cl_1).text
    print(cl2)
    print(cl1)
     elements = soup.select('[aria-describedby="i25"]')
    
    print(len(elements),"123")
    for element in elements:
        print("ele",element.text)
    row = soup.find('tr', text=lambda text: 'Price to book' in text)
    # find the second column in the row
    value = row.find_all('td')[1].text
    print(value,"bt")
    

    # Find the tr element with class "roXhBd"
    tb_elements = soup.find_all("table", {"class":"slpEwd"})
    tr_element = soup.find_all('tr', {'class': 'roXhBd'})
    print(len(tb_elements))

    print(len(tr_element))
    #print(tb_elements[2])
    
    print(tr_element[6],"tre")
    # Find the td element within the tr element with class "J9Jhg"
    td_element = tr_element.find('td', {'class': 'J9Jhg'})
    while td_element !=None:
        td_element = tr_element.find('td', {'class': 'J9Jhg'})
        print(td_element,"tde")
        # Find the span element within the td element with a data-is-tooltip-wrapper attribute
        span_element = td_element.find('span', {'data-is-tooltip-wrapper': 'true'})
        if td_element!= None:
            print(span_element,"spe")
            # Find the div element within the span element with id "balanceSheetTT5"
            div_element = span_element.find('div', {'id': 'balanceSheetTT5'})
            if div_element!=None:
                print(div_element,"dve")
            else:
                pass
        else:
            pass
    else:
        pass
    # Check if the div element with id "balanceSheetTT5" exists
    if div_element:
        # Find the td element within the tr element with class "QXDnM"
        td_element = tr_element.find('td', {'class': 'QXDnM'})

        # Extract the text content of the td element
        data = td_element.text
        print(data)
    else:
        print("Div element with id 'balanceSheetTT5' not found.")

    for cl2 in soup:
        pass
        #print(cl2 ,"\n\n\n\n\n")
        



    data={
        "price":price,
        #"soup":soup,
        "cl2":cl2,
        #"table":tb_elements,
        "tr":tr_element,
    }
    return render(request, "filter1.html", data)
def filter2(request):
    value=request.POST.get("pbratio")
    data=active_companies_dict.data
    for n in data.values():
        bse4=f"https://www.google.com/finance/quote/{n[0]}:BOM"
        print(bse4)
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        }
        response= requests.get(bse4, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        tb_elements = soup.find_all("table", {"class":"slpEwd"})
        tr_element = soup.find_all('tr', {'class': 'roXhBd'})
        pb = tr_element[1].find('td', {'class': "QXDnM"}).text
        print(pb)
    id1="500209"
    bse2=f"https://www.google.com/finance/quote/{id1}:BOM"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    response= requests.get(bse2, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    tb_elements = soup.find_all("table", {"class":"slpEwd"})
    tr_element = soup.find_all('tr', {'class': 'roXhBd'})
    pb = tr_element[1].find('td', {'class': "QXDnM"}).text
    print(pb,"pb")
    #print(soup)
    if len(soup)>0:
        print("yeeeeeeeeeesssssssssss")
    else:
        print("nooooooooooooooooooo")
    price_class="YMlKec fxKbKc"
    price=soup.find(class_=price_class).text

    # Find the tr element with class "roXhBd"
    tb_elements = soup.find_all("table", {"class":"slpEwd"})
    tr_element = soup.find_all('tr', {'class': 'roXhBd'})
    td_element = tr_element[1].find('td', {'class': "QXDnM"}).text
    
    print("p1,p1")
    print(td_element,)
    print(len(tb_elements))

    print(len(tr_element))
    #print(tb_elements[2])
    
    #print(tr_element[6],"tre")
    # Find the td element within the tr element with class "J9Jhg"
    #td_element = tr_element.find('td', {'class': 'J9Jhg'})
    while td_element !=None:
        td_element = tr_element.find('td', {'class': 'J9Jhg'})
        print(td_element,"tde")
        # Find the span element within the td element with a data-is-tooltip-wrapper attribute
        span_element = td_element.find('span', {'data-is-tooltip-wrapper': 'true'})
        if td_element!= None:
            print(span_element,"spe")
            # Find the div element within the span element with id "balanceSheetTT5"
            div_element = span_element.find('div', {'id': 'balanceSheetTT5'})
            if div_element!=None:
                print(div_element,"dve")
            else:
                pass
        else:
            pass
    else:
        pass
    # Check if the div element with id "balanceSheetTT5" exists
    if div_element:
        # Find the td element within the tr element with class "QXDnM"
        td_element = tr_element.find('td', {'class': 'QXDnM'})

        # Extract the text content of the td element
        data = td_element.text
        print(data)
    else:
    #    print("Div element with id 'balanceSheetTT5' not found.")

    for cl2 in soup:
        pass
        #print(cl2 ,"\n\n\n\n\n")
        



    data={
        "price":price,
        #"soup":soup,
        "cl2":cl2,
        #"table":tb_elements,
        "tr":tr_element,
    }
    return render(request, "filter2.html", data)"""
#name: class="EY8ABd-OWXEXe-TAWMXe"   value: class="QXDnM" for 23 data
#<div class="gyFHrc"><span data-is-tooltip-wrapper="true"><div class="mfs7Fc" jscontroller="e2jnoe" jsaction="mouseenter:tfO1Yc; focus:AHmuwe; blur:O22p3e; mouseleave:JywGue; touchstart:p6p2H; touchend:yfqBxc;mlnRJb:fLiPzd;" aria-describedby="c196" data-tooltip-x-position="2" data-tooltip-anchor-boundary-type="2">P/E ratio</div><div class="EY8ABd-OWXEXe-TAWMXe" role="tooltip" aria-hidden="true" id="c196">The ratio of current share price to trailing 12-month EPS that signals if the price is high or low compared to other stocks</div></span><div class="P6K39c">28.57</div></div>
#class="YMlKec fxKbKc">₹2,960.00 rel25
#class="YMlKec fxKbKc">₹2,960.00 ph27
#class="YMlKec fxKbKc">₹11.88
"""AVG. VOL """#The average number of shares traded each day over the past 30 days</div></span><div class="P6K39c">21.75K
"""REVENUE """#The total amount of income generated by the sale of goods or services related to the company's primary operations</div></span></td><td class="QXDnM">2.37T<"""
"""Operating expense"""#Represents the total incurred expenses through normal operations</div></span></td><td class="QXDnM">541.22B
"""Net income"""#>Company’s earnings for a period net of operating costs, taxes, and interest</div></span></td><td class="QXDnM">189.51B
"""Earnings per share"""#Represents the company's profit divided by the outstanding shares of its common stock.</div></span></td><td class="QXDnM">28.01
"""Net profit margin"""#Measures how much net income or profit is generated as a percentage of revenue.</div></span></td><td class="QXDnM">8.01	



