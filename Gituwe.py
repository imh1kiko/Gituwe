import os
import shutil
os.chdir(os.path.dirname(__file__))
if not os.path.isdir("tmp"):
   os.makedirs("tmp")

logo = """ 

  ::::::::  ::::::::::: ::::::::::: :::    ::: :::       ::: :::::::::: 
 :+:    :+:     :+:         :+:     :+:    :+: :+:       :+: :+:        
 +:+            +:+         +:+     +:+    +:+ +:+       +:+ +:+        
 :#:            +#+         +#+     +#+    +:+ +#+  +:+  +#+ +#++:++#   
 +#+   +#+#     +#+         +#+     +#+    +#+ +#+ +#+#+ +#+ +#+        
 #+#    #+#     #+#         #+#     #+#    #+#  #+#+# #+#+#  #+#        
  ########  ###########     ###      ########    ###   ###   ##########                            

                                          _   _ 
                    | | _  _  _ . _  _   / / /_/
                    |/ /_'/ _\ / /_// / /_/ . / 

                                                                            


"""

print(logo)

# Asking all neccesary info
in_file = input(" Drag the source file:  ")
def outFolder():
    outname = input(" Name of the end-file (empty = same as source):  ").replace(" ", "_")
    # Dissect file location
    buffer = in_file.split("\\")
    i = 0
    outF = ""
    while i < len(buffer)-1:
        outF += buffer[i]+"\\"
        i+=1
        pass

    #If no filename is given, dissect filename from in-file, otherwise, use given name.
    if outname != '':
        outF+=outname
        pass
    else:
        b1 = in_file.split("\\")
        arl = len(b1)-1
        b2 = b1[arl].split(".", maxsplit=1)
        outname = str(b2[0])
        outF += outname
    return outF

outname = outFolder()
vbrate = input(" What is the video bitrate? (default: 1000kbps):  ")
abrate = input(" What is the audio bitrate? (leave empty, if no audio):  ")
resize = input(" Resize video to... (leave empty if you want original size):  ")
merge = " -i " + in_file + " -o tmp/temp.mkv -e vp9 --no-comb --no-deinterlace --no-detelecine --no-hqdn3d --no-nlmeans --no-unsharp --no-lapsharp --no-deblock -2 -T --encoder-preset VeryFast --loose-anamorphic"

ffmpegvar = " -i tmp/temp.mkv -c copy " + outname + ".webm"

# Complete the command
def completeCommand():
    completeMerge = merge

    if vbrate != '':
        completeMerge += " -b " + vbrate 
    else:
        completeMerge += " -b 1000"
    pass

    if abrate != '':
        completeMerge += " -E opus --all-audio -B " + abrate
    else:
        completeMerge += " -a none"
        pass

    if resize != '':
        completeMerge += " --height " + resize
        pass

    return completeMerge

os.system('HandBrakeCLI.exe' + completeCommand()) 
os.system('ffmpeg.exe' + ffmpegvar)
print(ffmpegvar)

shutil.rmtree("tmp")