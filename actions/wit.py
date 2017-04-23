
def first_entity_value(entities, entity):
    """
    Returns first entity value
    """
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

def get_from_context_or_entities(context, entities, entity):
	if entity in context:
		return context[entity]
	else:
		return first_entity_value(entities, entity)