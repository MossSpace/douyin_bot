import tool.JsonTool as json_tool
from resource.BaseVideo import BaseVideoEntity


class Douyin:
    video_template = {'aweme_id', 'desc', 'duration', 'video'}
    # 爬取文件保存位置
    save_path = r'D:\test\douyin'

    def dy_package(self, json_data: dict):
        result = []
        for e in json_tool.pick_up(self.video_template, json_data):
            video = e.get('video')
            download_url = video.get('play_addr').get('url_list')[0]
            ve = BaseVideoEntity(f_id=e.get('aweme_id'),
                                 desc=e.get('desc'),
                                 video_height=video.get('height'),
                                 video_width=video.get('width'),
                                 video_duration=video.get('duration'),
                                 download_url=download_url,
                                 source='抖音')
            result.append(ve)
        return result
