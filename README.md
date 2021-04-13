# Batch Video Format Transforming
A python program that can transform all video files in a folder into a common format supported by ffmpeg


<h4>Before you use:</h4>
<p>•	Install ffmpeg (https://www.ffmpeg.org/), a free command line tool to transform different video type files, including h264, avi, mp4, etc.<br>
•	Install ffmpy, a python wrapper for ffmpeg. (https://ffmpy.readthedocs.io/en/latest/)<br>
•	I use Jupyter Notebook but other python IDE should also work if you have correctly installed the said packages.</p>


<h4> Two things you need to set in the script:</h4>
<p>1.Your full file path. Example: r'C:\Users\K lab Yuejun\Box' Note: the file path should be the full path. And please DON'T include a '\' at the end of your path<br>
2.The format you need your video files to change into. Exmaple: '.avi', '.mp4'
