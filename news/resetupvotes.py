from apscheduler.schedulers.background import BackgroundScheduler
from .models import Post


def reset():
    Post.objects.all().update(amount_of_upvotes=0)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(reset, trigger="cron", hour="23", minute="59")
    scheduler.start()
