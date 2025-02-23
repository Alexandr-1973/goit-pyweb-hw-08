from models import Author, Quote
import connect

def print_results(info_list):
    [print (result.quote) for result in info_list]

while True:
    search_info=input("Input search parameters ")
    if search_info=="exit":
        break
    else:
        command, value=search_info.split(":")
        command = command.strip()
        value = value.strip()
        results_list=[]
        if command=="name":
            results_list=Quote.objects(author=Author.objects.get(fullname=value))
            # [print(q.quote) for q in Quote.objects(author=Author.objects.get(fullname=value))]
        elif command=="tag":
            results_list=Quote.objects.filter(tags__in=[value])
            # [print(q.quote) for q in Quote.objects.filter(tags__in=[value])]
        elif command=="tags":
            results_lst=Quote.objects.filter(tags__in=value.split(","))
            # [print(q.quote) for q in Quote.objects.filter(tags__in=value.split(","))]
        print_results(results_list)