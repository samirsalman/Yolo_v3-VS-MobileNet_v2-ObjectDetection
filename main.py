from DetectionModel import DetectionModel
from utils.youtube_downloader import YoutubeDownloader
from models import Models

# example video (traffic video)
url = 'https://www.youtube.com/watch?v=UM0hX7nomi8'

youtube_downloader = YoutubeDownloader(url=url)
# download the video from youtube
video_name = youtube_downloader.download_video()

# ----------------------------------------------------------------------------------

MODEL = Models.MOBILENET_V2

# init the MobileNet model
net = DetectionModel(weights_path=MODEL["weights"],
                     pbtext_path=MODEL["pbtxt"],
                     classnames_path=MODEL["classnames"],
                     yolo=False)

# ---------------------------------------------------------------------------------
# test the model
net.live_test(camera=False, video=video_name)
