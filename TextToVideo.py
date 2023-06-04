import cv2
import numpy as np
from TextToAudio import convert_text_to_speech
from AudioLength import get_audio_length
from Audio_Video_Merge import add_background_audio


def make_video(text):
    convert_text_to_speech(text)
    video_length=get_audio_length("audio\output.mp3")
    # create size for frame
    frame_size = (720, 720)
    border_size = 2

    # create blue background image
    bg = np.full((frame_size[0], frame_size[1], 3), (0, 0, 0), dtype=np.uint8)

    # calculate the text size and position
    text_color = (255, 255, 255)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    font_scale = 0.75 * 1.8
    thickness = 1
    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)

    # check if text needs to be split into multiple lines
    max_text_width = frame_size[1] - 20  # leave some margin on both sides
    if text_size[0] > max_text_width:
        words = text.split()
        lines = []
        line = ""
        for word in words:
            new_line = line + word + " "
            new_line_size, _ = cv2.getTextSize(new_line, font, font_scale, thickness)
            if new_line_size[0] > max_text_width:
                lines.append(line.strip())
                line = word + " "
            else:
                line = new_line
        lines.append(line.strip())
    else:
        lines = [text]

    # calculate the position for each line of text
    line_height = text_size[1] + 10  # add some spacing between lines
    total_text_height = len(lines) * line_height
    text_y = (frame_size[0] - total_text_height) // 2 + text_size[1]

    # draw centered text on bg
    for line in lines:
        text_size, _ = cv2.getTextSize(line, font, font_scale, thickness)
        text_x = (frame_size[1] - text_size[0]) // 2
        cv2.putText(bg, line, (text_x, text_y), font, font_scale, text_color, thickness, cv2.LINE_AA)
        text_y += line_height

    # create white border
    bordered_bg = cv2.copyMakeBorder(bg, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=(255, 255, 255))

    # write video
    out = cv2.VideoWriter('videos\output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 15, (bordered_bg.shape[1], bordered_bg.shape[0]))
    for _ in range(video_length * 15):  # Multiply video_length by 15 to determine the number of frames
        out.write(bordered_bg)
    out.release()

make_video("A week ago a friend invited a couple of other couples over for dinner. Eventually, the food (but not the wine) was cleared off the table for what turned out to be some fierce Scrabbling. Heeding the strategy of going for the shorter, more valuable word over the longer cheaper word")

add_background_audio("videos\output.mp4", "audio\output.mp3", "videos\output.mp4")