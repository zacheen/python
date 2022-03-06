import pythoncom
import PyHook3

# screen_num = 0   x1 = 1800 - x1
# screen_num = 1   x1 = x1
# screen_num = 2   x1 = x1 + 1800

mouse_pos = []
def region_to_width (x1, y1=0, x2=0 ,y2=0):

    if type(x1) == type([]):
        y1 = x1[1]
        x2 = x1[2]
        y2 = x1[3]
        x1 = x1[0]

    if x1 > x2:
        x = x2
        width = x1-x2
    elif x1 < x2:
        x = x1
        width = x2-x1
    else :
        width = 0
        x = x1
        # return (0,0,0,0)
    if y1 > y2 :
        y = y2
        length = y1-y2
    elif y1 < y2 :
        y = y1
        length = y2 - y1
    else :
        length = 0
        y = y1
        # return (0,0,0,0)

    real_pos = (x, y ,width+1 ,length+1)

    if x < 0:
        trans_pos = (x + 1920, y ,width+1 ,length+1)
    elif  x < 1920:
        trans_pos = (x, y ,width+1 ,length+1)
    elif x < 3840:
        trans_pos = (x - 1920, y ,width+1 ,length+1)
    else:
        return None

    print(str(real_pos)+ "  "+str(trans_pos))
    return trans_pos

def left_down( event ):
    print("left_down")

def OnMouseEvent(event):
    global mouse_pos
    # print("click")
    if event.MessageName == "mouse left down":
        # called when mouse events are received
        # print ('MessageName:',event.MessageName)
        # print ('Message:',event.Message)
        # print ('Time:',event.Time)
        # print ('Window:',event.Window)
        # print ('WindowName:',event.WindowName)
        # print ('Position:',event.Position)
        # print ('Wheel:',event.Wheel)
        # print ('Injected:',event.Injected)
        mouse_pos.append(event.Position[0])
        mouse_pos.append(event.Position[1])

    elif event.MessageName == "mouse left up":
        mouse_pos.append(event.Position[0])
        mouse_pos.append(event.Position[1])
        region = region_to_width(mouse_pos)
        mouse_pos = []



# return True to pass the event to other handlers
    return True

# create a hook manager
hm = PyHook3.HookManager()
# watch for all mouse events
hm.MouseAll = OnMouseEvent
# hm.SubscribeMouseLeftDown(left_down) 
# set the hook
hm.HookMouse()
# wait forever
pythoncom.PumpMessages()