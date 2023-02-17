def ParseObjToJson(yourObj):
    return yourObj.__dict__.__str__().replace("\'", "\"")

