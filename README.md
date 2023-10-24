# PaintingToMusic
This program converts an image into music. More specifically, it converts pixel data into music data using a sound-color correspondence.

I used the sound-color correspondance from the following article: https://www.flutopedia.com/sound_color.htm

## How It Works

1. Feed an image to the program.
2. It goes through each pixel of the image to determine its color, using OpenCV-Python.
3. It then matches the color to a specific sound note and plays it. To play a specific musical note, I used musicalbeeps library.

Since some of the images can be extremely large and can contain a lot of pixels, playing notes even for a very brief moment for every pixels can take large amount of time. To address that issue, I've shrunk down the image by a resize factor, which can be passed as a parameter. 

Moreover, since sound notes in the Western Music system are discrete and colors are continuous, I used color similarity to find the most similar color from the sound-color correspondance chart with the given color of a pixel. More information can be found at the Arts-Paper that I wrote for the program. You can read it [here](https://github.com/RyanX5/PaintingToMusic/blob/main/Arts-Paper.pdf).

## Additional Details

This project was a part of HONORS ARTS class final paper, at **Univeristy of Louisiana Monroe.** The class was about the relationship between visual arts and music. I thought it would be a great idea to draw an objective relationship between music and visuals, and code a program that could demonstrate that.

None of the theories used to make the program is scientifically recognized or proven, including the sound-color correspondance. I highly encourage you to read the [article](https://www.flutopedia.com/sound_color.htm) yourself to draw your own conclusions.

## Futher Improvements

1. Make the usage seamless by turning the program into a commandline script, that allows the user to set the parameters easily.
2. Make it so that the sounds are played in a scale (Major, Harmonic, etc) so that they sound more musical and not chromatic.
3. Add visual elements to the program.





