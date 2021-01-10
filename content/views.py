from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Content
from .forms import CommentForm
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.

def content_index(request):
    content_list = Content.objects.all()
    query = request.GET.get('q')
    if query:
        query_list = query.split(' ')
        content_list2 = []
        for qs in query_list:
            for found in content_list.filter(Q(category__icontains=qs) | Q(ingredients__icontains=qs)):
                if not found in content_list2:
                    content_list2.append(found)
        paginator = Paginator(content_list2, 15)  # Show 15 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'content/index.html', {'contents': page_obj})
    else:
        paginator = Paginator(content_list, 15)  # Show 15 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'content/index.html', {'contents': page_obj})


def content_detail(request, id):
    content = get_object_or_404(Content, id=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.content = content
        comment.save()
        return HttpResponseRedirect(content.get_absolute_url())
    context = {
        'content': content,
        'form': form,
    }
    return render(request, 'content/detail.html', context)
