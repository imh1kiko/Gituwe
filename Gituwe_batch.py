import os
import shutil
from os import walk
from pathlib import Path, PureWindowsPath
execPath = os.path.dirname(__file__)
os.chdir(execPath)
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

                        ___  ____ ___ ____ _  _ 
                        |__] |__|  |  |    |__| 
                        |__] |  |  |  |___ |  | 
                             
                             


"""

print(logo)

###
def loop(inf):
        # Before beginning, check for temp existance
        os.chdir(execPath)
        if not os.path.isdir("tmp"):
            os.makedirs("tmp")

        merge = " -i " + inf + " -o tmp/temp.mkv -e vp9 --no-comb --no-deinterlace --no-detelecine --no-hqdn3d --no-nlmeans --no-unsharp --no-lapsharp --no-deblock -2 -T --encoder-preset VeryFast --loose-anamorphic -a none -b 1000"

        # Render
        os.system('HandBrakeCLI.exe' + merge) 
        os.system('ffmpeg.exe' + ffmpegvar)

        # Delete temp, so no prompt is thrown for overwrite
        shutil.rmtree("tmp")
        pass
###

# Find all files in folder, create array with location and file name
# send this to loop until the end of array

# Get location input
locPath = input("What location would you like to mass render? (drag-drop)  ")

# Change cwd to input
os.chdir(locPath)

# Walk the dir for all files, delete any that do not end with "gif, mp4, avi, wmv, mkv"
files = []
i=0

for (dirpath, dirnames, filenames) in walk(locPath):
    files.extend(filenames)
    pass

while i<len(files):
    # Construct input file for loop
    inf = locPath+"\\"+files[i]
    # Change suffix
    p = PureWindowsPath(files[i]).with_suffix('.webm')
    p = str(p).replace(" ", "_")
    print("===============================>>>"+p)
    # Create output var
    os.chdir(execPath)  
    ffmpegvar = " -i tmp/temp.mkv -c copy " + locPath+"\\"+p

    # Send into loop
    loop(inf)
    i+=1
    pass

