class BaseVideoEntity:

    def __init__(self, f_id, download_url, source, desc='', title='', video_height=0, video_width=0, video_duration=0):
        self.f_id = f_id
        self.desc = desc
        self.title = title
        self.video_height = video_height
        self.video_width = video_width
        self.video_duration = video_duration
        self.download_url = download_url
        self.source = source
