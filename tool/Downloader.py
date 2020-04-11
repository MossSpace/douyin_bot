import requests
import os
import urllib3
from tool import Session

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ua = 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 ' \
     'Mobile/15A5341f Safari/604.1 '


def __down_file(download_url, file_id, save_path):
    """
    下载文件
    :param download_url: 文件下载地址
    :param file_id: 下载后本地保存名称
    """
    if file_id not in Session.HUNTER_ID_CACHE:
        ss = requests.session()
        res = ss.get(download_url, headers={'User-Agent': ua}, verify=False)
        if len(res.content) > 100:
            with open(save_path + r'\%s.mp4' % file_id, 'wb') as f:
                f.write(res.content)
                Session.HUNTER_ID_CACHE.add(file_id)
    else:
        print('ID重复————————————')


def download_video(package_function, save_path, json_content):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    videos = package_function(json_content)
    for e in videos:
        __down_file(e.download_url, e.f_id, save_path)
