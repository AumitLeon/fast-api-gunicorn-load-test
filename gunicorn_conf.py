from uvicorn.workers import UvicornWorker

class CustomoUvicornWorker(UvicornWorker):
    CONFIG_KWARGS = {"proxy_headers": True, "forwarded_allow_ips": "*"}

worker_class = "gunicorn_conf.CustomoUvicornWorker"

workers = 4


#max_requests = 500
