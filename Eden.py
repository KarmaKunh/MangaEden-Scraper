import subprocess
import re
import os
import _thread
import time
import requests
import random
import threading
import filecmp
import shutil

FNULL = open(os.devnull, 'w')

sleepTime= 0.5

lock = threading.Lock()
printLock= threading.Lock()
chapterProgressionLock= threading.Lock()

proxies =[ { 'http': 'http://67.207.83.225:80'},
           { 'http': 'http://89.187.177.95:80'},
           { 'http': 'http://89.187.177.107:80'},
           { 'http': 'http://89.187.177.90:80'},
           { 'http': 'http://89.187.177.91:80'},
           { 'http': 'http://89.187.177.106:80'},
           { 'http': 'http://89.187.177.96:80'},
           { 'http': 'http://89.187.177.87:80'},
           { 'http': 'http://89.187.177.102:80'},
           { 'http': 'http://89.187.177.93:80'},
           { 'http': 'http://167.71.149.82:80'},
           { 'http': 'http://192.109.165.41:80'},
           { 'http': 'http://89.187.177.100:80'}]

proxiesUses= {}
for i in proxies:
    proxiesUses[ i.get("http")]= 0

#print( proxiesUses)

chapterProgression=[ ""]
chapterConcluded= []


    
def pageDownloader( manga, chapter, page):
    '''
    prox= {}
    sleep= "no"
    while ( prox== {}):
        lock.acquire()
        if ( proxies!=[]):
            prox= proxies.pop()
            if( proxiesUses[ prox.get("http")]==5):
                print( "Waiting1 1 sec for :"+ prox.get("http")+" Ch: "+ chapter+" Pg: "+ page)
                sleep="yes"
                proxiesUses[ prox.get("http")]= 1
            else:
                proxiesUses[ prox.get("http")]= proxiesUses[ prox.get("http")]+ 1
        
        lock.release()
        if( sleep=="yes"):
            time.sleep( sleepTime)
    
    research= "https://www.mangaeden.com/it/it-manga/"+manga+"/"+chapter+"/"+page

    check= 0
    while( check== 0):
        try:
            req= requests.get(research, proxies=prox)
            check= 1
        except:
           print("Exception1 with: "+prox.get("http")+" Ch: "+ chapter+" Pg: "+ page)
           time.sleep( sleepTime)

    proxies.insert( 0, prox)
    
    '''

    prox= {}
    sleep= "no"
    while ( prox== {}):
        lock.acquire()
        if ( proxies!=[]):
            prox= proxies.pop()
            if( proxiesUses[ prox.get("http")]==5):
                print( "Waiting1 1 sec for :"+ prox.get("http")+" Ch: "+ chapter+" Pg: "+ page)
                sleep="yes"
                proxiesUses[ prox.get("http")]= 1
            else:
                proxiesUses[ prox.get("http")]= proxiesUses[ prox.get("http")]+ 1
        
        lock.release()
        if( sleep=="yes"):
            time.sleep( sleepTime)

    research= "https://www.mangaeden.com/it/it-manga/"+manga+"/"+chapter+"/"+page
    
    try:   
            req= requests.get( research, proxies=prox)
            open('pages/research/manga/'+manga+'/'+chapter+'/'+page+'.html', 'wb').write(req.content)
    except:
            print("Exception2 with: "+prox.get("http")+" Ch: "+ chapter+" Pg: "+ page)
            
    while( filecmp.cmp('pages/research/manga/'+manga+'/'+chapter+'/'+page+'.html', 'pages/501', shallow = False) ):
        try:   
            req= requests.get( research, proxies=prox)
            open('pages/research/manga/'+manga+'/'+chapter+'/'+page+'.html', 'wb').write(req.content)
            if( filecmp.cmp(fileCheck, 'pages/501', shallow = False)):
                print("Inside---------------------------------<<<<<")
                time.sleep( 3)
            
        except:
            print("Exception with: "+prox.get("http"))
            time.sleep( 3)

    proxies.insert( 0, prox)

    open('pages/research/manga/'+manga+'/'+chapter+'/'+page+'.html', 'wb').write(req.content)

    file = open("pages/research/manga/"+manga+"/"+chapter+"/"+page+".html", encoding="utf8")
    fileRead= file.read()
    links = re.findall(r'src=\"(.*)\" onerror', fileRead)
    research= links[0].replace('\"', '')
    file.close()
    

    

    prox= {}
    sleep= "no"
    while ( prox== {}):
        lock.acquire()
        if ( proxies!=[]):
            prox= proxies.pop()
            if( proxiesUses[ prox.get("http")]==5):
                print( "Waiting2 1 sec for :"+ prox.get("http")+" Ch: "+ chapter+" Pg: "+ page)
                sleep="yes"
                proxiesUses[ prox.get("http")]= 1
            else:
                proxiesUses[ prox.get("http")]= proxiesUses[ prox.get("http")]+ 1
        
        lock.release()
        if( sleep=="yes"):
            time.sleep( sleepTime)

    extension= re.findall(r'(\.jpg|\.png)', fileRead)
    
    try:   
            req= requests.get( 'https:'+research, proxies=prox, headers={'referer': 'https://www.mangaeden.com/it/'})
            open('manga/'+manga+'/'+chapter+'/'+page+ extension[ 0], 'wb').write(req.content)
    except:
            print("Exception2 with: "+prox.get("http")+" Ch: "+ chapter+" Pg: "+ page)
            
    while( filecmp.cmp('manga/'+manga+'/'+chapter+'/'+page+ extension[ 0], 'pages/501', shallow = False) ):
        try:   
            req= requests.get( 'https:'+research, proxies=prox, headers={'referer': 'https://www.mangaeden.com/it/'})
            open('manga/'+manga+'/'+chapter+'/'+page+ extension[ 0], 'wb').write(req.content)
            if( filecmp.cmp(fileCheck, 'pages/501', shallow = False)):
                print("Inside---------------------------------<<<<<")
                time.sleep( 3)
            
        except:
            print("Exception with: "+prox.get("http"))
            time.sleep( 3)

    proxies.insert( 0, prox)

    
    #print( extension[0])
    
    open('manga/'+manga+'/'+chapter+'/'+page+ extension[ 0], 'wb').write(req.content)
    
    open('pages/research/manga/'+manga+'/'+chapter+'/check/'+page, 'a').close()
    
    #subprocess.check_call(['wget.exe', '--output-document=pages/research/manga/'+manga+'/'+chapter+'/'+page+'.html', research], stdout=FNULL, stderr=subprocess.STDOUT)

   
    
    
def chaptetrDownloader( manga, chapter, chapterProgIndex):
    
    if( not( os.path.isdir("manga/"+manga+"/"+chapter))):
        os.makedirs("manga/"+manga+"/"+chapter)
    if( not( os.path.isdir("pages/research/manga/"+manga+"/"+chapter))):
        os.makedirs("pages/research/manga/"+manga+"/"+chapter)
        os.makedirs('pages/research/manga/'+manga+'/'+chapter+'/check')
        
        
    research= "https://www.mangaeden.com/it/it-manga/"+manga+"/"+chapter+"/1"
    subprocess.check_call(['wget.exe', '--output-document=pages/research/manga/'+manga+'/'+chapter+'/'+chapter+'.html', research], stdout=FNULL, stderr=subprocess.STDOUT)
    
    file = open("pages/research/manga/"+manga+"/"+chapter+"/"+chapter+".html", encoding="utf8")

    fileRead= file.read()

    links = re.findall(r'data\-page=\"([0-9]*)\"', fileRead)

    linksWrite= []

    for i in links:
        i= i.replace('\"', '')
        linksWrite.append( i)

    file.close()

    for i in linksWrite:
        #pageDownloader(manga, chapter, i)
        _thread.start_new_thread( pageDownloader, (manga, chapter, i))
        #round(a_float, 2)

    count= 0
    while( count< len( linksWrite)):
        time.sleep( 1)
        count= 0
        for x in os.listdir('pages/research/manga/'+manga+'/'+chapter+'/check/'): 
            count= count+1
            chapterProgressionLock.acquire()
            chapterProgression.insert( chapterProgIndex, "Chapter "+ chapter+": DOWNLOADING - "+ str( int( count/len( linksWrite)*100))+"%")
            chapterProgression.remove( chapterProgression[ chapterProgIndex+ 1])
            chapterProgressionLock.release()
            
    printLock.acquire()
    chapterConcluded.append( chapter)
    #print( "Chapter "+ chapter+" - DOWNLOADED")
    printLock.release()


    


def checkProgression( chapters):
    while( len( chapterConcluded)< chapters):
        time.sleep( 1)
        clearScreen()
        for i in chapterProgression:
            print( i)

    



def clearScreen():
    subprocess.call( 'cls', shell=True)


def checkProxies():
    print( "PROXY CHECK - wait some seconds")
    count=0
    while( count< len( proxies)):
        try:
            requests.get( "https://www.facebook.com/", proxies= proxies[ count])
            count= count+1
        except:
            print( str( proxies[ count]) +" REMOVED - unreachable machine")
            proxies.remove( proxies[ count])
            
            if( count!= 0):
                count= count-1

    print()
    print( str( len( proxies))+ " PROXIES are working")
    print()
    print( "PROXY CHECK COMPLETED")
    print()
    print()

        


#----- Input Ricerca Utente e Download Pagina Ricerca


checkProxies()    
    

print( "MANGAEDEN Manga Downloader")
print( "Quale Manga vuoi scaricare?")
researchManga= input( "> ")

researchManga= researchManga.replace(" ", "+")
research= "https://www.mangaeden.com/it/it-directory/?title="+researchManga

subprocess.check_call(['wget.exe', '--output-document=pages/research/'+researchManga+'.html', research], stdout=FNULL, stderr=subprocess.STDOUT)

file = open("pages/research/"+researchManga+".html", encoding="utf8")

fileRead= file.read()

links = re.findall(r'class=\"(?:closedManga)?(?:openManga)?\">(.*)<\/a>', fileRead)

#print( links)

linksWrite= []

for i in links:
    i= i.replace('\"', '')
    linksWrite.append( i)

file.close()

#----- ELENCO MANGA TROVATI in Pagina Ricerca

print( "Trovati [ ", len( linksWrite), " ] risultati")
print( "Elenco Manga")
count=1
for i in linksWrite:
    print( count,". "+i)
    count= count+ 1

#----- SELEZIONE MANGA Interessato
    
print( "Seleziona un indice dall'elenco")
selectedIndex= input( "> ")

selectedManga= linksWrite[ int(selectedIndex)-1]
selectedManga= selectedManga.replace(" ", "-")

print( selectedManga)

#----- DOWNLOAD PAGINA PRINCIPALE Manga Interessato

selectedManga= selectedManga.lower()
research= "https://www.mangaeden.com/it/it-manga/"+selectedManga
subprocess.check_call(['wget.exe', '--output-document=pages/research/'+selectedManga+'.html', research], stdout=FNULL, stderr=subprocess.STDOUT)

#----- Individuazione Elenco Capitoli

file = open("pages/research/"+selectedManga+".html", encoding="utf8")

fileRead= file.read()

links = re.findall(r'href="\/it\/it-manga\/.*\/(.*)\/.*\/" class=\"chapterLink\"', fileRead)

#print( links)

linksWrite= []

for i in links:
    i= i.replace('\"', '')
    linksWrite.append( i)

file.close()

linksWrite.reverse()

print( "Manga: "+ selectedManga)
print( "Capitoli: "+ str( len( linksWrite)))
print()
print( "Quanti Capitoli Scaricare?")
selectedChapters= input( "> ")
    
x= 0
chapterList= []
while ( x< int( selectedChapters)):
    chapterProgression.insert( x, "Chapter "+ linksWrite[ x]+": DOWNLOADING - 0%")
    thread= threading.Thread( target=chaptetrDownloader, args=( selectedManga, linksWrite[ x], x))
    thread.start()
    chapterList.append( thread)
    x= x+1

thread= threading.Thread( target=checkProgression, args=[ int( selectedChapters)])
thread.start()

for x in chapterList:
    x.join()

thread.join()

#---- FINE


shutil.rmtree("pages/research/manga", ignore_errors=False, onerror=None)

print()
print()
print( "All Chapters correctly downloaded")
print()
input( "PRESS TO END")

#input("PRESS TO END")
