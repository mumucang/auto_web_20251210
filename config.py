import os.path

project_path = os.path.dirname(os.path.abspath(__file__))
datas_path = os.path.join(project_path, 'datas')
logs_path = os.path.join(project_path, 'logs')
pictures_path = os.path.join(project_path, 'pictures')
reporters_path = os.path.join(project_path, 'reporters')
project_url = "http://192.168.190.132/ecshop/"


if __name__ == '__main__':
    print(os.path.dirname(os.path.abspath(__file__)))
    print(datas_path)
