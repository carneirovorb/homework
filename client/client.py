import socket               # Import socket module
import sys

params = sys.argv[1:]


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
host = params[0]
port = int(params[1])     
directory=params[2]

s.connect((host, port))



while True:
    i=1
    request = input()
    if request == "ls":        
        s.sendall(request.encode())
        list = s.recv(1024)
        print(list.decode())
        continue
    
    
    s.sendall(request.encode())
    l = s.recv(1024)
    

    #charQtd = len(str(l.decode()).split("/")[0])+1
   # size = int(str(l.decode()).split("/")[0])
   # print(l[-(len(l)-charQtd)::])
    
    #print(size)
    
    if not str(l)=="b'notExist'":    
        with open(directory+request, "wb") as f:
            while True:
                i +=1024                 
                end = str(l)[-5::][:4]
                print(end)  
                if(end=="hehe"):
                    f.write((str(l)[:-5]).encode())
                    break
                f.write(l)   
                l = s.recv(1024) 

            f.close()
            print("File %s saved"%request)
    else:
        print("File {} does not exist in the server".format(request))    
        
    
   # s.close ()


