from moviepy.editor import VideoFileClip


def extract_audio(video_path: str, audio_path: str):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
    except Exception as Ex:
        print("!Error extract_audio", Ex)


# extract_audio(video_path="dataset/62.mp4", audio_path=f"my/cloning/62.wav")
