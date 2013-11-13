import win32event
import pythoncom
TIMEOUT = 200 # ms
StopEvent = win32event.CreateEvent(None, 0, 0, None)
OtherEvent = win32event.CreateEvent(None, 0, 0, None)
class myCoolApp(object):
    def OnQuit(self):
          # assume 'areYouSure' is a global function that makes a final
          # check via a message box, a fancy dialog, or whatever else!
          if areYouSure():
              win32event.SetEvent(StopEvent) # Exit msg pump
def _MessagePump():
     waitables = StopEvent, OtherEvent
     while True:
         rc = win32event.MsgWaitForMultipleObjects(
             waitables,
             0,       # Wait for all = false, so it waits for any one
             TIMEOUT, # (or win32event.INFINITE)
             win32event.QS_ALLEVENTS) # Accept all kinds of events
         # You can call a function here, if it doesn't take too long. It will
         # be executed at least every TIMEOUT ms -- possibly a lot more often,
         # depending on the number of Windows messages received.
         if rc == win32event.WAIT_OBJECT_0:
             # Our first event listed, the StopEvent, was triggered, so
             # we must exit, terminating the message pump
             break
         elif rc == win32event.WAIT_OBJECT_0+1:
             # Our second event listed, "OtherEvent", was set. Do
             # whatever needs to be done -- you can wait on as many
             # kernel-waitable objects as needed (events, locks,
             # processes, threads, notifications, and so on).
             pass
         elif rc == win32event.WAIT_OBJECT_0+len(waitables):
             # A windows message is waiting - take care of it. (Don't
             # ask me why a WAIT_OBJECT_MSG isn't defined <
             # WAIT_OBJECT_0...!).
             # This message-serving MUST be done for COM, DDE, and other
             # Windows-y things to work properly!
             if pythoncom.PumpWaitingMessages():
                  break # we received a wm_quit message
         elif rc == win32event.WAIT_TIMEOUT:
             # Our timeout has elapsed.
             # Do some work here (e.g, poll something you can't thread)
             # or just feel good to be alive.
             pass
         else:
             raise RuntimeError("unexpected win32wait return value")
