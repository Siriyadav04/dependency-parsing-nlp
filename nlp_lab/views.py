from django.shortcuts import render
from nlp_modules.dependency import parse_sentence


def home(request):

    result = None
    tree = []

    if request.method == "POST":

        text = request.POST.get("text")

        # get selected language
        lang = request.POST.get("language")

        if text:

            parsed = parse_sentence(text, lang)

            result = []

            for item in parsed:

                result.append(
                    f"{item['word']} → {item['dep']} → {item['head']}"
                )

            # build tree
            root = None
            children = {}

            for item in parsed:

                if item["dep"] == "root":
                    root = item["word"]

                else:
                    head = item["head"]

                    if head not in children:
                        children[head] = []

                    children[head].append(
                        (item["word"], item["dep"])
                    )

            if root:

                tree.append(f"{root} (ROOT)")

                if root in children:

                    for child, dep in children[root]:

                        tree.append(
                            f" ├── {child} ({dep})"
                        )

    return render(
        request,
        'home.html',
        {
            "result": result,
            "tree": tree
        }
    )