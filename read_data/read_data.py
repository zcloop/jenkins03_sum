import yaml


class ReadData(): #定义一个类，专门用来读取各种格式的文件中的数据
    def read_yaml(self): #读取yaml文件的方法，读出数据并返回
        with open("./data/data_sum.yaml","r",encoding="utf-8") as f:
            return yaml.load(f) #

    def read_txt(self):
        pass

    def read_csv(self):
        pass

if __name__ == '__main__':
    print(ReadData().read_yaml())