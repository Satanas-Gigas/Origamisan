import time
import logging
import psutil
from django.db import connection

logger = logging.getLogger("performance")

class PerfMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.process = psutil.Process()

    def __call__(self, request):
        start_time = time.perf_counter()
        mem_before = self.process.memory_info().rss  # bytes

        response = self.get_response(request)

        duration_ms = (time.perf_counter() - start_time) * 1000
        mem_after = self.process.memory_info().rss
        mem_diff_kb = (mem_after - mem_before) / 1024

        # Кол-во SQL запросов и суммарное время
        num_queries = len(connection.queries)
        sql_time_ms = sum(float(q.get("time", 0)) for q in connection.queries) * 1000

        logger.info(
            "path=%s method=%s status=%s time_ms=%.2f sql_ms=%.2f sql_count=%s mem_diff_kb=%.1f",
            request.path, request.method, getattr(response, "status_code", "NA"),
            duration_ms, sql_time_ms, num_queries, mem_diff_kb
        )

        return response