import sets
found_ids = sets.Set()
def no_duplicates(msg, document):
    msg_id = msg.getheader('Message-ID')
    if msg_id in found_ids:
        return False
    found_ids.add(msg_id)
    return document
