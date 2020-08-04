import serial		//파이썬으로 시리얼 통신을 조작하기 위한 모듈입니다.
import MySQLdb		//파이썬으로 DB를 조작하기 위한 모듈입니다.

//시리얼 통신환경을 설정해줍니다. 
//"/dev/ttyACM0"는 아두이노와의 통신포트를 의미하며, 저와 다를 수 있으니 본인의 포트를 확인해주세요.
port = serial.Serial("/dev/ttyACM0", "9600")

//데이터베이스 접속환경을 설정해줍니다.
db = MySQLdb.connect("localhost", "root", "비밀번호", "db명")
curs = db.cursor()
 
while True:
        try:
            data = port.readline()	//시리얼 포트에서 읽어들인 값을 data라는 변수에 저장합니다.
 
            print("Arduino-ir: ")
            print(data)  
 			
            //데이터베이스에 읽어들인 값을 저장합니다.
            //"""INSERT INTO 테이블명 (열 이름) VALUES (데이터의 형태)""", (저장할 값) 형태입니다.
            curs.execute("""INSERT INTO sensor (sensor) VALUES (%s)""", (data))
            db.commit()
 
        except KeyboardInterrupt:
                break
                
port.close()
