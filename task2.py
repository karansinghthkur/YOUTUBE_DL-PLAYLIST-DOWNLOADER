import youtube_dl
url=input('ENTER URL OF PLAYLIST TO DOWNLOAD:')#TAKES INPUT OF URL PLAYLIST

ydl_opts = {
    'format': 'bestaudio/best',       
    'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',        
    'noplaylist' : False,        
    'listformats': True 
}#GETS THE INFORMATION OF FORMAT NEEDED TO BE DOWNLOADED
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
frmt=input("ENTER common format code from given lists : " )
#INPUT THE FORMAT TO SPECIFY THE PLAYLIST
ydl_optss = {
    'format': frmt,       
    'outtmpl': 'e:/python/downloadedvids/%(title)s.%(ext)s',#FILE LOCATION TO DOWNLOAD        
    'noplaylist' : False,#noplaylist' : False ensurrres if url is playlist entire playlist is downloaded
    }
with youtube_dl.YoutubeDL(ydl_optss) as ydl:
    ydl.download([url]) 
    
#DOWNLOADS THE VIDEO SUCESSFULLY USING URL   
