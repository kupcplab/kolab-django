from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Notice, Column
from django.db.models import Q

def notice_list(request):
    query = request.GET.get('q', '')
    
    notice_list = Notice.objects.all()

    if query:
        notice_list = notice_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    paginator = Paginator(notice_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    start_num = page_obj.paginator.count - (page_obj.number - 1) * paginator.per_page
    numbered_notices = []
    for i, notice in enumerate(page_obj):
        numbered_notices.append({
            'notice': notice,
            'num': start_num - i
        })

    context = {
        'page_obj': page_obj,
        'numbered_notices': numbered_notices,
        'query': query,
    }

    return render(request, 'board/notice/notice_list.html', context)


def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'board/notice/notice_detail.html', {
        'notice': notice
    })

def column_list(request):
    query = request.GET.get('q', '')
    
    column_list = Column.objects.all()

    if query:
        column_list = column_list.filter(
            Q(title__icontains=query)
        )

    paginator = Paginator(column_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    start_num = page_obj.paginator.count - (page_obj.number - 1) * paginator.per_page
    numbered_columns = []
    for i, column in enumerate(page_obj):
        numbered_columns.append({
            'column': column,
            'num': start_num - i
        })

    context = {
        'page_obj': page_obj,
        'numbered_columns': numbered_columns,
        'query': query,
    }

    return render(request, 'board/column/column_list.html', context)