from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Course

class CourseModelTest(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title="Python Regular Expressions",
            description="learn to write regular expresions in Python"
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)

class CourseViewsTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing"
            description="learn to write test in Python"
        )
        self.course2 = Course.objects.create(
            titte="New Course"
            description="A new courses"
        )
        self.step = Step.objects.create(
            title="introduction to Doctest"
            description="Learn to write test in your docstring"
            course=self.course
        )

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])
