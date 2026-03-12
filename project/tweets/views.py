from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm

# Simple test view
def test(request):
    return render(request, "tweets/index.html")


# List all tweets
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')  # lowercase variable
    return render(request, 'tweets/tweets.html', {'tweets': tweets})


# Create a new tweet
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)  # handle image upload
        if form.is_valid():
            tweet = form.save(commit=False)  # get model instance
            tweet.user = request.user        # assign logged-in user
            tweet.save()
            return redirect('tweet_list')    # redirect after saving
    else:
        form = TweetForm()  # empty form for GET request

    return render(request, 'tweets/tweet_form.html', {'form': form})