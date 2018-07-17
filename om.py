import pymysql as pm

try:
    con = pm.connect(host='localhost',database='Ankita',user='root',password='Ankita@123')
    NoteDB = NoteDB.db.cursor()

query = 'create table note(id int(10) primary key, msg varchar(8000) DEFAULT NULL, time datetime DEFAULT CURRENT_TIMESTAMP)'

cursor.execute(query)
con.commit()
print("connection established")
con.close()

#functions

    def add_note( note):
        q = "insert into note(msg) values('%s')" % (note.get_msg())
        try:
            con.cursor.execute(q)
            con.commit()
        except Exception as e:
            print("problem",e)
            NoteDB.db.rollback()
            raise


    def get_one_note( idt):
        q = "select * from note where id=%d" % (idt)
        try:
            con.cursor.execute(q)
            result = con.cursor.fetchall()
            obj = Note(idt=result[0], msg=result[1], time=result[2])
            return obj
        except Exception as e:
            raise


    def get_all_notes():
        q = "select * from note order by time desc;"
        try:
            con.cursor.execute(q)
            notes = []
            results = con.cursor.fetchall()
            for result in results:
                obj = Note(idt=result[0], msg=result[1], time=result[2])
                notes.append(obj)
            return notes
        except Exception as e:
            raise


    def update_note(note):
        q = "update note set msg='%s' where id=%d" % (note.get_msg(), note.get_idt())
        try:
            con.cursor.execute(q)
            con.commit()
        except Exception as e:

            con.rollback()
            raise


    def search_notes( query):
        q = "select * from note where msg like '%{0}%' order by time desc".format(query)
        try:
            con.cursor.execute(q)
            notes = []
            results = con.cursor.fetchall()
            for result in results:
                obj = Note(idt=result[0], msg=result[1], time=result[2])
                notes.append(obj)
            return notes
        except Exception as e:
            raise


    def delete_note(note):
        q = "delete from note where id=%d" % (note.get_idt())
        try:
            con.cursor.execute(q)
            con.commit()
        except Exception as e:
            con.rollback()
            raise