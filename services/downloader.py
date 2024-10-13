import os
import re
from pytube import YouTube
import instaloader

async def download_media(url, platform):
    if platform == "youtube":
        return await download_youtube(url)
    elif platform == "instagram":
        return await download_instagram(url)
    else:
        return None

async def download_youtube(url):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        filename = video_stream.download(output_path="downloads")
        return filename
    except Exception as e:
        print(f"Failed to download YouTube video: {e}")
        return None

async def download_instagram(url):
    try:
        L = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(L.context, extract_instagram_shortcode(url))
        filename = f"downloads/{post.shortcode}.mp4" if post.is_video else f"downloads/{post.shortcode}.jpg"
        
        L.download_post(post, target="downloads")
        return filename
    except Exception as e:
        print(f"Failed to download Instagram media: {e}")
        return None

def extract_instagram_shortcode(url):
    match = re.search(r'instagram.com/(?:p|reel)/([^/?]+)', url)
    return match.group(1) if match else None

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted file: {filename}")
    else:
        print(f"File not found: {filename}")
