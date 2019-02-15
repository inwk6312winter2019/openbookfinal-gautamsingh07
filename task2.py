import logging

fin= open("access.log", 'r') 

log_file1 = "GET.log"
logging.basicConfig(filename = log_file1, level = logging.GET)
logging.GET('GET')

log_file2 = "POST.log"
logging.basicConfig(filename = log_file2, level = logging.POST)
logging.POST('POST')

log_file3 = "PUT.log"
logging.basicConfig(filename = log_file3, level = logging.PUT)
logging.PUT('PUT')

log_file4 = "DELETE.log"
logging.basicConfig(filename = log_file4, level = logging.DELETE)
logging.DELETE('DELETE')

