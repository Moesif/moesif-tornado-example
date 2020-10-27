
def identify_user(handler):
    # Your custom code that returns a user id string
    return "my_user_id"

def identify_company(handler):
    # Your custom code that returns a company id string
    return "my_company_id"

def get_token(handler):
    # Your custom code that returns a string for session/API token
    return "23jdf0owekfmcn4u3qypxg09w4d8ayrcdx8nu2ng]s98y18cx98q3yhwmnhcfx43f"

def should_skip(handler):
    # Your custom code that returns true to skip logging
    return "health/probe" in handler.request.full_url()

def mask_event(event_model):
    # Your custom code to change or remove any sensitive fields
    if 'password' in event_model.request.body:
        event_model.request.body['password'] = None
    return event_model

def get_metadata(handler):
    return {
        'datacenter': 'westus',
        'deployment_version': 'v1.2.3',
    }

moesif_config = {
    'APPLICATION_ID': 'Your Moesif Application Id',
    'DEBUG': True,
    'IDENTIFY_USER': identify_user,
    'IDENTIFY_COMPANY': identify_company,
    'LOG_BODY': True,
    'GET_SESSION_TOKEN': get_token,
    'SKIP': should_skip,
    'MASK_EVENT_MODEL': mask_event,
    'GET_METADATA': get_metadata,
}
