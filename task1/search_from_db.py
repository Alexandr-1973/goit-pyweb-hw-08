from models import Author, Quote
import connect

while True:
    search_info=input("Input search parameters ")

    if any(x in search_info for x in ["name:", "tag:", "tags:"]):
        command, value = search_info.split(":")
        command = command.strip()
        value = value.strip()
        results_list = []

        match command:
            case "name":
                results_list = Quote.objects(author__in=Author.objects.filter(fullname__iregex=value))
            case "tag":
                results_list = Quote.objects.filter(tags__iregex=value)
            case "tags":
                results_list = Quote.objects.filter(tags__iregex="|".join(value.split(",")))

        if not results_list:
            print("results not found")
        else:
            [print(result.quote) for result in results_list]
    elif "exit" in search_info:
        break
    else:
        print("Bad command")
