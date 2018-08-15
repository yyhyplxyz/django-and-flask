import requests
#urllib或request发送http请求

class HTTP:
    @staticmethod #(静态方法 不用self)
    #Python2有经典类和新式类，写不写继承object没有关系
    def get( url, return_json=True):
        r = requests.get(url)
        #restful api返回json格式
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

