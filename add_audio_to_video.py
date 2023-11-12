from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip


# def save_video_without_audio(input_video_path, output_video_path):
#     video = VideoFileClip(input_video_path)
#     video_without_audio = video.without_audio()
#     video_without_audio.write_videofile(output_video_path)


def add_audio(video_path: str, audio1_path: str, audio2_path: str, output_path: str):
    video = VideoFileClip(video_path)

    video_without_audio = video.without_audio()

    audio1 = AudioFileClip(audio1_path)
    audio2 = AudioFileClip(audio2_path)

    final_audio = CompositeAudioClip([audio1, audio2])

    video_with_audio = video_without_audio.set_audio(final_audio)
    video_with_audio.write_videofile(output_path)
