#Introduction#

MarsForum is lightweight forum web app. It has basic functions such as category, tag, and user profile. This forum is designed to be simple and user-friendly. It only provides a quick and easy way for people post threads and discussion.

#Example Site#

[http://marsforum.herokuapp.com/discussion/index](http://marsforum.herokuapp.com/discussion/index)

Welcome to test it, and issue any improvement and bug.

#Features#

+	JQuery and Ajax handle comment display
+	Tags
+	Category
+	Announcements
+	Save posts as drafts

#Roadmap#

1.	User profile page
	
	1.	User profile pic(PIL and pic upload)
	2.	User profile page with user's info
	3.	User's posts and drafts
	4.	message inbox

2.	Edit and delete post and comments through JQuery and Ajax

3.	Pagination

4.	Markdown supported

5.	Autoadjust images posted by users

6.	Sever media and static files through S3

#Requirements#

See requirements.txt above. Install needed libraries before test.

(Gunicorn is included because of the deployment on Heroku. It's not required if other web server is used)