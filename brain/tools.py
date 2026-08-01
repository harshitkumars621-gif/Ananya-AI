def calculator(text):

    text = text.lower().replace(" ", "")

    try:

        if "+" in text:
            a, b = text.split("+")
            return str(float(a) + float(b))

        if "-" in text:
            a, b = text.split("-")
            return str(float(a) - float(b))

        if "*" in text:
            a, b = text.split("*")
            return str(float(a) * float(b))

        if "/" in text:
            a, b = text.split("/")
            return str(float(a) / float(b))

    except:
        return None

    return None