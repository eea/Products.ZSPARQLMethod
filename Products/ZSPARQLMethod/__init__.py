from AccessControl.Permissions import view_management_screens
from App.ImageFile import ImageFile

def initialize(context):
    import Method
    context.registerClass(
        Method.ZSPARQLMethod,
        permission=view_management_screens,
        constructors=(Method.manage_addZSPARQLMethod_html,
                      Method.manage_addZSPARQLMethod),
    )

misc_ = {
    'method.gif': ImageFile('www/method.gif', globals()),
}
