from Products.Five import BrowserView
from Products.GSGroupMember.groupmembership import GroupMembers
from zope.component import adapts, createObject, getUtility
from zif.jsonserver.jsoncomponent import JSONWriter #@UnresolvedImport

def fn_sorter(a,b):
    if a[1] > b[1]:
        return 1
    else:
        return -1

class MembersView(BrowserView):
    # make the template publishable
    def __init__(self, context, request):
        self.context = context
        self.request = request
	#self.groupName = context.get_property('title')
        self.siteInfo = createObject('groupserver.SiteInfo', context)


class JSONMembers(BrowserView):
    # make the template publishable
    def __init__(self, context, request):
        self.context = context
        self.request = request
        #self.groupMembers = createObject('groupserver.GroupMembers', context)
        self.groupMembers = GroupMembers(context)

    def __call__(self, *args, **kw):
        self.request.response.setHeader('Content-Type',
                                        'text/javascript; charset=UTF-8')

        members = self.groupMembers.members
        memberlist = []
        # 'url': member.url,
        for member in members:
            imageUrl = member.imageUrl or ''
            if imageUrl:
                imageUrl = '<img width="40" height="40" src="%s"/>' % imageUrl
            joined = member.get_property('creation_date', '') or ''
            if joined:
                joined = joined.strftime("%b '%y")

            gn = member.get_property('givenName', '') or ''
            fn = member.get_property('familyName', '') or ''
            
            if gn or fn:
                name = ' '.join((gn,fn)).strip()
            else:
                name = member.get_property('fn', '') or ''
            
            ml = ['<a href="'+member.url+'">'+imageUrl+'<p>'+name+'</p></a>',
                  member.get_property('organisation', '') or '',
                  member.get_property('region', '') or '',
                  member.get_property('locality', '') or '',
                  member.get_property('countryName', '') or '',
                  joined]
            if filter(None, ml):
                memberlist.append(ml)
        
        memberlist.sort(fn_sorter)
        writer = JSONWriter()

        return writer.write( {'aaData': memberlist} )

