"""
    Mongodb工具类
"""
import pymongo
class MongoUtil:

    def __init__(self, dbname = 'spider'):
        self.url = 'localhost'
        self.port = 27017
        self.client = pymongo.MongoClient(self.url, self.port)
        self.db = self.client[dbname]

    def add_data(self, table_name, record):
        try:
            coll = self.db[table_name]
            coll.save(record)
        except pymongo.errors.DuplicateKeyError:
            print('record exists')
        except Exception as e:
            print(e)

    def add_datas(self, table_name, records):
        try:
            coll = self.db[table_name]
            for record in records:
                coll.save(record)
        except pymongo.errors.DuplicateKeyError:
            print('record exists')
        except Exception as e:
            print(e)

    def del_data(self, table_name, data):
        coll = self.db[table_name]
        record = coll.remove(data)

    def update_data(self):
       pass

    def find_data(self, table_name, data):

        coll = self.db[table_name]
        record = coll.find_one(data)
        return record

    def find_datas(self):
        pass

def main():
    mu = MongoUtil('test')
    list = [{"aqi": 20, "area": "上海", "pm2_5": 14, "pm2_5_24h": 14, "position_name": "十五厂", "primary_pollutant": "", "quality": "优", "station_code": "1142A", "time_point": "2017-07-29T14:00:00Z"}, {"aqi": 29, "area": "上海", "pm2_5": 20, "pm2_5_24h": 17, "position_name": "静安监测站", "primary_pollutant": "", "quality": "优", "station_code": "1147A", "time_point": "2017-07-29T14:00:00Z"}, {"aqi": 29, "area": "上海", "pm2_5": 20, "pm2_5_24h": 11, "position_name": "浦东新区监测站", "primary_pollutant": "", "quality": "优", "station_code": "1149A", "time_point": "2017-07-29T14:00:00Z"}, {"aqi": 30, "area": "上海", "pm2_5": 19, "pm2_5_24h": 16, "position_name": "徐汇上师大", "primary_pollutant": "", "quality": "优", "station_code": "1144A", "time_point": "2017-07-29T14:00:00Z"}, {"aqi": 34, "area": "上海", "pm2_5": 19, "pm2_5_24h": 15, "position_name": "", "primary_pollutant": "", "quality": "优", "station_code": "", "time_point": "2017-07-29T14:00:00Z"}]
    list2 = ['http://www.baidu.com', 'http://www.baidu.com2', 'http://www.baidu.com3']
    mu.add_datas('test', list)
    mu.add_datas('url', list2)
if __name__ == '__main__':
    main()



