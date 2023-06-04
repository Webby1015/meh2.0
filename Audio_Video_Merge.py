from moviepy.editor import VideoFileClip, AudioFileClip

def add_background_audio(video_path, audio_path, output_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    video = video.set_audio(audio)
    video.write_videofile(output_path, codec="libx264", audio_codec="aac", verbose=False,logger=None)
