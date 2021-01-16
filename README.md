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

By the way, the main page of each manga is still got by wget. Whit future releases i'm going to convert it to the "Request" lib too

---------------------------

ABOUT PROXIES:

When I started coding the script, i dint know i would need the use of a lot of proxies to get everything done, but testing the programm i realized their importance to avoid web server refusing my requests

The Script got a series of proxies saved in a "Dictionary" and checks for their functioning just when the execution starts, removing not reachable ones

---------------------------

ABOUT FILE 501 INSIDE "Pages" FOLDER:

This file is really important
Sometime a page request get "refused" by mangaeden webserver because too much request were just sent whit the same IP ( Proxy )
The WebServer realize im a Scraper and decide to joke me
It responds with a fake page telling "ERROR 501" so that "Response" lib does not return an error and cant understan if the correct response was jkust sent by the webserver

When this moment comes, having this fake page stored allows the programm to compare it with one he just dowloaded
if they match, too much requests have been sent with the same proxy, and current download thread, sleeps for 0.5 seconds before retrying


---------------------------

Well, basically this is how the script gets everything done

All the new stuff is stored insed "manga/manga-name/chapter-number/" folder




Hope my work is not so bad for you


Whit Love,

Karma



Milano - italy
