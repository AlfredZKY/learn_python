from marshmallow import Schema, fields, pprint
import datetime as dt


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)


'''
    要对一个类或者一个json数据实现相互转换（即序列化和反序列化，序列化的意思是将数据转化为可存储或可传输的数据类型），
    需要一个中间载体，这个载体就是Schema。除了转换以外，Schema还可以用来做数据校验。
    每个需要转换的类，都需要一个对应的Schema：
'''


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()


user = User(name="Monty", email="monty@python.org")
schema = UserSchema()
result = schema.dump(user)
pprint(result)


data = {
        'created_at': '2020-03-12T10:49:15.353060',
        'email': 'monty@python.org',
        'name': 'Monty'
        }
