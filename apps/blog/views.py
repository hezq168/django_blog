from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views import View

from blog.models import Post, Tag, Comments, Type, Notice, Stars, UserProfile
from blog.forms import CommentsForm

import json


def index(request):
    # 获取所有文章
    if request.method == 'GET':
        _post = Post.objects.all()
        context = {'post': _post}
        return render(request, 'blog/index.html', context)
    else:
        pass


def post(request, id):
    if request.method == 'GET':
        # 获取文章内容
        post = Post.objects.filter(id=id).first()
        comment_form = CommentsForm()
        # 添加阅读数
        post.page_view += 1
        post.save()
        context = {'post': post, 'comment_form': comment_form}
        return render(request, 'blog/post.html', context)
    elif request.method == 'POST':
        comment_form = CommentsForm(request.POST)
        print(comment_form)
        if comment_form.is_valid():
            comm = request.POST['comment']
            id = int(request.POST['id'])
            post = Post.objects.get(id=id)
            # user = BlogUser.objects.get(id=1)
            obj = Comments(post=post, content=comm)
            try:
                obj.save()
            except:
                return HttpResponse('error')
            return HttpResponseRedirect('/blog/post/' + str(id))
        else:
            id = int(request.POST['id'])
            post = Post.objects.filter(id=id).first()
            comment_form = CommentsForm()

            context = {'post': post, 'comment_form': comment_form}

            return render(request, 'blog/post.html', context)
    else:
        pass


# 博客分类
class Category(View):
    # 获取分类
    def get(self, request, _id):
        _post = Post.objects.filter(type=_id)
        return render(request, 'blog/category.html', {'post': _post})


class TagView(View):
    # 获取标签
    def get(self, request, _id):
        _post = Post.objects.filter(tag=_id)
        _tag = Tag.objects.filter(id=_id).first()
        return render(request, 'blog/tag.html', {'post': _post, 'tag': _tag})


class NoticeView(View):
    # 网站公告
    def get(self, request, _id):
        _notice = Notice.objects.filter(id=_id).first()
        return render(request, 'blog/notice.html', {'notice': _notice})


class CommentView(View):
    """
    评论
    """

    @method_decorator(login_required)
    def post(self, request):
        code = request.POST.get('code', None)
        _id = int(request.POST.get('id', None))
        description = request.POST.get('description', None)
        msg = {'status': 'ok', 'data': '', 'error': ''}
        if code and description:
            check_code = request.session['CheckCode']
            if code.lower() == check_code:
                _post = Post.objects.get(id=_id)
                Comments.objects.create(content=description, post=_post)
                msg['data'] = '评论成功，待管理员审核通过后显示！'
                return HttpResponse(json.dumps(msg))
            else:
                msg['status'] = 'no'
                msg['error'] = '验证码不正确！'
        else:
            msg['status'] = 'no'
            msg['error'] = '评论或验证码不能为空！'

        return HttpResponse(json.dumps(msg))


class StarsView(View):
    """
    关注
    """
    @method_decorator(login_required)
    def post(self, request):
        post_id = request.POST.get('post_id', None)
        exiset_records = Stars.objects.filter(user=request.user, post=post_id)
        if exiset_records:
            # 如果记录已经存在，则表示用户取消关注
            exiset_records.delete()
            msg = {'status': 'ok', 'data': '关注取消！', 'error': ''}
        else:
            _post = Post.objects.get(id=post_id)
            Stars.objects.create(post=_post, user=request.user)
            msg = {'status': 'ok', 'data': '关注成功！', 'error': ''}
        return HttpResponse(json.dumps(msg))
