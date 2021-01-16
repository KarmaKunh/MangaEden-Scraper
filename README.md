# MangaEden-Scraper

This is a simple scraper for the site MangaEden written in Python 3.9

It enables you to dowload any kind of manga series from the site https://www.mangaeden.com/it/

I called the script "EDEN"


Premise:

I'm new to GitHub and this is the first time i upload something here

I would like to learn more about the platform but for the moment everything may look a bit rough. 

Just Take it as it is ;)


---------------------------

HOW DOES IT WORK?

The Scraper code is composed of a single script file ( "Eden.py" ) in Python 3.9 which takes care of all the stuff

The Script make use of wget ( GNU Wget 1.20.3 built on mingw3 - here:https://eternallybored.org/misc/wget/ )

to download manga main pages


The adoption of Wget as the base tool to scrape the site was an early idea and more over the development I moved to the "Request" lib of python which I had to install through PIP ( the package installer for Python )

"Request" gave me more controll over the download process of the sigle files and most important, allowed me to easily change proxy for each request when needed


