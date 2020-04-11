import tool.JsonTool as json_tool
from resource.BaseVideo import BaseVideoEntity


class DouyinHuoshan:
    video_template = {'id', 'description', 'title', 'video'}
    # 爬取文件保存位置
    save_path = r'D:\test\douyin_huoshan'

    def dy_hs_package(self, json_data: dict):
        result = []
        for e in json_tool.pick_up(self.video_template, json_data):
            video = e.get('video')
            download_url = video.get('h265_url')[0]
            ve = BaseVideoEntity(f_id=e.get('id'),
                                 desc=e.get('description'),
                                 title=e.get('title'),
                                 video_height=video.get('height'),
                                 video_width=video.get('width'),
                                 video_duration=video.get('duration'),
                                 download_url=download_url,
                                 source='抖音火山')
            result.append(ve)
        return result
