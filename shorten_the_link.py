import pyshorteners

link=input("enter the link").strip()

shortener=pyshorteners.Shortener()

shortened_link= shortener.tinyurl.short(link)

print("shortened link:", shortened_link)