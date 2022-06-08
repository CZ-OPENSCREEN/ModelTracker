from django.utils.deprecation import MiddlewareMixin
from ModelTracker.Tracker import ModelTracker


class ModelTrackerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ModelTracker.thread.request = request



