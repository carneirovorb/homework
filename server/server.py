import socket                   # Import socket module
import sys
import os
from threading import Thread



port = 5039
host = "127.0.0.1"
file_directory="./"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))    
s.listen(5)    

cache = [[],[],[]] # [fileName][fileSize][cacheData]
freeCache = 64*(1024**2)
lockCache = False

def deleteCachedFile(index):
    del(cache[0][index])
    del(cache[1][index])
    del(cache[2][index])

def insertInCache(fileName,fileSize, fileContent):
        cache[2].append(fileContent) 
        cache[0].append(fileName) 
        cache[1].append(fileSize) 


def cacheInclude(fileContent, fileName):
    global freeCache
    global cache
    fileSize = len(fileContent)


    while freeCache<fileSize and not lockCache: #Deletar arquivos acessados por último para liberar espaço apenas se cache n tiver bloqueada
        freeCache -= cache[1][0]
        deleteCachedFile(0)

    if freeCache>=fileSize:
        insertInCache(fileName,fileSize, fileContent)
        freeCache -= fileSize


def conection(conn, addr):

    while True:    

        data = conn.recv(1024).decode()
        if data:
            list = os.popen("ls "+file_directory).readlines()        
            
            if data=="ls":                                     
                conn.sendall(str(cache[0]).encode())
                continue

            print("Client {} is  requesting  file {}".format(addr[0], data))

            if data in cache[0]:
                lockCache = True
                index = cache[0].index(data)
                fileName = cache[0][index]
                fileSize= cache[1][index]
                f_send =cache[2][index]
                deleteCachedFile(index)
                insertInCache(fileName,fileSize, f_send)
                lockCache = False
                print("Cache  hit.  File  %s  sent  to  the  client."%data)
            

            elif not (data+"\n" in list):
                print("File  {}  does  not  exist  in  the  server".format(data))
                conn.sendall("notExist".encode())
                continue
                
            else:
                with open(file_directory+data, "rb") as f:
                    print("Cache  miss.  File  %s  sent  to  the  client."%data)
                
                    # send file
                    f_send = f.read()
                    f.close() 
                    if  len(f_send)<=64*1024**2:
                        cacheInclude(f_send, data)
            #print(f_send)
           
            conn.send(f_send)
            conn.send("hehe".encode())
            # close connection
           
            # conn.close()
                


        #conn.send(data)
    #75999697056

while True:    
    print ('Server listening....')
    conn, addr = s.accept()   
    print ('Conexão efetuada com ', addr)
    Thread(target=conection,args=[conn,addr]).start()