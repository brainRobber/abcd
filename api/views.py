import json, os, time, shutil, logging

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from blog.models import *

@csrf_exempt
def write_blog(request):
	resp = {}
	error = ''
	print request.POST
	blog_text = request.POST['blog_text']
	blog_title = request.POST['blog_title']
	try:
		blog = BlogPost.objects.get(title=blog_title)
	except Exception, e:
		blog = None
	if blog:
		resp['status'] = error
		resp['error'] = "Duplicate entry"
		return HttpResponse(json.dumps(resp),content_type='application/json')
	blog_text_list = blog_text.split('\\n\\n')
	try:
		blog = BlogPost(title=blog_title)
		blog.save()
	except Exception, e:
		print "error occured"
		log.exception("error creating post")
	for para in blog_text_list:
		print para
		try:
			paragraph_object = BlogParagraph(paragraph=para, blog_post=blog)
			paragraph_object.save()
		except Exception, e:
			log.exception("error saving text of blog")

	resp['status'] = 'success'
	resp['error'] = error
	return HttpResponse(json.dumps(resp),content_type='application/json')

@csrf_exempt
def get_blogs(request):
	resp = {}
	print request.method
	if request.method == "POST":
		print request.POST
		print "inside post if"
		initial = int(request.POST['num'])
		print initial
	else:
		initial = 0
	print "reached here"
	print initial
	all_posts = BlogPost.objects.all()[initial:initial+5]
	if all_posts:
		post_list = []
		for post in all_posts:
			post_dic = {}
			post_dic['post_id'] = post.id
			post_dic['title'] = post.title
			#all_paragraphs = post.blogparagraph_set.all()
			all_paragraphs = BlogParagraph.objects.filter(blog_post=post)
			if all_paragraphs:
				para_list = []
				for para in all_paragraphs:
					para_dic = {}

					para_dic['paragraph_id'] = para.id
					para_dic['paragraph'] = para.paragraph
					
					para_list.append(para_dic)
			post_dic['text'] = para_list
			post_list.append(post_dic)

	resp['status'] = 'success'
	resp['posts'] = post_list
	resp['num'] = initial+5

	return HttpResponse(json.dumps(resp), content_type='application/json')

@csrf_exempt
def write_comment(request, para_id):
	resp = {}
	error = []
	#para_id = request.POST['para_id']
	comment_text = request.POST['comment_text']
	try:
		comment = BlogComment(text=comment_text, paragraph_id=para_id)
		comment.save()
	except Exception, e:
		log.exception("error saving comment")

	if error:
		resp['status'] = 'error'
		resp['error'] = error
	else:
		resp['status'] = 'success'

	return HttpResponse(json.dumps(resp), content_type='application/json')

def get_comments(request, blog_id):
	resp = {}
	try:
		post = BlogPost.objects.get(id=blog_id)
	except Exception, e:
		post = None
	if post:
		paragraphs = post.blogparagraph_set.all()
		para_list = []
		for para in paragraphs:
			para_dic = {}
			para_dic['id'] = para.id
			#comments = para.blogcomment_set.all()
			comments = BlogComment.objects.filter(paragraph=para)
			comment_list = []
			for comment in comments:
				comment_dic = {}

				comment_dic['id'] = comment.id
				comment_dic['text'] = comment.text
				
				comment_list.append(comment_dic)
			para_dic['comments'] = comment_list
			para_list.append(para_dic)

		resp['status'] = 'success'
		resp['comments'] = para_list
	else:
		resp['status'] = 'error'
		resp['message'] = 'Blog post with this id does not exist'

	return HttpResponse(json.dumps(resp), content_type='application/json')
