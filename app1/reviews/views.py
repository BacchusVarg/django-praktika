from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

# Create your views here.

def reviews(request):

    comments = Comment.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')  # Перенаправляем на ту же страницу
    else:
        form = CommentForm()
    
    return render(request, 'reviews/reviews.html', {'comments': comments, 'form': form})