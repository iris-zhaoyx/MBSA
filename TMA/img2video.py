from moviepy.editor import ImageSequenceClip
import os

def make_video(image_folder, output_vid, fps=30):
    """将指定文件夹内的所有图片转换成视频。
 
    参数:
    image_folder (str): 包含图片的文件夹路径。
    output_vid (str): 输出视频文件的路径。
    fps (int): 输出视频的帧速率，默认为24。
    """
    # 获取文件夹内所有图片的路径
    print("image_folder",image_folder)
    image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith((".jpg"))]
    # 按文件名排序
    image_files.sort()
    # 创建视频文件
    clip = ImageSequenceClip(image_files, fps=fps)
    # 输出到文件
    output_vid=output_vid+image_folder.split('/')[-1]+'.mp4'
    clip.write_videofile(output_vid)
 
    # 使用示例
    #make_video('path_to_images', 'output_video.mp4', fps=30)

if __name__ == "__main__":
    filePath= img_path
    output_path=output_path
    for root, dirs, files in os.walk(filePath, topdown=False):
        #image_folder = root.split('/')[-1]
        make_video(root, output_path, fps=30)
