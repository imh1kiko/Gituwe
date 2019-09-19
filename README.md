# Gituwe
Automation of HandbrakeCLI and FFmpeg to render most video formats and gifs into webm.
<br>
<br>
<br>

# Why?
More as a personal use thing. It's definitely in no condition to be released to public. If anything, I'd rather not have anyone even look at this trainwreck.
<br>
<br>

As we know, Discord's file sharing limit is **8MB**. That means, you either use some sort of file-sharing service (like *MEGA* or *Firefox Send*), or you squash that file down. 

Seeing gifs going over 30MB on some websites is also frustrating. With this, you can squash it down to 80% of it's size (depending on the settings of course, but generally, defaults are good). If it says anything, I used batch processed a lot of debatable hentai gifs. Here's some comparisons.
(Don't judge. I know you ain't any better.)

[PlaceHolder for images]
<br>
<br>
<br>
Ironically, I actually hated webms. **A LOT**. Prejudice, perhaps.

# How does it work?

Currently, it uses python, because doing all of this in batch was just straight up pain in the ass.

For *Gituwe.py*, after launching, you wanna drag-drop the file you wanna convert into the window. From there on, you go through the settings. Pretty much self explanatory. File name, video bitrate, audio bitrate, if you wanna resize, and then it starts the conversion.

## Gituwe Batch Process

Kinda broken. I'm unsure what keeps throwing an error. So far, the folder name should have no spaces. Not too sure about filenames.

Batch processing works on folder, rather than file. Anything you wanna convert, add to that folder, and then throw it into it. Thing is, you're gonna have to edit the code yourself, as I found out, python imports are just annoying.

The line you need to edit is where "merge" variable is.


