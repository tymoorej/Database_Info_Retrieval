from bsddb3 import db

def yearSearch(Starting_Year):
    DB_File = "ye.idx"
    database = db.DB()
    database.set_flags(db.DB_DUP) #declare duplicates allowed before you create the database
    database.open(DB_File,None, db.DB_BTREE, db.DB_CREATE)
    curs = database.cursor()

    middleSet = set()
    result = curs.set(str(int(Starting_Year)+1).encode("utf-8"))
    print("LUKE: ",result)
    if(result != None):
        while(result != None):
            middleSet.add(result[1])
            result = curs.next()
    else:
        print("No result was found")
        return ()

    curs.close()
    database.close()
    return middleSet

def main():
    print(yearSearch(2018))


if __name__ == "__main__":
    main()
