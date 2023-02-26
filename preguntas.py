"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv

def pregunta_01(vdata="data.csv"):
    open_file = open(vdata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    num=[]
    for i in data:
       num.append(int(i[1]))
    
    return sum(num)


def pregunta_02(vdata="data.csv"):
    open_file = open(vdata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    List_in=[]
    for k in data:
        List_in.append(k[0])
    List_sort=sorted(List_in)
    
    List_Fin=[("A",0)]
    count=0
    
    for i in List_sort:
        if i[0] != List_Fin[count][0]:
            List_Fin.append((i[0],1))
            count+=1
        elif i[0] == List_Fin[count][0]:
            List_Fin[count]=(i[0],List_Fin[count][1]+1)
            count+=0
    return List_Fin
                

def pregunta_03(vdata="data.csv"):
    open_file = open(vdata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    List_in=[]
    for k in data:
        List_in.append((k[0],int(k[1])))
    List_sort=sorted(List_in)

    List_Fin=[("A",0)]
    count=0
    
    for i in List_sort:
        if i[0] != List_Fin[count][0]:
            List_Fin.append((i[0],i[1]))
            count+=1
        elif i[0] == List_Fin[count][0]:
            List_Fin[count]=(i[0],List_Fin[count][1]+i[1])
            count+=0
    return List_Fin


def pregunta_04(vdata="data.csv"):

    open_file = open(vdata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)

    List_in=[]
    for i in data:
        List_in.append(i[2].strip().split("-")[1])

    List_sort=sorted(List_in)
    List_Fin=[("01",0)]
    count=0

    for i in List_sort:
        if i != List_Fin[count][0]:
            List_Fin.append((i,1))
            count+=1
        elif i == List_Fin[count][0]:
            List_Fin[count]=(i,List_Fin[count][1]+1)
            count+=0

    return List_Fin


def pregunta_05(vdata="data.csv"):

    open_file = open(vdata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    List_in=[]
    for k in data:
        List_in.append((k[0],int(k[1])))
    List_sort=sorted(List_in)
    

    List_Fin=[("A",List_sort[0][1],List_sort[0][1])]
    count=0
    
    for i in List_sort:
        if i[0] != List_Fin[count][0]:
            List_Fin.append((i[0],i[1],i[1]))
            count+=1
        elif i[0] == List_Fin[count][0]:
            if i[1]>=List_Fin[count][1]:
                List_Fin[count]=(i[0],i[1],List_Fin[count][2])
            elif i[1]<=List_Fin[count][2]:
                List_Fin[count]=(i[0],List_Fin[count][1],i[1])
            count+=0
    return List_Fin



def pregunta_06(vdata="data.csv"):
    open_file = open(vdata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)

    List_in=[]
    for i in data:
        List_in.append(i[4].split(","))
  
    List_Fin=[('aaa',1,1)]
    L_t=[]
    count=0
    for i in List_in:
        for k in i:
            vt=k.split(":")
            vt[1]=int(vt[1])
            L_t.append(vt)
    L_t=sorted(L_t)

    for i in L_t:
         if i[0] != List_Fin[count][0]:
                List_Fin.append((i[0],i[1],i[1]))
                count+=1
         elif i[0] == List_Fin[count][0]:
                    List_Fin[count]=(i[0],min(i[1],List_Fin[count][1]),max(i[1],List_Fin[count][2]))         
            
    return List_Fin


def pregunta_07(vdata="data.csv"):
    open_file = open(vdata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)

    List_in=[(0,[])]
           
    L_data=[]
    for i in data:
        L_data.append((int(i[1]),i[0]))
    List_in={0:[]}

    for i in L_data:
        if i[0] not in List_in:
            List_in[i[0]]=[i[1]]
        else:
            List_in[i[0]].append(i[1])
    List_in=sorted(List_in.items())        
    
    return List_in

def pregunta_08(vdata="data.csv"):

    open_file = open(vdata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)

    List_in=[(0,[])]
           
    L_data=[]
    for i in data:
        L_data.append((int(i[1]),i[0]))

    L_data=sorted(L_data, key=lambda x: x[1])
    
    List_in={0:[]}

    for i in L_data:
        if i[0] not in List_in:
            List_in[i[0]]=[i[1]]
        else:
            if i[1] not in List_in[i[0]]: 
                List_in[i[0]].append(i[1])
            elif i[1] is List_in[i[0]]:
                pass
    List_in=sorted(List_in.items())        
    return List_in


def pregunta_09(vdata="data.csv"):
    open_file = open(vdata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)

    List_in=[]
    for i in data:
        List_in.append(i[4].split(","))
    L_t=[]
    for i in List_in:
        for k in i:
            vt=k.split(":")
            vt[1]=int(vt[1])
            L_t.append(vt)
    L_t=sorted(L_t)

    Dic_fin={}

    for i in L_t:
        if i[0] not in Dic_fin:
            Dic_fin[i[0]]=1
        elif i[0] in Dic_fin:
            Dic_fin[i[0]]+=1

    return Dic_fin


def pregunta_10(vdata="data.csv"):
    open_file = open(vdata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)

    List_in=[]
    for i in data:
        List_in.append((i[0],len(i[3].split(",")),len(i[4].split(","))))
   
    return List_in



def pregunta_11(vdata="data.csv"):
    open_file = open(vdata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)
    
    Dict_Fin1={}
    for i in data:
        for k in i[3].split(","):
            if k not in Dict_Fin1:
                Dict_Fin1[k]=int(i[1])
            elif k in Dict_Fin1:
                Dict_Fin1[k]+=int(i[1])
    Dict_Fin={}
    for i in sorted(Dict_Fin1.keys()):
        Dict_Fin[i]=Dict_Fin1[i]
    
    return Dict_Fin

def pregunta_12(vdata="data.csv"):
    open_file = open(vdata, encoding = "utf8")
    read_file = csv.reader(open_file, delimiter = '\t')
    data = list(read_file)

    Dict_Fin1={}
    for i in data:
        if i[0] not in Dict_Fin1:
            Dict_Fin1[i[0]]=0
        elif i[0] in Dict_Fin1:pass
    
    for i in data:
            for k in i[4].split(","):
                for l in k.split(":"):
                    try: l=int(l)
                    except: pass
                    if isinstance(l , int):
                        Dict_Fin1[i[0]]+=l
                    elif isinstance(l , str):
                        pass
    Dict_Fin={}
    for i in sorted(Dict_Fin1.keys()):
        Dict_Fin[i]=Dict_Fin1[i]
   
    return Dict_Fin


