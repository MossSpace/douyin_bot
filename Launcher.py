import json
import os
import sys
import mitmproxy
import tool.Downloader as downloader
from resource.douyin_config import Douyin

res = os.path.abspath(__file__)
base_path = os.path.dirname(os.path.dirname(res))

print('File Path is :%s' % res)
print('Parent Folder is :%s' % base_path)

sys.path.append(base_path)


class Hunter:

    douyin_hunter = Douyin()

    def response(self, flow: mitmproxy.http.HTTPFlow):
        response = flow.response
        if 'json' in str(response.headers.get('Content-Type')):
            data = json.loads(str(response.get_content(), 'utf-8'))
            downloader.download_video(self.douyin_hunter.dy_package, self.douyin_hunter.save_path, data)
            # print('此次下载视频数：%s ,当前下载视频总数：%s' % (count, self.video_count))


addons = [
    Hunter()
]
