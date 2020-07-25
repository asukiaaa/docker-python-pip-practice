import fire
import datetime

def hello(name=None):
    if name is None:
        print('hello')
    else:
        print('hello' + name)

def show_time():
    print(datetime.datetime.now().strftime('%y:%m:%d %H:%M:%S'))

if __name__ == '__main__':
    fire.Fire()
