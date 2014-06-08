import MySQLdb

class Database(object):

    db = None
    cursor = None
    table = None

    def __init__(self, table):
        self.table = table
        self.db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="apievaluation")
        self.cursor = self.db.cursor()

        try:
            self.cursor.execute("SELECT * FROM %s" % table)
            result = self.cursor.fetchall()
            #print len(result)
        except Exception as e:
            self.cursor.execute("CREATE TABLE `"+self.table+"` ("+
                  "`id` int(11) unsigned NOT NULL AUTO_INCREMENT,"+
                  "`timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"+
                  "`status` varchar(20) DEFAULT NULL,"+
                  "`image` varchar(50) DEFAULT '',"+
                  "`execution_time` float DEFAULT NULL,"+
                  "`face_topLeft_X` float DEFAULT NULL,"+
                  "`face_topLeft_Y` float DEFAULT NULL,"+
                  "`face_bottomRight_X` float DEFAULT NULL,"+
                  "`face_bottomRight_Y` float DEFAULT NULL,"+
                  "`gender` char(11) DEFAULT NULL,"+
                  "`gender_accuracy` int(11) DEFAULT NULL,"+
                  "`age` int(11) DEFAULT NULL,"+
                  "`confidence` int(11) DEFAULT NULL,"+
                  "PRIMARY KEY (`id`)"+
                ") ENGINE=InnoDB DEFAULT CHARSET=utf8;")
            self.db.commit()



    def add_image(self, status=-1, image=-1, execution_time=-1,face_topLeft_x=-1,face_topLeft_y=-1, face_bottomRight_x=-1,face_bottomRight_y=-1, gender=-1, gender_accuracy=-1, age=-1, confidence=-1):
        try:
            query = """INSERT INTO `"""+self.table+"""` (`status`, `image`, `execution_time`, `face_topLeft_X`, `face_topLeft_Y`, `face_bottomRight_X`, `face_bottomRight_Y`, `gender`, `gender_accuracy`, `age`, `confidence`) VALUES ('%s','%s',%s, %s, %s, %s, %s, '%s', %s, %s, %s)""" % (status,image,execution_time,face_topLeft_x,face_topLeft_y,face_bottomRight_x,face_bottomRight_y,gender,gender_accuracy,age,confidence)
            #print query
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            print e

