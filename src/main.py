import sys
import time

from src.serviceprovider.service import Service

_author_ = 'JeffMinsungKim'

class Main:

    if __name__ == '__main__':
        start = time.time()
        service = Service()
        service.display_recent_link()
        end = time.time() - start
        print("Python Elapsed %.02f seconds" % end)
    else:
        sys.exit(1)