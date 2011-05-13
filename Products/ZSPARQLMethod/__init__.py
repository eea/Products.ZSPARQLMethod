from AccessControl.Permissions import view_management_screens

def initialize(context):
    import Method
    context.registerClass(
        Method.ZSPARQLMethod,
        permission=view_management_screens,
        constructors=(Method.manage_addZSPARQLMethod_html,
                      Method.manage_addZSPARQLMethod),
    )

    import ValueBox
    context.registerClass(
        ValueBox.ValueBox,
        permission=view_management_screens,
        constructors=(ValueBox.manage_addValueBox_html,
                      ValueBox.manage_addValueBox),
    )
