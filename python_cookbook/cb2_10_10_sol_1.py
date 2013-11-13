#!/usr/bin/python
import time, sys, os, email
now = time.time()
# get archive of previously-seen message-ids and times
kde_dir = os.expanduser('~/.kde')
if not os.path.isdir(kde_dir):
    os.mkdir(kde_dir)
arfile = os.path.join(kde_dir, 'duplicate_mails')
duplicates = {}
try:
    archive = open(arfile)
except IOError:
    pass
else:
    for line in archive:
        when, msgid = line[:-1].split(' ', 1)
        duplicates[msgid] = float(when)
    archive.close()
redo_archive = False
# suck message in from stdin and study it
msg = email.message_from_file(sys.stdin)
msgid = msg['Message-ID']
if msgid:
    if msgid in duplicates:
        # duplicate message: alter its subject
        subject = msg['Subject']
        if subject is None:
            msg['Subject'] = '**** DUP **** ' + msgid
        else:
            del msg['Subject']
            msg['Subject'] = '**** DUP **** ' + subject
    else:
        # non-duplicate message: redo the archive file
        redo_archive = True
        duplicates[msgid] = now
else:
    # invalid (missing message-id) message: alter its subject
    subject = msg['Subject']
    if subject is None:
        msg['Subject'] = '**** NID **** '
    else:
        del msg['Subject']
        msg['Subject'] = '**** NID **** ' + subject
# emit message back to stdout
print msg
if redo_archive:
    # redo archive file, keep only msgs from the last two hours
    keep_last = now - 2*60*60.0
    archive = file(arfile, 'w')
    for msgid, when in duplicates.iteritems():
        if when > keep_last:
            archive.write('%9.2f %s\n' % (when, what))
    archive.close()
