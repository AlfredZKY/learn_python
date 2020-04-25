 # 
 # Created by preference on 2020/04/25
 # Author: AlfredZKY
 # Files:learn_mongo.py
 # WorkPlace:learn_python
 # 



import pymongo
from bson import ObjectId

# client = pymongo.MongoClient('mogondb://localhost:27017')
client = pymongo.MongoClient(host='localhost',port=27017)

# 制定数据库
# db = client['test']
db = client.tests # 没有就自己创建

# 指定集合，也就是表
# collection = db.students
collection = db.students # 没有就自己创建

def MongoInsert():
    # 插入数据
    student = {
        'id':'20170101',
        'name':'Zky',
        'age':20,
        'gender':'male'
    }

    result = collection.insert_one(student)
    print(result)

    student1 = {
        'id':'20170102',
        'name':'Mike',
        'age':21,
        'gender':'male'
    }

    student2 = {
        'id':'20170103',
        'name':'Nike',
        'age':22,
        'gender':'male'
    }

    result = collection.insert_many([student1,student2])
    print(result)

    student3 = {
        'id':'20170104',
        'name':'Marry',
        'age':22,
        'gender':'male'
    }

    result = collection.insert_one(student3)
    print(result)
    print(result.inserted_id)

def MongoFind():
    # 查询单条数据结果
    result = collection.find_one({'name':'Mike'})
    print(type(result))
    print(result)

    # 根据对象 ObjectId 来查询数据
    result = collection.find_one({'_id':ObjectId('5e9d9caccc27df229442dbcd')})
    print(result)

    # 查询多条数据
    # results = collection.find({'age':22})

    # 查询年龄大于20的数据
    results = collection.find({'age':{'$gt':20}})
    print(results)
    for result in results:
        print(result)
    
    # 统计查询结果有多少条数据，可以调用count方法
    count = collection.count_documents({'age':20})
    print(count)

    print('--------------------------------')
    # 排序 pymongo.ASCENDING 升序 pymongo.DESCENDING 降序 
    results = collection.find().sort('name',pymongo.ASCENDING)
    print([result['name'] for result in results])

    # 偏移 如果可能只需要某几个元素，可以利用skip方法偏移几个位置，比如偏移2就代表忽略前两个元素，得到第三个元素及以后的元素
    results = collection.find().sort('name',pymongo.ASCENDING).skip(2)
    print([result['name'] for result in results])

    # limit 指定要取得结果个数
    results = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(1)
    print([result['name'] for result in results])

def MongoUpdate():
    condition = {'name':'Mike'}
    student = collection.find_one(condition)
    student['age'] = 27
    result = collection.update_one(condition,{'$set':student})
    print(result)
    print(result.matched_count, result.modified_count) 

def MongoDelete():
    # result = collection.remove({'name':'Mike'})
    # print(result)
    print('==========================')
    # delete_one delete_many
    result = collection.delete_one({'name':'Nike'})
    print(result)
    print(result.deleted_count)


if __name__ == '__main__':
    #MongoInsert()
    # MongoFind()
    # MongoUpdate()
    MongoDelete()
    client.close()