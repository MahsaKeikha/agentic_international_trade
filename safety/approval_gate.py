def require_human_approval(action,approved=False):
    if not approved: raise PermissionError(f'Human approval required for {action}')
    return True
