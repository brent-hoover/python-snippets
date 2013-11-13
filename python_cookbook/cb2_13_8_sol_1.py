ReplFormat = """
This message contained an attachment that was stripped out.
The filename was: %(filename)s,
The original type was: %(content_type)s
(and it had additional parameters of:
%(params)s)
"""
import re
BAD_CONTENT_RE = re.compile('application/(msword|msexcel)', re.I)
BAD_FILEEXT_RE = re.compile(r'(\.exe|\.zip|\.pif|\.scr|\.ps)$')
def sanitise(msg):
    ''' Strip out all potentially dangerous payloads from a message '''
    ct = msg.get_content_type()
    fn = msg.get_filename()
    if BAD_CONTENT_RE.search(ct) or (fn and BAD_FILEEXT_RE.search(fn)):
        # bad message-part, pull out info for reporting then destroy it
        # present the parameters to the content-type, list of key, value
        # pairs, as key=value forms joined by comma-space
        params = msg.get_params()[1:]
        params = ', '.join([ '='.join(p) for p in params ])
        # put informative message text as new payload
        replace = ReplFormat % dict(content_type=ct, filename=fn, params=params)
        msg.set_payload(replace)
        # now remove parameters and set contents in content-type header
        for k, v in msg.get_params()[1:]:
            msg.del_param(k)
        msg.set_type('text/plain')
        # Also remove headers that make no sense without content-type
        del msg['Content-Transfer-Encoding']
        del msg['Content-Disposition']
    else:
        # Now we check for any sub-parts to the message
        if msg.is_multipart():
            # Call sanitise recursively on any subparts
            payload = [ sanitise(x) for x in msg.get_payload() ]
            # Replace the payload with our list of sanitised parts
            msg.set_payload(payload)
    # Return the sanitised message
    return msg
# Add a simple driver/example to show how to use this function
if __name__ == '__main__':
    import email, sys
    m = email.message_from_file(open(sys.argv[1]))
    print sanitise(m)
