def allow_to_class(name, password):
    match name:
        case "Yes":
            print("Yes allowed..")
        case "No":
            print("No allowed..")
        case _:
            print("not allowed..")


allow_to_class("Shankar","Yes")