import pymysql


def conn():
    inception = {
        "host": "127.0.0.1",
 	"user": "root",
	"password": "",
        "port": "6669"
    }
    try:
        pymysql.connect(host=inception['host'],user=inception['user'],passwd=inception['password'],port=int(inception['port']),db='',charset="utf8")
    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    conn()
