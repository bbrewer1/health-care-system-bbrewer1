from django_q.tasks import async_task

from mysite.myapi.services import sleep_and_print

def test_queue():
    async_task("sleep_and_print", 1)
    async_task("sleep_and_print", 2)
    async_task("sleep_and_print", 3)
    async_task("sleep_and_print", 4)
    async_task("sleep_and_print", 5)
    async_task("sleep_and_print", 6)
    async_task("sleep_and_print", 7)
    async_task("sleep_and_print", 8)
    async_task("sleep_and_print", 9)
    async_task("sleep_and_print", 10)
    async_task("sleep_and_print", 11)
    async_task("sleep_and_print", 12)
    async_task("sleep_and_print", 13)
    async_task("sleep_and_print", 14)
    async_task("sleep_and_print", 15)
    async_task("sleep_and_print", 16)
    async_task("sleep_and_print", 17)
    async_task("sleep_and_print", 18)
    async_task("sleep_and_print", 19)
    async_task("sleep_and_print", 20)