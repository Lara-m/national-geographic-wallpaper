# National Geographic Wallpaper - Minified Version


## Compatibility

** Works with... I'm not sure. Linux stuff, most likely. (didn't test on anything but arch tbh) **

## Usage

` python WallPaperFetcher.py {working directort} {source} `

working directory: specify where the photo can be saved. Full path. Like "/home/randomuser/Pictures/Wallpapers"

source: 
> " " - default - national geographics (literally put nothing)
>
> "nasa"
>
> "gopro"
>
> "bing"
>
> "desktoppr"
>
> "unsplash"
>
> "picsum"
>
> "splashbase"
>
> "cats"



## Bckstory

Who wrote it: Lara_m 

Where you got it from: https://github.com/Lara-m/national-geographic-wallpaper

What it is based on: https://github.com/atareao/national-geographic-wallpaper

What the hell am I doing? The previous version didn't work with python 3 which broke my arch (with my help, ofc). :sniff: So here is the backwarded remake for python 3. Also added a few other apis. and removed whatever I couldn't be bothered to use css selectors for. (Sorry Lorenzo!)

## Notes

nasa may take a while to load. Or even fail on occassions. Gotta retry.

Let me if anything went too bad.

## Extra stuff

[Use this guide for systemd scheduling]
(https://major.io/2015/02/11/rotate-gnome-3s-wallpaper-systemd-user-units-timers/)

And just use something like this in service:

` ExecStart=/usr/bin/python /home/randomuser/NGW/WallPaperFetcher.py /home/randomuser/Pictures/Wallpapers cats `
