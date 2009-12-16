from Products.Five import BrowserView

class AJAXMembers(BrowserView):
    # make the template publishable
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.groupsInfo = createObject('groupserver.GroupsInfo', context)

    def __call__(self, *args, **kw):
        self.request.response.setHeader('Content-Type', 'application/x-js; charset=UTF-8')

        return 'foo'
