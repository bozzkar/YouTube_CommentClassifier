def comments_generator(client, video_url,data_file):
    
    comment_feed = client.GetYouTubeVideoCommentFeed(uri=video_url)
    count=0

    while comment_feed is not None and count<=500:
        for comment in comment_feed.entry:
             count+=1
	     comment_content = comment.content.text
	     if comment_content is not None:
		comment_content_lines = comment_content.splitlines()
		comment_content_stripped = ''.join(comment_content_lines)
       	     	print >>data_file, comment_content_stripped
	     	#print >>data_file, '\n' 

        next_link = comment_feed.GetNextLink()
        if next_link is None:
             comment_feed = None
        else:
	     print '\n' + str(count)
             comment_feed = client.GetYouTubeVideoCommentFeed(next_link.href)

def main():
	video_id = sys.argv[1]
	video_url = 'https://gdata.youtube.com/feeds/api/videos/'+video_id+'/comments?orderby=published&max-results=50'
	comments_out = open('comments_output.txt','w+')
	yt_service = gdata.youtube.service.YouTubeService()
    	yt_service.ssl = True
	comments_generator(yt_service,video_url,comments_out)
	print >> "Done"

main()
