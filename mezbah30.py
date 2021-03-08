import pickle

def storeData():
    davide = {'key': 'davide','name':'mezbah davide',
              'age' : '25', 'pay' : '100000$'}
    mezbah = {'key' : 'mezbah', 'name' : 'davide mezbah',
              'age' : '26', 'pay' : '100000$'}

    db = {}
    db['davide'] = mezbah
    db['mezbah'] = davide

    dbfile = open('examplePickle','ab')

    pickle.dump(db,dbfile)
    dbfile.close()

def loadData():
    dbfile = open('examplePickle', 'rb')


    
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])

if __name__ == '__main__':
    storeData()
    loadData()