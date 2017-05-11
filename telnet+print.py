
import telnetlib
import getpass


host = raw_input("请输入路由器IP地址 : ") 
str1 = raw_input("请输入telnet用户名 : ") 
str2 = getpass.getpass("请输入telnet密码 : ") 
finish = '#'                                   

        
x1=telnetlib.Telnet(host)

x1.read_until("Username: ") 
x1.write(str1+"\n") 


x1.read_until("Password: ") 
x1.write(str2+"\n")


x1.write("sh run\n")   
x1.write("    ") 
        
x1.write("exit\n")  

ra=x1.read_all()

print(ra);
x1.close()
print("------ 以上屏幕输出是show run信息！------"+"\n")

x2=open("show run.txt",'wb')
x2.write(ra)
x2.close()
print("------ 已将屏幕输出信息保存到show run.txt文件中！------ " +"\n")
