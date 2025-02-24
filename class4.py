#FIBBONACCI SERIES
#The sum of two elements defines the next
# a, b = 0, 1
# while a<100:
#     print(a)
#     a, b = b, a+b
    
    # MATCH CASE
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 200:
            return "OK"
        
    
