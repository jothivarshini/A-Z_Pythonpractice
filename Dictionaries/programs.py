database_dict={1:{"Interface":"Ethernet0","IP" :"1.1.1.1", "status":"up"},2:{"Interface":"Ethernet1","IP" :"2.2.2.2", "status":"down"},3:{"Interface":"Serial0","IP" :"3.3.3.3", "status" :"up"},4:{"Interface":"Serial1","IP" :"4.4.4.4.", "status" :"up"}}
print(database_dict)

for key in database_dict:
    if database_dict[key]["status"]=="up":
        print (database_dict[key]["Interface"],database_dict[key]["IP"])
