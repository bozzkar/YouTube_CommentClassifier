import gdata.youtube
import gdata.youtube.service
import sys
import os
import time

video_id = sys.argv[1]

def labelComments():
	os.system("sed -e 's/^/0\t/' "+video_id+"_comments_output.txt>"+video_id+"_comments_output_pp.txt")
	os.system("sed -i -e '/[0-9]:[0-9]/ s/$/ timesuggest/' "+video_id+"_comments_output_pp.txt")
	time.sleep(2)
	os.system("python text-predict.py -f -a 0 "+video_id+"_comments_output_pp.txt vulgar_comments.txt.model "+video_id+"_vulgar_labels.txt")
	time.sleep(2)	
	os.system("python text-predict.py -f -a 0 "+video_id+"_comments_output_pp.txt adv_comments.txt.model "+video_id+"_adv_labels.txt")
	time.sleep(2)
	os.system("python text-predict.py -f -a 0 "+video_id+"_comments_output_pp.txt skip_comments.txt.model "+video_id+"_skip_labels.txt")
	time.sleep(2)	

def mapLabelToComments():

	commentsFile = video_id+'_comments_output.txt'
	vulgarLabelsFile = video_id+'_vulgar_labels.txt'
	adLabelsFile = video_id+'_adv_labels.txt'
	skipLabelsFile = video_id+'_skip_labels.txt'
	
	vulgarCategoryFile = open(video_id+'_offensive.txt','w+')
	adCategoryFile = open(video_id+'_spam.txt','w+')
	skipCategoryFile = open(video_id+'_positive.txt','w+')

	with open(commentsFile) as cf,open(vulgarLabelsFile) as vf,open(adLabelsFile) as adf,open(skipLabelsFile) as sf:
		cfcontent = cf.readlines()
		vfcontent = vf.readlines()
		adfcontent = adf.readlines()
		sfcontent = sf.readlines()
	
	vfcontent.pop(0)
	vfcontent.pop(1)
	vfcontent.pop(2)
	adfcontent.pop(0)
	adfcontent.pop(1)
	adfcontent.pop(2)
	sfcontent.pop(0)
	sfcontent.pop(1)
	sfcontent.pop(2)
	
	
	for cf,vf,adf,sf in zip(cfcontent,vfcontent,adfcontent,sfcontent):
		if vf == '1\n':
			print >> vulgarCategoryFile,cf.rstrip('\n')
		if adf == '1\n':
			print >> adCategoryFile,cf.rstrip('\n')
		if sf == '1\n':
			print >> skipCategoryFile,cf.rstrip('\n')
	
			
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
	video_url = 'https://gdata.youtube.com/feeds/api/videos/'+video_id+'/comments?orderby=published&max-results=50'
	comments_out = open(video_id+'_comments_output.txt','w+')
	yt_service = gdata.youtube.service.YouTubeService()
    	yt_service.ssl = True
	comments_generator(yt_service,video_url,comments_out)
	labelComments()
	mapLabelToComments()
	print "Done"

main()
